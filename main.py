import time
from pynput import mouse, keyboard

running = False
m = mouse.Controller()
i = 0
def macro():
    global i, running
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


    i += 1
    print("[*] Repetitions done: ". i)

def on_press(key):
    global running
    if key == keyboard.Key.f8:
            running = True
            macro()

def quit(key):
    global running
    if key == keyboard.Key.f7:
        running = False
        print("[*] Quitting.")
        exit(0)




listener = keyboard.Listener(on_press=on_press)
listener2 = keyboard.Listener(on_press=quit)
listener.start()
listener2.start()
print("[*] FischSnail Macro active.")
print("    F8 = run macro | F7 = quit")
listener.join()
listener2.join()
