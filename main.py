from bot import bot
from handlers.user_handlers import register_user_handlers
from handlers.move_handlers import register_move_handlers
from handlers.report_handlers import register_report_handlers

register_user_handlers(bot)
register_move_handlers(bot)
register_report_handlers(bot)

bot.delete_webhook(drop_pending_updates=True)
bot.polling(skip_pending=True)




    