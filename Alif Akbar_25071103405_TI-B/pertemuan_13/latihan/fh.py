import os

def tampilkan_menu():
    print("==========================")
    print("PYTHON FILE MANAGER v1.0")
    print("==========================")
    print("[1] Read File")
    print("[2] Write File")
    print("[3] Delete File")
    print("[4] Append File")
    print("[5] Search Files")
    print("[0] Exit")

def baca_file():
    print(f"\nFile Tersedia:")
    list_file = []
    for filename in os.listdir():
        if os.path.isfile(filename) and filename.endswith(".txt"):
            list_file.append((filename, os.path.getsize(filename)))

    if not list_file:
        print("Tidak ada file .txt yang tersedia.")
        return
    for i, filename in enumerate(list_file, start=1):
        print(f"[{i}] {filename} ")
    
    try:        
        pilihan = int(input("Pilih file yang ingin dibaca: ")) - 1
        if 0 <= pilihan < len(list_file):
            nama_file = list_file[pilihan]
            with open(nama_file, "r") as f:
                isi = f.read()
            print(f"\nIsi file '{nama_file}':\n{isi}")
        else:
            print("File tidak ditemukan.")
    except ValueError:
        print("Input tidak valid.")


def tulis_file():
    print(f"\nFile Tersedia:")
    list_file = []
    for filename in os.listdir():
        if os.path.isfile(filename) and filename.endswith(".txt"):
            list_file.append(filename)

    if not list_file:
        print("Tidak ada file .txt yang tersedia.")
        return

    for i, filename in enumerate(list_file, start=1):
        print(f"[{i}] {filename}")

    try:
        pilihan = int(input("Pilih file yang ingin ditulis: ")) - 1
        if 0 <= pilihan < len(list_file):
            isi = input(f"Masukkan isi untuk file '{list_file[pilihan]}': ")
            with open(list_file[pilihan], "w") as f:
                f.write(isi)
            print(f"File '{list_file[pilihan]}' berhasil ditulis.")
        else:
            print("File tidak ditemukan. Apakah Anda ingin membuat file baru? (y/n)")
            if input().lower() == 'y':
                nama_file = input("Masukkan nama file baru (dengan ekstensi .txt): ")
                isi = input(f"Masukkan isi untuk file '{nama_file}': ")
                with open(nama_file, "w") as f:
                    f.write(isi)
                print(f"File '{nama_file}' berhasil dibuat dan ditulis.")
            else:
                print("Operasi dibatalkan.")
    except ValueError:
        print("Input tidak valid.")
    except PermissionError:
        print("Anda tidak memiliki izin untuk menulis file ini.")
    except FileNotFoundError:
        print("File tidak ditemukan.")

def hapus_file():
    print(f"\nFile Tersedia:")
    list_file = []
    for filename in os.listdir():
        if os.path.isfile(filename) and filename.endswith(".txt"):
            list_file.append(filename)

    if not list_file:
        print("Tidak ada file .txt yang tersedia.")
        return

    for i, filename in enumerate(list_file, start=1):
        print(f"[{i}] {filename}")

    try:
        pilihan = int(input("Pilih file yang ingin dihapus: ")) - 1
        if 0 <= pilihan < len(list_file):
            os.remove(list_file[pilihan])
            print(f"File '{list_file[pilihan]}' berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input tidak valid.")
    except PermissionError:
        print("Anda tidak memiliki izin untuk menghapus file ini.")
    except FileNotFoundError:
        print("File tidak ditemukan.")

def append_file():
    print(f"\nFile Tersedia:")
    list_file = []
    for filename in os.listdir():
        if os.path.isfile(filename) and filename.endswith(".txt"):
            list_file.append(filename)

    if not list_file:
        print("Tidak ada file .txt yang tersedia.")
        return

    for i, filename in enumerate(list_file, start=1):
        print(f"[{i}] {filename} ")

    try:
        pilihan = int(input("Pilih file yang ingin di-append: ")) - 1
        if 0 <= pilihan < len(list_file):
            isi = input(f"Masukkan isi untuk file '{list_file[pilihan]}': ")
            with open(list_file[pilihan], "a") as f:
                f.write(isi)
            print(f"File '{list_file[pilihan]}' berhasil di-append.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input tidak valid.")
    except PermissionError:
        print("Anda tidak memiliki izin untuk menulis tambahan file ini.")
    except FileNotFoundError:
        print("File tidak ditemukan.")

def search_files():
    keyword = input("Masukkan keyword untuk mencari file: ")
    hasil_pencarian = []
    for filename in os.listdir():
        if os.path.isfile(filename) and filename.endswith(".txt") and keyword in filename:
            hasil_pencarian.append(filename)

    if hasil_pencarian:
        print(f"\nHasil pencarian untuk '{keyword}':")
        for i, filename in enumerate(hasil_pencarian, start=1):
            size = os.path.getsize(filename)
            print(f"[{i}] {filename} ({size} bytes)")
    else:
        print(f"Tidak ditemukan file dengan keyword '{keyword}'.")

# Perulangan agar menu muncul terus sampai memilih keluar
while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        baca_file()
    elif pilihan == "2":
        tulis_file()
    elif pilihan == "3":
        hapus_file()
    elif pilihan == "4":
        append_file()
    elif pilihan == "5":
        search_files()
    elif pilihan == "0":
        print("Terima kasih telah menggunakan Python File Manager.")
        break
    else:
        print("Pilihan tidak valid.")