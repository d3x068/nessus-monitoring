# Telegram Bot for Resource Monitoring

This Python script monitors system resource usage (CPU, memory, disk) and integrates with a Telegram bot to:

1. Send automatic alerts to a Telegram group if resource usage exceeds predefined thresholds.
2. Respond to the `/status` command in the group, providing real-time resource usage.

## Features
- **Resource Monitoring**: Alerts when CPU, memory, or disk usage exceeds 70%.
- **Command Handling**: Responds to the `/status` command with detailed system stats.

---

## Prerequisites

### 1. Python Dependencies
Install the required Python libraries:
```bash
pip install psutil requests
```

### 2. Telegram Bot Setup
1. Create a bot using [BotFather](https://t.me/BotFather).
2. Obtain the bot token.
3. Add the bot to your group.

---

## Configuration

### **Environment Variables**
Replace the placeholders in the script:
- **BOT_TOKEN**: Your Telegram bot token from BotFather.
- **CHAT_ID**: The group chat ID where the bot operates.

---

## Script Usage

Save the script as `resource_monitor_bot.py` and run it:
```bash
python3 resource_monitor_bot.py
```

Please make sure that the service file is in the right path --> /etc/systemd/system/resource_monitor.service
```bash
$ sudo systemctl enable resource_monitor
$ sudo systemctl start resource_monitor
```

---

## Functional Overview

### **1. Resource Monitoring**
The script checks system resources every 60 seconds. If usage exceeds the thresholds (default 70%), it sends an alert to the group.

### **2. Group Commands**
#### `/status`
Responds with current CPU, memory, and disk usage. Example response:
```
System Status:
CPU Usage: 45%
Memory Usage: 68%
Disk Usage: 72%
```

---

## License
This script is open-source and available under the MIT License.

---

## Contact
For questions or suggestions, feel free to reach out.

