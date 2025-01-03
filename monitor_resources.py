import psutil
import requests
import time

# telegram bot details
BOT_TOKEN = ""
CHAT_ID = ""

# threshold
MEMORY_THRESHOLD = 70
CPU_THRESHOLD = 70
DISK_THRESHOLD = 70

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        "chat_id": CHAT_ID,
        "text":message,
        "parse_mode":"HTML"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

# monitoring function
def monitor_resources():
    while True:
        # check CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        if (cpu_usage > CPU_THRESHOLD):
            send_telegram_message(f"<b>CPU Usage Alert</b>: {cpu_usage}%")
        
        # check memory usage
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        if (memory_usage > MEMORY_THRESHOLD):
            send_telegram_message(f"<b>Memory Usage Alert</b>: {memory_usage}%")
        
        # check disk usage
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent
        if (disk_usage > DISK_THRESHOLD):
            send_telegram_message(f"<b>Disk Usage Alert</b>: {disk_usage}%")
        
        # sleep
        time.sleep(60)

if __name__ == "__main__":
    monitor_resources()