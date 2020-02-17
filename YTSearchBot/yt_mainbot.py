import logging
from uuid import uuid4
from yt_search import youtubeSearch
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown


# # Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

# logger = logging.getLogger(__name__)




#Command handlers
#Sends message when /start is used
def start(update, context):
    update.message.reply_text('Hello!')

#Sends message when /search is used
def help(update, context):
    update.message.reply_text('Help!')

#Sends message when @botname is used
def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query

    if not query:
        results = [
            InlineQueryResultArticle(
                id=uuid4(),
                title="Caps",
                input_message_content=InputTextMessageContent(
                    query.upper())),
            InlineQueryResultArticle(
                id=uuid4(),
                title="Bold",
                input_message_content=InputTextMessageContent(
                    "*{}*".format(escape_markdown(query)),
                    parse_mode=ParseMode.MARKDOWN)),
            InlineQueryResultArticle(
                id=uuid4(),
                title="Italic",
                input_message_content=InputTextMessageContent(
                    "_{}_".format(escape_markdown(query)),
                    parse_mode=ParseMode.MARKDOWN))]
    else:
        _youtubesearch = youtubeSearch()
        _youtubesearch.main(query) 
        results =[
            InlineQueryResultArticle(
                id = uuid4(),
                title = _youtubesearch.description,
                input_message_content = InputTextMessageContent(
                    _youtubesearch.message
                )
            )
        ]
        
    
    update.inline_query.answer(results)

# def error(update, context):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater("YOUR TOKEN HERE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # # log all errors
    # dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()