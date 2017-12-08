"""
Made by Opatio Co. Ltd. Co CEO Jaewon Lee
2017.11.28 S.KR

Key Hooker
"""

import keyboard

#1 desire shortcut
print('1 : Press and release your desired shortcut: ')
shortcut1 = keyboard.read_shortcut()
print('Shortcut selected:', shortcut1)

#2 desire shortcut
print('2 : Press and release your desired shortcut: ')
shortcut2 = keyboard.read_shortcut()
print('2 : Shortcut selected:', shortcut2)

#3 desire shortcut
print('3 : Press and release your desired shortcut: ')
shortcut3 = keyboard.read_shortcut()
print('3 : Shortcut selected:', shortcut3)

#4 desire shortcut
print('3 : Press and release your desired shortcut: ')
shortcut4 = keyboard.read_shortcut()
print('3 : Shortcut selected:', shortcut4)

#Let's Trigging
def on_triggered():
    keyboard.send('w', do_press=True, do_release=True)

#1 listener
keyboard.add_hotkey(shortcut1, on_triggered)

#2 listener
keyboard.add_hotkey(shortcut2, on_triggered)

#3 listener
keyboard.add_hotkey(shortcut3, on_triggered)

#4 listener
keyboard.add_hotkey(shortcut4, on_triggered)

#Quit
print("Press ESC to stop.")
keyboard.wait('esc')
