from boardConstructor.BoardsSwitcher import boardsSwitcher

def main():
    # open a board
    global myBoardSwitcher
    myBoardSwitcher = boardsSwitcher()
    myBoardSwitcher.main()


if __name__ == '__main__':
    main()
