<h1 align="center">Мини-игра «3 в ряд»

<img src="/assets/images/icon/fructs.png" alt="Demo" width="100" height="100">.

<img src="/assets/images/icon/logo.png" alt="Demo" width="300" height="250">

</h1>

***

## Описание
<b>Жанр:</b> [Казуальная головоломка](https//ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%B7%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D0%B8%D0%B3%D1%80%D0%B0)<br>
<b>Платформа:</b> ПК ([Tkinter](https://ru.wikipedia.org/wiki/Tkinter) + [Python](https://ru.wikipedia.org/wiki/Python))<br>
<b>Цель игры:</b> Собрать три и более одинаковых фруктов в ряд (горизонтально или вертикально), 
чтобы они исчезли и принесли очки игроку.<br>

Игровое поле представляет собой сетку размером 5 x 4, заполненную случайными фруктами. Игрок может менять местами два соседних фрукта, если это приводит к образованию комбинации из трёх или более одинаковых фруктов в ряд или столбец.

p.s: Игра сырая. Расписано все очень коротко. Цель проекта: демонстрация визуала и небольшого функционала.

## Запуск игры

1. Скопировать файлы проекта.

```commandline
git clone https://github.com/Nolucker391/game-fruits-in-row.git
```

2. Установить зависимости.

`pip -r requirements.txt`

3. Запуск приложения.

`python app/main.py`

## Инструменты

* [Python](https://www.python.org/downloads) `3.13.1`
* [Tkinter](https://pypi.org/project/pygame) `latest`
* [logger](https://pypi.org/project/pygame-widgets) `latest`
* [Pillow](https://pypi.org/project/jsonschema) `11.1.0`
* [os]()`latest`