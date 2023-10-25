#!/usr/bin/env python3

import random
import sys
import os
import re
import pathlib
import subprocess
import multiprocessing

from libs._utils import *
from srvr.srv import start_flask_app

import settings

## This import all variables from settings file
sets={var:vars(settings)[var] for var in dir(settings) if not var.startswith('__')}

def main():
	# print(sets)
	conf = set_conf()
	conf.update(sets)

	api_keys = list()
	with open('.api_keys.store') as f:
		for line in f.read().split('\n'):
			if line.strip().startswith("#"):
				continue
			if len(line) == 0:
				continue
			api_keys.append(line)

	# Set api key
	# conf['path_new_post'] = '/home/dany/Dropbox/Projects/icontent_ai/posts/48'
	conf['api_key'] = api_keys[random.randint(0,len(api_keys)-1)]

	# Select language
	lan_list = conf['LAN_LIST']
	lan_idx = random.randint(0, len(lan_list)-1)
	lan = lan_list[lan_idx][1]
	lan_code = lan_list[lan_idx][0]
	conf['lan_code'] = lan_code
	conf['lan_full'] = lan
	print("Writing article in ->", lan)
	
	# Init the new post folder
	print("Create NEW FOLDERS ->", conf['path_new_post'])
	init_folders(conf)

	print()

	# print(conf)
	# return

	try:
		# STEP 1
		# Text generation
		print("Module for generating text..")
		if 'TEXT_GEN' not in conf:
			print("TEXT GENERATION: disabled")

		elif conf['TEXT_GEN'] == 'chatgpt_api8':
			from modules.text_chatgpt_api8 import chatGPT_3_5
			chatGPT_3_5(conf)
		
		elif conf['TEXT_GEN'] == 'chatgpt_gpt4_ai_chatbot':
			from modules.text_chatgpt_gpt4_ai_chatbot import chatGPT_4
			chatGPT_4(conf)
		
		else:
			print("TEXT GENERATION: disabled")
		print()

		# STEP 2
		# Image generation
		print("Module for generating Images..")
		if 'IMAGE_GEN' not in conf:
			print("IMAGE GENERATION: disabled")

		elif conf['IMAGE_GEN'] == 'text_to_image7':
			from modules.img_text_to_image7 import text_to_image7
			text_to_image7(conf)

		elif conf['IMAGE_GEN'] == 'midjourney_api5':
			from modules.img_midjourney_api5 import midjourney
			midjourney(conf);
			png_split_4(conf)

		elif conf['IMAGE_GEN'] == 'midjourney_best_experience':	
			from modules.img_midjourney_best_experience import midjourney_best_exp
			midjourney_best_exp(conf)
			png_split_4(conf)

		else:
			print("IMAGE GENERATION: disabled")
		print()

		# STEP 3
		# Image conversion
		print("Converting Images")
		png_2_webp(conf)
		print()

		# STEP 4
		# JSON Create
		print("Creating the html")
		desky_prov_json(conf)

	except Exception as e:
		print("Error", e)

	# flask_process.join()

main()