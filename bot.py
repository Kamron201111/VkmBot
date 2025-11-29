import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN
from utils.youtube import search_youtube, download_audio
from utils.spotify import search_spotify
from utils.google_search import google_music_search

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("🎧 Musiqa qidiruvchi botga xush kelibsiz!\nQo‘shiq nomini yuboring.")

@dp.message_handler()
async def search(msg: types.Message):
    query = msg.text
    yt = search_youtube(query)
    sp = search_spotify(query)
    gg = google_music_search(query)

    text = "🔎 Natijalar:\n"
    text += f"\n📌 YouTube: {yt['title']}\n{yt['url']}"
    text += f"\n\n🎵 Spotify: {sp}\n"
    text += f"\n🌐 Google: {gg}\n"

    await msg.answer(text)

    audio_path = download_audio(yt['url'])
    await msg.answer_audio(open(audio_path,'rb'))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)
