import os
import random
import asyncio
from datetime import time
from zoneinfo import ZoneInfo

from telegram import Bot
from telegram.ext import Application

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = -5256876508

materi = [
    {
        "tema": "Al-Qur'an & Tafsir",
        "isi": """📖 QS. Al-An'am: 9

Allah menjelaskan bahwa jika Rasul dijadikan dari kalangan malaikat, mereka tetap akan berada dalam keraguan.

🧠 Penjelasan:
Ayat ini menunjukkan bahwa orang yang keras kepala bisa tetap mencari alasan untuk menolak kebenaran, meskipun tanda-tanda sudah jelas.

💡 Pelajaran:
Jangan sampai keraguan membuat kita menolak kebenaran yang sudah jelas."""
    },
    {
        "tema": "Akhlak",
        "isi": """🌿 Kejujuran

Allah berfirman dalam QS. At-Taubah: 119 agar orang-orang beriman bertakwa dan bersama orang-orang yang benar.

🧠 Penjelasan:
Kejujuran bukan hanya dalam ucapan, tetapi juga dalam niat, tindakan, dan amanah.

💡 Pelajaran:
Kejujuran mungkin terasa berat sesaat, tetapi ia membawa ketenangan dan kepercayaan."""
    },
    {
        "tema": "Renungan",
        "isi": """🌙 Tentang Niat

Rasulullah ﷺ bersabda bahwa amal-amal bergantung pada niat.

🧠 Pendalaman:
Satu perbuatan yang sama dapat memiliki nilai berbeda karena niat yang berbeda.

💡 Renungan:
Sebelum melakukan sesuatu, tanyakan kepada diri sendiri:
“Untuk siapa sebenarnya aku melakukan ini?”

📚 Rujukan:
HR. Bukhari dan Muslim."""
    }
]

async def kirim_materi(context):
    bot = context.bot
    materi_pilihan = random.choice(materi)

    pesan = f"""📚 LITERATUR ISLAM HARI INI

Tema: {materi_pilihan['tema']}

{materi_pilihan['isi']}
"""

    await bot.send_message(
        chat_id=CHAT_ID,
        text=pesan
    )

async def main():
    app = Application.builder().token(TOKEN).build()

    # Jadwal WIB
    zona_waktu = ZoneInfo("Asia/Jakarta")

    # 05:00
    app.job_queue.run_daily(
        kirim_materi,
        time=time(5, 0, tzinfo=zona_waktu)
    )

    # 15:00
    app.job_queue.run_daily(
        kirim_materi,
        time=time(15, 0, tzinfo=zona_waktu)
    )

    # 21:00
    app.job_queue.run_daily(
        kirim_materi,
        time=time(21, 0, tzinfo=zona_waktu)
    )

    print("Bot Literatur Islam berjalan...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
