import os
import random
from telegram import Bot

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = -5256876508

materi = [
    """📚 LITERATUR ISLAM HARI INI

Tema: Al-Qur'an & Tafsir

📖 QS. Al-An'am: 9

Allah menjelaskan bahwa jika Rasul dijadikan dari kalangan malaikat, orang-orang yang ingkar tetap akan berada dalam keraguan.

🧠 Penjelasan:
Masalahnya bukan selalu kurangnya bukti, tetapi hati yang tidak mau menerima kebenaran.

💡 Pelajaran:
Jangan biarkan keraguan membuat kita menolak kebenaran.

📚 Rujukan: QS. Al-An'am: 9""",

    """📚 LITERATUR ISLAM HARI INI

Tema: Akhlak — Kejujuran

📖 QS. At-Taubah: 119

Allah memerintahkan orang-orang beriman untuk bertakwa dan bersama orang-orang yang benar.

🧠 Penjelasan:
Kejujuran bukan hanya dalam ucapan, tetapi juga dalam niat dan perbuatan.

💡 Pelajaran:
Kejujuran membangun kepercayaan dan ketenangan hati.

📚 Rujukan: QS. At-Taubah: 119""",

    """📚 LITERATUR ISLAM HARI INI

Tema: Renungan — Niat

🧠 Penjelasan:
Amal yang terlihat sama dapat memiliki nilai yang berbeda karena niat yang berbeda.

💡 Renungan:
Sebelum melakukan sesuatu, tanyakan kepada diri sendiri:
“Untuk siapa sebenarnya aku melakukan ini?”

📚 Rujukan: HR. Bukhari dan Muslim"""
]

async def main():
    bot = Bot(token=TOKEN)
    pesan = random.choice(materi)
    await bot.send_message(chat_id=CHAT_ID, text=pesan)
    print("Materi berhasil dikirim.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
