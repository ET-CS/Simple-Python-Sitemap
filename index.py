## import modules and helper functions
import os
import os.path; path = os.path.dirname(os.path.abspath(__file__))
import tenjin
#tenjin.set_template_encoding('cp932')   # template encoding
from tenjin.helpers import *
import settings

# Check if thumbnails available
def checkThumbnails():
    for key in settings.context['items']:
        filename = key[0].split('//')[1]+'.png'
        thumbnail = 'thumbs/'+filename
        if os.path.isfile(path+'/thumbs/'+filename):
            key.append(thumbnail)
        else:
            key.append('')

# Everything starts here...
def index(req):
    engine = tenjin.Engine(path=[path+'/views'], layout='_layout.pyhtml')
    checkThumbnails()
    output = engine.render('table.pyhtml', settings.context)
    return output
