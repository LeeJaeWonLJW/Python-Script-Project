import keyboard

def print_pressed_keys(e):
    nice = ""
    line = "".join(str(code) for code in keyboard._pressed_events)
    nice += line
    print(nice)
keyboard.hook(print_pressed_keys)
print("Press ESC to stop.")
keyboard.wait('esc')
