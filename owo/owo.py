import pyautogui
import random
import time
import tkinter as tk
from threading import Thread

# Global değişkenler
count = 0
wb_count = 0
start_time = time.time()
running = False
hunt_counter = 0  # "OwO Hunt Sayacı"
time_left = 0  # Kalan saniye sayacı
work_time = 0  # Çalışma süresi sayacı
work_running = False  # Çalışma sayacının durumu

def random_word():
    words = [
        'apple', 
        'banana', 
        'cherry', 
        'dog', 
        'elephant', 
        'fish', 
        'grape', 
        'honey', 
        'ice', 
        'jungle',
        'kiwi', 
        'lemon', 
        'mango', 
        'nut', 
        'orange', 
        'pear', 
        'quince', 
        'raspberry', 
        'strawberry',
        'tangerine', 
        'umbrella', 
        'violet', 
        'watermelon', 
        'xylophone', 
        'yellow', 
        'zebra'
    ]
    pyautogui.write(random.choice(words))
    pyautogui.press("enter")

def update_log(text):
    root.after(0, lambda: log_text.insert(tk.END, text + "\n"))
    root.after(0, lambda: log_text.yview_moveto(1))

def update_hunt_counter():
    root.after(0, lambda: hunt_counter_label.config(text=f"OwO Hunt Sayacı: {hunt_counter}"))

def update_time_left():
    root.after(0, lambda: time_left_label.config(text=f"Bir Sonraki Hunt için Kalan Süre: {time_left} saniye"))

def update_work_time():
    hours = work_time // 3600
    minutes = (work_time % 3600) // 60
    seconds = work_time % 60
    root.after(0, lambda: work_time_label.config(text=f"Çalışma Süresi: {hours:02d}:{minutes:02d}:{seconds:02d}"))

def start_work_timer():
    global work_time, work_running
    if work_running:
        return  # Zaten çalışıyorsa tekrar başlatma
    work_running = True
    def timer_loop():
        global work_time
        while work_running:
            time.sleep(1)
            work_time += 1
            update_work_time()
    Thread(target=timer_loop, daemon=True).start()

def start_bot():
    global running, count, wb_count, start_time, hunt_counter, time_left, work_running
    running = True
    
    update_log("Bot başlatılmadan önce 10 saniye bekleniyor...")
    
    start_work_timer()
    
    for i in range(10, 0, -1):
        update_log(f"{i} saniye kaldı...")
        time.sleep(1)
    
    update_log("\nHunt & Battle Başladı")
    while running:
        pyautogui.write("owo hunt")
        pyautogui.press("enter")
        
        time.sleep(0.2)
        
        pyautogui.write("owo b")
        pyautogui.press("enter")
        
        update_log("Hunt & Battle Yapıldı!")
        
        wb_count += 1
        hunt_counter += 1
        update_hunt_counter()
        update_log(f"Molaya Kalan 100 / {wb_count}")
        count += 1
        
        if count % 3 == 0:
            time.sleep(2)
            random_word()
        if wb_count == 100:
            pyautogui.write("owo zoo")
            pyautogui.press("enter")
            rest_time = random.randint(60, 300)
            update_log(f"\nMola Verildi! Süre: {rest_time // 60} dakika {rest_time % 60} saniye")
            for i in range(rest_time, 0, -1):
                update_log(f"Mola: {i // 60} dakika {i % 60} saniye kaldı...")
                time.sleep(1)
            update_log("\nMola Sona Erdi!")
            wb_count = 0
        if time.time() - start_time >= 300:
            pyautogui.write("owo pray")
            pyautogui.press("enter")
            update_log("\n'w pray' komutu yazıldı!")
            start_time = time.time()
        wait_time = random.randint(18, 25)
        for i in range(wait_time, 0, -1):
            time_left = i
            update_time_left()
            time.sleep(1)

def stop_bot():
    global running, work_running
    running = False
    work_running = False  # Çalışma sayacını durduruyoruz
    update_log("\nBot durduruldu.")

def run_bot_thread():
    Thread(target=start_bot, daemon=True).start()

root = tk.Tk()
root.title("OwO Hunt Bot")
root.geometry("800x600")
root.config(bg="#1e1e2f")

main_frame = tk.Frame(root, bg="#1e1e2f")
main_frame.pack(fill=tk.BOTH, expand=True)

left_frame = tk.Frame(main_frame, bg="#2f2f3f", width=200)
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

right_frame = tk.Frame(main_frame, bg="#121212")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

start_button = tk.Button(left_frame, text="Başlat", command=run_bot_thread, width=20, bg="#4CAF50", fg="white", font=("Helvetica", 12))
start_button.pack(pady=20)

stop_button = tk.Button(left_frame, text="Durdur", command=stop_bot, width=20, bg="#F44336", fg="white", font=("Helvetica", 12))
stop_button.pack(pady=10)

hunt_counter_label = tk.Label(left_frame, text=f"OwO Hunt Sayacı: {hunt_counter}", bg="#2f2f3f", fg="white", font=("Helvetica", 14))
hunt_counter_label.pack(pady=10)

time_left_label = tk.Label(left_frame, text=f"Bir Sonraki Hunt için Kalan Süre: {time_left} saniye", bg="#2f2f3f", fg="white", font=("Helvetica", 14))
time_left_label.pack(pady=10)

work_time_label = tk.Label(left_frame, text="Çalışma Süresi: 00:00:00", bg="#2f2f3f", fg="white", font=("Helvetica", 14))
work_time_label.pack(pady=10)

log_text = tk.Text(right_frame, height=15, width=70, bg="#121212", fg="white", font=("Courier", 10), wrap=tk.WORD)
log_text.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(right_frame, command=log_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

log_text.config(yscrollcommand=scrollbar.set)

# "by yigitat" etiketi eklemek için çalışma süresinin hemen altına parlak bir turkuvaz rengi ekliyoruz
footer_label = tk.Label(left_frame, text="by yigitat", bg="#2f2f3f", fg="#00FFFF", font=("Helvetica", 12, "bold"))
footer_label.pack(pady=5)

if __name__ == "__main__":
    root.mainloop()
