class Library:
    def __init__(self, filename="books.txt"):
        try:
            self.file = open(filename, "a+")
        except FileNotFoundError:
            print("File not found, creating new one...")
            self.file = open(filename, "w+")

    def __del__(self):
        self.file.close()

    
Library()