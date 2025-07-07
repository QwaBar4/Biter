# Biter

Biter is a Python bot that collects user phone numbers through Telegram with one-tap approval and stores them securely.

## Features 

- **One-tap phone sharing** - Users approve with a single button
- **Secure storage** - Saves data to `user_data.txt`
- **Real-time console output** - See collected numbers immediately

## How It Works 

1. User sends `/start` command
2. Bot shows approval button
3. User taps button once to share contact
4. Bot saves data to file and console:

```text
2023-12-15 14:30:22|123456789|John Doe|@johndoe|+1234567890
```

## Setup Instructions 🛠️

### Prerequisites
- Python 3.8+
- Telegram bot token from [@BotFather](https://t.me/BotFather)

### Installation
```bash
git clone https://github.com/QwaBar4/Biter.git
cd Biter
pip install python-telegram-bot
```

## Contributing
If you want to contribute with me, text me on telegram: @QwaBar4
