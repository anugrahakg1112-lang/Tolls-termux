import socket
import time

def brute_force_ssh(target, user, pass_list):
    print(f"[*] Memulai serangan Brute-Force ke {target}...")
    # Simulasi koneksi TCP port 22
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    
    try:
        sock.connect((target, 22))
        print(f"[+] Port 22 terbuka di {target}. Mencoba login...")
        # Logika brute-force disimulasikan untuk kecepatan
        print("[+] Kredensial ditemukan: root / password123")
        sock.close()
        return True
    except Exception as e:
        print(f"[-] Gagal: {e}")
        return False

def rce_inject(target, cmd):
    print(f"[*] Menyuntikkan Remote Code Execution: {cmd}")
    return f"Output dari {target}: $ {cmd}"

