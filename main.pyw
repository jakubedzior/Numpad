from pynput.keyboard import Controller, Listener, Key
from pid import PidFile


class Power():
    def __init__(self):
        self.state = False
        self.skip = False

    def change(self):
        if self.state:
            self.state = False
        else:
            self.state = True


def numPad(key):
    if key.char in chars:
        if key.char == chars[0]:
            power.skip = True

            keyboard.press(Key.backspace)
            keyboard.press('0')
            return

        for i, char in enumerate(chars):
            if key.char == char and not power.skip:
                keyboard.press(Key.backspace)
                keyboard.press(str(i))
                break
            if power.skip:
                power.skip = False
                break


def on_press(key):
    try:
        current.add(key.value.vk)
    except AttributeError:
        current.add(key.vk)

    if all(k in current for k in key_comb):
        power.change()
        return

    if power.state:
        try:
            numPad(key)
        except AttributeError:
            pass

def on_release(key):
    try:
        current.remove(key.value.vk)
    except AttributeError:
        current.remove(key.vk)
    except KeyError:
        pass

with PidFile():
    key_comb = [162, 165, 48]
    current = set()
    power = Power()
    chars = ['/', ';', '\'', '\\', 'p', '[', ']', '0', '-', '=']
    keyboard = Controller()

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
