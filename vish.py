import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    Message, 
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)

API_TOKEN = "8453813923:AAHzP4w2Wxknyb9S7HZQDtG87sIR8ui1RvE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- Кнопки внизу экрана (Reply) ---
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Меню")],
        [KeyboardButton(text="ℹ️ О боте"), KeyboardButton(text="❓ Помощь")]
    ],
    resize_keyboard=True
)

# --- Inline кнопки под сообщением ---
inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⚡️ Действие 1", callback_data="action1"),
            InlineKeyboardButton(text="🔥 Действие 2", callback_data="action2")
        ],
        [
            InlineKeyboardButton(text="💎 Действие 3", callback_data="action3")
        ]
    ]
)


# --- Команда /start ---
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет 👋\nВыбирай кнопки внизу или жми на меню:",
        reply_markup=main_menu
    )

# --- Когда жмут на 📋 Меню (Reply-кнопка) ---
@dp.message(lambda msg: msg.text == "📋 Меню")
async def show_inline(message: Message):
    await message.answer(
        "Вот твое меню действий 👇",
        reply_markup=inline_menu
    )

# --- Обработка Inline-кнопок ---
@dp.callback_query()
async def process_callback(callback_query):
    data = callback_query.data

    if data == "action1":
        await callback_query.message.answer("⚡️ Выполнилось действие 1")
    elif data == "action2":
        await callback_query.message.answer("🔥 Выполнилось действие 2")
    elif data == "action3":
        await callback_query.message.answer("💎 Выполнилось действие 3")

    await callback_query.answer()  # закрывает "часики" у кнопки


# --- Дополнительные кнопки (Reply) ---
@dp.message(lambda msg: msg.text == "ℹ️ О боте")
async def about(message: Message):
    await message.answer("Я бот-шаблон 🤖, умею работать и с Reply, и с Inline кнопками.")

@dp.message(lambda msg: msg.text == "❓ Помощь")
async def help_command(message: Message):
    await message.answer("Доступные кнопки:\n"
                         "📋 Меню – показать Inline-действия\n"
                         "ℹ️ О боте – информация\n"
                         "❓ Помощь – справка")

# --- Запуск ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())