import os
import sys
import urllib
import http.client
import json
import requests
import random
import time

from prompts.img_prompt import *

def midjourney(conf):
   
   prompt = gen_img_prompt(conf)
   conf['img_prompt_used'] = prompt
   print("Generating for", prompt)
   
   url = "https://midjourney-api5.p.rapidapi.com/imagine"

   payload = { "prompt": prompt }
   headers = {
      "content-type": "application/json",
      "X-RapidAPI-Key": conf['api_key'],
      "X-RapidAPI-Host": "midjourney-api5.p.rapidapi.com"
   }

   response = requests.post(url, json=payload, headers=headers)

   if response.status_code != 200:
      print("Task creation", response.status_code, response.reason)
      fn_out = os.path.join(conf['path_new_post'], 'text_to_image.err')
      with open(fn_out, 'w') as fp:
         fp.write(json.dumps(response.json(), indent=3))
      raise Exception("Invalid response from midjourney 1 Task Creation: "+json.dumps(response.json()))

   c = response.json()
   taskid = c['taskId']

   print("Wait image task to finish")

   url = "https://midjourney-api5.p.rapidapi.com/task/"
   querystring = {"taskId":taskid}

   print(c)

   progress = 0
   while progress != 100:
      time.sleep(60)
      response = requests.get(url, headers=headers, params=querystring)

      if response.status_code != 200:
         print("Text To Image res", response.status_code, response.reason)
         fn_out = os.path.join(conf['path_new_post'], 'text_to_image.err')
         with open(fn_out, 'w') as fp:
            fp.write(json.dumps(response.json(), indent=3))
         raise Exception("Invalid response from ChatGPT API")

      c = response.json()
      print(c)

      progress = c['progress']
      if progress == 100:
         try:
            url = c['imageUrl'];
            response = requests.get(url, headers=headers, params=querystring)
            
            # Combine the save directory and filename to create the full file path
            filename = url.split("/")[-1].split("?")[0]
            fn_out = os.path.join(conf['path_new_post'], "mid_big_"+filename)

            # Save the content of the response (the PNG file) to the specified file path
            with open(fn_out, "wb") as file:
               file.write(response.content)

            print(f"Downloaded: {filename}")
         except:
            print("Error getting the file")
            print(c)

         break
