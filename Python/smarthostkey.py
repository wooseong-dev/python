from pynput.keyboard import Key, Listener, KeyCode
#import win32api
#pip install pynput
#

MY_HOT_KEYS = [
    {"function1" : {Key.ctrl_l, Key.alt_l, KeyCode(char="n")}}
]
'''
def function1():
    print("함수1")
    win32api.WinExec("calc.exe")
    win32api.WinExec("C:\\program Files (x86)")
'''
current_keys = set()
def key_pressed(key):
    print("Pressed {}".format(key))
    for data in MY_HOT_KEYS:
        FUNCTION = list(data.keys())[0]
        KEYS = list(data.values())[0]

        if key in KEYS:
            current_keys.add(key)

            if all(k in current_keys for k in KEYS):
                function = eval(FUNCTION)
                function()

def key_released(key):
    print("Released {}".format(key))
    if key in current_keys:
        current_keys.remove(key)
    if key == Key.esc:
        return False

with Listener(on_press = key_pressed, on_release=key_released) as listener:
    listener.join()

    