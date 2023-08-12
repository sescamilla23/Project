from menu import *


def main():
    application = QApplication([])
    window = Menu()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
