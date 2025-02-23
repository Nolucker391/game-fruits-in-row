import os
from PIL import Image
from logger import logger

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "../assets/images")

# Пути к изображениям
URLS = {
    "stats": os.path.join(ASSETS_DIR, "statuds.png"),
    "level_xp": os.path.join(ASSETS_DIR, "uroven.png"),
    "level": os.path.join(ASSETS_DIR, "level.png"),
    "avokado": os.path.join(ASSETS_DIR, "mascot01.png"),
    "strawbery": os.path.join(ASSETS_DIR, "mascot2.png"),
    "settings_icon": os.path.join(ASSETS_DIR, "settings.png"),
    "key_icon": os.path.join(ASSETS_DIR, "key.png"),
    "background": os.path.join(ASSETS_DIR, "fon.png"),
}

logger.info("Загрузка изображений фруктов...")

# Загружаем изображения фруктов
fruit_images = [
    Image.open(os.path.join(ASSETS_DIR, "avokado.png")).convert("RGBA").resize((50, 50)),
    Image.open(os.path.join(ASSETS_DIR, "avokado-tmn.png")).convert("RGBA").resize((50, 50)),
    Image.open(os.path.join(ASSETS_DIR, "limon.png")).convert("RGBA").resize((50, 50)),
    Image.open(os.path.join(ASSETS_DIR, "klubnika-svet.png")).convert("RGBA").resize((50, 50)),
    Image.open(os.path.join(ASSETS_DIR, "klubnika-tenm.png")).convert("RGBA").resize((50, 50)),
]

logger.info("Изображения фруктов загружены успешно.")
