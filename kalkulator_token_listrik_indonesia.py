# Data Tarif Listrik PLN (Ditulis langsung dalam kode tanpa file/library eksternal)
TARIF_PLN = {
    "1": {"nama": "R-1/TR 450 VA (Subsidi)", "tarif": 415.00, "va": 450},
    "2": {"nama": "R-1/TR 900 VA (Subsidi)", "tarif": 605.00, "va": 900},
    "3": {"nama": "R-1/TR 900 VA RTM (Non-Subsidi)", "tarif": 1352.00, "va": 900},
    "4": {"nama": "R-1/TR 1.300 VA (Non-Subsidi)", "tarif": 1444.70, "va": 1300},
    "5": {"nama": "R-1/TR 2.200 VA (Non-Subsidi)", "tarif": 1444.70, "va": 2200},
    "6": {"nama": "R-2/TR 3.500 VA - 5.500 VA", "tarif": 1699.53, "va": 5500},
    "7": {"nama": "R-3/TR 6.600 VA ke atas", "tarif": 1699.53, "va": 6600},
}

# Data Preset Kategori dan Peralatan Listrik yang Diperluas
KATEGORI_ALAT = {
    "1": {
        "nama_kategori": "Entertainment & Hobi",
        "alat": {
            "1": {"nama": "Televisi (TV LED)", "watt_default": 75, "volt_default": 220},
            "2": {"nama": "Konsol Game (PlayStation / Xbox / Switch)", "watt_default": 150, "volt_default": 220},
            "3": {"nama": "Sound System / Home Theater", "watt_default": 100, "volt_default": 220},
            "4": {"nama": "Komputer / PC Gaming", "watt_default": 350, "volt_default": 220},
            "5": {"nama": "Laptop / Komputer Kerja", "watt_default": 65, "volt_default": 220},
            "6": {"nama": "Proyektor", "watt_default": 200, "volt_default": 220},
        }
    },
    "2": {
        "nama_kategori": "Dapur & Peralatan Kuliner",
        "alat": {
            "1": {"nama": "Kulkas / Lemari Es (1/2 Pintu)", "watt_default": 120, "volt_default": 220},
            "2": {"nama": "Freezer Box", "watt_default": 200, "volt_default": 220},
            "3": {"nama": "Microwave / Oven Listrik", "watt_default": 900, "volt_default": 220},
            "4": {"nama": "Air Fryer", "watt_default": 1000, "volt_default": 220},
            "5": {"nama": "Dispenser Air (Panas/Dingin)", "watt_default": 350, "volt_default": 220},
            "6": {"nama": "Rice Cooker / Magic Com", "watt_default": 400, "volt_default": 220},
            "7": {"nama": "Blender / Juicer", "watt_default": 250, "volt_default": 220},
            "8": {"nama": "Kompor Induksi", "watt_default": 1200, "volt_default": 220},
        }
    },
    "3": {
        "nama_kategori": "Kenyamanan & Kebersihan Rumah",
        "alat": {
            "1": {"nama": "Air Conditioner (AC)", "watt_default": 800, "volt_default": 220},
            "2": {"nama": "Kipas Angin", "watt_default": 45, "volt_default": 220},
            "3": {"nama": "Mesin Cuci", "watt_default": 350, "volt_default": 220},
            "4": {"nama": "Mesin Pengering Pakaian (Dryer)", "watt_default": 1500, "volt_default": 220},
            "5": {"nama": "Vacuum Cleaner (Penyedot Debu)", "watt_default": 600, "volt_default": 220},
            "6": {"nama": "Setrika Listrik", "watt_default": 300, "volt_default": 220},
            "7": {"nama": "Water Heater (Pemanas Air mandi)", "watt_default": 800, "volt_default": 220},
            "8": {"nama": "Pompa Air Listrik", "watt_default": 250, "volt_default": 220},
        }
    },
    "4": {
        "nama_kategori": "Penerangan & Fasilitas Dasar",
        "alat": {
            "1": {"nama": "Lampu LED Utama", "watt_default": 15, "volt_default": 220},
            "2": {"nama": "Lampu Sorot / Taman", "watt_default": 50, "volt_default": 220},
            "3": {"nama": "Router Wi-Fi / Modem", "watt_default": 10, "volt_default": 220},
            "4": {"nama": "Charger HP / Fast Charger", "watt_default": 30, "volt_default": 220},
            "5": {"nama": "Air Purifier / Humidifier", "watt_default": 40, "volt_default": 220},
        }
    }
}

# Subprogram untuk mengubah angka numerik menjadi format mata uang Rupiah (Rp)
def format_rupiah(nominal):
    return f"Rp {nominal:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Subprogram untuk menampilkan dan memilih golongan tarif listrik PLN (termasuk R-1, R-2, dan R-3)
def pilih_tarif():
    print("\n=== PILIH GOLONGAN TARIF PLN ===")
    for kunci, data in TARIF_PLN.items():
        print(f"[{kunci}] {data['nama']} - Rp {data['tarif']}/kWh (Batas {data['va']} VA)")
    
    pilihan = input("Pilih nomor tarif (1-7, default 4): ").strip()
    if pilihan in TARIF_PLN:
        return TARIF_PLN[pilihan]
    else:
        print("Pilihan tidak valid, otomatis memilih R-1/1300 VA.")
        return TARIF_PLN["4"]

# Subprogram untuk menambahkan peralatan listrik, baik dari preset maupun input manual di dalam kategori pilihan
def tambah_peralatan(daftar_alat):
    print("\n=== PILIH KATEGORI PERALATAN LISTRIK ===")
    for kat_key, kat_val in KATEGORI_ALAT.items():
        print(f"[{kat_key}] {kat_val['nama_kategori']}")
    
    kat_pilihan = input("Pilih nomor kategori (1-4): ").strip()

    if kat_pilihan not in KATEGORI_ALAT:
        print("\n[ERROR] Kategori tidak ditemukan.")
        return

    kategori_terpilih = KATEGORI_ALAT[kat_pilihan]
    nama_kategori = kategori_terpilih["nama_kategori"]
    
    print(f"\n--- DAFTAR ALAT: {nama_kategori.upper()} ---")
    for alat_key, alat_val in kategori_terpilih["alat"].items():
        print(f"[{alat_key}] {alat_val['nama']} (Daya Standar: {alat_val['watt_default']}W)")
    print("[M] Input Manual Alat Sendiri (Masuk ke Kategori Ini)")

    alat_pilihan = input("Pilih kode alat atau ketik 'M' untuk manual: ").strip().upper()

    # Opsi Input Manual di dalam Kategori Terpilih
    if alat_pilihan == "M":
        print(f"\n--- INPUT MANUAL: KATEGORI {nama_kategori.upper()} ---")
        nama_alat = input("Masukkan nama peralatan listrik: ").strip()
        if not nama_alat:
            print("\n[ERROR] Nama peralatan tidak boleh kosong.")
            return
        
        try:
            volt_input = input("Masukkan Voltase listrik (Volt, default 220V): ").strip()
            voltase = float(volt_input) if volt_input != "" else 220.0
            watt = float(input("Masukkan Daya Listrik (Watt): "))
            jam = float(input("Masukkan lama pemakaian per hari (Jam): "))
            jumlah = int(input("Masukkan jumlah unit peralatan (default 1): ") or "1")

            if watt > 0 and jam > 0 and jumlah > 0 and voltase > 0:
                alat = {
                    "nama": nama_alat,
                    "kategori": nama_kategori,
                    "voltase": voltase,
                    "watt": watt,
                    "jam": jam,
                    "jumlah": jumlah
                }
                daftar_alat.append(alat)
                print(f"\n[SUKSES] {nama_alat} ({watt:.0f}W, {voltase:.0f}V) berhasil ditambahkan ke kategori '{nama_kategori}'!")
            else:
                print("\n[ERROR] Nilai watt, jam, voltase, dan jumlah harus lebih besar dari 0.")
        except ValueError:
            print("\n[ERROR] Input harus berupa angka valid.")
        return

    # Opsi Memilih Alat dari Preset Kategori
    if alat_pilihan not in kategori_terpilih["alat"]:
        print("\n[ERROR] Kode alat tidak ditemukan.")
        return

    data_preset = kategori_terpilih["alat"][alat_pilihan]
    nama_alat = data_preset["nama"]
    watt_default = data_preset["watt_default"]
    volt_default = data_preset["volt_default"]

    print(f"\n[TERPILIH] {nama_alat} ({nama_kategori})")
    try:
        volt_input = input(f"Masukkan Voltase listrik (Volt, default {volt_default}V): ").strip()
        voltase = float(volt_input) if volt_input != "" else float(volt_default)

        watt_input = input(f"Masukkan Daya Listrik (Watt, default {watt_default}W): ").strip()
        watt = float(watt_input) if watt_input != "" else float(watt_default)

        jam = float(input("Masukkan lama pemakaian per hari (Jam): "))
        jumlah = int(input("Masukkan jumlah unit peralatan (default 1): ") or "1")

        if watt > 0 and jam > 0 and jumlah > 0 and voltase > 0:
            alat = {
                "nama": nama_alat,
                "kategori": nama_kategori,
                "voltase": voltase,
                "watt": watt,
                "jam": jam,
                "jumlah": jumlah
            }
            daftar_alat.append(alat)
            print(f"\n[SUKSES] {nama_alat} ({watt:.0f}W, {voltase:.0f}V) berhasil ditambahkan ke kategori '{nama_kategori}'!")
        else:
            print("\n[ERROR] Input nilai watt, jam, voltase, dan jumlah harus lebih besar dari 0.")
    except ValueError:
        print("\n[ERROR] Input harus berupa angka valid.")

# Subprogram untuk menganalisis pemakaian energi terbesar beserta kategori dan menghasilkan tips penghematan
def analisis_penghematan(daftar_alat, total_kwh_bulanan):
    if not daftar_alat or total_kwh_bulanan == 0:
        return

    print("\n-------------------------------------------------------")
    print("      ANALISIS PENGGUNAAN & SARAN PENGHEMATAN ENERGI   ")
    print("-------------------------------------------------------")

    # Menghitung konsumsi kWh, persentase, dan menyimpan kategori setiap alat
    daftar_analisis = []
    for alat in daftar_alat:
        watt_total = alat["watt"] * alat["jumlah"]
        kwh_bln = (watt_total * alat["jam"] / 1000.0) * 30.0
        persen = (kwh_bln / total_kwh_bulanan) * 100.0 if total_kwh_bulanan > 0 else 0
        daftar_analisis.append({
            "nama": alat["nama"],
            "kategori": alat["kategori"],
            "kwh": kwh_bln,
            "persen": persen,
            "jam": alat["jam"]
        })

    # Mengurutkan alat dari penggunaan kWh tertinggi ke terendah menggunakan perulangan sederhana
    for i in range(len(daftar_analisis)):
        for j in range(i + 1, len(daftar_analisis)):
            if daftar_analisis[i]["kwh"] < daftar_analisis[j]["kwh"]:
                daftar_analisis[i], daftar_analisis[j] = daftar_analisis[j], daftar_analisis[i]

    print("[ALAT DENGAN KONSUMSI ENERGI TERBESAR]")
    for idx, item in enumerate(daftar_analisis[:3], start=1):
        print(f" {idx}. {item['nama']} [Kategori: {item['kategori']}]")
        print(f"    Konsumsi : {item['kwh']:.2f} kWh/bln ({item['persen']:.1f}% dari total tagihan)")

    print("\n[REKOMENDASI PENGHEMATAN ENERGI]")
    saran_diberikan = False
    list_saran = set()

    for item in daftar_analisis:
        nama_lower = item["nama"].lower()
        if ("ac" in nama_lower or "air conditioner" in nama_lower) and "ac" not in list_saran:
            print("• AC: Atur suhu ideal di 24°C-25°C dan manfaatkan timer pemati otomatis.")
            list_saran.add("ac")
            saran_diberikan = True
        elif "kulkas" in nama_lower and "kulkas" not in list_saran:
            print("• Kulkas: Jaga jarak kulkas dari dinding (min 10cm) dan hindari menyimpan makanan panas.")
            list_saran.add("kulkas")
            saran_diberikan = True
        elif ("water heater" in nama_lower or "pemanas air" in nama_lower) and "water_heater" not in list_saran:
            print("• Water Heater: Gunakan timer sakelar agar pemanas tidak menyala terus-menerus selama 24 jam.")
            list_saran.add("water_heater")
            saran_diberikan = True
        elif ("air fryer" in nama_lower or "oven" in nama_lower or "microwave" in nama_lower) and "dapur_pemanas" not in list_saran:
            print("• Microwave/Air Fryer: Cairkan makanan beku di suhu ruang terlebih dahulu sebelum dipanaskan.")
            list_saran.add("dapur_pemanas")
            saran_diberikan = True
        elif "rice cooker" in nama_lower and "rice_cooker" not in list_saran:
            print("• Rice Cooker: Masak nasi menggunakan air hangat agar proses memasak lebih cepat menghemat daya.")
            list_saran.add("rice_cooker")
            saran_diberikan = True
        elif ("tv" in nama_lower or "game" in nama_lower or "komputer" in nama_lower) and "elektronik" not in list_saran:
            print("• Perangkat Elektronik: Cabut steker dari stopkontak saat tidak dipakai untuk menghindari standby power.")
            list_saran.add("elektronik")
            saran_diberikan = True
        elif "setrika" in nama_lower and "setrika" not in list_saran:
            print("• Setrika: Kumpulkan pakaian dan setrika sekaligus dalam satu sesi untuk efisiensi daya pemanasan.")
            list_saran.add("setrika")
            saran_diberikan = True
        elif "dispenser" in nama_lower and "dispenser" not in list_saran:
            print("• Dispenser: Matikan sakelar pemanas/pendingin saat malam hari atau ketika sedang bepergian.")
            list_saran.add("dispenser")
            saran_diberikan = True
        elif "lampu" in nama_lower and "lampu" not in list_saran:
            print("• Lampu: Gunakan lampu LED dan manfaatkan pencahayaan alami matahari di siang hari.")
            list_saran.add("lampu")
            saran_diberikan = True

    if not saran_diberikan:
        print("• Gunakan stopkontak ber-sakelar untuk memutus total daya alat listrik yang sedang tidak digunakan.")
        print("• Hindari penggunaan peralatan listrik berdaya besar secara bersamaan.")

# Subprogram untuk menghitung estimasi pemakaian kWh, biaya listrik, peringatan overload daya, dan ringkasan
def tampilkan_ringkasan(daftar_alat, tarif_info, tipe_layanan, biaya_admin):
    print("\n=======================================================")
    print("           RINGKASAN ESTIMASI BIAYA LISTRIK            ")
    print("=======================================================")
    print(f"Golongan Tarif : {tarif_info['nama']}")
    print(f"Tarif per kWh  : Rp {tarif_info['tarif']:.2f}")
    print(f"Batas Meteran  : {tarif_info['va']} VA")
    print(f"Tipe Layanan   : {tipe_layanan}")
    if tipe_layanan == "Prabayar":
        print(f"Biaya Admin    : {format_rupiah(biaya_admin)}")
    print("-------------------------------------------------------")

    if len(daftar_alat) == 0:
        print("Belum ada peralatan yang ditambahkan.")
        print("=======================================================\n")
        return

    total_watt_serentak = 0
    total_kwh_bulanan = 0

    print(f"{'No':<3} {'Nama Alat':<25} {'Volt':<6} {'Watt':<7} {'Unit':<5} {'Jam/H':<6} {'kWh/Bln':<8}")
    print("-" * 65)

    for idx, alat in enumerate(daftar_alat, start=1):
        watt_total_alat = alat["watt"] * alat["jumlah"]
        kwh_harian = (watt_total_alat * alat["jam"]) / 1000.0
        kwh_bulanan = kwh_harian * 30.0

        total_watt_serentak += watt_total_alat
        total_kwh_bulanan += kwh_bulanan

        print(f"{idx:<3} {alat['nama']:<25} {alat['voltase']:<6.0f} {alat['watt']:<7.0f} {alat['jumlah']:<5} {alat['jam']:<6.1f} {kwh_bulanan:<8.2f}")

    print("-" * 65)
    
    # Perhitungan subtotal pemakaian
    subtotal_pemakaian = total_kwh_bulanan * tarif_info["tarif"]
    
    if tipe_layanan == "Prabayar":
        total_tagihan = subtotal_pemakaian + biaya_admin
    else:
        total_tagihan = subtotal_pemakaian

    print(f"Total Watt Serentak   : {total_watt_serentak:.0f} Watt / Batas {tarif_info['va']} VA")

    # Peringatan Overload Daya Listrik
    if total_watt_serentak > tarif_info["va"]:
        print("-------------------------------------------------------")
        print("[PERINGATAN OVERLOAD!]")
        print(f"Total daya ({total_watt_serentak:.0f} W) melebihi batas meteran ({tarif_info['va']} VA).")
        print("Listrik berisiko jepret jika semua alat menyala bersamaan!")
        print("-------------------------------------------------------")
    else:
        persen_beban = (total_watt_serentak / tarif_info["va"]) * 100
        print(f"Status Kapasitas Daya : AMAN ({persen_beban:.1f}% dari kapasitas meteran)")

    print(f"Total Konsumsi kWh    : {total_kwh_bulanan:.2f} kWh / bulan")
    print(f"Subtotal Pemakaian    : {format_rupiah(subtotal_pemakaian)}")
    
    if tipe_layanan == "Prabayar":
        print(f"Biaya Admin Bank      : {format_rupiah(biaya_admin)}")
        print(f"ESTIMASI ISI TOKEN/BLN: {format_rupiah(total_tagihan)}")
    else:
        print(f"ESTIMASI TAGIHAN/BULAN: {format_rupiah(total_tagihan)}")
    
    print(f"ESTIMASI BIAYA/HARI   : {format_rupiah(total_tagihan / 30.0)}")

    # Menampilkan analisis alat paling boros dan rekomendasi penghematan
    analisis_penghematan(daftar_alat, total_kwh_bulanan)

    print("=======================================================\n")

# Subprogram utama untuk menjalankan antarmuka menu, perulangan aplikasi, dan navigasi fitur
def main():
    daftar_alat = []
    tarif_aktif = TARIF_PLN["4"]  # Default: R-1/1300 VA
    tipe_layanan = "Pascabayar"
    biaya_admin = 2500.0

    berjalan = True
    while berjalan:
        print("=== KALKULATOR BIAYA LISTRIK INDONESIA (SEDERHANA) ===")
        print("1. Tambah Peralatan Listrik (Pilih Kategori & Kode)")
        print("2. Lihat Ringkasan & Total Biaya")
        print("3. Ubah Golongan Tarif PLN")
        print("4. Ubah Tipe Layanan (Pascabayar / Prabayar Token)")
        print("5. Hapus Semua Peralatan")
        print("6. Keluar")

        pilihan = input("\nPilih menu (1-6): ").strip()

        if pilihan == "1":
            tambah_peralatan(daftar_alat)
        elif pilihan == "2":
            tampilkan_ringkasan(daftar_alat, tarif_aktif, tipe_layanan, biaya_admin)
        elif pilihan == "3":
            tarif_aktif = pilih_tarif()
        elif pilihan == "4":
            print("\n--- TIPE LAYANAN LISTRIK ---")
            print("1. Pascabayar (Bayar tagihan bulanan)")
            print("2. Prabayar (Beli Token / Stroom)")
            opsi = input("Pilih tipe layanan (1/2): ").strip()
            if opsi == "2":
                tipe_layanan = "Prabayar"
                admin_in = input("Masukkan biaya admin bank (default 2500): ").strip()
                biaya_admin = float(admin_in) if admin_in != "" else 2500.0
                print("\n[SUKSES] Layanan diubah ke Prabayar (Token).")
            else:
                tipe_layanan = "Pascabayar"
                print("\n[SUKSES] Layanan diubah ke Pascabayar.")
        elif pilihan == "5":
            daftar_alat.clear()
            print("\n[SUKSES] Semua daftar peralatan telah dihapus!")
        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan Kalkulator Biaya Listrik!")
            berjalan = False
        else:
            print("\n[ERROR] Pilihan menu tidak valid. Silakan masukkan angka 1-6.\n")

if __name__ == "__main__":
    main()
