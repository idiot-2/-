#ля ля ля
import sys
import json
from dataclasses import dataclass

print("Каталог iгор: Назва, платформа, статус (грає/пройдено/відкладено); оцінка; фільтрація за статусом")

@dataclass
class Catalog:
    Name: str
    Platform: str
    Status: str
    Rating: int

listC = []

def input_game():
    name = input("Введіть назву гри: ")
    platform = input("Введіть платформу гри: ")
    status = input("Введіть статус гри (грає/пройдено/відкладено): ")
    rating = int(input("Введіть оцінку гри (1-10): "))

    x = Catalog(Name=name, Platform=platform, Status=status, Rating=rating)

    listC.append(x)

def Menu():
    while True:
        print("\nМеню:")
        print("1. Додати гру")
        print("2. Вивести каталог ігор")
        print("3. Вихід")

        choice = input("Виберіть дію: ")

        if choice == '1':
            input_game()
        elif choice == '2':
            for game in listC:
                print(f"Назва: {game.Name}, Платформа: {game.Platform}, Статус: {game.Status}, Оцінка: {game.Rating}")
        elif choice == '3':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

Menu()