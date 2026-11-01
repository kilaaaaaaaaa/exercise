def tarif_parkir(jenis, jam_masuk, jam_keluar):
    lama_parkir = jam_keluar - jam_masuk

    if lama_parkir < 0:
        lama_parkir = lama_parkir + 24

    if jenis == "mobil":
        tarif = lama_parkir * 3000
        if tarif > 24000:
            tarif = 24000

    elif jenis == "motor":
        tarif = lama_parkir * 1000
        if tarif > 12000:
            tarif = 12000

    else:
        tarif = -1

    return tarif

jenis = input("Masukkan jenis kendaraan (mobil/motor): ")
jam_masuk = int(input("Masukkan jam masuk (0-23): "))
jam_keluar = int(input("Masukkan jam keluar (0-23): "))

hasil = tarif_parkir(jenis, jam_masuk, jam_keluar)

print("Tarif parkir: Rp", hasil)