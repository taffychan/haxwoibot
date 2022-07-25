# -*- coding: utf-8 -*-
import re, requests
from bs4 import BeautifulSoup
from telegram.ext import CommandHandler, Updater

updater = Updater("<TOKEN>", workers=128)
dispatcher = updater.dispatcher

def check(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Content-type": "application/json",
    }
    datas = requests.get(url, headers=headers).text
    return datas

def hax_data_center():
    hax_html_text = check("https://hax.co.id/create-vps/")
    soup = BeautifulSoup(hax_html_text, "html.parser")
    hax_center_list = [x.text for x in soup("option", value=re.compile(r"^[A-Z]{2,}-"))]
    hax_center_str = "Hax 小鸡库存\n".join(hax_center_list)
    return hax_center_str

def woiden_data_center():
    woiden_html_text = check("https://woiden.id/create-vps/")
    soup = BeautifulSoup(woiden_html_text, "html.parser")
    woiden_center_list = [x.text for x in soup("option", value=re.compile(r"^[A-Z]{2,}-"))]
    woiden_center_str = "Woiden 小鸡库存\n".join(woiden_center_list)
    return woiden_center_str

def ping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pong~")

def both(update, context):
    res1 = hax_data_center()
    res2 = woiden_data_center()
    context.bot.send_message(chat_id=update.effective_chat.id, text=res1+"\n"+res2)

def hax(update, context):
    res = hax_data_center()
    context.bot.send_message(chat_id=update.effective_chat.id, text=res)

def woiden(update, context):
    res = woiden_data_center()
    context.bot.send_message(chat_id=update.effective_chat.id, text=res)

Ping = CommandHandler('ping', ping, run_async=True)
Both = CommandHandler('both', both, run_async=True)
Hax = CommandHandler('hax', hax, run_async=True)
Woiden = CommandHandler('woiden', woiden, run_async=True)
dispatcher.add_handler(Ping)
dispatcher.add_handler(Both)
dispatcher.add_handler(Hax)
dispatcher.add_handler(Woiden)

updater.start_polling()