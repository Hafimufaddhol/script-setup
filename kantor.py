import os
import subprocess
import webbrowser
import time

def connect_to_vpn(vpn_name):
    """Menghubungkan ke VPN menggunakan nama VPN dan environment variables untuk username dan password."""
    try:
        # Mendapatkan username dan password dari environment variables
        username = os.getenv('VPN_USERNAME')
        password = os.getenv('VPN_PASSWORD')

        if not username or not password:
            raise ValueError("Username atau password tidak ditemukan dalam environment variables.")

        print(f"Menghubungkan ke VPN: {vpn_name} dengan username {username}...")

        # Perintah untuk menghubungkan ke VPN menggunakan rasdial
        # Pastikan Anda menggunakan parameter yang sesuai dengan VPN yang dikonfigurasi
        subprocess.run(["rasdial", vpn_name, username, password], check=True)
        print("VPN berhasil terhubung!")
    except Exception as e:
        print("Gagal menghubungkan ke VPN.")
        print(e)

def open_directory(directory_path):
    """Membuka directory tertentu di file manager."""
    try:
        print(f"Membuka directory: {directory_path}...")
        os.startfile(directory_path)  # Untuk Windows
        print("Directory berhasil dibuka!")
    except Exception as e:
        print("Gagal membuka directory.")
        print(e)

def open_web_page(url):
    """Membuka halaman web di browser."""
    try:
        print(f"Membuka halaman web: {url}...")
        webbrowser.open(url)
        print("Halaman web berhasil dibuka!")
    except Exception as e:
        print("Gagal membuka halaman web.")
        print(e)

if __name__ == "__main__":
    # Nama VPN
    vpn_name = "VPN kantor"

    # Path directory jaringan yang ingin dibuka
    directory_path = r"\\192.168.1.20"  # Alamat jaringan

    # URL halaman web
    url = "http://192.168.1.10/sipp/"  # URL YouTube

    # Menghubungkan ke VPN
    connect_to_vpn(vpn_name)

    # Tunggu beberapa detik agar VPN terhubung
    time.sleep(5)

    # Membuka directory jaringan
    open_directory(directory_path)

    # Membuka halaman web YouTube
    open_web_page(url)
