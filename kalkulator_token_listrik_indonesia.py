# Data Tarif Listrik PLN 
TARIF_PLN = {
    "1": {"nama": "R-1/TR 450 VA (Subsidi)", "tarif": 415.00, "va": 450},
    "2": {"nama": "R-1/TR 900 VA (Subsidi)", "tarif": 605.00, "va": 900},
    "3": {"nama": "R-1/TR 900 VA RTM (Non-Subsidi)", "tarif": 1352.00, "va": 900},
    "4": {"nama": "R-1/TR 1.300 VA (Non-Subsidi)", "tarif": 1444.70, "va": 1300},
    "5": {"nama": "R-1/TR 2.200 VA (Non-Subsidi)", "tarif": 1444.70, "va": 2200},
    "6": {"nama": "R-2/TR 3.500 VA - 5.500 VA", "tarif": 1699.53, "va": 5500},
}

# Data Pajak Penerangan Jalan (PPJ) per Daerah
DATA_PPJ = {
    "1": {"daerah": "DKI Jakarta", "persen": 2.4},
    "2": {"daerah": "Kota Bandung", "persen": 6.0},
    "3": {"daerah": "Kota Surabaya", "persen": 8.0},
    "4": {"daerah": "Kota Semarang", "persen": 10.0},
    "5": {"daerah": "Kota Medan", "persen": 10.0},
    "6": {"daerah": "Luar Daerah / Lainnya", "persen": 5.0},
}

def format_rupiah(nominal):
    """Subprogram sederhana untuk memformat angka menjadi format Rupiah"""
    return f"Rp {nominal:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def pilih_tarif():
    """Subprogram untuk memilih golongan tarif listrik PLN"""
    print("\n=== PILIH GOLONGAN TARIF PLN ===")
    for kunci, data in TARIF_PLN.items():
        print(f"[{kunci}] {data['nama']} - Rp {data['tarif']}/kWh (Batas {data['va']} VA)")
    
    pilihan = input("Pilih nomor tarif (1-6, default 4): ").strip()
    if pilihan in TARIF_PLN:
        return TARIF_PLN[pilihan]
    else:
        print("Pilihan tidak valid, otomatis memilih R-1/1300 VA.")
        return TARIF_PLN["4"]

def pilih_daerah():
    """Subprogram untuk memilih wilayah/daerah PPJ"""
    print("\n=== PILIH WILAYAH (PAJAK PPJ) ===")
    for kunci, data in DATA_PPJ.items():
        print(f"[{kunci}] {data['daerah']} (PPJ: {data['persen']}%)")
    
    pilihan = input("Pilih nomor daerah (1-6, default 6): ").strip()
    if pilihan in DATA_PPJ:
        return DATA_PPJ[pilihan]
    else:
        print("Pilihan tidak valid, otomatis memilih Luar Daerah (5%).")
        return DATA_PPJ["6"]

def tambah_peralatan(daftar_alat):
    """Subprogram untuk memasukkan input user ke dalam array (list)"""
    print("\nTAMBAH PERALATAN LISTRIK")
    nama = input("Masukkan nama peralatan (misal: AC Kamar): ").strip()
    if nama == "":
        nama = "Peralatan Tanpa Nama"
    
    try:
        watt = float(input("Masukkan daya listrik (Watt): "))
        jam = float(input("Masukkan lama pemakaian per hari (Jam): "))
        jumlah = int(input("Masukkan jumlah unit peralatan (default 1): ") or "1")

        if watt > 0 and jam > 0 and jumlah > 0:
            # Simpan data ke array sebagai dictionary
            alat = {
                "nama": nama,
                "watt": watt,
                "jam": jam,
                "jumlah": jumlah
            }
            daftar_alat.append(alat)
            print(f"\n[SUKSES] {nama} berhasil ditambahkan!")
        else:
            print("\n[ERROR] Input watt, jam, dan jumlah harus lebih besar dari 0.")
    except ValueError:
        print("\n[ERROR] Input harus berupa angka valid.")

def tampilkan_ringkasan(daftar_alat, tarif_info, ppj_info, tipe_layanan, biaya_admin):
    """Subprogram untuk menghitung total biaya dan menampilkan ringkasan"""
    print("\n=======================================================")
    print("           RINGKASAN ESTIMASI BIAYA LISTRIK            ")
    print("=======================================================")
    print(f"Golongan Tarif : {tarif_info['nama']}")
    print(f"Tarif per kWh  : Rp {tarif_info['tarif']:.2f}")
    print(f"Batas Meteran  : {tarif_info['va']} VA")
    print(f"Wilayah / PPJ  : {ppj_info['daerah']} ({ppj_info['persen']}%)")
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

    print(f"{'No':<3} {'Nama Alat':<18} {'Watt':<7} {'Unit':<5} {'Jam/H':<6} {'kWh/Bln':<8}")
    print("-" * 55)

    # Perulangan FOR untuk memproses array daftar peralatan
    for idx, alat in enumerate(daftar_alat, start=1):
        watt_total_alat = alat["watt"] * alat["jumlah"]
        kwh_harian = (watt_total_alat * alat["jam"]) / 1000.0
        kwh_bulanan = kwh_harian * 30.0

        total_watt_serentak += watt_total_alat
        total_kwh_bulanan += kwh_bulanan

        print(f"{idx:<3} {alat['nama']:<18} {alat['watt']:<7.0f} {alat['jumlah']:<5} {alat['jam']:<6.1f} {kwh_bulanan:<8.2f}")

    print("-" * 55)
    
    # Perhitungan rumus biaya dasar
    subtotal_pemakaian = total_kwh_bulanan * tarif_info["tarif"]
    biaya_ppj = subtotal_pemakaian * (ppj_info["persen"] / 100.0)
    
    # Percabangan IF-ELSE untuk menghitung total biaya berdasarkan tipe layanan
    if tipe_layanan == "Prabayar":
        total_tagihan = subtotal_pemakaian + biaya_ppj + biaya_admin
    else:
        total_tagihan = subtotal_pemakaian + biaya_ppj

    # Menampilkan total daya serentak dan batas meteran
    print(f"Total Watt Serentak   : {total_watt_serentak:.0f} Watt / Batas {tarif_info['va']} VA")

    # Percabangan IF-ELSE untuk Peringatan Daya Maksimum (Overload)
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
    print(f"Pajak PPJ ({ppj_info['persen']}%)        : {format_rupiah(biaya_ppj)}")
    
    if tipe_layanan == "Prabayar":
        print(f"Biaya Admin Bank      : {format_rupiah(biaya_admin)}")
        print(f"ESTIMASI ISl TOKEN/BLN: {format_rupiah(total_tagihan)}")
    else:
        print(f"ESTIMASI TAGIHAN/BULAN: {format_rupiah(total_tagihan)}")
    
    print(f"ESTIMASI BIAYA/HARI   : {format_rupiah(total_tagihan / 30.0)}")
    print("=======================================================\n")

def main():
    """Subprogram utama (entry point) aplikasi"""
    # Inisialisasi array dan variabel awal
    daftar_alat = []
    tarif_aktif = TARIF_PLN["4"]  # Default: R-1/1300 VA
    ppj_aktif = DATA_PPJ["6"]      # Default: Luar Daerah 5%
    tipe_layanan = "Pascabayar"
    biaya_admin = 2500.0

    # Perulangan WHILE untuk menjaga menu interaktif tetap aktif
    berjalan = True
    while berjalan:
        print("")
        print("KALKULATOR BIAYA LISTRIK INDONESIA (Beta) ")
        print("1. Tambah Peralatan Listrik")
        print("2. Lihat Ringkasan & Total Biaya")
        print("3. Ubah Golongan Tarif PLN")
        print("4. Ubah Wilayah (Pajak PPJ)")
        print("5. Ubah Tipe Layanan (Pascabayar / Prabayar Token)")
        print("6. Hapus Semua Peralatan")
        print("7. Keluar")

        pilihan = input("\nPilih menu (1-7): ").strip()

        # Percabangan IF-ELIF-ELSE untuk navigasi menu
        if pilihan == "1":
            tambah_peralatan(daftar_alat)
        elif pilihan == "2":
            tampilkan_ringkasan(daftar_alat, tarif_aktif, ppj_aktif, tipe_layanan, biaya_admin)
        elif pilihan == "3":
            tarif_aktif = pilih_tarif()
        elif pilihan == "4":
            ppj_aktif = pilih_daerah()
        elif pilihan == "5":
            print("\nTIPE LAYANAN LISTRIK")
            print("1. Pascabayar (Bayar tagihan bulanan)")
            print("2. Prabayar (Beli Token Listrik)")
            opsi = input("Pilih tipe layanan (1/2): ").strip()
            if opsi == "2":
                tipe_layanan = "Prabayar"
                admin_in = input("Masukkan biaya admin bank (default 2500): ").strip()
                if admin_in != "":
                    try:
                        biaya_admin = float(admin_in)
                    except ValueError:
                        biaya_admin = 2500.0
                else:
                    biaya_admin = 2500.0
                print("\n[SUKSES] Layanan diubah ke Prabayar (Token).")
            else:
                tipe_layanan = "Pascabayar"
                print("\n[SUKSES] Layanan diubah ke Pascabayar.")
        elif pilihan == "6":
            daftar_alat.clear()
            print("\n[SUKSES] Semua daftar peralatan telah dihapus!")
        elif pilihan == "7":
            print("\nTerima kasih telah menggunakan Kalkulator Biaya Listrik!")
            berjalan = False
        else:
            print("\n[ERROR] Pilihan menu tidak valid. Silakan masukan angka 1-7.\n")

# Menjalankan program utama
if __name__ == "__main__":
    main()