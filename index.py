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

# Check if thumbnails available
def checkThumbnails():
    for key in settings.context['items']:
        thumbnail = 'thumbs/'+key[0].split('//')[1]+'.png'
        if os.path.isfile(path+'/'+thumbnail):
            key.append(thumbnail)
        else:
            key.append('')

# Everything starts here...
def index(req):
    engine = tenjin.Engine(path=[path+'/views'], layout='_layout.pyhtml')
    checkThumbnails()
    return engine.render('table.pyhtml', settings.context)
