def main():
    print('salom')
    

from src.commands import (
    vazifa_qoshish,
    vazifalar_royxati,
    vazifa_yangilash,
    vazifa_ochirish,
    bajarilgan_belgilash
)

def menyu():
    while True:
        print("\n--- TODO CLI ---")
        print("1. Vazifa qoshish")
        print("2. Vazifalarni korish")
        print("3. Vazifani yangilash")
        print("4. Vazifani ochirish")
        print("5. Bajarilgan deb belgilash")
        print("6. Chiqish")
        tanlov = input("Tanlovni kiriting (1-6): ")

        if tanlov == "1":
            nomi = input("Vazifa nomi: ")
            tavsif = input("Tavsif: ")
            sana = input("Sana (YYYY-MM-DD): ")
            turkum = input("Turkum: ")
            vazifa_qoshish(nomi, tavsif, sana, turkum)
        elif tanlov == "2":
            vazifalar_royxati()
        elif tanlov == "3":
            try:
                id_raqam = int(input("Yangilanishi kerak bolgan ID: "))
                yangi_nomi = input("Yangi nomi: ")
                yangi_tavsif = input("Yangi tavsif: ")
                yangi_sana = input("Yangi sana: ")
                yangi_turkum = input("Yangi turkum: ")
                vazifa_yangilash(id_raqam, yangi_nomi, yangi_tavsif, yangi_sana, yangi_turkum)
            except ValueError:
                print("ID raqam bolishi kerak.")
        elif tanlov == "4":
            try:
                id_raqam = int(input("Ochiriladigan ID: "))
                vazifa_ochirish(id_raqam)
            except ValueError:
                print("ID raqam bolishi kerak.")
        elif tanlov == "5":
            try:
                id_raqam = int(input("Bajarilgan deb belgilanadigan ID: "))
                bajarilgan_belgilash(id_raqam)
            except ValueError:
                print("ID raqam bolishi kerak.")
        elif tanlov == "6":
            print("Dastur yakunlandi.")
            break
        else:
            print("Notogri tanlov.")
