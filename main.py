import time
from pynput import mouse, keyboard
import tkinter as tk

running = False
m = mouse.Controller()
window = tk.Tk()

def window_init():
###########################################################################################################
    global window
    window.title("Fisch Snail Macro")
    window.geometry("400x300")
    window.configure(background="#051730")      #Window
    window.maxsize(400, 300)
    window.minsize(400, 300)                       #Frame
###########################################################################################################
    btn_start = tk.Button(window, text="Start (F8)", bg="green", fg="white", font=("Comic Sans", 12, "bold"), height=1, width=6, command=lambda: start(keyboard.Key.f8))
    btn_start.place(x=65, y=200)                         #Start Button
###########################################################################################################
    btn_end = tk.Button(window, text="End (F7)", bg="red", fg="white", font=("Comic Sans", 12, "bold"), height=1, width=6, command=lambda: quit(keyboard.Key.f7))
    btn_end.place(x=260, y=200)
###########################################################################################################
    ttl = tk.Text(window, height=1, width=16, bg="#051730", fg="white", font=("Comic Sans", 16, "bold"))
    ttl.place(x=110, y=25)
    ttl.insert(tk.END, "Fisch Snail Macro")
###########################################################################################################
    credits = tk.Text(window, height=1, width=16, bg="#051730", fg="light grey", font=("Comic Sans", 9, "bold"))
    credits.place(x=150, y=70)
    credits.insert(tk.END, "By @glitch54932")
###########################################################################################################
    window.mainloop()

def macro():
    global running
    while running:
        print("[*] Macro running...")
        m.press(mouse.Button.left)
        time.sleep(0.35)
        m.release(mouse.Button.left)
        time.sleep(2)
        for _ in range(3):
            m.press(mouse.Button.left)
            time.sleep(0.1)
            m.release(mouse.Button.left)
            time.sleep(0.1)

def start(key):
    global running, window
    if key == keyboard.Key.f8:
            running = True
            window.after(3000, macro)

def quit(key):
    global running
    if key == keyboard.Key.f7:
        running = False
        print("[*] Quitting.")
        exit(0)


if "__main__" == __name__:

    listener = keyboard.Listener(on_press=start)
    listener2 = keyboard.Listener(on_press=quit)
    listener.start()
    listener2.start()
    print("[*] Fisch Snail Macro active.")
    print("    F8 = run macro | F7 = quit")
    window_init()
    listener.join()
    listener2.join()
