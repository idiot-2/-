import json
import os
from dataclasses import dataclass

save_file = "data.json"


@dataclass
class Catalog:
    Name: str
    Platform: str
    Status: str
    Rating: int

listC = []

platM = ["PC", "PS", "Xbox", "Switch", "Mobile", "Handheld PC", "VR", "Cloud", "Web / Browser", "Smart TV", "Retro Consoles", "Arcade"]
statM = ["граю", "відкладено", "пройдено"]


#1.
def input_game():

    name = input_name()
    platform = input_platform()
    status = input_status()
    rating = input_rating()

    x = Catalog(Name=name, Platform=platform, Status=status, Rating=rating)

    listC.append(x)


#2.
def catalog_out():
    if catalog_none():
        return
    sort_catalog()
    print(f"\nІгор у каталозі: {len(listC)}")
    print("Назва — Платформа — Статус — Оцінка\n")
    for game in listC:
        game_out(game)


def game_out(g):
    print(f"{g.Name} — {g.Platform} — {g.Status} — {g.Rating}")


#3.
def edit_game():
    if catalog_none():
        return
    sort_catalog()
    print()
    for i, game in enumerate(listC, start=1):
        print(f"{i}. {game.Name}")
    print("0. Повернутися до меню")

    while True:
        try:
            game_index = int(input("\nВведіть номер гри для редагування: ")) - 1
        except ValueError:
            print("Невірний ввід. Введіть ціле число.")
            continue
        if 0 <= game_index < len(listC):
            game = listC[game_index]
            break
        elif game_index == -1:
            print("Повернення до меню.")
            return
        else:
            print("Помилка: невірний номер гри. Спробуйте ще раз.")

    game_out(game)

    print("\nОберіть поле для редагування:")
    print("1. Назва")
    print("2. Платформа")
    print("3. Статус")
    print("4. Оцінка")

    
    choice = input("Ваш вибір: ")

    if choice == '1':
        listC[game_index].Name = input_name(game_index)
    elif choice == '2':
        listC[game_index].Platform = input_platform()
    elif choice == '3':
        listC[game_index].Status = input_status()
    elif choice == '4':
        listC[game_index].Rating = input_rating()
    else:
        print("Невірний вибір. Повернення до меню.")
        return


#4.
def delete_game():
    if catalog_none():
        return

    print()
    sort_catalog()
    for i, game in enumerate(listC, start=1):
        print(f"{i}. {game.Name}")
    print("0. Повернутися до меню")

    while True:
        try:
            game_index = int(input("\nВведіть номер гри для видалення: ")) - 1
        except ValueError:
            print("Невірний ввід. Введіть ціле число.")
            continue
        if 0 <= game_index < len(listC):
            del listC[game_index]
            print("Гра видалена.")
            break
        elif game_index == -1:
            print("Повернення до меню.")
            return
        else:
            print("Помилка: невірний номер гри. Спробуйте ще раз.")


#5.
def statistics():
    if catalog_none():
        return

    print(f"\nВсього Ігор у каталозі: {len(listC)}")

    process = 0
    vidkladeno = 0
    proydeno = 0

    for game in listC:
        if game.Status == "граю":
            process += 1
        elif game.Status == "відкладено":
            vidkladeno += 1
        elif game.Status == "пройдено":
            proydeno += 1

    print(f"\nГраю: {process}")
    print(f"Відкладено: {vidkladeno}")
    print(f"Пройдено: {proydeno}")

    avg_rating = sum(game.Rating for game in listC) / len(listC)

    print(f"\nСередня оцінка: {avg_rating:.1f}")


#6.
def filter_status():
    if catalog_none():
        return
    
    status = input_status()
    filtered_games = [game for game in listC if game.Status == status]
    if filtered_games:
        print(f"\nІгри зі статусом '{status}':")
        for game in filtered_games:
            game_out(game)
    else:
        print(f"\nІгор зі статусом '{status}' не знайдено.")







def save_catalog():
    if listC:
        with open(save_file, "w", encoding="utf-8") as f:
            json.dump([game.__dict__ for game in listC], f, indent=4, ensure_ascii=False)


def load_catalog():
    if os.path.exists(save_file):
        with open(save_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for game_data in data:
                game = Catalog(**game_data)
                listC.append(game)
    
    no_error = True

    for index, game in enumerate(listC, start=1):
        if not isinstance(game.Name, str):
            print(f"Помилка: Невірний тип імені у грі '{game.Name}' (№{index})")
            no_error = False
        
        if not isinstance(game.Platform, str):
            print(f"Помилка: Невірний тип платформи у грі '{game.Name}' (№{index})")
            no_error = False

        if not isinstance(game.Status, str):
            print(f"Помилка: Невірний тип статусу у грі '{game.Name}' (№{index})")
            no_error = False

        if not isinstance(game.Rating, int):
            print(f"Помилка: Невірний тип оцінки у грі '{game.Name}' (№{index})")
            no_error = False
        

        if game.Status not in statM:
            print(f"Помилка: Неіснуючий статус у грі '{game.Name}' (№{index})")
            no_error = False
        
        if game.Rating > 10 or game.Rating < 1:
            print(f"Помилка: Оцiнка не вiдповiдає значенню (1-10) у грі '{game.Name}' (№{index})")
            no_error = False
        

    return no_error



def catalog_none():
    if not listC:
        print("\nКаталог ігор порожній.")
        return True
    return False











def input_name(current_index=None):
    while True:
        name = input("\nВведіть назву гри: ")

        if if_game_exists(name, current_index):
            print("\nГра з такою назвою вже існує. Введіть іншу назву.")
            continue
        return name

def if_game_exists(name, exclude_index=None):
    return any(game.Name == name for i, game in enumerate(listC) if i != exclude_index)

def input_status():
    while True:
        print("\nВведіть статус гри")
        for i, status in enumerate(statM, start=1):
            print(f"{i}. {status}")
        choice = input("Ваш вибір: ")
        if choice.isdigit() and 1 <= int(choice) <= len(statM):
            return statM[int(choice) - 1]
        else:
            print("\nНевірний вибір статусу. Спробуйте ще раз.")

def input_platform():
    while True:
        print("\nВведіть платформу гри")
        for i, platform in enumerate(platM, start=1):
            print(f"{i}. {platform}")
        print(f"{i + 1}. Свiй варіант")
        choice = input("Ваш вибір: ")
        if choice.isdigit() and 1 <= int(choice) <= len(platM):
            return platM[int(choice) - 1]
        elif choice == str(len(platM) + 1):
            custom_platform = input("Введіть власну платформу: ")
            return custom_platform
        else:
            print("\nНевірний вибір платформи. Спробуйте ще раз.")

def input_rating():
    while True:
        try:
            rating = int(input("Введіть оцінку гри (1-10): "))
            if 1 <= rating <= 10:
                return rating
            else:
                print("\nОцінка повинна бути в межах від 1 до 10. Спробуйте ще раз.")
        except ValueError:
            print("Невірний ввід. Введіть ціле число від 1 до 10.")

def sort_catalog():
    listC.sort(key=lambda game: statM.index(game.Status))






def Menu():
    while True:
        save_catalog()
        print("\n\nМеню:")
        print("1. Додати гру")
        print("2. Вивести каталог ігор")
        print("3. Редагувати")
        print("4. Видалити гру")
        print("5. Статистика")
        print("6. Фільтрувати за статусом")
        print("0. Вихід")

        choice = input("Виберіть дію: ")

        if choice == '1':
            input_game()

        elif choice == '2':
            catalog_out()

        elif choice == '3':
            edit_game()
        
        elif choice == '4':
            delete_game()

        elif choice == '5':
            statistics()

        elif choice == '6':
            filter_status()

        elif choice == '0':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if load_catalog():
    Menu()
else:
    print("Видалiть або вiдредагуйте файл збереження")
    input()