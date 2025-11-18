from turtle import *
import random
import math
import ru_local as ru

tracer(False)


def recursive_square(order: int, size: float) -> None:
    
    """
    Draws a recursive rotating square pattern.
    Args:
        order (int): The recursion depth.
        size (float): The side length of the square.
    Returns:
        None
    """

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

    step = size / 3
    if order == 0:
        pencolor(colors[0])
        for _ in range(4):
            forward(step)
            right(90)
    else:
        pencolor(colors[order % len(colors)])
        for _ in range(4):
            forward(step)
            right(90)

        up()
        right(10)
        forward(step * 0.1)
        down()

        recursive_square(order - 1, size * 0.8)


def tree_fractal(order: int, size: float) -> None:
    
    """
    Draws a branching tree-like fractal.
    Args:
        order (int): The recursion depth.
        size (float): The length of the branch.
    Returns:
        None
    """
    
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
    
    """
    Draws a branching fractal pattern.
    Args:
        order (int): Recursion depth.
        size (float): Length of the line segment.
    Returns:
        None
    """

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
    
    """
    Draws a single side of the Koch snowflake.
    Args:
        order (int): The recursion depth.
        size (float): The length of the line segment.
    Returns:
        None
    """

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan']
    color(random.choice(colors))

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
    
    """
    Draws the Minkowski fractal curve.
    Args:
        order (int): The recursion depth.
        size (float): The length of the overall segment.
    Returns:
        None
    """

    if order == 0:
        forward(size)
    else:
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'brown']
        pencolor(colors[order % len(colors)])

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
    
    """
    Draws a variant of the Ice fractal with 90-degree spikes.
    Args:
        order (int): The recursion depth.
        size (float): The length of the line segment.
    Returns:
        None
    """

    if order == 0:
        forward(size)
    else:
        ice_fractal_variant(order-1, size/2)
        left(90)
        ice_fractal_variant(order-1, size/4)
        left(180)
        ice_fractal_variant(order-1, size/4)
        left(90)
        ice_fractal_variant(order-1, size/2)


def ice_fractal_60(order: int, size: float) -> None:
    
    """
    Draws the 'Ice' fractal with 60-degree spike.
    Args:
        order (int): The recursion depth.
        size (float): The length of the line segment.
    Returns:
        None
    """
    
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
    
    """
    Draws the 'Levi' fractal pattern using turtle graphics.
    Args:
        size (float): Length of the line segment.
        order (int): Recursion depth.
    Returns:
        None
    """
    
    step = size / 2
    if order == 0:
        fd(step)
    else:
        lt(45)
        levi(order - 1, step)
        rt(90)
        levi(order - 1, step)
        lt(45)


def circle_cloud_fractal(x: float, y: float, depth: int, radius: float) -> None:

    """
    Draws a recursive fractal composed of branching circles.
    Args:
        x (float): The x-coordinate of the center of the current circle.
        y (float): The y-coordinate of the center of the current circle.
        depth (int): The current recursion depth.
        radius (float): The radius of the current circle.
    Returns:
        None
    """

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
        circle_cloud_fractal(new_x, new_y, new_radius, depth - 1)


def fractal_1(depth: int, size: float) -> None:
    
    """
    Draws a custom fractal pattern based on recursive branching.
    Args:
        depth (int): The recursion depth.
        size (float): The length of the branch.
    Returns:
        None
    """

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
    
    """
    Draws the 'Crystal Fractal' pattern using turtle graphics.
    Args:
        order (int): Length of the line segment.
        size (float): Recursion depth.
    Returns:
        None
    """

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan']
    color(random.choice(colors))

    if order == 0:
        return
    for i in range(3):
        fd(size)
        lt(120)
    fd(size)
    lt(20)
    crystal_fractal(order - 1, size * 0.8)



def main():
    speed(0)
    pensize(2)

    print(ru.MENU)
    print(ru.SQUARE)
    print(ru.TREE)
    print(ru.BRANCH)
    print(ru.KOH)
    print(ru.SNOWFLAKE)
    print(ru.MINKOWSKY)
    print(ru.ICE_FRAC_1)
    print(ru.ICE_FRAC_2)
    print(ru.LEVI)
    print(ru.CLOUD)
    print(ru.FRAC_1)
    print(ru.LOLL)

    choice = input(ru.CHOICE)

    try:
        depth: int = int(input(ru.DEPTH))
        size: float = float(input(ru.SIZE))
    except ValueError:
        print(ru.ERROR)
        return

    reset()
    speed(0)
    pensize(2)
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

    else:
        print(ru.NONAME)

    update()
    exitonclick()


if __name__ == "__main__":
    main()
