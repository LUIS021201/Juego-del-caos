import tkinter as tk
import random
import time



def main():

    root.geometry("600x600")
    root.title("Juego del caos")
    label_font = ("Arial", 16)
    message = tk.Label(root,
                    text="De click en algun lugar dentro del triangulo \ny luego presione el boton para comenzar la simulación",
                    font=label_font)
    message.pack(side="top")
    canvas.pack()

    # Draw a horizontal line from (50, 100) to (150, 100)
    # canvas.create_line(50, 100, 150, 100)

    canvas.create_oval(punto_a[0] - 2, punto_a[1] - 2, punto_a[0] + 2, punto_a[1] + 2, fill='black')
    canvas.create_oval(punto_b[0] - 2, punto_b[1] - 2, punto_b[0] + 2, punto_b[1] + 2, fill='black')
    canvas.create_oval(punto_c[0] - 2, punto_c[1] - 2, punto_c[0] + 2, punto_c[1] + 2, fill='black')



    canvas.bind('<Button-1>', draw_point_clicked)
    button = tk.Button(canvas, text="Comenzar simulación", command=start_simulation)
    canvas.create_window(200, 500, window=button)

    button = tk.Button(canvas, text="Limpiar puntos", command=clean_points)
    canvas.create_window(350, 500, window=button)

    root.mainloop()


def is_point_in_triangle(p, a, b, c):
    # Calculate the vectors representing the three sides of the triangle
    v0 = c[0] - a[0], c[1] - a[1]
    v1 = b[0] - a[0], b[1] - a[1]
    v2 = p[0] - a[0], p[1] - a[1]

    # Calculate the dot products of the vectors
    dot00 = v0[0] * v0[0] + v0[1] * v0[1]
    dot01 = v0[0] * v1[0] + v0[1] * v1[1]
    dot02 = v0[0] * v2[0] + v0[1] * v2[1]
    dot11 = v1[0] * v1[0] + v1[1] * v1[1]
    dot12 = v1[0] * v2[0] + v1[1] * v2[1]

    # Calculate the barycentric coordinates of the point
    inv_denom = 1.0 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    # Check if the point is inside the triangle
    return (u >= 0) and (v >= 0) and (u + v < 1)


def start_simulation():
    global all_points, in_process, ubi_punto, point, punto_a, punto_b, punto_c
    if point != None and not in_process:
        all_points.append(point)
        puntos = [punto_a, punto_b, punto_c]
        start_time = time.time()
        in_process = True
        while (time.time() - start_time) < 7:

            punto_escogido = random.choice(puntos)

            if punto_escogido == punto_a:
                punto_medio = get_middle_point(ubi_punto, punto_a)
                all_points.append(draw_point(punto_medio[0], punto_medio[1]))
            elif punto_escogido == punto_b:
                punto_medio = get_middle_point(ubi_punto, punto_b)
                all_points.append(draw_point(punto_medio[0], punto_medio[1]))
            else:
                punto_medio = get_middle_point(ubi_punto, punto_c)
                all_points.append(draw_point(punto_medio[0], punto_medio[1]))

            root.update()
            # time.sleep(0.01)

        in_process = False


def get_middle_point(p1, p2):
    return ((p1[0] + (p2[0] - p1[0]) / 2), (p2[1] + (p1[1] - p2[1]) / 2))


def draw_point(x, y):
    global ubi_punto
    ubi_punto = (x, y)
    return canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='black')


def draw_point_clicked(event):
    global point, in_process, punto_a, punto_b, punto_c
    if not in_process:
        x, y = event.x, event.y
        if is_point_in_triangle((x, y), punto_a, punto_b, punto_c):
            if point is not None:
                canvas.delete(point)

            point = draw_point(x, y)


def clean_points():
    global all_points, in_process
    if not in_process:
        for punto in all_points:
            canvas.delete(punto)


if __name__ == "__main__":
    root = tk.Tk()

    canvas = tk.Canvas(root, width=600, height=550)

    punto_a = (300, 100)

    punto_b = (150, 400)

    punto_c = (450, 400)

    point = None
    ubi_punto = None
    in_process = False
    all_points = []
    main()



