import tkinter
from PIL import Image, ImageTk
from app.config import URLS
from logger import logger

logger.info("Создание главного окна...")

# Создание главного окна
root = tkinter.Tk()
root.title("Фрукты 3 в ряд")
root.geometry("350x500")

# Размеры сетки
GRID_ROWS, GRID_COLS = 5, 4  # Поле 5x4
CELL_SIZE = 55  # Размер клетки
START_X, START_Y = 55, 160  # Начальные координаты сетки

# Загружаем фоновое изображение
logger.info("Загрузка фонового изображения...")
background_img = Image.open(URLS.get("background"))
background_photo = ImageTk.PhotoImage(background_img)

logger.info("Фоновое изображение загружено успешно.")
