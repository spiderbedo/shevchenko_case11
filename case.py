from turtle import *
import math

tracer(False)

FRACTAL_SETTINGS = {
    '1': {'name': 'Рекурсивные квадраты', 'depth': (3, 6), 'size': (100, 300)},
    '2': {'name': 'Дерево', 'depth': (5, 8), 'size': (100, 200)},
    '3': {'name': 'Ветви', 'depth': (4, 6), 'size': (200, 400)},
    '4': {'name': 'Кривая Коха', 'depth': (3, 5), 'size': (200, 400)},
    '5': {'name': 'Снежинка Коха', 'depth': (3, 4), 'size': (200, 300)},
    '6': {'name': 'Кривая Минковского', 'depth': (2, 4), 'size': (150, 300)},
    '7': {'name': 'Ледяной фрактал (90°)', 'depth': (3, 5), 'size': (200, 400)},
    '8': {'name': 'Ледяной фрактал (60°)', 'depth': (3, 5), 'size': (200, 400)},
    '9': {'name': 'Кривая Леви', 'depth': (8, 12), 'size': (500, 750)},
    '10': {'name': 'Облако из кругов', 'depth': (4, 6), 'size': (80, 150)},
    '11': {'name': 'Пользовательский фрактал 1', 'depth': (3, 5), 'size': (100, 200)},
    '12': {'name': 'Кристальный фрактал', 'depth': (5, 8), 'size': (50, 100)}
}


BACKGROUND_COLORS = {
    '1': 'white',
    '2': 'black',
    '3': 'lightblue',
    '4': 'lightyellow',
    '5': 'lightgray'
}

FRACTAL_COLORS = {
    '1': 'red',
    '2': 'blue',
    '3': 'green',
    '4': 'purple',
    '5': 'orange',
    '6': 'brown',
    '7': 'cyan',
    '8': 'magenta'
}


def recursive_square(order: int, size: float) -> None:
    step = size / 3
    if order == 0:
        for _ in range(4):
            forward(step)
            right(90)
    else:
        for _ in range(4):
            forward(step)
            right(90)
        up()
        right(10)
        forward(step * 0.1)
        down()
        recursive_square(order - 1, size * 0.8)


def tree_fractal(order: int, size: float) -> None:
    colormode(255)
    cg = 255 - int(order * (250 / 6)) % 255
    color(0, cg, 0)
    if order == 0:
        forward(size)
    else:
        forward(size)
        right(45)
        tree_fractal(order - 1, size / 2)
        left(90)
        tree_fractal(order - 1, size / 2)
        right(45)
        backward(size)


def branch(order, size):
    if order == 0:
        left(180)
        return
    x = size / (order + 1)
    for i in range(order):
        forward(x)
        left(45)
        branch(order - i - 1, 0.5 * x * (order - i - 1))
        left(90)
        branch(order - i - 1, 0.5 * x * (order - i - 1))
        right(135)
    forward(x)
    left(180)
    forward(size)


def koch_curve(order: int, size: float) -> None:
    if order == 0:
        forward(size)
    else:
        step = size / 3
        koch_curve(order - 1, step)
        left(60)
        koch_curve(order - 1, step)
        right(120)
        koch_curve(order - 1, step)
        left(60)
        koch_curve(order - 1, step)


def minkowski_curve(order: int, size: float) -> None:
    if order == 0:
        forward(size)
    else:
        step = size / 4
        minkowski_curve(order - 1, step)
        left(90)
        minkowski_curve(order - 1, step)
        right(90)
        minkowski_curve(order - 1, step)
        right(90)
        minkowski_curve(order - 1, step)
        minkowski_curve(order - 1, step)
        left(90)
        minkowski_curve(order - 1, step)
        left(90)
        minkowski_curve(order - 1, step)
        right(90)
        minkowski_curve(order - 1, step)


def ice_fractal_variant(order: int, size: float) -> None:
    if order == 0:
        forward(size)
    else:
        ice_fractal_variant(order - 1, size / 2)
        left(90)
        ice_fractal_variant(order - 1, size / 4)
        left(180)
        ice_fractal_variant(order - 1, size / 4)
        left(90)
        ice_fractal_variant(order - 1, size / 2)


def ice_fractal_60(order: int, size: float) -> None:
    step1 = size / 2
    if order == 0:
        forward(step1)
    else:
        step2 = size / 4
        ice_fractal_60(order - 1, step1)
        left(120)
        ice_fractal_60(order - 1, step2)
        right(180)
        ice_fractal_60(order - 1, step2)
        right(-120)
        ice_fractal_60(order - 1, step2)
        left(180)
        ice_fractal_60(order - 1, step2)
        right(-120)
        ice_fractal_60(order - 1, step1)


def levi(order: int, size: float) -> None:
    step = size / 1.5
    if order == 0:
        fd(step)
    else:
        lt(45)
        levi(order - 1, step)
        rt(90)
        levi(order - 1, step)
        lt(45)


def circle_cloud_fractal(x: float, y: float, depth: int, radius: float) -> None:
    if depth == 0 or radius < 2:
        return
    up()
    goto(x, y - radius)
    down()
    circle(radius)
    branches = 3
    angle_step = 360 / branches
    for i in range(branches):
        angle = math.radians(i * angle_step)
        new_x = x + math.cos(angle) * radius * 0.8
        new_y = y + math.sin(angle) * radius * 0.8
        new_radius = radius * 0.55
        circle_cloud_fractal(new_x, new_y, depth - 1, new_radius)


def fractal_1(depth: int, size: float) -> None:
    if depth == 0:
        return
    for _ in range(3):
        forward(size)
        angle = 30 + (depth * 15)
        left(angle)
        fractal_1(depth - 1, size * 0.5)
        right(angle)
        backward(size)
        right(120)


def crystal_fractal(order: int, size: float) -> None:
    if order == 0:
        return
    for i in range(3):
        fd(size)
        lt(120)
    fd(size)
    lt(30)
    crystal_fractal(order - 1, size * 0.8)


def show_menu():
    print("\n=== ГЕНЕРАТОР ФРАКТАЛОВ ===")
    print("1. Рекурсивные квадраты")
    print("2. Дерево")
    print("3. Ветви")
    print("4. Кривая Коха")
    print("5. Снежинка Коха")
    print("6. Кривая Минковского")
    print("7. Ледяной фрактал (90°)")
    print("8. Ледяной фрактал (60°)")
    print("9. Кривая Леви")
    print("10. Облако из кругов")
    print("11. Пользовательский фрактал 1")
    print("12. Кристальный фрактал")
    print("\nВведите номер фрактала (или пустую строку для выхода):")


def show_background_colors():
    print("\n=== ВЫБОР ЦВЕТА ФОНА ===")
    print("1. Белый")
    print("2. Черный")
    print("3. Голубой")
    print("4. Светло-желтый")
    print("5. Светло-серый")


def show_fractal_colors():
    print("\n=== ВЫБОР ЦВЕТА ФРАКТАЛА ===")
    print("1. Красный")
    print("2. Синий")
    print("3. Зеленый")
    print("4. Фиолетовый")
    print("5. Оранжевый")
    print("6. Коричневый")
    print("7. Бирюзовый")
    print("8. Пурпурный")


def get_user_choice(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        print("Неверный выбор. Попробуйте снова.")


def main():
    while True:
        show_menu()
        choice = input()

        if choice == '':
            print("Выход из программы.")
            break

        if choice not in FRACTAL_SETTINGS:
            print("Неверный номер фрактала!")
            continue

        fractal_info = FRACTAL_SETTINGS[choice]
        print(f"\nВыбран фрактал: {fractal_info['name']}")
        print(f"Рекомендуемая глубина: {fractal_info['depth'][0]}-{fractal_info['depth'][1]}")
        print(f"Рекомендуемый размер: {fractal_info['size'][0]}-{fractal_info['size'][1]}")

        # Выбор цвета фона
        show_background_colors()
        bg_choice = get_user_choice("Выберите цвет фона (1-5): ", ['1', '2', '3', '4', '5'])

        # Выбор цвета фрактала
        show_fractal_colors()
        fractal_color_choice = get_user_choice("Выберите цвет фрактала (1-8): ",
                                               ['1', '2', '3', '4', '5', '6', '7', '8'])

        # Ввод параметров
        try:
            depth = int(input(f"Введите глубину рекурсии ({fractal_info['depth'][0]}-{fractal_info['depth'][1]}): "))
            size = float(input(f"Введите размер ({fractal_info['size'][0]}-{fractal_info['size'][1]}): "))
        except ValueError:
            print("Ошибка ввода! Используются значения по умолчанию.")
            depth = fractal_info['depth'][0]
            size = fractal_info['size'][0]

        reset()
        speed(0)
        pensize(2)
        bgcolor(BACKGROUND_COLORS[bg_choice])
        pencolor(FRACTAL_COLORS[fractal_color_choice])

        step = -size / 4
        step2 = size / 4

        if choice == '1':
            up()
            goto(0, step2)
            down()
            recursive_square(depth, size)
        elif choice == '2':
            up()
            goto(0, step)
            left(90)
            down()
            tree_fractal(depth, size)
        elif choice == '3':
            up()
            goto(0, -100)
            left(90)
            down()
            branch(5, 400)
        elif choice == '4':
            up()
            goto(step, 0)
            down()
            for _ in range(3):
                koch_curve(depth, size)
        elif choice == '5':
            up()
            goto(-size / 2, step2)
            down()
            for _ in range(3):
                koch_curve(depth, size)
                right(120)
        elif choice == '6':
            up()
            goto(step, 0)
            down()
            minkowski_curve(depth, size)
        elif choice == '7':
            up()
            goto(step, 0)
            down()
            ice_fractal_variant(depth, size)
        elif choice == '8':
            up()
            goto(step, 0)
            down()
            ice_fractal_60(depth, size)
        elif choice == '9':
            up()
            goto(0, 0)
            down()
            levi(depth, size)
            rt(120)
        elif choice == '10':
            circle_cloud_fractal(0, 0, depth, size)
        elif choice == '11':
            up()
            goto(0, 0)
            down()
            fractal_1(depth, size)
        elif choice == '12':
            up()
            goto(step, 0)
            down()
            crystal_fractal(depth, size)

        update()
        print("\nФрактал нарисован! Нажмите на окно для закрытия.")
        print("После закрытия окна можно выбрать следующий фрактал.\n")


if __name__ == "__main__":
    main()
