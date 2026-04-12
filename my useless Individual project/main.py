from aiogram import Bot, Dispatcher
from handlers import user

async def main():
    bot = Bot(token = '8543941623:AAG528tzAAyaLugxyXGxvz1hFnnq18VUQ_k')
    dp = Dispatcher()
    dp.include_router(user)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:    
        import asyncio
        asyncio.run(main())
    except:
        pass