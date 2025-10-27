import json
import os

fayl_nomi = "database.json"

def fayl_yarat():
    if not os.path.exists(fayl_nomi):
        with open(fayl_nomi, "w", encoding="utf-8") as fayl:
            json.dump([], fayl, indent=4, ensure_ascii=False)

def fayl_oqish():
    fayl_yarat()
    with open(fayl_nomi, "r", encoding="utf-8") as fayl:
        return json.load(fayl)

def fayl_yozish(malumotlar):
    with open(fayl_nomi, "w", encoding="utf-8") as fayl:
        json.dump(malumotlar, fayl, indent=4, ensure_ascii=False)
