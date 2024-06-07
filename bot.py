import asyncio
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot, Dispatcher
#from handlers import other_handlers, user_handlers
from background import keep_alive
from config_data.config import Config, load_config
from handlers import user_handlers


# Функция конфигурирования и запуска бота
async def main():
    # Загружаем конфиг в переменную config
    config: Config = load_config()
    BOT_TOKEN: str = config.tg_bot.token
    # Инициализируем бот и диспетчер dfgdgdhjd

    bot: Bot = Bot(token=BOT_TOKEN)
    dp: Dispatcher = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
 #   dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling hhfk
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

keep_alive()
if __name__ == '__main__':
    asyncio.run(main())