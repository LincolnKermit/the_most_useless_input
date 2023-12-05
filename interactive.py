from pynput import keyboard
import os

os.system("clear")

text = ""

def cursor(text):
    print(text + "_", end='\r')

def on_press(key):
    global text
    try:
        if key == keyboard.Key.enter:
            print()
        elif key == keyboard.Key.backspace:
            text = text[:-1]
            os.system('cls' if os.name == 'nt' else 'clear')
            cursor(text)
        else:
            # Ajoute la lettre au texte
            text += key.char
            os.system('cls' if os.name == 'nt' else 'clear')
            cursor(text)
    except AttributeError:
        pass

text = ""


# Configurer le gestionnaire d'événements du clavier
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
