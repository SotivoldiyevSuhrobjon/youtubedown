from pprint import pprint

from aiogram.dispatcher import FSMContext
from pytube import YouTube
from aiogram import Dispatcher
from aiogram.types import *
from playhouse.shortcuts import model_to_dict
import json

from keyboards.inline.youtube_keyboard import choose_size
from loader import dp
import requests
from loader import bot
from states.AllStates import MyStates
from utils.misc.youtube_function import video_detail, size_detail, link_detail


async def bot_start(message: Message):
    await message.answer(
        "Assalomu alaykum instagramdan video yuklaydigan botimizga xush kelibsiz instagram urlni kiriting")


async def get_video_handler(msg: Message):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    text = msg.text
    querystring = {"url": f"{text}"}

    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "868d868a4bmshab5dabfa78980dfp1a86cfjsnaf421c502844",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    json = response.json()
    # pprint(json)
    video = json['media']
    thumbnail = json['thumbnail']
    title = json['title']
    await msg.answer_video(video, thumbnail, caption=title)
    # print("rasm", json['thumbnail'])
    # print("nomi", json['title'])


async def youtube_download_handler(msg: Message):
    chat_id = msg.chat.id
    video_dict = await video_detail(msg.text)
    quality = await size_detail(video_dict)
    # await link_detail(video_dict, quality)
    photo_url = video_dict['thumbnails'][-2]['url']
    btn = await choose_size(quality)
    title = video_dict['title']
    await msg.answer_photo(photo_url, caption=title, reply_markup=btn)


# url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
# text = request.text
# video_id = text.split('/')[-1]
# chat_id = request['from']['id']
#
# querystring = {"videoId": f"{video_id}"}
#
# headers = {
#     "content-type": "application/octet-stream",
#     "X-RapidAPI-Key": "868d868a4bmshab5dabfa78980dfp1a86cfjsnaf421c502844",
#     "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring, )
# res = response.json()
# pprint(res)
# size = res['videos']
# chat_id = request['from']['id']
# video = res['videos']['items']
# link = video[0]['url']
# past = video[0]['sizeText']
# orta = video[1]['sizeText']
# yuqori = video[3]['sizeText']
# btn = await choose_size(past, orta, yuqori)
# photo = res['thumbnails'][0]['url']
# title = res['title']
#
# await bot.send_photo(chat_id=f"{chat_id}", photo=photo, caption=title, reply_markup=btn)


async def send_video_callback_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    url_dict = call.message.text
    text = call.data
    quality = text.split(':')[-1]
    link = await link_detail(url_dict, quality)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(get_video_handler, regexp='instagram.com')
    dp.register_message_handler(youtube_download_handler, regexp='https://youtu.be/', )

    dp.register_callback_query_handler(send_video_callback_handler, state=MyStates.url, text_contains='size', )
