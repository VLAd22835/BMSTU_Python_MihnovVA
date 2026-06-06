; =========================================
;  LLVM IR код для программы MiniGo
;  Сгенерировано компилятором MiniGo
; =========================================

declare i32 @printf(i8*, ...)

@.str_fmt = private constant [4 x i8] c"%d\0A\00"
@.str_hello = private constant [25 x i8] c"MiniGo program output:\0A\00"

define i32 @main() {
entry:
  ; Выводим приветствие
  %fmt_hello = getelementptr [25 x i8], [25 x i8]* @.str_hello, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %fmt_hello)

  ; Вычисляем выражение
  %val1 = sub i32 add i32 4, 4, 2
  %fmt = getelementptr [4 x i8], [4 x i8]* @.str_fmt, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %fmt, i32 %val1)

  ; Вычисляем выражение
  %val2 = sdiv i32 mul i32 10, 2, 4
  %fmt = getelementptr [4 x i8], [4 x i8]* @.str_fmt, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %fmt, i32 %val2)

  ret i32 0
}