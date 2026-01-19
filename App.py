from Hangman.Hangman import menu as hangman_menu
import Hangman.Data

from bgk.App import menu as bgk_menu

from utils import clear

clear()


def main_menu():
    while True:
        pilihan = input("halo t : ")

        if pilihan == "t":
            bgk_menu()
        else:
            return


if __name__ == "__main__":
    main_menu()
