import json
import os
import shutil
import sys

from keybert import KeyBERT  # type: ignore
import ctranslate2
import pyonmttok
from transformers import MarianMTModel, MarianTokenizer
from huggingface_hub import snapshot_download

from pprint import pprint
from slugify import slugify


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICS_DIR = os.path.join(CURRENT_DIR, "..", "pics_trcflab")
OUTPUT_DIR = os.path.join(CURRENT_DIR, "content/post")

model_dir_ca = snapshot_download(
    repo_id="projecte-aina/aina-translator-en-ca", revision="main"
)
tokenizer_ca = pyonmttok.Tokenizer(
    mode="none", sp_model_path=model_dir_ca + "/spm.model"
)


def translate_es(text):
    model_name = f"Helsinki-NLP/opus-mt-en-es"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs, num_beams=4, max_length=5000, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text


def translate_ca(text):

    tokenized = tokenizer_ca.tokenize(text)

    translator = ctranslate2.Translator(model_dir_ca)
    translated = translator.translate_batch([tokenized[0]])

    return tokenizer_ca.detokenize(translated[0][0]["tokens"])


def get_slug(title, date, kw_model):

    keywords = [slugify(k[0]) for k in kw_model.extract_keywords(title)][:3]

    slug = f"{date}-{'-'.join(keywords)}"
    return slug


def create_news_json():

    kw_model = KeyBERT()

    with open("news.txt") as f:
        content = f.readlines()

    news = []

    item = {
        "body": {
            "en": "",
            "es": "",
            "ca": "",
        },
        "title": {
            "en": "",
            "es": "",
            "ca": "",
        },
    }
    cnt = 1
    for line in content:
        line = line.strip()
        if line.startswith("NOTICIA"):
            print(f"Starting news item {cnt}")
            if item.get("title", {}).get("en"):
                item["body"]["en"].strip()
                try:
                    item["body"]["es"] = translate_es(item["body"]["en"])
                    item["body"]["ca"] = translate_ca(item["body"]["en"])
                except Exception as e:
                    print(f"Error in item: {item['title']['en']}")
                    print(e)


                item["slug"] = get_slug(item["title"]["en"], item["date"], kw_model)
                news.append(item)
                cnt += 1

                item = {
                    "body": {
                        "en": "",
                        "es": "",
                        "ca": "",
                    },
                    "title": {
                        "en": "",
                        "es": "",
                        "ca": "",
                    },
                }

        elif line.startswith("Foto "):
            item["pic"] = line
        elif line.startswith("Títol"):
            item["title"]["en"] = line.replace("Títol:", "").strip()
            try:
                item["title"]["es"] = translate_es(item["title"]["en"])
                item["title"]["ca"] = translate_es(item["title"]["en"])
            except Exception as e:
                print(f"Error in item: {item['title']['en']}")
                print(e)
        elif line.startswith("Data"):
            values = line.replace("Data:", "").strip().split("/")
            item["date"] = f"{values[2]}-{values[1]}-{values[0]}"
        else:
            line = line.replace("Cos de la noticia:", "").strip()

            if line:
                item["body"]["en"] += line + "\n"

    with open("news.json", "w") as f:
        f.write(json.dumps(news))


def create_news_file(news_item, file_path):
    title = news_item["title"].replace('"', '\\"')

    file_contents = """
---
title: "{title}"
date: {date}
image:
  filename: featured.jpg
  focal_point: 'Smart'
---

{body}
""".format(
        title=title, date=news_item["date"], body=news_item["body"]
    ).strip()

    with open(file_path, "w") as f:
        f.write(file_contents)


def create_news_image(news_image, file_path):

    pic_info = news_item.get("pic")
    if not pic_info:
        print(f"No pic info for news item {news_item['title']}")
        return

    file_name = "".join(pic_info.split(" ")[:2]).rstrip(".") + ".jpg"
    file_path = os.path.join(PICS_DIR, file_name)

    file_exists = os.path.exists(file_path)
    print(f"{file_path} -> {file_exists}")

    if not file_exists:
        print(f"{file_path} does not exist")
        return

    dest_path = os.path.join(OUTPUT_DIR, news_item["slug"], "featured.jpg")

    shutil.copy2(file_path, dest_path)
    print(f"Copied {file_name} to news item directory")


if not os.path.exists("news.json"):
    create_news_json()
    print("news.json created")


sys.exit(1)

with open("news.json") as f:
    news = json.load(f)


for news_item in news:

    target_dir = os.path.join(OUTPUT_DIR, news_item["slug"])
    if not os.path.exists(target_dir):
        os.mkdir(target_dir, mode=0o774)

    news_file = os.path.join(target_dir, "index.en.md")
    if not os.path.exists(news_file):
        create_news_file(news_item, news_file)

    image_file = os.path.join(target_dir, "featured.jpg")
    if not os.path.exists(image_file):
        create_news_image(news_item, image_file)
