import sys
import os
from pathlib import Path
from colorama import Fore, Style


def visualize_directory(directory):
    directory = Path(directory)
    if not directory.is_dir():
        print(f"{Fore.RED}Error:{Style.RESET_ALL} The specified path is not a directory.")
        return

    print(f"{Fore.BLUE}Directories:{Style.RESET_ALL}")
    for item in directory.iterdir():
        if item.is_dir():
            print(f"{Fore.BLUE}{item.name}{Style.RESET_ALL}/")

    print(f"\n{Fore.GREEN}Files:{Style.RESET_ALL}")
    for item in directory.iterdir():
        if item.is_file():
            print(f"{Fore.GREEN}{item.name}{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Please provide the directory path as argument.")
        sys.exit(1)

    directory_path = sys.argv[1]
    visualize_directory(directory_path)
