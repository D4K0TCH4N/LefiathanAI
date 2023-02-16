# Telegram Bot OpenAI ChatGPT version Python
import openai
from aiogram.types import Message
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message, ParseMode

bot_tkn = '5469636837:AAGdtRZVJtC1cXWPgfVKS1yKjSBPbN2fvfc'
openai.api_key = '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'

bot = Bot(token=bot_tkn)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start', 'help'])
async def cmd_handler(pesan: types.Message):
    if pesan.text == "/help":
        await pesan.answer("Perintah yang tersedia: awalai dengan \n#ai untk memulai pertanyaan")
    else:
        # Get the user's first name from the message object
         user_first_name = pesan.from_user.first_name
        # Send a greeting message that includes the user's first name
         await pesan.reply(f"Hello {user_first_name}, apa yang bisa saya bantu?", parse_mode=ParseMode.HTML)

@dp.message_handler(lambda message: message.text.startswith("#ai "))
async def ai_answer(pesan: types.Message):
        respon = openai.Completion.create(model='text-davinci-003', prompt=pesan.text, temperature=0, max_tokens=1000)
        parse = respon['choices'][0]['text']
        await pesan.reply(parse)

print('Lefiathan Aktif !')
executor.start_polling(dp)
