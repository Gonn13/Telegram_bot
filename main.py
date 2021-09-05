token = "1893390873:AAE63gdnXuWbP4vCaMBD

INPUT_TEXT = 0
def start(update, context):
  update.message.reply_text("hola lokita! que querés hacer? enviame /volume para ver los volúmenes ballenas de la moneda que quieras")
def volume_command_handler(update,context):
  update.message.reply_text("enviame el par de la forma /BTCUSDT para trackear los volúmenes de ballenas")
  return INPUT_TEXT

  
 

def input_text(update,context):
  text = update.message.text
  text=str.upper(text[1:])
  update.message.reply_text("bien ahí lokita!me enviaste el par:"+text)
 
if __name__=="__main__":
  updater=Updater(token = token, use_context= True)
  dp = updater.dispatcher
 
  #dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))
  dp.add_handler(CommandHandler("start", start))

  dp.add_handler(ConversationHandler (
      entry_points = [ CommandHandler("volume",volume_command_handler)
                      
      ],
      states = {
          INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
          #INPUT_TEXT: [MessageHandler(update.message.text, input_text)]
      },
      fallbacks = []
  )
                 )
  updater.start_polling()

  print('Bot is polling')

  updater.idle()
