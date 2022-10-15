
import requests
from bs4 import BeautifulSoup
import telebot
from token_bot import token

Temp_teraz = ""


Temp_feel = ""

Temp_dawl = ""

Temp_wiatr = ""


def telegram_bot(token):
    bot = telebot.TeleBot("5455027588:AAH_oMg4rw7VqJadKf3Ym-n6xdQIXNjFPBg")

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Lomza temp: " + Temp_teraz + "\n" + "Feelings as: " + Temp_feel + "\n" + "Dawl: " + Temp_dawl + "\n" + "Wind speed: " +  Temp_wiatr)

    bot.polling()

def get_data():
    global Temp_teraz
    global Temp_details
    global Temp_feel
    global Temp_dawl
    global Temp_wiatr
    responce = requests.get(r"https://pogoda.interia.pl/prognoza-dlugoterminowa-lomza,cId,19110")

    soup = BeautifulSoup(responce.text, "lxml")

    with open ("weather.html", "w") as file:
        file.write(responce.text)

    Temp_teraz = soup.find("div", class_="weather-currently-temp-strict").text

    Temp_details = soup.find_all("span", class_="weather-currently-details-value")

    Temp_feel = Temp_details[0].text

    Temp_dawl = Temp_details[1].text.replace(" ", "").replace("hPa", "")

    Temp_wiatr = Temp_details[2].text.replace(" ", "")

if __name__ == "__main__":
    get_data()


telegram_bot(token)