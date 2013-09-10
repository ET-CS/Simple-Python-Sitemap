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
    engine = tenjin.Engine(path=[path+'/views'], layout=settings.skin+'/_layout.pyhtml')
    for key in settings.context['items']:
        filename = key[0].split('//')[1]+'.png'
        thumbnail = 'thumbs/'+filename
        if os.path.isfile(path+'/thumbs/'+filename):
            key.append(thumbnail)
        else:
            key.append('')

    output = engine.render(settings.skin+'/table.pyhtml', settings.context)
    return output
