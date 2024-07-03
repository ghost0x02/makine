#Bu kod press makinesini uzaktan kontrol edebilen bir GUI kodudur.
#Kodumuzda X-Y-Z entegrasyonu görüyorsunuz, konsol olmadan nasıl çalışır?
#Konsol olmadan klavyenin yön tuşlarından sağ-sol "X" kontrol eder.
#Yukarı-aşağı "Y" kontrol eder.
#Ve son olarak 1-2 tuşları "X" kontrol eder.
#Hidrolik sistemleri koda göre derleyebilirsiniz.
#Bu bir test kodudur makineye bağlanılabilir.

import tkinter as tk
from tkinter import messagebox


x, y, z = 0, 0, 0

def menu():
    print("MENÜYE HOŞ GELDİNİZ")
    messagebox.showinfo("Seçenekler", "PRES MAKİNESİ KONTROL PANELİ AKTİF")

def start_press():
    print("Pres başladı")
    messagebox.showinfo("Başlat", "Pres başladı")

def stop_press():
    print("Pres durdu")
    messagebox.showinfo("Dur", "Pres durdu")

def emergency_stop():
    print("Acil durdurma aktif")
    messagebox.showerror("Acil Durum", "Acil durdurma aktif!")

def cut_option():
    print("Kesim seçeneği seçildi")
    messagebox.showinfo("Kesim", "Kesim seçeneği seçildi")

def stamp_option():
    print("Basım seçeneği seçildi")
    messagebox.showinfo("Basım", "Basım seçeneği seçildi")


def update_coordinates(dx, dy, dz):
    global x, y, z
    x += dx
    y += dy
    z += dz
    coords_label.config(text=f"X: {x}, Y: {y}, Z: {z}")


def on_key_press(event):
    key = event.keysym
    if key == 'Up':
        update_coordinates(0, 1, 0)
    elif key == 'Down':
        update_coordinates(0, -1, 0)
    elif key == 'Left':
        update_coordinates(-1, 0, 0)
    elif key == 'Right':
        update_coordinates(1, 0, 0)
    elif key == '1':
        update_coordinates(0, 0, 1)
    elif key == '2':
        update_coordinates(0, 0, -1)

root = tk.Tk()
root.title("Pres Makinesi Kontrolü")

start_button = tk.Button(root, text="Başlat", command=start_press, bg='white', fg='magenta')
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Dur", command=stop_press, bg='white', fg='magenta')
stop_button.pack(pady=10)

emergency_button = tk.Button(root, text="Acil Durum", command=emergency_stop, bg='red', fg='white')
emergency_button.pack(pady=10)

cut_button = tk.Button(root, text="Kesim", command=cut_option, bg='white', fg='magenta')
cut_button.pack(pady=10)

stamp_button = tk.Button(root, text="Basım", command=stamp_option, bg='white', fg='magenta')
stamp_button.pack(pady=10)

menu_button = tk.Button(root, text="Menu", command=menu, bg='white', fg='magenta')
menu_button.pack(pady=10)

coords_label = tk.Label(root, text=f"X: {x}, Y: {y}, Z: {z}", font=("Helvetica", 16))
coords_label.pack(pady=20)


root.bind('<KeyPress>', on_key_press)

root.mainloop()
