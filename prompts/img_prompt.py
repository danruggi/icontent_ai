import random

def gen_img_prompt(conf):
	prompts = [
		"rustic hostel reception photo quality",
		"small rustic hostel for happy artisans digital art",
		"hostel with mountain view",
		"hostel with alps view",
		"hostel with seaview",
		"hostel shared dormitory with bunk beds with view of milan, italy",
		"hostel shared dormitory with bunk beds with view of garda lake, italy",
		"hostel shared dormitory with bunk beds  with london view",
		"hostel shared dormitory with bunk beds  with new delhi view",
		"small rustic hostel in beautiful nature",
		"rustic hostel with happy guests",
		"people partying in an hostel"
	];
	prompt = prompts[random.randint(0, len(prompts)-1)]
	return prompt
