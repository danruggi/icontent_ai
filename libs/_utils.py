from PIL import Image
import json
import re, os, sys
import re
import pathlib
import time
import random
from datetime import datetime

def find_next_folder(conf):
    posts=conf['path_posts']
    all_folders = list()
    files_folders = os.scandir(posts)
    for ff in files_folders:
        if not ff.is_dir():
            continue
        if not re.search(r'^\d+$', ff.name):
            continue
        
        all_folders.append(int(ff.name))
    
    i=0;
    while True:
        if i not in all_folders:
            return os.path.join(posts, str(i))
        i+=1;

def set_conf():
    conf = dict()
    conf['path'] = sys.path[0]
    conf['path_posts'] = os.path.join(conf['path'], 'posts')

    d = pathlib.Path(conf["path_posts"]);
    if not d.exists():
        os.mkdir(conf["path_posts"])
    
    conf['path_new_post'] = find_next_folder(conf)

    return conf

def init_folders(conf):

    
    d = pathlib.Path(conf["path_new_post"]);
    if not d.exists():
        os.mkdir(conf["path_new_post"])
    
    post_num = conf["path_new_post"].split("/")[-1]

    for lan in conf['LAN_LIST']:
        out_lan_folder = os.path.join(conf['out_base_folder'], lan[0])
        d = pathlib.Path(out_lan_folder);
        if not d.exists():
            os.mkdir(out_lan_folder)



# Open a single PNG image
def png_2_webp(conf):
    files = os.scandir(conf['path_new_post']);
    for file in files:
        if not file.name.endswith('png'):
            continue

        with Image.open(file.path) as img:
            
            webpfn = file.name.replace('png', 'webp')
            fn_out = os.path.join(conf['path_new_post'], webpfn)

            # Convert and save it as WebP
            print("Saving webp", fn_out)
            img.save(fn_out, 'webp')

        print("Deleting PNG", file.path)
        os.remove(file.path)

def png_split_4(conf):
    files = os.scandir(conf['path_new_post']);
    for file in files:
        if not file.name.startswith('mid_big_'):
            continue

        with Image.open(file.path) as img:
            
            # Get the dimensions of the original image
            width, height = img.size

            print(width, height)
            
            # Calculate the dimensions for the four 1024x1024 images
            image1 = img.crop((0, 0, 1024, 1024))
            image2 = img.crop((1024, 0, 2048, 1024))
            image3 = img.crop((0, 1024, 1024, 2048))
            image4 = img.crop((1024, 1024, 2048, 2048))

        # Save the four images
        image1.save(os.path.join(conf['path_new_post'],"mid_image1.png"))
        image2.save(os.path.join(conf['path_new_post'],"mid_image2.png"))
        image3.save(os.path.join(conf['path_new_post'],"mid_image3.png"))
        image4.save(os.path.join(conf['path_new_post'],"mid_image4.png"))

        print("Deleting PNG", file.path)
        os.remove(file.path)

def create_idx_image(conf, fpath):
    with Image.open(fpath) as img:
        # Resize the image to 480x480
        img = img.resize((480, 480))

        # Calculate the coordinates for cropping
        left = 0
        top = (480 - 320) / 2
        right = 480
        bottom = top + 320

        # Crop the central part (360x480)
        img = img.crop((left, top, right, bottom))

        # Save the resulting image
        img.save(conf['out_img_idx_path'], 'webp')

def gpt_txt_to_json(conf):
    out = dict()
    fn = os.path.join(conf['path_new_post'], 'lm_text.txt');
    with open(fn) as f:
        t = f.read()

    t = t.replace("\\n", "\n")
    # c = json.loads(data)
    # t = c['text']
    tA = t.split('\n')
    tA = [x for x in tA if x != '']

    out['title'] = tA[0].replace("Title:", '').strip()
    out['desc'] = tA[1].replace("Description:", '').strip()
    out['par'] = list()
    for i in range(2, len(tA)):
        out['par'].append(tA[i])

    # print(out)
    return out

def desky_prov_json(conf):
    import shutil

    # Output files and folders settings
    post_num = conf['path_new_post'].split("/")[-1]
    conf['out_json_folder'] = os.path.join(conf['out_base_folder'], conf['lan_code'])
    conf['out_json_path'] = os.path.join(conf['out_json_folder'], post_num+".json")
    conf['out_json_idx_path'] = os.path.join(conf['out_base_folder'], conf['lan_code']+'_arts.json')
    out_img_folder = os.path.join(conf['out_base_folder'], 'imgs', post_num) 
    
    d = pathlib.Path(out_img_folder);
    if not d.exists():
        os.mkdir(out_img_folder)

    conf['out_img_folder'] = out_img_folder
    conf['out_img_idx_path'] = os.path.join(out_img_folder, 'sm_img_title.webp')

    ## FULL JSON
    c = gpt_txt_to_json(conf)

    files = os.scandir(conf['path_new_post']);
    img_idx_created = False;
    c['images'] = list()
    for file in files:
        if not file.name.endswith('webp'):
            continue
        if not img_idx_created:
            create_idx_image(conf, file.path)
            img_idx_created = True

        new_file_path = os.path.join(conf['out_img_folder'], file.name)
        
        shutil.copy(file.path, new_file_path)

        c['images'].append(new_file_path)



    # Format the date and time as 'YYYYMMDD_HHMM'
    now = datetime.now()
    formatted_time = now.strftime('%Y%m%d_%H%M')
    
    c['art_id'] = conf['path_new_post'].split("/")[-1]
    c['ts'] = formatted_time

    print()
    print("Out FULL JSON")
    print(c)

    with open(conf['out_json_path'], 'a+') as fp:
        fp.write(json.dumps(c))
        fp.write("\n")

    ## INDEX JSON
    c_idx = dict()
    c_idx['ts'] = c['ts']
    c_idx['title'] = c['title']
    c_idx['desc'] = c['desc']
    c_idx['excert'] = c['par'][0][:100]+"..."
    c_idx['img'] = conf['out_img_idx_path']
    c_idx['post_num'] = post_num;

    with open(conf['out_json_idx_path'], 'a+') as fp:
        fp.write(json.dumps(c_idx))
        fp.write("\n")
    # print(fn_json_prod_prov)
