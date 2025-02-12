# Eitaa Auto-Poster Bot

**Eitaa Auto-Poster Bot** is an automated bot designed to fetch and post various types of content (jokes, quotes, anime images, and backgrounds) to an Eitaa channel at regular intervals. The bot ensures that each post is unique and supports both text and image-based content.

## 🚀 Features
- ✅ **Auto-fetch content** from multiple APIs  
- ✅ **Supports text & images** (downloads and uploads images correctly)  
- ✅ **Prevents duplicate posts**  
- ✅ **Adds a custom caption** to all posts  
- ✅ **Fully asynchronous** for better performance  

## 🛠 How It Works
1. Fetches a random post (joke, quote, anime image, or background)  
2. Checks if the post has already been shared  
3. Sends text messages directly to the channel  
4. Downloads and uploads image-based content properly  
5. Adds a promotional caption to each post  

## ⚙ Installation & Usage
1. Install the required dependencies:  
   ```bash
   pip install aiohttp eitaapy
   ```
2. Edit the `TOKEN` and `CHAT_ID` with your Eitaa bot credentials  
3. Run the bot:  
   ```bash
   python bot.py
   ```  

## 📌 Requirements
- Python 3.7+  
- `aiohttp` for async HTTP requests  
- `eitaapy` for interacting with the Eitaa API  

---

🌟 **Support & Contributions**  
Feel free to contribute or suggest improvements! If you enjoy this project, don't forget to support us by joining our channel: **@none** 🚀
