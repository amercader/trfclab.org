import json
import os
import shutil

from keybert import KeyBERT  # type: ignore

from pprint import pprint
from slugify import slugify


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICS_DIR = os.path.join(CURRENT_DIR, "..", "pics_trcflab")
OUTPUT_DIR = os.path.join(CURRENT_DIR, "content/en/post")


def get_slug(title, datei, kw_model):

    keywords = [slugify(k[0]) for k in kw_model.extract_keywords(title)][:3]

    slug = f"{date}-{'-'.join(keywords)}"
    return slug


def create_news_json():

    kw_model = KeyBERT()

    with open("news.txt") as f:
        content = f.readlines()

    news = []

    item = {"body": ""}
    for line in content:
        line = line.strip()
        if line.startswith("NOTICIA"):
            if item.get("title"):
                item["body"].strip()

                item["slug"] = get_slug(item["title"], item["date"], kw_model)
                news.append(item)

            item = {"body": ""}

        elif line.startswith("Foto "):
            item["pic"] = line
        elif line.startswith("Títol"):
            item["title"] = line.replace("Títol:", "").strip()

        elif line.startswith("Data"):
            values = line.replace("Data:", "").strip().split("/")
            item["date"] = f"{values[2]}-{values[1]}-{values[0]}"
        else:
            line = line.replace("Cos de la noticia:", "").strip()

            if line:
                item["body"] += line + "\n"

    with open("news.json", "w") as f:
        f.write(json.dumps(news))


def create_news_file(news_item, file_path):
    title = news_item["title"].replace('"', '\\"')

    file_contents = """
---
title: "{title}"
date: {date}
image:
  focal_point: 'top'
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

with open("news.json") as f:
    news = json.load(f)


for news_item in news:

    target_dir = os.path.join(OUTPUT_DIR, news_item["slug"])
    if not os.path.exists(target_dir):
        os.mkdir(target_dir, mode=0o774)

    news_file = os.path.join(target_dir, "index.md")
    if not os.path.exists(news_file):
        create_news_file(news_item, news_file)

    image_file = os.path.join(target_dir, "featured.jpg")
    if not os.path.exists(image_file):
        create_news_image(news_item, image_file)
