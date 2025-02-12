import asyncio
import aiohttp
import random
import os
from eitaapy import Robot

TOKEN = "bot278980:167a2ef5-fcb1-4597-b873-1c5e19505c6c"  # Token ربات ایتا
CHAT_ID = "news_irna"  # آیدی چت یا لینک کانال
SLEEP = 2

class Start:
    def __init__(self, token, chat_id):
        self.client = Robot(token=token)
        self.chat_id = chat_id
        self.posted_texts = set()
    async def fetch_content(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content_type = response.headers.get("Content-Type", "")
                if "image" in content_type:
                    return url
                if "application/json" in content_type:
                    data = await response.json()
                    return data.get("result")
                return None
    async def download_image(self, url):
        filename = "background.jpg"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    with open(filename, "wb") as f:
                        f.write(await response.read())
                    return filename
        return None
    async def get_unique_post(self):
        for _ in range(5):
            source = random.choice([
                "https://api-free.ir/api/jok.php",
                "https://api-free.ir/api2/dialog",
                "https://api-free.ir/api2/enime/",
                "https://api-free.ir/api2/background/"
            ])
            content = await self.fetch_content(source)
            if content and content not in self.posted_texts:
                if "back" in content:return content
                self.posted_texts.add(content)
                return content
        return None
    async def post_to_eitaa(self):
        while True:
            post_text = await self.get_unique_post()
            if post_text:
                print(post_text)
                if post_text.startswith("https://"):
                    image_path = await self.download_image(post_text)
                    if image_path:
                        try:
                            print(await self.client.send_file(self.chat_id, image_path,caption=f"\n\nکانال ما را حمایت کنید : @none"))
                            os.remove(image_path)
                        except:...
                else:await self.client.send_message(chat_id=self.chat_id, text=post_text+f"\n\nکانال ما را حمایت کنید : @none")
            await asyncio.sleep(SLEEP)
async def main():
    bot = Start(TOKEN, CHAT_ID)
    await bot.post_to_eitaa()
if __name__ == "__main__":
    asyncio.run(main())
