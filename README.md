# Telegram Bot for Resource Monitoring

This Python script monitors system resource usage (CPU, memory, disk) and integrates with a Telegram bot to:

1. Send automatic alerts to a Telegram group if resource usage exceeds predefined thresholds.
2. Respond to the `/status` command in the group, providing real-time resource usage.

## Features
- **Resource Monitoring**: Alerts when CPU, memory, or disk usage exceeds 70%.
- **Command Handling**: Responds to the `/status` command with detailed system stats.
- **Group Integration**: Works in group chats, sending updates and receiving commands.

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

### **Retrieve Group Chat ID**
1. Add the bot to your group.
2. Send a message or command in the group.
3. Use the following `curl` command to find the group ID:
   ```bash
   curl https://api.telegram.org/bot<your_bot_token>/getUpdates
   ```
   Look for the `chat.id` field in the response. Group IDs are negative (e.g., `-123456789`).

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

## Code Structure
- **send_telegram_message**: Sends a message to the group.
- **check_resources**: Monitors system resource usage.
- **handle_incoming_messages**: Handles incoming messages and commands.
- **Multithreading**: Ensures both monitoring and command handling run simultaneously.

---

## License
This script is open-source and available under the MIT License.

---

## Contact
For questions or suggestions, feel free to reach out.

