import time
import os
import requests
from bs4 import BeautifulSoup
import telepot
from datetime import datetime

URL_FILE = 'url.txt'
ID_FILE = 'tori_ids.txt'
TELEGRAM_BOT_TOKEN = 'bot_token'
TELEGRAM_OWN_USER_ID = 123

def find_tori_items():
    add_file_if_not_exits(URL_FILE)
    add_file_if_not_exits(ID_FILE)
    bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
    x = 1;

    while True:
        # Tekstitiedostossa voi olla url katottavana omilla riveillään. Tämä käy rivit läpi.
        urls = get_from_file(URL_FILE)
        for url in urls:
            open_webpage_and_find_items(url, bot)
            print("Refreshed ", x," times")
            x = x+1
        # Sleep ajan kanssa joutuu välillä pelailemaan, ettei tori blokkaa. 
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
        already_found_ids = get_from_file(ID_FILE)
        for item in items:
            id = get_id(item['id'])
            
            if id not in already_found_ids:
                # Tallentaa löydetyt id:t tekstitiedostoon
                append_to_file(id, ID_FILE)
                bot.sendMessage(TELEGRAM_OWN_USER_ID, 'Katoppa tää: ' + item['href'])
        
    except Exception as e:
        dt_string = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        error_text = dt_string + " " + str(e)
        # Tallentaa virheviestit erilliseen tiedostoon
        append_to_file(error_text, 'errors.txt')
        time.sleep(30)
        
def add_file_if_not_exits(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            print("Created ", file_name)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_tori_items()
