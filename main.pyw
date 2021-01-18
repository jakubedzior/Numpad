from pynput.keyboard import Controller, Listener, Key


class Power():

    def __init__(self):
        self.state = False
        self.skip = False

    def change(self):
        if self.state:
            self.state = False
        else:
            self.state = True


def num_pad(key):
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
        if power.state:
            num_pad(key)
        if key.char == '$':
            keyboard.press(Key.backspace)
            power.change()

    except AttributeError:
        pass


with open('state.txt', 'w+') as f:
    if f.read() == 'True':
        exit()
    f.write('True')

power = Power()
chars = ['/', ';', '\'', '\\', 'p', '[', ']', '0', '-', '=']

keyboard = Controller()
with Listener(on_press=on_press) as listener:
    listener.join()
