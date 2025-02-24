import random
import tkinter
from PIL import Image, ImageTk

from settings import root, background_photo, GRID_COLS, GRID_ROWS, START_Y, START_X, CELL_SIZE
from config import fruit_images, URLS
from logger import logger

logger.info("Создание игрового поля...")


# Создаем Canvas для фонового изображения
canvas = tkinter.Canvas(root)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0, anchor="nw", image=background_photo)

status_img = Image.open(URLS.get("stats")).convert("RGBA").resize((230, 30))
status_photo = ImageTk.PhotoImage(status_img)
canvas.create_image(45, 10, anchor="nw", image=status_photo)

uroven_img = Image.open(URLS.get("level_xp")).convert("RGBA").resize((190, 45))
uroven_photo = ImageTk.PhotoImage(uroven_img)
canvas.create_image(65, 45, anchor="nw", image=uroven_photo)


level_img = Image.open(URLS.get("level")).convert("RGBA")
level_photo = ImageTk.PhotoImage(level_img)
canvas.create_image(95, 102, anchor="nw", image=level_photo)

overlay1_img = Image.open(URLS.get("avokado")).resize((70, 110))
overlay1_photo = ImageTk.PhotoImage(overlay1_img)
overlay2_img = Image.open(URLS.get("strawbery")).resize((70, 100))
overlay2_photo = ImageTk.PhotoImage(overlay2_img)
canvas.create_image(55, 85, anchor="nw", image=overlay1_photo)
canvas.create_image(210, 90, anchor="nw", image=overlay2_photo)


fruit_images_resized = [ImageTk.PhotoImage(img) for img in fruit_images]  # Обычные иконки
fruit_images_big = [ImageTk.PhotoImage(img.resize((60, 60))) for img in fruit_images]  # Увеличенные

# Игровое поле
fruit_objects = []
fruit_positions = {}  # {canvas_id: (row, col)}
fruit_images_dict = {}  # {canvas_id: индекс_фрукта}

# Переменные для перемещения
selected_fruit = None
original_pos = None
selection_border = None  # Граница выделения

# Функция создания игрового поля
def create_game_board():
    for row in range(GRID_ROWS):
        row_objects = []
        for col in range(GRID_COLS):
            fruit_idx = random.randint(0, len(fruit_images) - 1)
            fruit = canvas.create_image(
                START_X + col * CELL_SIZE, START_Y + row * CELL_SIZE,
                anchor="nw", image=fruit_images_resized[fruit_idx]
            )
            fruit_positions[fruit] = (row, col)
            fruit_images_dict[fruit] = fruit_idx
            row_objects.append(fruit)
        fruit_objects.append(row_objects)

def get_grid_position(x, y):
    """Определяет, в какой ячейке сетки находится точка"""
    col = (x - START_X) // CELL_SIZE
    row = (y - START_Y) // CELL_SIZE
    if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
        return row, col
    return None

def swap_fruits(fruit1, fruit2):
    """Меняет местами два фрукта и обновляет позиции в логике и на экране."""
    row1, col1 = fruit_positions[fruit1]
    row2, col2 = fruit_positions[fruit2]

    # Получаем координаты фруктов
    x1, y1 = canvas.coords(fruit1)
    x2, y2 = canvas.coords(fruit2)

    # Обновляем координаты на Canvas
    canvas.coords(fruit1, x2, y2)
    canvas.coords(fruit2, x1, y1)

    # Обновляем позиции фруктов в словаре fruit_positions
    fruit_positions[fruit1], fruit_positions[fruit2] = (row2, col2), (row1, col1)

    # Обновляем изображения фруктов в словаре fruit_images_dict
    fruit_images_dict[fruit1], fruit_images_dict[fruit2] = (
        fruit_images_dict[fruit2], fruit_images_dict[fruit1]
    )

    # Обновляем массив фруктов на поле
    fruit_objects[row1][col1], fruit_objects[row2][col2] = (
        fruit_objects[row2][col2], fruit_objects[row1][col1]
    )

def on_click(event):
    """Выбираем фрукт при нажатии."""
    global selected_fruit, original_pos, selection_border
    item = canvas.find_closest(event.x, event.y)[0]  # Находим ближайший объект
    if item in fruit_positions:
        selected_fruit = item
        original_pos = fruit_positions[item]

        # Увеличиваем фрукт
        fruit_idx = fruit_images_dict[item]
        canvas.itemconfig(item, image=fruit_images_big[fruit_idx])

        # Рисуем рамку вокруг фрукта
        x, y = canvas.coords(item)
        selection_border = canvas.create_rectangle(
            x - 0.1, y - 0.1, x + 58, y + 55, outline="red", width=3
        )

def on_release(event):
    """Меняем фрукты местами при отпускании кнопки мыши."""
    global selected_fruit, selection_border
    if selected_fruit:
        old_row, old_col = original_pos
        new_pos = get_grid_position(event.x, event.y)

        if new_pos:
            new_row, new_col = new_pos

            # Проверяем, что перемещение на одну клетку по горизонтали или вертикали
            if (abs(new_row - old_row) == 1 and new_col == old_col) or \
                    (abs(new_col - old_col) == 1 and new_row == old_row):
                target_fruit = fruit_objects[new_row][new_col]

                # Меняем фрукты местами (логика и изображения)
                swap_fruits(selected_fruit, target_fruit)

        # Возвращаем фрукт к обычному размеру
        fruit_idx = fruit_images_dict[selected_fruit]
        canvas.itemconfig(selected_fruit, image=fruit_images_resized[fruit_idx])

        # Удаляем рамку
        canvas.delete(selection_border)
        selection_border = None
        selected_fruit = None

# Привязываем события
canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)
logger.info("Готово. Запуск игры.")


settings_over = Image.open(URLS.get("settings_icon")).resize((25, 25))
over_settings_photo = ImageTk.PhotoImage(settings_over)

key_over = Image.open(URLS.get("key_icon")).resize((25, 25))
over_key_photo = ImageTk.PhotoImage(key_over)

canvas.create_image(35, 432, anchor="nw", image=over_settings_photo)
canvas.create_image(265, 432, anchor="nw", image=over_key_photo)
