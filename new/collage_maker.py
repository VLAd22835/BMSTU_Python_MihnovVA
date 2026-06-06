from PIL import Image
import os
from pathlib import Path

# ===== НАСТРОЙКИ =====
INPUT_DIR = "p"  # сюда кладёте 3 фото
OUTPUT_DIR = "collages"  # сюда сохранится коллаж

# Размеры (можно менять)
TOP_IMG_WIDTH = 400  # ширина одного верхнего фото
TOP_IMG_HEIGHT = 600  # высота верхних фото
BOTTOM_IMG_HEIGHT = 600  # высота нижнего фото (сводка)

# Отступы
PADDING = 10
BG_COLOR = (255, 255, 255)  # белый фон


def create_collage_from_3_photos(photo_paths, output_path):
    """
    Берёт 3 фото и делает коллаж:
    - 2 фото сверху (рядом)
    - 1 фото снизу (на всю ширину)
    """

    if len(photo_paths) != 3:
        print(f"❌ Нужно 3 фото, а получено {len(photo_paths)}")
        return False

    # Загружаем фото
    images = []
    for path in photo_paths:
        try:
            img = Image.open(path)
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            images.append(img)
            print(f"  ✓ Загружено: {os.path.basename(path)} ({img.size[0]}x{img.size[1]})")
        except Exception as e:
            print(f"  ✗ Ошибка загрузки {path}: {e}")
            return False

    # Ресайзим первые 2 фото (верхние
    top_left = images[0].resize((TOP_IMG_WIDTH, TOP_IMG_HEIGHT), Image.Resampling.LANCZOS)
    top_right = images[1].resize((TOP_IMG_WIDTH, TOP_IMG_HEIGHT), Image.Resampling.LANCZOS)

    # Ресайзим нижнее фото (сводка) — растягиваем на всю ширину
    bottom_width = TOP_IMG_WIDTH * 2 + PADDING
    bottom_img = images[2].resize((bottom_width, BOTTOM_IMG_HEIGHT), Image.Resampling.LANCZOS)

    # Размеры коллажа
    collage_width = bottom_width
    collage_height = TOP_IMG_HEIGHT + PADDING + BOTTOM_IMG_HEIGHT

    # Создаём пустое полотно
    collage = Image.new("RGB", (collage_width, collage_height), BG_COLOR)

    # Вставляем верхние фото
    collage.paste(top_left, (0, 0))
    collage.paste(top_right, (TOP_IMG_WIDTH + PADDING, 0))

    # Вставляем нижнее фото
    collage.paste(bottom_img, (0, TOP_IMG_HEIGHT + PADDING))

    # Сохраняем
    collage.save(output_path, "JPEG", quality=92)
    print(f"  💾 Сохранён: {output_path}")
    return True


def main():
    # Создаём папку для результата
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    # Проверяем входную папку
    if not os.path.exists(INPUT_DIR):
        print(f"❌ Папка '{INPUT_DIR}' не найдена!")
        print(f"   Создайте папку '{INPUT_DIR}' и положите в неё ровно 3 фото.")
        return

    # Получаем все фото из папки
    all_files = [f for f in os.listdir(INPUT_DIR)
                 if f.lower().endswith(('.jpeg', '.jpg', '.png'))]

    # Полные пути
    photo_paths = [os.path.join(INPUT_DIR, f) for f in all_files]

    print(f"📁 Найдено фото в '{INPUT_DIR}': {len(photo_paths)}")

    if len(photo_paths) != 3:
        print(f"\n❌ Ошибка: нужно ровно 3 фото, а у вас {len(photo_paths)}")
        print("   Удалите лишние или добавьте недостающие файлы в папку 'photos'")
        return

    # Имя выходного файла (можно поменять)
    output_filename = "collage.jpg"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    # Создаём коллаж
    print("\n🖼️ Создаём коллаж...")
    success = create_collage_from_3_photos(photo_paths, output_path)

    if success:
        print("\n✅ Готово!")
        # Показываем путь к результату
        if os.name == 'nt':  # Windows
            print(f"   Открыть папку: explorer {os.path.abspath(OUTPUT_DIR)}")
        elif os.name == 'posix':  # Mac/Linux
            print(f"   Открыть папку: open {os.path.abspath(OUTPUT_DIR)}")


if __name__ == "__main__":
    main()