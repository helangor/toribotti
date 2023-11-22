import time
import requests
from bs4 import BeautifulSoup
import telepot
from datetime import datetime

def find_tori_items():
    telegram_bot_token = '5593480384:AAGmKiwluDt5zBCbwcRyIxXo97I6N0sX3T8'
    bot = telepot.Bot(telegram_bot_token)
    x = 1;

    while True:
        # Tekstitiedostossa voi olla useampi tori juttu katottavana, käy kaikki läpi
        # Luo tälläinen tiedosto, jossa jokainen url omalla rivillä
        urls = get_from_file('url.txt')
        for url in urls:
            open_webpage_and_find_items(url, bot)
            print("Refreshed ", x," times")
            x = x+1
        time.sleep(500)

       
def get_id(item_id):
    return item_id.split("_")[1]

def append_to_file(text, file_name):
    with open(file_name, "a+") as file_object:
        file_object.write(text + "\n")
    
def get_from_file(file_name):
    with open(file_name, "r") as file_object:
        ids = file_object.read().splitlines()
        return ids
    
def open_webpage_and_find_items(url, bot):
    try:
        URL = url
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        items = soup.find_all(class_='item_row_flex')
        id_file_name = 'tori_ids.txt'
        already_found_ids = get_from_file(id_file_name)
        for item in items:
            id = get_id(item['id'])
            
            if id not in already_found_ids:
                # Tallentaa löydetyt id:t tekstitiedostoon
                append_to_file(id, id_file_name)
                #Botille annetaan oma telegram id 
                bot.sendMessage(442989985, 'Katoppa tää: ' + item['href'])
        
    except Exception as e:
        # Add datetime to error 
        dt_string = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        error_text = dt_string + " " + str(e) 
        append_to_file(error_text, 'errors.txt')
        time.sleep(30)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_tori_items()
