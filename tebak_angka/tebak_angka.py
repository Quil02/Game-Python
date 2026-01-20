from utils import clear, option_after_game
from random import randint
from sys import exit


# logika game
def input_number():
    print("Semua nya harus berupa number\n")
    while True:
        try:
            first = int(input("Number minimal : "))
            last = int(input("Number Maksimal : "))
            percobaan = int(input("Maksimal percobaan : "))
            number = int(input("Number yang harus di tebak : "))

        except ValueError:
            clear()
            print("Anda Memasukan input yang SALAH! coba lagi")
        else:
            return first, last, percobaan, number


def number_generator(first, last, percobaan, number=0):
    while True:
        if number == 0:
            number = randint(first, last)
            return first, last, percobaan, number

        elif number != 0:
            if first > number:
                clear()
                print("Number minimal lebih besar dari number yang harus di tebak")
                print("Silahkan buat ulang\n")
                first, last, percobaan, number = input_number()

            elif last < number:
                clear()
                print("Number Maksimal lebih kecil dari number yang harus di tebak")
                print("Silahkan buat ulang\n")
                first, last, percobaan, number = input_number()

            elif first > last:
                clear()
                print("Nilai Min dan Max terbalik")
                print("Silahkan buat ulang\n")
                first, last, percobaan, number = input_number()

            else:
                return first, last, percobaan, number


def game(first, last, percobaan, number):
    while True:
        if percobaan != 0:
            print(f"nomer yang di sembunyikan ada di antara ({first} - {last})")
            print(f"percobaan Anda tersisa {percobaan}")
            tebakan = int(input("Masukan angka tebakan : "))

            if tebakan > number:
                if tebakan < last:
                    last = tebakan
                clear()
                percobaan -= 1
                print("Tebakan anda telalu besar")

            elif tebakan < number:
                if tebakan > first:
                    first = tebakan
                clear()
                percobaan -= 1
                print("Tebakan Anda telalu kecil")

            elif tebakan == number:
                clear()
                print(f"Selamat Anda menang nomor yang di sembutikan adalah {number}")
                option_after_game()
                return

        elif percobaan == 0:
            clear()
            print(f"Anda kalah nomer yang di sembunyikan adalah {number}")
            option_after_game()
            return


# menu game
def menu():
    clear()
    while True:
        print("===Tebak Angka===")
        print("1. Angka Sendiri")
        print("2. 1-10")
        print("3. 1-100")
        print("4. 1-1000\n")
        print("===Pilihan lain nya")
        print("b. Kembali ke menu utama")
        print("q. Keluar dari permainan")

        menu_option = input("Masukan Pilihan : ")

        if menu_option == "1":
            clear()
            input_data = input_number()
            number_data = number_generator(*input_data)
            game(*number_data)
            break

        elif menu_option == "2":
            clear()
            game(*number_generator(1, 10, 3))
            break
        elif menu_option == "3":
            clear()
            game(*number_generator(1, 100, 5))
            break
        elif menu_option == "4":
            clear()
            game(*number_generator(1, 1000, 7))
            break
        elif menu_option == "b":
            return
        elif menu_option == "q":
            exit()
        else:
            print("Input Anda tidak Valid")
            input("Click Apapun untuk melanjutkan...")


if __name__ == "__main__":
    menu()
