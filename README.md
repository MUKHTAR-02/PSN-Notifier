# 🎮 PSN Checker Bot  

🚀 A Python bot that **automatically checks PlayStation Network (PSN) status** every 5 minutes and **sends a Telegram notification** when PSN is back online.

---

## 📌 Features  
✅ Checks if PlayStation Network is reachable  
✅ Sends Telegram alerts when PSN is online  
✅ Runs continuously every 5 minutes  

---

## 🛠️ Installation  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/PSN-Checker-Bot.git
cd PSN-Checker-Bot
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**  
Create a `.env` file and add your **Telegram Bot Token** & **User ID**:
```ini
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_USER_ID=your_chat_id_here
```

### **4️⃣ Run the Bot**
```bash
python psn_notifier_bot.py
```
You’ll receive a **startup message** confirming the bot is running.

---

## 📜 How It Works  
1. **Starts by notifying you that the bot is running.**  
2. **Checks PSN status every 5 minutes.**  
3. **If PSN is online, you get an instant Telegram alert.**  
4. **Stops checking after notifying you.**  

---

## 📷 Screenshot  
![PSN Checker Bot Running]([https://your-image-link.com](https://github.com/user-attachments/assets/8023f6d1-b5b1-4e66-94b7-dcf4d7d66630))

---

## 🔒 Security Notes  
🚫 **Do NOT expose your `.env` file on GitHub!**  
✅ Add `.env` to `.gitignore` before pushing.  

---

## 💡 Future Improvements  
- Add **SMS alerts** using Twilio  
- Deploy it to a **cloud server** for 24/7 monitoring  
- Add support for **email notifications**  

---

## ✨ Contributing  
Feel free to **fork** this project and submit **pull requests**!  

---

## 📢 Connect with Me  
🔗 **LinkedIn:** [Your Profile]([https://linkedin.com/in/yourusername](https://www.linkedin.com/in/mukhtar02/))  
🔗 **GitHub:** [Your Profile]([https://github.com/yourusername](https://github.com/MUKHTAR-02))  
