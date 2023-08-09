from telebot import TeleBot
from telebot.types import Message

TOKEN = '6061474094:AAHSpXuNC_NZNkjOsMAebf7AYQfLHv7mK-U'

bot = TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start', 'help', 'about'])
def welcome(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(chat_id, user_id)
    if message.text == '/start':
        bot.send_message(chat_id, 'Привет! Я бот-попугай!')
    elif message.text == '/help':
        help_message = '''
Доступные команды:
/start - Начать диалог
/help - Получить список доступных команд
/about - Узнать информацию о боте
'''
        bot.send_message(chat_id, help_message)
    elif message.text == '/about':
        bot.send_message(chat_id, 'Моя история началась в субботу в 17:42')

def handle_dialog(message: Message):
    chat_id = message.chat.id
    user_message = message.text

    if user_message == 'Привет':
        bot.send_message(chat_id, 'Привет')
    elif user_message == 'Как дела?':
        bot.send_message(chat_id, 'Спасибо, отлично!')
    elif user_message == 'Привет! Как тебя зовут?':
        bot.send_message(chat_id, 'Привет! Я Бот-Попугай, приятно познакомиться. Чем я могу тебе помочь?')
    elif user_message == 'Какой язык является наиболее распространенным в мире?':
        bot.send_message(chat_id, 'Английский язык является наиболее распространенным в мире ')
    elif user_message == 'Какие музыкальные жанры популярны сейчас?':
        bot.send_message(chat_id, 'В музыке популярность жанров может меняться со временем и различаться в зависимости от региона и предпочтений слушателей. На данный момент популярными жанрами являются поп-музыка, рэп, рок, R&B, электронная музыка и латиноамериканская музыка.')
    elif user_message == 'Какие социальные сети пользуются большой популярностью?':
        bot.send_message(chat_id, 'Социальные сети, которые пользуются большой популярностью, включают Facebook, Instagram, Twitter, YouTube, LinkedIn и TikTok. Однако популярность социальных сетей может различаться в зависимости от региона и предпочтений пользователей.')
    elif user_message == 'Какие технологические компании считаются лидерами в отрасли?':
        bot.send_message(chat_id, 'В технологической отрасли существует множество компаний, которые считаются лидерами в своих областях. Некоторые из них включают Apple, Google, Microsoft, Amazon, Facebook и Samsung. Однако стоит отметить, что конкуренция в отрасли высока, и рейтинги компаний могут меняться со временем.')
    elif user_message == 'Какие способы оплаты обычно принимают интернет-магазины?':
        bot.send_message(chat_id, 'Интернет-магазины обычно принимают различные способы оплаты, включая кредитные и дебетовые карты (Visa, Mastercard, American Express), электронные платежные системы (PayPal, Stripe), банковские переводы и иногда наличные при доставке (COD). Конкретные способы оплаты могут различаться в зависимости от магазина и региона.')
    elif user_message == 'Какие советы можно дать начинающему предпринимателю?':
        bot.send_message(chat_id, '''Для начинающего предпринимателя рекомендуется обратить внимание на следующие советы:
 • Найдите нишу или идею, которая вам нравится и имеет потенциал на рынке.
 • Разработайте бизнес-план, определите цели и стратегию развития.
 • Исследуйте свою целевую аудиторию и конкурентов.
 • Уделяйте внимание маркетингу и продвижению своего бизнеса.
 • Будьте готовы к трудностям и гибким в изменении стратегии.
 • Ищите возможности для обучения и развития своих навыков.
 • Создайте надежную команду или сеть поддержки.
 • Будьте настойчивыми и не бойтесь испытывать новые идеи.
''')
    elif user_message == 'Какие книги стоит прочитать в этом году?':
        bot.send_message(chat_id, 'В выборе книг важно учитывать ваши предпочтения и интересы. В этом году было выпущено множество отличных книг в различных жанрах. Некоторые рекомендации включают "Крестный отец" Марио Пьюзо, "1984" Джорджа Оруэлла, "Маленькие женщины" Луизы Мэй Олкотт, "Сто лет одиночества" Габриэля Гарсиа Маркеса и "Цветы для Элджернона" Даниеля Киза.')
    else:
        bot.send_message(chat_id,'Попробуйте задать вопрос еще раз')

@bot.message_handler(content_types=['text', 'photo', 'voice', 'sticker', 'video'])
def answer(message: Message):
    chat_id = message.chat.id
    if message.text:
        handle_dialog(message)
        text = message.text
        # bot.send_message(chat_id, text)
        # bot.send_message(chat_id, '😁😂🤣😃😄😅😆😀😉😊😋😎')
        # bot.send_message(chat_id, f'<b>{text}</b>')
        # bot.send_message(chat_id, f'<i>{text}</i>')
        # bot.send_message(chat_id, f'<u>{text}</u>')
        # bot.send_message(chat_id, f'<s>{text}</s>')
        # bot.send_message(chat_id, f'<code>{text}</code>')
        # bot.send_message(chat_id, f'<pre>{text}</pre>')
        # bot.send_message(chat_id, f'<tg-spoiler>{text}</tg-spoiler>')

    if message.photo:
       photo_id = message.photo[0].file_id
       bot.send_photo(chat_id, photo_id)

    if message.voice:
        voice_id = message.voice.file_id
        bot.send_voice(chat_id, voice_id)

    if message.sticker:
        sticker_id = message.sticker.file_id
        bot.send_sticker(chat_id, sticker_id)

    if message.video:
        video_id = message.video.file_id
        bot.send_video(chat_id, video_id)

# Зацикливание бота
bot.polling(none_stop=True)