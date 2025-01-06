import psutil
import requests
import time
from threading import Thread

# telegram bot details
# CHAT_ID = ""
# BOT_TOKEN = ""

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

def handle_incoming_messages():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    last_update_id = None

    while True:
        try:
            params = {'offset':last_update_id, 'timeout':10}
            response = requests.get(url, params=params).json()

            for result in response.get('result',[]):
                last_update_id = result["update_id"] + 1
                message = result.get("message", {})
                chat_id = message.get("chat", {}).get("id")
                text = message.get("text","")

                # only respond in the configured group chat
                if chat_id == int(CHAT_ID) and text.strip().lower() == "/status":
                    # fetch and send current resource usage
                    cpu_usage = psutil.cpu_percent(interval=1)
                    memory_info = psutil.virtual_memory()
                    memory_usage = memory_info.percent
                    disk_info = psutil.disk_usage('/')
                    disk_usage = disk_info.percent

                    response_message = (
                        f"<b>System Status</b>:\n"
                        f"CPU Usage : {cpu_usage} %\n"
                        f"Memory Usage : {memory_usage} %\n"
                        f"Disk Usage : {disk_usage} %\n"
                    )
                    send_telegram_message(response_message)
        except Exception as e:
            print(f"Error handling incoming messages: {e}")
        time.sleep(1)

if __name__ == "__main__":
    Thread(target=handle_incoming_messages).start()
    monitor_resources()