class Library:
    def __init__(self, filename="books.txt"):
        try:
            self.file = open(filename, "a+", encoding="utf-8")
        except FileNotFoundError:
            print("Veritabanı bulunamadı...")
            self.file = open(filename, "a+")


    def __del__(self):
        self.file.close()


    def list_books(self):
        try:
            self.file = open("books.txt", "r", encoding="utf-8")
            lines = self.file.readlines()
            
            lines = [line.strip() for line in lines]

            for line in lines:
                kitap_bilgisi = line.split(",")
                if len(kitap_bilgisi) == 4:
                    kitap_adı, yazar,yıl,sayfa = kitap_bilgisi
                    
                    print(f"\n Kitap adı: {kitap_adı} \n Yazar: {yazar} \n Yıl: {yıl} \n Sayfa: {sayfa}\n")
                else:
                    print(f"Geçersiz format: {line}")

        except Exception:
            print(f"Kitap sistemde bulunamadı.")
            
        self.file.close()
        
    def remove_books(self):
        
        kaldırılacak_kitap = input("Kaldırmak istediğiniz kitabın adını giriniz:")
        try:
            self.file = open("books.txt",r,encoding="utf-8")
            lines = self.file.readlines()
            lines = [line.strip() for line in lines]
            
            for i, line in enumerate(lines):
                
        except Exception:
            print(f"Kitap kaldırılamadı.")
            
    
    def add_books(self):
            
            try:
                self.file = open("books.txt", "a+", encoding="utf-8")
                kitap_adı = input("Kitap adı giriniz: ")
                yazar = input("Yazar adı giriniz: ")
                yıl = int(input("Yayınlanma yılı giriniz: "))
                sayfa = int(input("Sayfa sayısı giriniz: "))

                kitap_bilgisi = f"{kitap_adı},{yazar},{yıl},{sayfa}"
                
                self.file.write(f"{kitap_bilgisi}")
                self.file.write(f"\n")
                print("Kitap eklendi.")

            except ValueError as e:
                print("Kitap geçersiz formatta.", e)
                
            self.file.close()
            

Library()
Library().list_books()
Library().add_books()


