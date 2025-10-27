from src.storage import fayl_oqish, fayl_yozish

def vazifa_qoshish(nomi, tavsif, sana, turkum):
    malumotlar = fayl_oqish()
    yangi_id = malumotlar[-1]["id"] + 1 if malumotlar else 1
    yangi_vazifa = {
        "id": yangi_id,
        "name": nomi,
        "description": tavsif,
        "date": sana,
        "category": turkum,
        "completed": False
    }
    malumotlar.append(yangi_vazifa)
    fayl_yozish(malumotlar)
    print("Vazifa muvaffaqiyatli qo‘shildi.")

def vazifalar_royxati():
    malumotlar = fayl_oqish()
    if not malumotlar:
        print("Hech qanday vazifa yo‘q.")
        return
    for v in malumotlar:
        holat = "✅" if v["completed"] else "❌"
        print(f"{v['id']}. {v['name']} ({v['category']}) - {v['date']} {holat}")

def vazifa_yangilash(vazifa_id, yangi_nomi, yangi_tavsif, yangi_sana, yangi_turkum):
    malumotlar = fayl_oqish()
    topildi = False
    for v in malumotlar:
        if v["id"] == vazifa_id:
            v["name"] = yangi_nomi
            v["description"] = yangi_tavsif
            v["date"] = yangi_sana
            v["category"] = yangi_turkum
            topildi = True
            break
    if topildi:
        fayl_yozish(malumotlar)
        print("Vazifa yangilandi.")
    else:
        print("Bunday ID topilmadi.")

def vazifa_ochirish(vazifa_id):
    malumotlar = fayl_oqish()
    yangilangan = [v for v in malumotlar if v["id"] != vazifa_id]
    if len(yangilangan) == len(malumotlar):
        print("Bunday ID topilmadi.")
    else:
        fayl_yozish(yangilangan)
        print("Vazifa o‘chirildi.")

def bajarilgan_belgilash(vazifa_id):
    malumotlar = fayl_oqish()
    topildi = False
    for v in malumotlar:
        if v["id"] == vazifa_id:
            v["completed"] = True
            topildi = True
            break
    if topildi:
        fayl_yozish(malumotlar)
        print("Vazifa bajarilgan deb belgilandi.")
    else:
        print("Bunday ID topilmadi.")
