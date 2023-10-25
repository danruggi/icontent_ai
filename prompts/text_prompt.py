import random

def gen_text_prompt(conf):
	pax = random.randint(10, 50);
	pax = 5*(pax//5)
	lan = conf['lan_full']
	
	title_ways = ['original', 'clickbait', 'serious']
	way1 = title_ways[random.randint(0,len(title_ways)-1)]
	way2 = title_ways[random.randint(0,len(title_ways)-1)]

	
	words = 10*(random.randint(600, 1000)//10);
	prompt = f"I need a title, a description, plus 5 paragraphs continous text article. Article must be in {lan}, should be around {words} words\n";
	
	words = (random.randint(2, 14));
	

	prompt += f"Output must begin with 'Title:' and a {words} words {way1} title.\n"
	prompt += f"Second block must begin with 'Description:' and a 10-20 words {way2} description, not mentioning deskydoo.\n"
	prompt += "No other titles.\n\n"

	prompt += "Following 5 Paragraphs must be separated by newlines, in 5 blocks.\n"
	words = 10*(random.randint(10, 120)//10);
	prompt_list_1=[
		f"article begins writing a {words} words paragraph about managing a {pax} persons hostel, without a property management system\n",
		f"article begins writing a {words} words text about setting up a hostel\n",
		f"article begins writing a {words} words text about managing a hostel\n",
		f"article begins writing a {words} words text about benefits working in a hostel\n",
		f"article begins writing a {words} words text about receptions skills needed managing a hostel\n",
		f"article begins writing a {words} words text about management skills needed managing a hostel\n",
	]

	# About a free pms
	words = 10*(random.randint(50, 120)//10);
	prompt_list_2=[
		f"next, a {words} words paragraph about benefits of getting a free property management system in your hostel\n",
		f"next, a {words} words paragraph about advantages of using a free property management system in your hostel\n",
		f"next, a {words} words paragraph about benefits of using a cloud based free property management system in your hostel\n",
		f"next, a {words} words paragraph about benefits of using a property management system that manage also houskeeping in your hostel\n",
		f"next, Write a {words} words paragraph about benefits of using a software that also manage housekeeping and employees\n",
		f"next, Write a {words} words paragraph about benefits of using a software that also manage housekeeping\n",
		f"next, Write a {words} words paragraph about benefits of using a software that also record staff activities\n",
	]

	# About staff management
	words = 10*(random.randint(40, 100)//10);
	prompt_list_3=[
		f"next, introduce briefly deskydoo free PMS in {words} words, speaking about drag & drop calendar interface, booking page\n",
		f"next, introduce briefly deskydoo free PMS in {words} words, speaking about drag & drop calendar, payments informations directly available in calendar\n",
		f"next, introduce briefly deskydoo free PMS in {words} words, speaking about drag & drop calendar, arrival leaving easy to view\n",
		f"next, introduce briefly deskydoo free PMS in {words} words, speaking about drag & drop calendar, occupied beds/rooms immediatly visible\n",
		f"next, introduce briefly deskydoo free PMS in {words} words, speaking about drag & drop calendar, occupied beds/rooms immediatly visible\n",
		f"next, introduce briefly deskydoo free PMS in {words} words, speaking about drag & drop calendar, available with beds view and room view\n",
		f"next, introduce briefly deskydoo free PMS in {words} words, speaking about drag & drop calendar, housekeeping management directly on calendar\n",
		f"next, introduce briefly deskydoo free PMS in {words} words, speaking about drag & drop calendar, available on mobile phones\n",
	]

	words = 10*(random.randint(80, 250)//10);
	prompt_list_4=[
		f"next, explain deskydoo free PMS in {words} words, speaking about reservation page with all the needed informations in one view, payments management, smoth operations\n",
		f"next, explain deskydoo free PMS in {words} words, speaking about page with all the needed informations in one view, fast learning curve\n",
		f"next, explain deskydoo free PMS in {words} words, speaking about page with all the needed informations in one view, reports system\n",
		f"next, explain deskydoo free PMS in {words} words, speaking about page with all the needed informations in one view, booking management, checkin, checkout\n",
		f"next, explain deskydoo free PMS in {words} words, speaking about page with all the needed informations in one view, checkout algorithms to solve common errors\n",
		f"next, explain deskydoo free PMS in {words} words, speaking about page with all the needed informations in one view, guests managemet\n",
	]

	prompt_list_5=[
		f"next, explain some concepts about this arguments using some words that can be SEO relevant, not using a list of words, but continous text.\n",
		f"next, resume concepts using some words that can be SEO relevant, not a list of words, but in continous text.\n",
	]

	tone_ways = ['funny', 'serious', 'normal', 'as you want to explain to a child', 'scientific']
	tone1 = tone_ways[random.randint(0,len(tone_ways)-1)]
	
	prompt_fin = f"This article need to be written in {tone1} tone"

	prompt += prompt_list_1[random.randint(0,len(prompt_list_1)-1)];
	prompt += prompt_list_2[random.randint(0,len(prompt_list_2)-1)];
	prompt += prompt_list_3[random.randint(0,len(prompt_list_3)-1)];
	prompt += prompt_list_4[random.randint(0,len(prompt_list_4)-1)];
	prompt += prompt_list_5[random.randint(0,len(prompt_list_5)-1)];
	prompt += prompt_fin

	return prompt