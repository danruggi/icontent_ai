# https://rapidapi.com/haxednet/api/text-to-image7

import os
import sys
import urllib
import http.client
import json
import requests
import random

from prompts.img_prompt import *

def text_to_image7(conf):
   conn = http.client.HTTPSConnection("text-to-image7.p.rapidapi.com")

   headers = {
      "X-RapidAPI-Key": conf['api_key'],
      'X-RapidAPI-Host': "text-to-image7.p.rapidapi.com"
   }

   prompt = gen_img_prompt(conf)
   conf['img_prompt_used'] = prompt
   print("Generating for", prompt)

   encoded_string = urllib.parse.quote(prompt)
   conn.request("GET", f"/?prompt={encoded_string}&batch_size=3&negative_prompt=ugly%2C%20duplicate%2C%20morbid%2C%20mutilated%2C%20%5Bout%20of%20frame%5D%2C%20extra%20fingers%2C%20mutated%20hands%2C%20poorly%20drawn%20hands%2C%20poorly%20drawn%20face%2C%20mutation%2C%20deformed%2C%20blurry%2C%20bad%20anatomy%2C%20bad%20proportions", headers=headers)

   res = conn.getresponse()
   data = res.read()
   c = json.loads(data.decode("utf-8"))

   if res.status != 200:
      print("Text To Image res", res.status, res.reason)
      fn_out = os.path.join(conf['path_new_post'], 'text_to_image.err')
      with open(fn_out, 'w') as fp:
         fp.write(json.dumps(c, indent=3))
      raise Exception("Invalid res from ChatGPT API")


   print(c)

   urls = c['data'] if 'data' in c else [];
   for url in urls:
      try:
         response = requests.get(url)
         if response.status_code == 200:
            # Extract the filename from the URL
            filename = url.split("/")[-1]
            # Combine the save directory and filename to create the full file path
            file_path = filename

            fn_out = os.path.join(conf['path_new_post'], filename)

            # Save the content of the response (the PNG file) to the specified file path
            with open(fn_out, "wb") as file:
               file.write(response.content)

            print(f"Downloaded: {filename}")
         else:
            fn_out = os.path.join(conf['path_new_post'], 'text_to_image.err')
            print(f"Failed to download: {url}, Status code: {response.status_code}")
            with open(fn_out, 'w') as fp:
               fp.write(f"Failed to download: {url}, Status code: {response.status_code}")

      except Exception as e:
         print(f"Error downloading {url}: {str(e)}")