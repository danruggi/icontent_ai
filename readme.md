<!-- Version 0.0 alfa -->
<!-- Developed by Daniele Rugginenti -->

# Automate Content Generation with AI
This pipeline automates the generation of text and images for publishing articles on your website. I initially developed it for my own website to enhance SEO. You can see an example of entirely AI-generated articles here: AI-Generated Articles. What's more, it allows you to create content for free.

# How the Pipeline Works
The process is straightforward:

- Define random text prompts.
- Define random image prompts.
- Utilize configurable APIs to obtain text and images.
- Crop images into quarters if necessary.
- Convert images to WebP format.
- Generate a JSON file containing file paths.
- Publish the JSON file in the web folder.
- Use PHP to read the JSON files, and you can find examples for a PHP index and loading articles in the "examples" folder.

# What You Need
Here's what you need to do:

- Clone the project to your web server.
- Register on rapidAPI.
- Sign up for the APIs you want to use (links provided in settings.py and on the bottom of this help).
- Create a file called .api_keys.store in the main directory and add your API keys, one per line without spaces.
- Customize the text prompts; you can start with static ones if desired.
- Run ./icontent_ai.py.
- Configure your web server to read the JSON files.
- If you require assistance configuring this on your web server or website, feel free to contact me. There are different ways to accomplish it.

# Compatibility with WordPress
Yes, it's compatible with WordPress. You simply need to call the web service with the right parameters, which can also be done using Python.

# Is it Free?
Absolutely. This script is open source and free to use. 
The free tier on rapidAPI has some limitations, allowing around 5 to 10 calls per month per API per key. 
If you plan to use it more frequently, you can explore using multiple APIs or opt for paid usage of specific APIs.

# API
After some tests, the best APIs to use are:
For text: https://rapidapi.com/nextbaseapp/api/chatgpt-gpt4-ai-chatbot
For Images: https://rapidapi.com/yourdevmail/api/midjourney-api5

You just need to configure the script as:
TEXT_GEN = 'chatgpt_api8'
IMAGE_GEN = 'text_to_image7'
to use those relative modules

