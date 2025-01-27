class Encoder: 
    def __init__(self) -> None: ...


    def encode(self, text: str) -> str: 
        ascii_text: list[int] = self.encode_to_ascii(text)
        str_ascii_text: str = "#".join(list(map(str, ascii_text)))
        
        str_ascii_text = str_ascii_text.replace("0", "&")
        str_ascii_text = str_ascii_text.replace("1", "*")
        str_ascii_text = str_ascii_text.replace("2", "=")
        str_ascii_text = str_ascii_text.replace("3", "$")
        str_ascii_text = str_ascii_text.replace("4", "@")
        str_ascii_text = str_ascii_text.replace("5", "-")
        str_ascii_text = str_ascii_text.replace("6", "}")
        str_ascii_text = str_ascii_text.replace("7", "{")
        str_ascii_text = str_ascii_text.replace("8", ":")
        str_ascii_text = str_ascii_text.replace("9", "<")

        return str_ascii_text


    def encode_to_ascii(self, text: str) -> list[int]:
        return [ord(s) for s in text]
    

if __name__ == '__main__':
    e = Encoder()
    print(Encoder.encode(e, "hi"))
    print(Encoder.encode(e, "hello"))
    print(Encoder.encode(e, "tyler was gone"))
    print(Encoder.encode(e, "WELCOME BACK"))
    print(Encoder.encode(e, ""))
