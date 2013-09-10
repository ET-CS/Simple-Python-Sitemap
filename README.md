Simple-Python-Sitemap
=====================

Simple one page python based Sitemap. Designed for mod_python.

    This sitemap is still in early development and have no css design

## Prerequisities ##

1. Tenjin. - used as template engine. (easy_install Tenjin)

## Installation ##

1. Clone this repo and set your apache using mod_python to index.py
2. Copy setting.py.demo to settings.py - this is your private settings file 
3. visit your new python based Sitemap

### mod_python ###

Add to your VirtualHost in apache:

    AddHandler mod_python .py
    PythonHandler mod_python.publisher | .py
    AddHandler mod_python .psp .psp_
    PythonHandler mod_python.psp | .psp .psp_
    PythonDebug On

## Configure ##

Edit your settings.py with your list of websites:

    context = { 
        'title': 'My Sitemap',
        'items': [
            [ 'www.example.com', 'Link 1', 'My first website.' ],
            [ 'www.example.com', 'Link 2', 'My second website.' ],
            [ 'www.example.com', 'Link 3', 'My third website.' ],
            [ 'www.example.com', 'Link 4', 'Another website.' ],
            [ 'www.example.com', 'Link 5', 'Yet another website.' ],
            [ 'www.example.com', 'Link 6', 'My last website.' ]
        ]
    }



made by [ET][ET]

[ET]: http://www.etcs.me
[git]: git@github.com:ET-CS/Simple-Python-Sitemap.git