print("-------------------------------------------------")
print("                PENGINGAT by Aul!            ")
print("-------------------------------------------------")

while True:
    try:
        jam = int(input("Masukkan jam (0-23):  "))
        if not (0 <= jam <= 23):
            print("Error: Jam harus antara 0 dan 23. Silahkan coba lagi!")
            continue
    except ValueError:
        print("Error: Input harus berupa angka. Coba Lagi!")
        continue

    if 5 <= jam < 11:
        print("Pagiii! jangan lupa sarapan")
    elif 11 <= jam < 15:
        print("Jangan lupa makan siang yaa!")
    elif 15 <= jam < 18:
        print("Soree! ngemil kayaknya enak")
    elif 18 <= jam < 23:
        print("Jangan lupa makan malam yaa!")
    else:
        print("Tidur!! Tidak boleh begadang!")
        break


