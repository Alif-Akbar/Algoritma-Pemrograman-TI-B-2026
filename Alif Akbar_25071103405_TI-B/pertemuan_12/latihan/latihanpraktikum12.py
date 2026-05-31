struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
            },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
                }
            },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                    }
                }
            },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
            },
        "README.txt": 8
        }
    }

def total_ukuran(folder):
    total = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            total += total_ukuran(value)
        else:
            total += value
    return total

def hitung_file(folder):
    count = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            count += hitung_file(value)
        else:
            count += 1
    return count

def cari_terbesar(folder: dict):
    terbesar = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            terbesar = max(terbesar, cari_terbesar(value))
        else:
            terbesar = max(terbesar, value)
    return terbesar

def tampilkan_hirarki(folder, indent=0):
    for key, value in folder.items():
        print(" " * indent + key)
        if isinstance(value, dict):
            tampilkan_hirarki(value, indent + 4)
        else:
            print(" " * (indent + 4) + f"({value} KB)")


print("Total ukuran file:", total_ukuran(struktur))
print("Jumlah file:", hitung_file(struktur))
print("Ukuran file terbesar:", cari_terbesar(struktur))
print("\nHirarki folder:")
tampilkan_hirarki(struktur)