import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

import requests
from PIL import Image, ImageTk

from cfg import api_key_nasa


def nasa():
    window = tk.Tk()
    monitor_height = window.winfo_screenheight()
    monitor_width = window.winfo_screenwidth()

    path = "image.png"
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key_nasa}'
    result = requests.get(url)
    photo_link = result.json()['hdurl']

    image = requests.get(photo_link)
    out = open(path, "wb")
    out.write(image.content)
    out.close()
    title = 'Nasa'

    window.title(title)
    image_size = Image.open(path).size
    width = image_size[0]
    height = image_size[1]
    if width > monitor_width - 50 or height > monitor_height - 50:
        width = int(width / 2)
        height = int(height / 2)
        new_image = Image.open(path).resize((width, height))
        new_image.save(path)
    bg_image = ImageTk.PhotoImage(file=path)
    window.geometry(f'{width}x{height}')
    window.resizable(width=False, height=False)
    label = tk.Label(window, image=bg_image)
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    button = tk.Button(text='Обновить фото дня', background='black', foreground='lime', font=('Arial', 15))
    button.place(relx=0.1, rely=0.8)

    def button_pressed(event):
        timestamp = os.path.getmtime(path)
        datestamp = datetime.fromtimestamp(timestamp)
        if datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) > datestamp:
            new_path = "image.png"
            url = f'https://api.nasa.gov/planetary/apod?api_key={api_key_nasa}'
            result = requests.get(url)
            new_photo_link = result.json()['hdurl']
            new_image = requests.get(new_photo_link)
            new_out = open(new_path, "wb")
            new_out.write(new_image.content)
            new_out.close()
            new_image_size = Image.open(new_path).size
            new_width = new_image_size[0]
            new_height = new_image_size[1]
            if new_width > monitor_width - 50 or new_height > monitor_height - 50:
                new_width = int(new_width / 2)
                new_height = int(new_height / 2)
                image = Image.open(path).resize((new_width, new_height))
                image.save(path)
            new_bg_image = ImageTk.PhotoImage(file=path)
            window.geometry(f'{new_width}x{new_height}')
            label.configure(image=new_bg_image)
            label.image = new_bg_image
        else:
            messagebox.showinfo('Попробуйте позже', 'Фотография и так сегодняшняя, попробуйте позже')

    button.bind('<Button-1>', button_pressed)
    window.mainloop()
