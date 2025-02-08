import os
import requests
import time
import random
import asyncio
from telegram import Bot
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys securely
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_USER_ID")

# Initialize the bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_notification(message):
    """Sends a custom message to Telegram asynchronously."""
    await bot.send_message(chat_id=TELEGRAM_USER_ID, text=message)
    print(f"✅ Notification sent: {message}")

def is_psn_online(retry_count=0):
    """Checks if PlayStation Network authentication servers are reachable with rate limit handling."""
    # psn_url = "https://www.playstation.com/en-us/network-status/"  # Alternative Sony status page
    psn_url = "https://www.playstation.com/en-us/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        response = requests.get(psn_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✅ PlayStation Network is online.")
            return True
        elif response.status_code == 429:
            if retry_count >= 5:  # Stop after 5 retries
                print("❌ Too many retries. Waiting longer before retrying...")
                time.sleep(600)  # Wait 10 minutes before trying again
                return False

            wait_time = random.randint(180, 600) * (retry_count + 1)  # 3-10 min * retry_count
            print(f"⚠️ Rate limit hit (429). Waiting {wait_time} seconds before retrying...")
            time.sleep(wait_time)
            return is_psn_online(retry_count + 1)  # Retry with increased count
        else:
            print(f"❌ PSN check failed with status: {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("⚠️ PSN is not reachable.")
        return False

async def main():
    """Main function to start the bot and check PSN status."""
    await send_notification("🚀 PSN Checker Bot is now running! I'll notify you when PlayStation Network is online.")

    while True:
        if is_psn_online():
            await send_notification("🎮 PlayStation Network is ONLINE! You can now connect.")
            break  # Stop checking after sending the notification
        print("🔄 PSN is still down. Checking again in 5 minutes...")
        time.sleep(300)  # Wait 5 minutes before retrying

# Run the async function
asyncio.run(main())
