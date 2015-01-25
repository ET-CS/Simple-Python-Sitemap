#!/usr/bin/env python
## Import modules and helper functions
import os
# Get working directory
import os.path; path = os.path.dirname(os.path.abspath(__file__))
# tenjin Template Engine
import tenjin
# Tenjin.set_template_encoding('cp932')		# template encoding
from tenjin.helpers import *
# Import settings file
import settings
from selenium import webdriver
from PIL import Image

# Check if thumbnails available
def checkThumbnails():
    for key in settings.context['items']:
        thumbnail = 'thumbs/'+key[0].split('//')[1]+'.png'
        if not os.path.isfile(path+'/'+thumbnail):
            print "downloading " + key[0]
            br = webdriver.PhantomJS()
            print br.get_window_size()
            br.set_window_size(1400, 900)
            print br.get_window_size()
            br.get(key[0])
            br.save_screenshot(thumbnail)
            if os.path.isfile(path+'/'+thumbnail):
        	im = Image.open(thumbnail)
        	im = im.crop((0, 0, 1400, 900))
        	im.save(thumbnail);
        	br.quit

checkThumbnails()
