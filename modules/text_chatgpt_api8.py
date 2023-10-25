# https://rapidapi.com/haxednet/api/chatgpt-api8
import requests
import random
import sys
import os
import json

from prompts.text_prompt import gen_text_prompt

def chatGPT_3_5(conf):
	url = "https://chatgpt-api8.p.rapidapi.com/"

	prompt = gen_text_prompt(conf)

	print()
	print("#### PROMPT:")
	print(prompt)

	conf['text_prompt_used'] = prompt

	print("Generating text..")
	payload = [
		{
			"content": prompt,
			"role": "user"
		}
	]
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": conf['api_key'],
		"X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
	}

	response = requests.post(url, json=payload, headers=headers)

	if response.status_code != 200:
		print("ChatGPT response", response.status_code, response.json())
		fn_out = os.path.join(conf['path_new_post'], 'lm_text.err')
		with open(fn_out, 'w') as fp:
			fp.write(json.dumps(response.json(), indent=3))
		raise Exception("Invalid response from ChatGPT API")
	
	textout = response.text;
	print(response.json())
	c = response.json()

	fn_out = os.path.join(conf['path_new_post'], 'lm_text.txt')
	with open(fn_out, 'w') as f:
		f.write(c['text'])

