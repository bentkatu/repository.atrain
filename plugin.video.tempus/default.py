# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Add-on: Tempus
# Author: whufclee, ad

import os           # access operating system commands
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)
import re           # allows use of regex commands, if you're intending on scraping you'll need this
import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows

from koding import route, Add_Dir, Addon_Setting, Data_Type, Find_In_Text
from koding import Open_URL, OK_Dialog, Open_Settings, Play_Video, Run, Text_File

debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id
home         = xbmc.translatePath('special://home') # Set the path of the home Kodi folder

# Our master XML we want to load up
main_xml     = 'https://raw.githubusercontent.com/bentkatu/repository.atrain/master/plugin.video.tempus/resources/video.xml'

#----------------------------------------------------------------
@route(mode='start')
def Start():
    Main_Menu(main_xml)
#----------------------------------------------------------------
@route(mode='main_menu',args=['url'])
def Main_Menu(url=main_xml):

# If debug mode is enabled show the koding tutorials
    if debug == 'true':
        Add_Dir ( '[COLOR=lime]Koding Tutorials[/COLOR]', '', "tutorials", True, '', '', '' )

#############################################################
# COMMENT OUT THE FOLLOWING 2 LINES WHEN READY FOR RELEASE!!!
    #else:
        #Add_Dir ( '[COLOR=lime]Enable debug mode for some cool dev tools![/COLOR]', '', "koding_settings", False, '', '', '' )
#############################################################

# An optional example title/message, however in our example we're going to do one via our online xml so we've commented this out
    # my_message= "{'title' : 'Support & Suggestions', 'msg' : \"If you come across any online content you'd like to get added please use the support thread at noobsandnerds.com and I'll be happy to look into it for you.\"}"
    # Add_Dir(
    #     name="Support/Suggestions", url=my_message, mode="simple_dialog", folder=False,
    #     icon="https://cdn2.iconfinder.com/data/icons/picons-basic-2/57/basic2-087_info-512.png")

# Read the contents of our file into memory
    if url.startswith('http'):
        contents  = Open_URL(url)
    else:
        contents  = Text_File(url,'r')

# This isn't essential but we'll replace all linebreaks (\n) and tabs (\t) with an empty string.
# This removes them and just makes it a smaller file to work with and easier to debug.
    contents = contents.replace('\n','').replace('\t','')

# Split the contents up into sections - we're finding every instance of <item> and </item> and everything inbetween
    raw_links = Find_In_Text(content=contents, start='<item>', end=r'</item>')
    xbmc.log(repr(raw_links),2)
    counter = 1
# Now loop through each of those matches and pull out the relevant data
    for item in raw_links:
        xbmc.log('# Checking link %s'%counter,2)
        counter += 1
        title  = Find_In_Text(content=item, start='<title>', end=r'</title>')
        title  = title[0] if (title!=None) else 'Unknown Video'
        thumb  = Find_In_Text(content=item, start='<thumbnail>', end=r'</thumbnail>')
        thumb  = thumb[0] if (thumb!=None) else ''
        fanart = Find_In_Text(content=item, start='<thumbnail>', end=r'</thumbnail>')
        fanart = fanart[0] if (fanart!=None) else ''

    # If this contains sublinks grab all of them
        if not '<sublink>' in item:
            links  = Find_In_Text(content=item, start='<link>', end=r'</link>')

    # Otherwise just grab the link tag
        else:
            links  = Find_In_Text(content=item, start='<sublink>', end=r'</sublink>')

    # If it's an xml file then we set the link to the xml path rather than a list of links
        if links[0].endswith('.xml') or links[0]=='none' or links[0] == '' or links[0].startswith('msg~'):
            links = links[0]

    # If link is none we presume it's a folder
        if links == 'none' or links == '':
            Add_Dir( name=title, url='', mode='', folder=False, icon=thumb, fanart=fanart )

    # If link is a string it's either another menu or a message
        elif Data_Type(links)=='str':

        # If it's a message clean up the string and load up the simple_dialog function
            if links.startswith('msg~'):
                links = links.replace('msg~','')
                Add_Dir( name=title, url="{%s}"%links, mode='simple_dialog', folder=False, icon=thumb, fanart=fanart )

        # Otherwise we presume it's a menu
            else:
                Add_Dir( name=title, url=links, mode='main_menu', folder=True, icon=thumb, fanart=fanart )

    # Otherwise send through our list of links to the Play_Link function
        else:
            Add_Dir( name=title, url="{'url':%s}"%links, mode='play_link', folder=False, icon=thumb, fanart=fanart )
#----------------------------------------------------------------
# Simple function to check playback, it will return true or false if playback successful
@route(mode='play_link',args=['url'])
def Play_Link(url):
# If only one item in the list we try and play automatically
    if len(url)==1:
        if not Play_Video(url[0]):
            OK_Dialog( 'PLAYBACK FAILED','This stream is currently offline.' )

# If more than one link then we give a choice of which link to play
    elif len(url)>1:
        link_list   = []
        counter     = 1
        for item in url:
            link_list.append( 'Link '+str(counter) )
            counter += 1
        choice = Select_Dialog( 'CHOOSE STREAM', link_list )
        if choice >= 0:
            if not Play_Video( url[choice] ):
                OK_Dialog( 'PLAYBACK FAILED','This stream is currently offline.' )
                Play_Link(url)
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#----------------------------------------------------------------

"""
    SECTION 6:
    Essential if creating list items, this tells kodi we're done creating our list items.
    The list will not populate without this. In the run command you need to set default to
    whatever route you want to open into, in this example the 'start' route which opens the
    Start() function up at the top.
"""
if __name__ == "__main__":
    Run(default='start')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))