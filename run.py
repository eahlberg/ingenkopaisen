#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import random
import os
import sys

FILENAME = os.getcwd() + "/data.txt"

def main():
    print get_saying()

def update():
    URL = "http://sv.wikipedia.org/wiki/Lista_över_svenska_idiomatiska_uttryck"
    r = requests.get(URL)
    html_doc = r.text
    save_to_file(r.text.encode("utf-8"))

def save_to_file(text):
    with open(FILENAME, "wb") as f:
        f.write(text)

def load():
    text = None
    with open(FILENAME, "r") as f:
        text = f.read()
    return text

def get_saying():
    soup = BeautifulSoup(load())
    uls = soup.findAll("ul")
    list_items = []
    for ul in uls:
        for li in ul.findAll("li"):
            list_items.append(li.text.encode("utf-8"))
    return list_items[random.randint(0, len(list_items)-1)]

if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) == 2:
        if args[1] == "-u":
            update()
            main()
        else:
            print "Invalid argument. Use ./run.py -u for update"
    else:
        if not os.path.isfile("data.txt"):
            print "Usage:"
            print "'./run.py -u' (first run) alt. ./run.py"
        else:
            main()
