import tkinter as tk
from tkinter import filedialog

def open_file():
    """
    Открывает диалог выбора файла и загружает его содержимое в текстовое поле.

    - Вызывает filedialog.askopenfilename для выбора файла.
    - Открывает выбранный файл в режиме чтения с кодировкой utf-8.
    - Очищает текущее содержимое текстового поля и вставляет содержимое файла.
    - Изменяет заголовок окна на путь к открытому файлу.
    """
    # Открываем диалог выбора файла
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if file_path:
        # Читаем содержимое и выводим в текстовое поле
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, content)
        root.title(file_path)

def save_file():
    """
    Открывает диалог сохранения файла и сохраняет содержимое текстового поля.

    - Вызывает filedialog.asksaveasfilename для выбора имени файла (с расширением .txt по умолчанию).
    - Открывает (или создаёт) файл в режиме записи с кодировкой utf-8.
    - Записывает содержимое текстового поля в файл.
    - Изменяет заголовок окна на путь к сохранённому файлу.
    """
    # Открываем диалог сохранения файла
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if file_path:
        # Записываем содержимое текстового поля в файл
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))
        root.title(file_path)

# Создаем главное окно
root = tk.Tk()
root.title("Простейший редактор")
root.geometry("600x400")

# Кнопки для открытия и сохранения
btn_open = tk.Button(root, text="Открыть", command=open_file)
btn_open.pack(fill=tk.X)

btn_save = tk.Button(root, text="Сохранить", command=save_file)
btn_save.pack(fill=tk.X)

# Текстовое поле для редактирования
text = tk.Text(root, wrap="word")
text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
