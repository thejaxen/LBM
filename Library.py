class Library:
    def __init__(self, filename="books.txt"):
        try:
            self.file = open(filename, "a+", encoding="utf-8") #Dosyayı a+ modunda açıyorum.
        except FileNotFoundError:
            print("Veritabanı bulunamadı...")
            self.file = open(filename, "a+")#Dosyayı açmayı tekrar deniyorum.

    def __del__(self):
        self.file.close()#Dosyayı kapatma işlemini gerçekleştiriyorum.

    def list_books(self):
        try:
            self.file = open("books.txt", "r", encoding="utf-8") #Dosyayı okuma modunda açıyorum.
            lines = self.file.readlines()#Her bir satırı tekrar tekrar okuyorum
            
            lines = [line.strip() for line in lines]#Okuduğum satırları düzenleyip listeme aktarıyorum.

            for line in lines: #Listedeki her satır için tekrardan satır içi iterasyon uloşturuyorum.
                kitap_bilgisi = line.split(",")#Satır içi elementlerimi virgüllerden kurtarıyorum ve kitap bilgisi değişkenime atıyorum.
                if len(kitap_bilgisi) == 4:#Satır içi elementlerimin sayısı 4 ise bunu geçerli format sayıyorum.
                    kitap_adı, yazar,yıl,sayfa = kitap_bilgisi#Satır içi elementlerimi yeni değişkenlerime atadım.
                    print(f"\n Kitap adı: {kitap_adı} \n Yazar: {yazar} \n Yıl: {yıl} \n Sayfa: {sayfa}\n")#Satır içindeki değişkenlerimi terminale yazdırıyorum.
                else:
                    print(f"Geçersiz format: {line}")#Herhangi bir satır içi element sayısı 4 ten fazla olduğunda geçersiz format olduğu için direkt satır olarak yazdırıyorum.

        except Exception:
            print(f"Kitaplar sistemde bulunamadı.")#Dosyayı açamadıysak demekki elimizde kitapta yok demektir. Bunu da yazdırıyoruz.
            
        self.file.close()#Dosyayla işim bittiği için kapatıyorum.

    def remove_books(self):

        kaldırılacak_kitap = input("Kaldırmak istediğiniz kitabın adını giriniz:")#Kaldırılacak kitabın adını kullanıcıdan alıyorum.
    
        try:
            with open("books.txt", "r", encoding="utf-8") as file:#Dosyayı okuma modunda açıyorum.
                lines = file.readlines()#Dosyadaki her satırı okuyorum.
                lines = [line.strip() for line in lines]#Ara boşlukları ortadan kaldırıyorum.

            filtered_lines = [line for line in lines if line.split(",")[0] != kaldırılacak_kitap]#Eğer satırımdaki satır içi elementlerimden ilki kaldırmak istediğim kitapla eşleşme yakalarsa filtreleyerek yeni liste oluşturuyorum, yakalamazsada olutşturuyorum.

            if len(filtered_lines) == len(lines):#Yeni listemdeki uzunluk eski listemle aynı ise eşleşme olmamıştır. Kaldırılacak kitap yok demektir.
                print("Kaldırılacak kitap bulunamadı")
            else:
                with open("books.txt", "w", encoding="utf-8") as file:#Dosyayı değiştirmek için yazma modunda açıyorum.
                    file.write('\n'.join(filtered_lines))#Yeni listemi tekrardan yazdırıyorum.
                    print("Kitap başarıyla kaldırıldı.")
                
        except Exception as e:
            print(f"Bir problem yaşandı: {e}")
            
    def add_books(self):
            
            try:
                self.file = open("books.txt", "a+", encoding="utf-8")#Yeni kitabı sona eklemek için sonu işaret eden pointerı kullanan a+ modunda açıyorum.
                kitap_adı = input("Kitap adı giriniz: ")
                yazar = input("Yazar adı giriniz: ")
                yıl = int(input("Yayınlanma yılı giriniz: "))
                sayfa = int(input("Sayfa sayısı giriniz: "))

                kitap_bilgisi = f"{kitap_adı},{yazar},{yıl},{sayfa}"#Kullanıcıdan aldığım bilgileri kitap_bilgisi değişkenime atıyorum.
                
                self.file.write(f"\n{kitap_bilgisi}")#Yeni kitabımı dosyamın içine yazdırıyorum.
                
                print("Kitap eklendi.")

            except ValueError as e:
                print("Kitap geçersiz formatta.", e)
                
            self.file.close()
            
lib = Library()

def main_menu():
        
    while True:

        print(f"\n*** MENU ***")
        print("1) Kitapları listele.")
        print("2) Kitap ekle.")
        print("3) Kitap kaldır.")

        print(f"\n")

        choice = input("İşlem seçin:")
            
        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_books()
        elif choice == '3':
            lib.remove_books()
        elif choice.lower() == 'q':
            print("İşlem sonlandırıldı.")
            break
        else:
            print("Geçersiz işlem.")

main_menu()
        




