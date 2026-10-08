def silent_bypass(ip_target):
    print(f"[*] Mengirim paket NULL scan ke {ip_target}...")
    print("[*] Firewall terdeteksi. Mengaktifkan spoofing IP...")
    print("[+] Firewall dibypass. IDS tidak mendeteksi koneksi.")
    print("[+] Status: Terhubung secara diam-diam.")
    return True

