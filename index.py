## import modules and helper functions
import os
import tenjin
#tenjin.set_template_encoding('cp932')   # template encoding
from tenjin.helpers import *
import settings

def index(req):
    path = os.path.dirname(os.path.abspath(__file__))
    engine = tenjin.Engine(path=[path+'/views'], layout='_layout.pyhtml')
    #context = { 'title': 'ETCS.ME Sitemap',
    #            'items': [ '<AAA>', 'B&B', '"CCC"' ] }
    output = engine.render('table.pyhtml', settings.context)
    return output
