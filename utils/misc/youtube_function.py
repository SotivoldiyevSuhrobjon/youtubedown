from pprint import pprint

import requests

from states.AllStates import MyStates


async def video_detail(url):
    video_id = url.split('/')[-1]
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    querystring = {"videoId": f"{video_id}"}

    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "e8b1965b1emsh8687d05853e9e2dp1dc16djsn60fff64aaa5c",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring, )
    res = response.json()
    return res


async def size_detail(data):
    quality = []
    dict_list = data['videos']['items']
    tuple_list = [(d['quality'], d['sizeText'], d['extension']) for d in dict_list]
    for i, t in enumerate(tuple_list, start=0):
        # new_tuple = t
        quality.append(t)
    return quality


#      # bu dictdan qualitylarni olish
#      # return quality
#      # [("360p", "12 MB"), ("480p", "55 MB")]
#
async def link_detail(url_dict, quality):

    pprint(url_dict)
    pprint(quality)
#     # dictni icidan qualityni urlini qaytaradi
#     # return url
#
