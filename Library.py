class Library:
    def __init__(self, filename="books.txt"):
        try:
            self.file = open(filename, "a", encoding="utf-8")
        except FileNotFoundError:
            print("Veritabanı bulunamadı...")
            self.file = open(filename, "w+")


    def __del__(self):
        self.file.close()


    def list_books(self):
          
        try:
            lines = self.file.readlines()
            
            lines = [line.strip() for line in lines]

            for line in lines:
                kitap_bilgisi = line.split(",")
                if len(kitap_bilgisi) == 4:
                    kitap_adı, yazar,yıl,sayfa = kitap_bilgisi
                    print(f"\nKitap adı: {kitap_adı} \nYazar: {yazar} \nYıl: {yıl} \nSayfa: {sayfa} \n")
                else:
                    print(f"Geçersiz format: {line}")

        except Exception as e:
            print(f"Kitap sistemde bulunamadı {e}")
            
    
    def add_books(self):
            
            try:
                kitap_adı = input("Kitap adı giriniz: ")
                yazar = input("Yazar adı giriniz: ")
                yıl = int(input("Yayınlanma yılı giriniz: "))
                sayfa = int(input("Sayfa sayısı giriniz: "))

                kitap_bilgisi = f"{kitap_adı},{yazar},{yıl},{sayfa}"
                self.file.write(f"{kitap_bilgisi}")
                print("Kitap eklendi.")

            except ValueError as e:
                print("Kitap geçersiz formatta.", e)
            

Library()
Library().list_books()
Library().add_book()