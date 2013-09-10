## import modules and helper functions
import os
import tenjin
#tenjin.set_template_encoding('cp932')   # template encoding
from tenjin.helpers import *
import settings
##to check if file exist on remote server

def fileExist(file):
    if file=="http://www.etcs.me/thumbnail.png":
        return True
    else:
        return False

def index(req):
    path = os.path.dirname(os.path.abspath(__file__))
    engine = tenjin.Engine(path=[path+'/views'], layout='_layout.pyhtml')
    #context = { 'title': 'ETCS.ME Sitemap',
    #            'items': [ '<AAA>', 'B&B', '"CCC"' ] }
    #settings.context['name'] = 'et'
    for key in settings.context['items']:
        thumbnail = key[0]+'/thumbnail.png'
        if fileExist(thumbnail):
            key.append(thumbnail)
        else:
            key.append('')
    output = engine.render('table.pyhtml', settings.context)
    return output
