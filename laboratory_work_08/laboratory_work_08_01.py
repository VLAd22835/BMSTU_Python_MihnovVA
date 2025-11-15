from tkinter import *
from tkinter.messagebox import *
from math import atan, pi


def taylor_arctg_x():
    """Функция y(x) через ряд Тейлора для x > 1"""
    eps = 0.0001
    Lfun = []
    x = Xmin
    while x <= Xmax:
        if x > 1:  # Ряд сходится только для x > 1
            n = 0
            result = pi / 2
            term = 1
            while abs(term) > eps:
                term = ((-1) ** (n + 1)) / ((2 * n + 1) * x ** (2 * n + 1))
                result += term
                n += 1
                if n > 1000:  # Защита от бесконечного цикла
                    break
            Lfun.append((x, result))
        else:
            Lfun.append((x, None))
        x += 1 / Kx
    return Lfun


def arctg_x_plus_b():
    """Функция z(x) = arctg(x) + b"""
    Lfun = []
    x = Xmin
    while x <= Xmax:
        fun = atan(x) + dY  # dY используется как параметр b
        Lfun.append((x, fun))
        x += 1 / Kx
    return Lfun


def GetData():
    '''Получить данные'''
    global Xmax, Xmin, Ymax, Ymin
    global dX, dY, Kx, Ky
    tmpXmax = float(ent3.get())
    tmpXmin = float(ent2.get())
    tmpYmax = float(ent5.get())
    tmpYmin = float(ent4.get())
    tmpdY = float(ent7.get())
    tmpdX = float(ent6.get())
    if ((tmpXmin >= tmpXmax) or
            (tmpYmin >= tmpYmax) or
            (tmpdX <= 0)):
        showwarning(title="Ошибка задания границ",
                    message="Должны выполняться неравенства:\n"
                            "Xmax > Xmin;\n"
                            "Ymax > Ymin;\n"
                            "Шаг меток > 0")
    else:
        Xmax = tmpXmax
        Xmin = tmpXmin
        Ymax = tmpYmax
        Ymin = tmpYmin
        dX = tmpdX
        dY = tmpdY
        Kx = MaxX / abs((Xmax - Xmin))
        Ky = MaxY / abs((Ymax - Ymin))


def SetMark(a, b, LrBt=1):
    '''Нанесение меток'''
    ax_XY = []
    if LrBt:  # слева и справа
        ax_XY.append((a, b))
        ax_XY.append((a + 10, b))
    else:  # внизу и вверху
        ax_XY.append((a, b))
        ax_XY.append((a, b - 10))
    cv.create_line(ax_XY, fill='black', width=2)


def plotXY():
    ''' Рисуем координатные линейки'''
    # Прямоугольник
    ax_XY = []
    ax_XY.append((5, 5))
    ax_XY.append((MaxX - 5, MaxY - 5))
    cv.create_rectangle(ax_XY, fill="white",
                        outline="green", width=2)

    # Разметка левой и правой сторон
    y = Ymin
    y_pix = MaxY
    flg = False
    while y < Ymax:
        textY = str(round(y, 2))  # Текст метки
        SetMark(0, y_pix, 1)  # Слева
        if flg:  # Надписываем каждую вторую метку
            cv.create_text(15, y_pix, text=textY,
                           anchor=W)
        SetMark(MaxX - 10, y_pix, 1)  # Справа
        if flg:
            cv.create_text(MaxX - 15, y_pix,
                           text=textY, anchor=E)
        y += dX  # Ед. пользователя
        y_pix -= dX * Ky  # Ед. в пикселах
        flg = not flg  # Разметка через раз

    # Разметка сверху и снизу
    x = Xmin
    x_pix = 0
    flg = False
    while x < Xmax:
        textX = str(round(x, 2))  # Текст метки
        SetMark(x_pix, 0, 0)  # Вверху
        if flg:
            cv.create_text(x_pix, 15, text=textX,
                           anchor=N)
        SetMark(x_pix, MaxY, 0)  # Внизу
        if flg:
            cv.create_text(x_pix, MaxY - 15,
                           text=textX, anchor=S)
        x += dX
        x_pix += dX * Kx
        flg = not flg


def Draw(event):
    '''Подготовка полотна и вызов функций для рисования'''
    cv.delete("all")  # Очистка полотна
    GetData()  # Получить данные
    plotXY()  # Нарисовать координатные линейки

    # Нарисовать функции
    Fdraw(taylor_arctg_x, 'red')  # Функция y(x) - красный
    Fdraw(arctg_x_plus_b, 'blue')  # Функция z(x) - синий

    # Добавить заголовок и легенду
    cv.create_text(MaxX // 2, 20,
                   text="Графики функций: y(x) - ряд Тейлора для arctg(x) и z(x) = arctg(x) + b",
                   font=("Arial", 12, "bold"))
    cv.create_text(100, 50, text="y(x) = π/2 - 1/x + 1/(3x³) - 1/(5x⁵) + ...", fill="red", anchor="w")
    cv.create_text(100, 70, text=f"z(x) = arctg(x) + {dY:.2f}", fill="blue", anchor="w")


def Fdraw(func, color):
    '''Получение значений функции
    Преобразование в пикселы
    Рисование на полотне'''
    Lxy = func()  # Значения функции в ед. пользователя
    Lpix = []  # Значения функции в пикселах
    for xy in Lxy:
        x = Kx * (xy[0] - Xmin)
        if xy[1] is not None:
            y = MaxY - Ky * (xy[1] - Ymin)
            Lpix.append((x, y))
        elif Lpix:  # Если текущая точка None, но есть предыдущие
            # Рисуем линию до текущей точки и начинаем новую
            if len(Lpix) > 1:
                cv.create_line(Lpix, fill=color, width=2)
            Lpix = []

    if len(Lpix) > 1:
        cv.create_line(Lpix, fill=color, width=2, smooth=True)


def Final(event):
    ''' Завершаем работу '''
    window_deleted()


def window_deleted():
    ''' Завершаем работу по [X]'''
    if askyesno("Выход", "Завершить работу?"):
        root.destroy()


def showXY(event):
    global ID1, ID2
    x = event.x
    y = event.y
    ent0.delete(0, END)
    ent1.delete(0, END)
    ent0.insert(0, str(round(Xmin + x / Kx, 2)))
    ent1.insert(0, str(round(Ymin + (MaxY - y) / Ky, 2)))
    cv.delete(ID1)
    cv.delete(ID2)
    ID1 = cv.create_line(0, y, MaxX, y, dash=(3, 5))
    ID2 = cv.create_line(x, 0, x, MaxY, dash=(3, 5))


# Основное окно
root = Tk()
root.title("Графика - Вариант 4")
root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(False, False)

# Размеры окна
Kp = 0.7
MaxX = int(root.winfo_screenwidth() * Kp)
MaxY = int(root.winfo_screenheight() * Kp)

# Холст
cv = Canvas(root, width=MaxX, height=MaxY, bg="white")
cv.grid(row=0, columnspan=9)
cv.bind('<Button-1>', showXY)

# Начальные параметры
Xmin = 1.0  # Для ряда Тейлора x должен быть > 1
Xmax = 10.0
Ymin = 0.0
Ymax = 2.0
dY = 0.5  # Параметр b для второй функции
dX = 1.0  # шаг меток

# Масштабные коэффициенты
Kx = MaxX / abs((Xmax - Xmin))
Ky = MaxY / abs((Ymax - Ymin))

# Идентификаторы для линий курсора
ID1 = 0
ID2 = 0

# Поля ввода координат курсора
lba0 = Label(root, text="X курсора:", width=10, fg="blue", font="Ubutu, 12")
lba0.grid(row=1, column=0, sticky='e')
ent0 = Entry(root, width=8, font="Ubuntu, 12")
ent0.grid(row=1, column=1, sticky='w')
ent0.insert(0, 0)

lba1 = Label(root, text="Y курсора:", width=10, fg="blue", font="Ubutu, 12")
lba1.grid(row=2, column=0, sticky='e')
ent1 = Entry(root, width=8, font="Ubuntu, 12")
ent1.grid(row=2, column=1, sticky='w')
ent1.insert(0, 0)

# Параметры системы координат
lba2 = Label(root, text="Xmin (≥1):", width=10, fg="blue", font="Ubutu, 12")
lba2.grid(row=1, column=2, sticky='e')
ent2 = Entry(root, width=8, font="Ubuntu, 12")
ent2.grid(row=1, column=3)
ent2.insert(0, Xmin)

lba3 = Label(root, text="Xmax:", width=10, fg="blue", font="Ubutu, 12")
lba3.grid(row=1, column=4, sticky='e')
ent3 = Entry(root, width=8, font="Ubuntu, 12")
ent3.grid(row=1, column=5)
ent3.insert(0, Xmax)

lba4 = Label(root, text="Ymin:", width=10, fg="blue", font="Ubutu, 12")
lba4.grid(row=2, column=2, sticky='e')
ent4 = Entry(root, width=8, font="Ubuntu, 12")
ent4.grid(row=2, column=3)
ent4.insert(0, Ymin)

lba5 = Label(root, text="Ymax:", width=10, fg="blue", font="Ubutu, 12")
lba5.grid(row=2, column=4, sticky='e')
ent5 = Entry(root, width=8, font="Ubuntu, 12")
ent5.grid(row=2, column=5)
ent5.insert(0, Ymax)

lba6 = Label(root, text="Шаг меток:", width=10, fg="blue", font="Ubutu, 12")
lba6.grid(row=1, column=6, sticky='e')
ent6 = Entry(root, width=8, font="Ubuntu, 12")
ent6.grid(row=1, column=7)
ent6.insert(0, dX)

lba7 = Label(root, text="Параметр b:", width=10, fg="blue", font="Ubutu, 12")
lba7.grid(row=2, column=6, sticky='e')
ent7 = Entry(root, width=8, font="Ubuntu, 12")
ent7.grid(row=2, column=7)
ent7.insert(0, dY)

# Кнопки управления
btn1 = Button(root, width=20, bg="#ccc", text="Нарисовать графики")
btn1.grid(row=1, column=8)
btn1.bind("<Button-1>", Draw)

btn2 = Button(root, width=20, bg="#ccc", text="Выход")
btn2.grid(row=2, column=8)
btn2.bind("<Button-1>", Final)

# Информационная метка
info_label = Label(root, text="Вариант 4: y(x) - ряд Тейлора для arctg(x), z(x) = arctg(x) + b",
                   font=("Arial", 10))
info_label.grid(row=3, column=0, columnspan=9, pady=5)

root.mainloop()