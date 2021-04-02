from os import system as cmd
from time import sleep
import ctypes
import random
import string
import platform
from colorama import Fore, init

ctypes.windll.kernel32.SetConsoleTitleW(
    "Discord Nitro Generator | Tayzzz | v1.0")
init(convert=True)


def main():

    clear_console()

    print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Nitro Generator made by {Fore.WHITE}Tayzzz{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License | {Fore.WHITE}This tool is for educational purposes only{Fore.RESET}")
    print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You can follow me on Github: {Fore.WHITE}https://github.com/Tayzzz{Fore.RESET}")

    try:
        amount = int(input(
            f"\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}How much codes will be generated: {Fore.WHITE}"))

        nitro = input(
            f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}What kind of nitro do you want ? {Fore.WHITE}classic {Fore.LIGHTBLACK_EX}or {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}? (Classic Nitro is 16chars and Boost Nitro is 24chars): {Fore.WHITE}")

        link = input(
            f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Do you want {Fore.WHITE}https://discord.com/gifts/ {Fore.LIGHTBLACK_EX}behind the code ? ({Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no): {Fore.WHITE}")
        if "boost" in nitro or "classic" in nitro:
            pass
        else:
            print(
                f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}or {Fore.WHITE}classic")
            sleep(3)
            exit()

        if "yes" in link or "no" in link:
            pass
        else:
            print(
                f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no")
            sleep(3)
            exit()
    except ValueError:
        print(
            f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Amount must be {Fore.WHITE}a number")
        sleep(3)
        clear_console()
        exit()
    except KeyboardInterrupt:
        clear_console()
        exit()

    a = 0
    nitros = open("nitro.txt", "w")
    nitros.write("")

    print()

    while a != amount:
        try:
            a += 1
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Discord Nitro Generator | {a-1} nitro(s) generated")

            if "classic" in nitro:
                code = "".join(random.choice(string.digits+string.ascii_letters)
                               for _ in range(16))
            else:
                code = "".join(random.choice(string.digits+string.ascii_letters)
                               for _ in range(24))
            if link == "yes":
                msg = f"https://discord.com/gifts/{code}"
            else:
                msg = code

            print(
                f"{Fore.WHITE}[ {Fore.YELLOW}- {Fore.WHITE}] {msg}")

            if a == amount:
                nitros.write(f"{msg}")
            else:
                nitros.write(f"{msg}\n")

        except KeyboardInterrupt:
            nitros.close()
            input(
                f"\n{Fore.WHITE}[ {Fore.GREEN}> {Fore.WHITE}] {len(open('nitro.txt').readlines())} nitros have been generated. (Press any key to close the generator)")
            exit()

    nitros.close()
    for line in open('nitro.txt').readlines():
        line.strip("\n")
    ctypes.windll.kernel32.SetConsoleTitleW(
        f"Discord Nitro Generator | Done !")

    input(
        f"\n{Fore.WHITE}[ {Fore.GREEN}> {Fore.WHITE}] {a} nitros have been generated. (Press any key to close the generator)")
    exit()


def clear_console():
    if platform.system() == "Windows":
        cmd("cls")
    else:
        cmd("clear")


if __name__ == "__main__":
    main()
