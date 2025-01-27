class Decoder: 
    def __init__(self) -> None: ...

    def decode(self, text: str) -> str: 
        text = text.replace("&", "0")
        text = text.replace("*", "1")
        text = text.replace("=", "2")
        text = text.replace("$", "3")
        text = text.replace("@", "4")
        text = text.replace("-", "5")
        text = text.replace("}", "6")
        text = text.replace("{", "7")
        text = text.replace(":", "8")
        text = text.replace("<", "9")

        return "".join([chr(n) for n in list(map(int, text.split("#")))])

