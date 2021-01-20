from pynput.mouse import Controller as Mouse
from pynput.mouse import Button as bt
from pynput.keyboard import Controller as Keyboard
from pynput.keyboard import Key


def changeWindow(kb):
    kb.press(Key.cmd)
    kb.press(Key.tab)
    kb.release(Key.cmd)
    kb.release(Key.tab)


def TellHer(ms, kb):
    # ms.position = ms.
    # ms.press(bt.left)
    # ms.release(bt.left)
    kb.type("nihao")
    kb.press(Key.space)
    kb.release(Key.space)
    # kb.press(Key.shift)
    # kb.release(Key.shift)
    kb.press(Key.space)
    kb.release(Key.space)
    kb.type("nihao")
    kb.press(Key.space)
    kb.release(Key.space)
    kb.press(Key.space)
    kb.release(Key.space)
    kb.press(Key.enter)
    kb.release(Key.enter)
    # kb.press(Key.shift)
    # kb.release(Key.shift)
    # time.sleep(0.3)


def main():
    ms = Mouse()
    kb = Keyboard()
    # changeWindow(kb)
    for i in range(200):
        TellHer(ms, kb)
        # kb.type("^v")
        # kb.press(Key.cmd)


if __name__ == '__main__':
    main()
