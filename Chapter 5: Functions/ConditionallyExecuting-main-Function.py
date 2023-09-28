# def area(width, length):
#     return width * length

# def perimeter(width, length):
#     return 2 * (width + length)

# def main():
#     width = float(input("Введите ширину прямоугольника: "))
#     length = float(input("Введите длину прямоугольника: "))
#     print('Площадь равна', area(width, length))
#     print('Периметр равен ', perimeter(width, length))


# if __name__ == '__main__':
#     main()

# `if __name__ == '__main__':` проверяет, выполняется ли текущий Python файл напрямую
# как отдельная программа. Если это так, код внутри этого блока будет выполнен.
# Если файл импортируется в другой файл как модуль,
# код внутри `if __name__ == '__main__':` не выполняется автоматически,
# что позволяет использовать этот файл как библиотеку или модуль в других программах.



# def times_ten(arg):
#     return arg * 10

# print(times_ten(10))


# value = 12
# result = times_ten(value)
# print(result)


# def my_function(a, b, c):
#     d = (a + c) / b
#     print(d)


# my_function(a=2, b=4, c=6)

import tkinter as tk
from tkinter import messagebox

def save_note():
    note = text.get("1.0", "end-1c")  # Get the text from the text widget
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    messagebox.showinfo("Note Saved", "Your note has been saved successfully.")

app = tk.Tk()
app.title("Note-taking App")

text = tk.Text(app, wrap=tk.WORD, height=10, width=40)
text.pack()

save_button = tk.Button(app, text="Save Note", command=save_note)
save_button.pack()

app.mainloop()





