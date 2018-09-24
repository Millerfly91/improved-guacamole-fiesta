from msvcrt import getch
import time
from enum import Enum


class ArrowKey(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 3
    DOWN = 4


class KeyInput:

    @staticmethod
    def getNextsArrowKey():
        key = getch()
        key = getch()
        if key == b'H':
            return ArrowKey.UP
        elif key == b'P':
            return ArrowKey.DOWN
        elif key == b'K':
            return ArrowKey.LEFT
        elif key == b'M':
            return ArrowKey.RIGHT


if __name__ == "__main__":
    while True:
        key = getch()
        # print(key)
        print(KeyInput.getNextsArrowKey())
        # for char in key:
        #     print(char)
        #
        # if str(key) in '\xe0':
        #     print("TRUE")
        # print(key.decode('cp1252', 'replace'))
        time.sleep(.25)
