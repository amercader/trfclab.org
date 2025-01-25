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


with open("news.json") as f:
    news = json.load(f)

new_news = []
for item in news:
    item["title"]["ca"] = translate_ca(item["title"]["en"])
    new_news.append(item)

with open("news.json", "w") as f:
    f.write(json.dumps(new_news))

print("Done")
