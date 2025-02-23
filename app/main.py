from app.game import create_game_board
from app.settings import root
from logger import logger

logger.info("Запуск игры...")

# Первоначальное заполнение игрового поля
create_game_board()

# Запуск главного цикла
root.mainloop()
