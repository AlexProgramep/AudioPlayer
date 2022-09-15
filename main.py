import os
from tkinter import filedialog, messagebox, Tk, Menu, Button
from pygame import mixer

root = Tk()
root.title("Музикальний плеєр")
mixer.init()
main_menu = Menu()


def open_audio():
    try:
        music = filedialog.askopenfilename()
        mixer.music.load(music)
        root.title(os.path.basename(music))
    except:
        messagebox.showerror("Помилка", "Можливо, файл не в звуковому форматі або битий або ви скасували пошук..")


def audio_start():
    try:
        mixer.music.play()
    except:
        messagebox.showerror("Помилка", "Ви не завантажили файл.")


def audio_continue():
    mixer.music.unpause()


def audio_stop():
    mixer.music.pause()


def help():
    messagebox.showinfo("Інформація", """Load - завантаження звукового файлу.
Start - включає файл (при повторному натисканні файл стартує заново).
Stop - ставить на паузу відтворення.
Continue - відновлює відтворення.""")


message_button = Button(text="Load", background="#555", foreground="#fff", command=open_audio)
message_button.place(x=0)

message_button1 = Button(text="Start", background="#555", foreground="#fff", command=audio_start)
message_button1.place(x=45)

message_button2 = Button(text="Continue", background="#555", foreground="#fff", command=audio_continue)
message_button2.place(x=90)

message_button3 = Button(text="Stop", background="#555", foreground="#fff", command=audio_stop)
message_button3.place(x=160)

main_menu.add_cascade(label="Інформація", command=help)

if __name__ == "__main__":
    root.config(menu=main_menu)
    root.mainloop()
