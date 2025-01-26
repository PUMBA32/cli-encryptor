import os
import sys

from src.decoder import Decoder  # For encoding text into code
from src.encoder import Encoder  # For decode code into text
from src.history import HistorySaver  # For save history about requests into .json  

# from src.gui import GUI


menu: list[str] = [
    "encode message",
    "decode message",
    "history of requests",
    "exit"
]


def cls() -> None:
    os.system("cls" if sys.platform == 'win32' else "clear")


def show_menu() -> None:
    for i, el in enumerate(menu):
        print(f'[{i+1}] {el}')
    print()


def main() -> None:
    cls()
    print("Welcome to the Ultimate encoder!")
    while 1:
        show_menu()
        inp: str = input(">>> ").strip()

        cls()
        match inp:
            case "1": 
                text: str = input("Enter text to encode: ").strip()
                
                result: str = Encoder.encode(text)  # Encode text into code
                print(f"Result of encoding: {result}\n")
                
                HistorySaver.save("encoding", text, result)  # Saving data about encoding about encoding
            case "2": 
                text: str = input("Enter text to decode: ").strip()
                
                result: str = Decoder.decode(text)  # Decode code into text
                print(f"Result od decoding: {result}\n")
                
                HistorySaver.save("encode", text, result)  # Saving data into json about decoding
            case "3": 
                HistorySaver.show_history()
            case _: break


if __name__ == '__main__':
    main()