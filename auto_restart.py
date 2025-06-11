import os
import time
import subprocess

RESTART_INTERVAL = 3 * 60 * 60  # 3 saat

while True:
    print("[Auto-Restart] ArchMusic başlatılıyor...")
    process = subprocess.Popen(["python3", "-m", "ArchMusic"])
    time.sleep(RESTART_INTERVAL)
    print("[Auto-Restart] 3 saat doldu, yeniden başlatılıyor...")
    process.terminate()
    time.sleep(5)