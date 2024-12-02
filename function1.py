def area_right_triangle(base, height):
    return 0.5 * base * height


print(area_right_triangle(int(input('输入三角形的底')), int(input('输入三角形的高'))))


def area_right_triangle_inner_print(base1, height1):
    print(0.5 * base1 * height1)


area_right_triangle_inner_print(int(input('输入三角形的底')), int(input('输入三角形的高')))
