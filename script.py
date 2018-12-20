# -*- coding: utf-8 -*-

import vk, requests, random, json, time
from pprint import pprint

ApiConfig = {
    'token': 'HERE YOUR TOKEN GOES, BITCH',
    'version': '5.80'
}

session = vk.Session(access_token=ApiConfig['token'])
vkapi = vk.API(session, version=ApiConfig['version'])

# 1. MessageCleaner

# while True:
#     conv = vkapi.messages.getConversations(access_token=ApiConfig['token'], v=ApiConfig['version'])
#     for cs in conv['items']:
#         try:
#             vkapi.messages.deleteConversation(peer_id=cs['conversation']['peer']['id'], access_token=ApiConfig['token'], v=ApiConfig['version'])
#             print(str(cs['conversation']['peer']['id']) + " deleted")
#             time.sleep(1)
#         except Exception:
#             pass

# 2. Friends Killer
while True:
    friends = vkapi.friends.get(access_token=ApiConfig['token'], v=ApiConfig['version'])
    for f in friends['items']:
        vkapi.friends.delete(user_id=f, access_token=ApiConfig['token'], v=ApiConfig['version'])
        print(str(f) + ' deleted')
        time.sleep(1)
