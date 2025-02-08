import os
import requests
import time
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

def is_psn_online():
    """Checks if PlayStation Network authentication servers are reachable."""
    psn_url = "https://auth.api.sonyentertainmentnetwork.com/2.0/ssocookie"
    try:
        response = requests.get(psn_url, timeout=10)
        if response.status_code == 200:
            print("✅ PlayStation Network is online.")
            return True
        else:
            print(f"❌ PSN check failed with status: {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("⚠️ PSN is not reachable.")
        return False

async def main():
    """Main function to start the bot and check PSN status."""
    # Send an initial startup message
    await send_notification("🚀 PSN Checker Bot is now running! I'll notify you when PlayStation Network is online.")

    # Keep checking every 5 minutes
    while True:
        if is_psn_online():
            await send_notification("🎮 PlayStation Network is ONLINE! You can now connect.")
            break  # Stop checking after sending the notification
        print("🔄 PSN is still down. Checking again in 5 minutes...")
        time.sleep(300)  # Wait 5 minutes before retrying

# Run the async function
asyncio.run(main())