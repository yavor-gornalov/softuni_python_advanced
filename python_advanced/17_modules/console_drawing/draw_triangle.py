def draw_triangle(size, current_num=1):
    if size < 1:
        return
    print(*[i for i in range(1, current_num + 1)], sep=" ")
    if current_num == size:
        return

    draw_triangle(size, current_num + 1)
    print(*[i for i in range(1, current_num + 1)], sep=" ")
