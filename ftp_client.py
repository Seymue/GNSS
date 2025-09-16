import os
from ftplib import FTP

HOST = "192.168.1.100"   # IP приёмника
USER = " "               # логин (у Javad часто пустой пробел)
PASS = "VEYZEV2"        # пароль
LOCAL_DIR = "downloaded" # куда сохранять файлы

def check_connection():
    try:
        with FTP(HOST) as ftp:
            ftp.login(user=USER, passwd=PASS)
            print(f"[+] Подключение к {HOST} успешно")
            files = ftp.nlst()
            print(f"[+] Найдено файлов: {len(files)}")
            return True
    except Exception as e:
        print(f"[!] Ошибка подключения: {e}")
        return False

def download_files():
    os.makedirs(LOCAL_DIR, exist_ok=True)
    with FTP(HOST) as ftp:
        ftp.login(user=USER, passwd=PASS)
        files = ftp.nlst()

        for fname in files:
            local_path = os.path.join(LOCAL_DIR, fname)
            try:
                with open(local_path, "wb") as f:
                    ftp.retrbinary(f"RETR " + fname, f.write)
                print(f"[✓] Скачан: {fname}")
            except Exception as e:
                print(f"[!] Ошибка при скачивании {fname}: {e}")

if __name__ == "__main__":
    if check_connection():
        download_files()
