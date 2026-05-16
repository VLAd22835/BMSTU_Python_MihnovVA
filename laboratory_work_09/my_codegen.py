# my_codegen.py (исправленная версия)
import sys
import os


class CodeGenerator:


    def __init__(self):
        self.var_count = 0
        self.code_lines = []

    def generate(self, ast, filename="program"):

        print(f"\n{'=' * 70}")
        print("3. ГЕНЕРАЦИЯ КОДА LLVM IR (ТЕКСТОВЫЙ РЕЖИМ)")
        print(f"{'=' * 70}")

        try:
            # Генерируем текстовый LLVM IR
            llvm_code = self._generate_text(ast)

            # Сохраняем в файл
            self._save_to_file(llvm_code, filename)

            # Пытаемся скомпилировать в исполняемый файл
            self._compile_to_executable(filename)

            return llvm_code, True

        except Exception as e:
            print(f"✗ Ошибка генерации кода: {e}")
            import traceback
            traceback.print_exc()
            return "", False

    def _generate_text(self, ast_node):
        """Генерация текстового LLVM IR"""
        print("🔧 Генерация текстового LLVM IR...")

        # Начинаем с заголовка
        code = [
            "; =========================================",
            ";  LLVM IR код для программы MiniGo",
            ";  Сгенерировано компилятором MiniGo",
            "; =========================================",
            "",
            "declare i32 @printf(i8*, ...)",
            "",
            "@.str_fmt = private constant [4 x i8] c\"%d\\0A\\00\"",
            "@.str_hello = private constant [25 x i8] c\"MiniGo program output:\\0A\\00\"",
            "",
            "define i32 @main() {",
            "entry:"
        ]

        # Добавляем вывод приветствия
        code.extend([
            "  ; Выводим приветствие",
            "  %fmt_hello = getelementptr [25 x i8], [25 x i8]* @.str_hello, i32 0, i32 0",
            "  call i32 (i8*, ...) @printf(i8* %fmt_hello)",
            ""
        ])

        # Обходим AST и генерируем вычисления
        results = self._traverse_ast_for_computations(ast_node)

        # Добавляем вычисления в код
        var_counter = 1
        for expr_result in results:
            code.extend([
                f"  ; Вычисляем выражение",
                f"  %val{var_counter} = {expr_result}",
                f"  %fmt = getelementptr [4 x i8], [4 x i8]* @.str_fmt, i32 0, i32 0",
                f"  call i32 (i8*, ...) @printf(i8* %fmt, i32 %val{var_counter})",
                ""
            ])
            var_counter += 1

        # Завершаем функцию main
        code.extend([
            "  ret i32 0",
            "}"
        ])

        llvm_code = "\n".join(code)
        print(f"✓ Сгенерировано {len(code)} строк LLVM IR")
        return llvm_code

    def _traverse_ast_for_computations(self, ast_node):
        """Обходит AST и собирает вычисления для генерации кода"""
        results = []

        def traverse(node):
            node_type = type(node).__name__

            if node_type == 'PackageNode':
                for func in node.functions:
                    traverse(func)

            elif node_type == 'FunctionNode':
                if node.name.getstr() == 'main':
                    traverse(node.body)

            elif node_type == 'BlockNode':
                for stmt in node.statements:
                    traverse(stmt)

            elif node_type == 'PrintNode':
                # Получаем строковое представление выражения
                expr_str = self._expression_to_llvm(node.value)
                results.append(expr_str)

        traverse(ast_node)
        return results

    def _expression_to_llvm(self, expr):
        """Преобразует выражение в строку LLVM IR"""
        expr_type = type(expr).__name__

        if expr_type == 'NumberNode':
            return expr.value.getstr()

        elif expr_type == 'SumNode':
            left = self._expression_to_llvm(expr.left)
            right = self._expression_to_llvm(expr.right)
            return f"add i32 {left}, {right}"

        elif expr_type == 'SubNode':
            left = self._expression_to_llvm(expr.left)
            right = self._expression_to_llvm(expr.right)
            return f"sub i32 {left}, {right}"

        elif expr_type == 'MulNode':
            left = self._expression_to_llvm(expr.left)
            right = self._expression_to_llvm(expr.right)
            return f"mul i32 {left}, {right}"

        elif expr_type == 'DivNode':
            left = self._expression_to_llvm(expr.left)
            right = self._expression_to_llvm(expr.right)
            return f"sdiv i32 {left}, {right}"

        return "0"

    def _save_to_file(self, llvm_code, filename):
        """Сохраняет LLVM IR в файл"""
        os.makedirs("output", exist_ok=True)

        ll_file = f"output/{filename}.ll"
        with open(ll_file, 'w', encoding='utf-8') as f:
            f.write(llvm_code)

        print(f"✓ LLVM IR сохранен в: {ll_file}")

        # Показываем часть кода
        print("\n Часть сгенерированного LLVM IR:")
        print("-" * 40)
        lines = llvm_code.split('\n')
        for i, line in enumerate(lines[:15]):
            print(f"  {line}")

    def _compile_to_executable(self, filename):
        """Компилирует LLVM IR в исполняемый файл"""
        ll_file = f"output/{filename}.ll"
        exe_file = f"output/{filename}"

        # Проверяем наличие clang
        if os.system("which clang > /dev/null 2>&1") != 0:
            print("  Clang не найден. Установите для создания исполняемого файла:")
            print("   macOS: xcode-select --install")
            print("   Ubuntu/Debian: sudo apt install clang")
            print("   Windows: установите LLVM или Visual Studio")
            return False

        try:
            print(f"🔨 Компиляция в исполняемый файл...")
            cmd = f"clang {ll_file} -o {exe_file}"

            if os.system(cmd) == 0:
                # Делаем исполняемым на Unix
                if sys.platform != "win32":
                    os.chmod(exe_file, 0o755)

                print(f"✓ Исполняемый файл создан: {exe_file}")
                print(f"\n️  Для запуска выполните:")
                print(f"   cd output && ./{filename}")
                return True
            else:
                print("✗ Ошибка компиляции с clang")
                return False

        except Exception as e:
            print(f"✗ Ошибка: {e}")
            return False