import random
from random import randint


a = input("""выберете игру, в которую хотите сыграть, на выбор:
          1. 'Камень, ножницы, бумага'
          2. 'Угадай число'
          3. 'Сапер' """+ '\n')



def chisl():
    yuru = input("""выберете уровень:
          1. легко (1-10)
          2. средне (1 - 100)
          3. сложно (1 - 1000)"""+ '\n')
    match yuru:
        case '1':
            fdsapf = int(randint(1, 10))
            dsad = int(input("напишите число от 1 до 10: "))
            if dsad < 1 or dsad > 10:
                print("чут чут не те числа или вообще чисел нет.")
            else: 
                while dsad != fdsapf:
                    if dsad < fdsapf:
                        print("твое число меньше.")
                    elif dsad > fdsapf:
                        print("твое число больше.")
                    dsad = int(input("напиши число еще раз: "))
                print(f"поздравляю, ура, число было {fdsapf}")
        case '2':
            fdsapf = int(randint(1, 100))
            dsad = int(input("напишите число от 1 до 100: "))
            if dsad < 1 or dsad > 100:
                print("чут чут не те числа или вообще чисел нет.")
            else: 
                while dsad != fdsapf:
                    if dsad < fdsapf:
                        print("твое число меньше.")
                    elif dsad > fdsapf:
                        print("твое число больше.")
                    dsad = int(input("напиши число еще раз: "))
                print(f"поздравляю, ура, число было {fdsapf}")
        case '3':
            fdsapf = randint(1, 1000)
            dsad = int(input("напишите число от 1 до 1000: "))
            if dsad < 1 or dsad > 1000:
                print("чут чут не те числа или вообще чисел нет.")
            else: 
                while dsad != fdsapf:
                    if dsad < fdsapf:
                        print("твое число меньше.")
                    elif dsad > fdsapf:
                        print("твое число больше.")
                    dsad = int(input("напиши число еще раз: "))
                print(f"поздравляю, ура, число было {fdsapf}")
    

def kamen():
    print("правила игры: ты пишешь значение, код рандомно выбирает, камень ножницы или бумага, удачи!")
    dsad = input("введите: камень, ножницы или бумага: ").lower()
    jop = randint(1, 3)
    kop = {1: "камень", 2: "ножницы", 3 : "бумага"}
    if dsad == kop[1]:
        match jop:
            case 1:
                print("Камень!")
                print("ничья.")
            case 2:
                print("Ножницы!")
                print("победа!")
            case 3:
                print("Бумага!")
                print("поражение(")
    elif dsad == kop[2]:
        match jop:
            case 1:
                print("Камень!")
                print("поражение(")
            case 2:
                print("Ножницы!")
                print("ничья.")
            case 3:
                print("Бумага!")
                print("победа!")
    elif dsad == kop[3]:
        match jop:
            case 1:
                print("Камень!")
                print("победа!")
            case 2:
                print("Ножницы!")
                print("оражение(")
            case 3:
                print("Бумага!")
                print("ничья.")
    else: print("произошла ошибка.")
    return 1




def saper():
    def create_field(size, bombs):
        field = [[' ' for _ in range(size)] for _ in range(size)]
        bomb_locations = random.sample(range(size * size), bombs)
        
        for loc in bomb_locations:
            row = loc // size
            col = loc % size
            field[row][col] = '*'
            
            for r in range(max(0, row - 1), min(size, row + 2)):
                for c in range(max(0, col - 1), min(size, col + 2)):
                    if field[r][c] != '*':
                        if field[r][c] == ' ':
                            field[r][c] = 1
                        else:
                            field[r][c] += 1
        return field

    def display_field(field, visible):
        print("  " + " ".join([chr(97 + i) for i in range(len(field))]))  
        for i, row in enumerate(field):
            print(i + 1, end=' ')
            for j in range(len(row)):
                if visible[i][j]:
                    print(row[j], end=' ')
                else:
                    print('?', end=' ')
            print()

    def main():
        size = 8
        bombs = 8
        field = create_field(size, bombs)
        visible = [[False for _ in range(size)] for _ in range(size)]
        game_over = False

        while not game_over:
            display_field(field, visible)
            user_input = input("введите координаты (например, a1): ").strip().lower()

            if len(user_input) != 2 or user_input[0] not in 'abcdefgh' or user_input[1] not in '12345678':
                print("некорректный ввод. Попробуйте снова.")
                continue

            col = ord(user_input[0]) - 97
            row = int(user_input[1]) - 1

            if field[row][col] == '*':
                print("вы попали на мину! игра окончена.")
                game_over = True
            else:
                visible[row][col] = True
                
                if all(visible[i][j] or field[i][j] == '*' for i in range(size) for j in range(size)):
                    print("поздравляем! вы выиграли!")
                    break
            if user_input == "stop":
                print("вы закончили игру.")
                game_over = True


    if __name__ == "__main__":
        main()

match a:
    case '1':
        kamen()
    case '2':
        chisl()
    case '3':
        saper()


