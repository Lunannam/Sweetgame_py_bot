# from anecAPI import anecAPI


# def delete_word(update,context):
#     text = context.args
#     print(text)
#     if not text:
#         context.bot.send_message(update.effective_chat.id, "Привет")
#     else:
#         string_text = " ".join(map(str,[t for t in text if 'абв' not in t]))
#         context.bot.send_message(update.effective_chat.id, string_text)
# 

def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, "я тебя не понимаю, пиши /game, если хочешь сыграть со мной?")


# def info(update, context):
#     context.bot.send_message(update.effective_chat.id,
#                              """Доступны следующие команды:
#                              /start - эхобот, повторяет всё сказанное через пробел,
#                              /info - информация,
#                              /game - играть в игру""")

def game(update, context):
    context.bot.send_message(update.effective_chat.id,
                            """ Игра с конфетами"\n
                            В игре участвуют два игрока\n
                            Первый ход определяется жеребьевкой.\n
                            Игроки ходят, совершая ход друг после друга\n
                            Правила игры\n
                            У нас есть некоторое количество конфет\n
                            За один ход можно забрать не более определенного количества конфет, о котором мы договоримся\n
                            Тот, кому достанется последняя конфета - проиграл\n""")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'Привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю, пиши /game, если хочешь сыграть со мной')


# def unknown(update, context):
#     word = update.message.text
#     print(word)
#     if 'mod' in word:
#         context.bot.send_message(update.effective_chat.id, anecAPI.modern_joke())
#     if 'sov' in word:
#         context.bot.send_message(update.effective_chat.id, anecAPI.soviet_joke())
#     else:
#         context.bot.send_message(update.effective_chat.id, anecAPI.random_joke())


    
# def give_word(update,context):
#     word = update.message.text
#     
#     list_num = parse(word)
#     list_result = bracket_opening(list_num)
#     result = calculate(list_result)
#     context.bot.send_message(update.effective_chat.id, result)
# 
# 
# 
    # word = update.message.text
    # if "бар" in word:
    #     joke = '''Белый медведь заходит в паб и говорит бармену:
    #             - Дайте мне виски и... кока-колу.
    #             - А почему такая пауза? - спрашивает бармен.
    #             - Это всё, что вас удивляет? - с обидой говорит медведь.'''
    #     context.bot.send_message(update.effective_chat.id, joke)
    #     return joke
    # elif "пока" in word:
    #     context.bot.send_message(update.effective_chat.id, 'Покачивай шляпой из бара')
    #     return word
    # context.bot.send_message(update.effective_chat.id, 'Вы, как всегда, правы, милорд')