
import requests
import telebot

# Замініть 'YOUR_OPENWEATHERMAP_API_KEY' на свій API-ключ OpenWeatherMap
OPENWEATHERMAP_API_KEY = '4eab7b6f09dd8af3e7ed4349ccaeb380'

bot = telebot.TeleBot("7049864536:AAEG1UI5Y9gleLIS0zYBhGTA3EEsMvfrsl0")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == '/start':
        bot.reply_to(message, "Привіт, я бот погоди! Введіть /help щоб дізнатись як працює бот. ")
    elif message.text == '/help':
        bot.reply_to(message, "Цей бот допоможе вам отримати погоду для вказаного міста. Введіть /weather <місто>, щоб дізнатися погоду. Наприклад: /weather Львів чи /weather Kyiv")
    else:
        bot.reply_to(message, "Не розумію вашого запиту. Використовуйте команду /help для довідки.")

@bot.message_handler(commands=['weather'])
def weather(message):
    city = message.text.split()[-1]  # Отримуємо місто з команди /weather
    weather_data = get_weather(city)
    
    if weather_data:
        message_to_send = f"Погода у місті {city.capitalize()}:\nТемпература: {weather_data['temp']}°C\nВологість: {weather_data['humidity']}%"
    else:
        message_to_send = "Не вдалося отримати погоду для цього міста. Спробуйте ще раз."
    
    bot.send_message(message.chat.id, message_to_send)

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return {'temp': temperature, 'humidity': humidity}
    except Exception as e:
        print("Error fetching weather:", e)
        return None
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Не розумію вашого повідомлення. Використовуйте команду /help для довідки.")

bot.polling(none_stop=True)
