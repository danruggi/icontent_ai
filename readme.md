<!-- Version 0.0 alfa -->
<!-- Developed by Daniele Rugginenti -->

# Automate content generation using the AI
This pipeline generate texts and images to publish articles on your website.

I developed it for my website to improve SEO, you can check an example here 
(all automated AI generated articles): https://deskydoo.com/fe/articles/articles_index 
I use it and I generate content *for free*. 

# Pipeline
Pipeline is quite simple:
- You define a random text prompt(s). 
- You define a random image prompt(s). 
- It uses configurable API to get texts and images
- It cut the midjourney image into 4, if needed  
- Convert those in webp
- Create a json containing paths
- Publish json in the webfolder 
- You read the jsons with php file() - examples for a php-index and for php-load-article in the "examples" folder

# What you need
1. clone the project on your webserver
2. register to **rapidAPI**
3. register to the APIs you want to use (links in settings)
4. **Create a file called** .api_keys.store in the main dir, and add your API keys, one por line, no spaces
5. Change prompts script, you can begin with static ones too
6. ./icontent_ai.py
7. Configure your webserver to read the json files.

If you need help to configure your webserver, you can contact me, there are different ways to do it.

# Does it work with wordpress? 
Sure. Just need to call the WS with the right parameters. 
Can be done via python too.

# Is it free?
This script is opensource and free to use.
Free Tier in rapiAPI is quite strict, you can get 5/10 calls a month/por API/por KEY. 
You can use multiple API, or you can pay the usage, if you intend to use more frequently.