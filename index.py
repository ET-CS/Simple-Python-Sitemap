## import modules and helper functions
import os
import os.path
import tenjin
#tenjin.set_template_encoding('cp932')   # template encoding
from tenjin.helpers import *
import settings

def thumbnailExist(filename):
    pass

def index(req):
    path = os.path.dirname(os.path.abspath(__file__))
    engine = tenjin.Engine(path=[path+'/views'], layout='_layout.pyhtml')
    for key in settings.context['items']:
        thumbnail = key[0]+'/thumbnail.png'
        filename = path+'/thumbs/'+key[0].split('//')[1]+'.png'
        if os.path.isfile(filename):
            key.append(thumbnail)
        else:
            key.append('')

    output = engine.render('table.pyhtml', settings.context)
    return output
