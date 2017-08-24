#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, string
import urllib.request
from urllib.request import urlopen
import urllib.error
import re


page = urlopen("http://sebsauvage.net/index.html").read()
urls = re.findall('href=[\'"]?([^\'" >]+)',page)
for url in urls:
    print( url)
