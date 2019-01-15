import sys
import os
import urllib.request
import simplejson

page = urllib.request.urlopen("https://web.whatsapp.com")

for line in page: print(str(line, encoding = "utf-8"), end = ' ')

print(type(page))
