out_base_folder = "/home/dany/Dropbox/Projects/deskydoo/desky/deskydoo/fe/articles";

# Languages for text, must be set up in format ("ISO2CODE", "FULL")
LAN_LIST = [
	# ('it','italian'), 
	('en','english'), 
	('es','spanish'),
]

# *************************
# TEXT GENERATION -- Chose between: (as 202310, the 3.5 works better to me)
# chatgpt_api8					https://rapidapi.com/haxednet/api/chatgpt-api8/								chatgpt 3.5
# chatgpt_gpt4_ai_chatbot		https://rapidapi.com/nextbaseapp/api/chatgpt-gpt4-ai-chatbot				chatgpt 4
TEXT_GEN = 'chatgpt_api8'



# *************************
# IMAGE GENERATION -- Choose between (as 202310, the api5 is the best to me)
# text_to_image7 				https://rapidapi.com/haxednet/api/text-to-image7
# midjourney_api5 				https://rapidapi.com/yourdevmail/api/midjourney-api5
# midjourney_best_experience 	https://rapidapi.com/liuzhaolong765481/api/midjourney-best-experience
IMAGE_GEN = 'text_to_image7'
