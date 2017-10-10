# -*- coding: utf-8 -*-

# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Tempus
# Author: whufclee, ad

import os           
import xbmc         
import xbmcaddon    
import xbmcplugin   


from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

debug        = Addon_Setting(setting='debug')       
addon_id     = xbmcaddon.Addon().getAddonInfo('id') 


BASE  = "plugin://plugin.video.youtube/playlist/"

YOUTUBE_CHANNEL_ID_1 = "PL0A4JBMYjGZBBk9v1JdginEB-U7lSN-HG"
YOUTUBE_CHANNEL_ID_2 = "PL0A4JBMYjGZAMIRneRPuSFuLx20ZOHol6" 
YOUTUBE_CHANNEL_ID_3 = "PL0A4JBMYjGZAd0ckLgtZ9M4V6SvgMoWUa" 
YOUTUBE_CHANNEL_ID_4 = "PL0A4JBMYjGZBD0B-yncwcwql-xVtGQaeY"     
YOUTUBE_CHANNEL_ID_5 = "PL0A4JBMYjGZDwMqzytGopC9KuqsIRBLef" 
YOUTUBE_CHANNEL_ID_6 = "PL0A4JBMYjGZDNn_sY0caw6c0PEhi8bBzt"
YOUTUBE_CHANNEL_ID_7 = "PL0A4JBMYjGZDl9ZkzOU7vZzZO8HNBxQbQ" 
YOUTUBE_CHANNEL_ID_8 = "PL0A4JBMYjGZBiafpyRNYtngBwjFId9yYq"
YOUTUBE_CHANNEL_ID_9 = "PL0A4JBMYjGZAV0Jsbpb4UWT7SALl1rG2_"
YOUTUBE_CHANNEL_ID_10 = "PL0A4JBMYjGZDe4et86QLBgMwbd4fSr-Xf"
YOUTUBE_CHANNEL_ID_11 = "PL0A4JBMYjGZCzBSCsOsm8g6zznPmOZF8s"
YOUTUBE_CHANNEL_ID_12 = "PL0A4JBMYjGZCsS9NZKGzzTtdzckZhyc6S"
YOUTUBE_CHANNEL_ID_13 = "PL0A4JBMYjGZCBiB0PKVJdTlu9Edac6Ory"
YOUTUBE_CHANNEL_ID_14 = "PL0A4JBMYjGZAAcJBpM_BapEGbu_VMRxbd"
YOUTUBE_CHANNEL_ID_15 = "PL0A4JBMYjGZABYRJkCx8JISbGyzDvE4Bl"      

@route(mode='main_menu')
def Main_Menu():
    Add_Dir( 
        name="[COLORorange]Halloween Food Recipes[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="http://www.drodd.com/images10/halloween-food-ideas21.jpg")
        
    Add_Dir( 
        name="[COLORorange]Halloween Drink Recipes[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://simplydarrling.com/wp-content/uploads/2015/10/spooky-drinks-cranberry-vodka-725x1095.jpg")
    
    Add_Dir( 
        name="[COLORorange]Halloween Decorations[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="http://www.nighouse.com/photo/04/042eb006bb4a88871a89a9dd3974b3e0.jpg")
        
    Add_Dir( 
        name="[COLORorange]Halloween Costume Ideas[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="http://girlshue.com/wp-content/uploads/2013/08/Unique-Scary-Halloween-Costume-Ideas-For-Couples-2013-2014-1.jpg")
    
    Add_Dir( 
        name="[COLORorange]Halloween Makeup Ideas[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="http://3.bp.blogspot.com/-AvlYcP8o-lo/UlN9ffiQaHI/AAAAAAAAIV4/iYvmBxHifzs/s1600/4376e8224f78d6501a6395ac0308d69d.jpg")

    Add_Dir( 
        name="[COLORorange]Halloween Pumpkin Carving[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="http://restrainmybrain.files.wordpress.com/2011/10/pumpkin-carving-art.jpg")

    Add_Dir( 
        name="[COLORorange]Halloween Games[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="http://www.whatsupmoms.com/wp-content/uploads/2015/10/qRtFdsPTPHc-1024x576.jpg")

    Add_Dir( 
        name="[COLORorange]Halloween Music[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="http://sofestive.com/wp-content/uploads/2014/10/halloween-music-playlist.png")

    Add_Dir( 
        name="[COLORorange]Halloween Funny Videos[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="http://3.bp.blogspot.com/-IAstm1oZdl0/UFEGC9J1n9I/AAAAAAAACHY/0TqXd3rsW4U/s1600/Funny-Jack-O-Halloween-Wallpapers.jpg")

    Add_Dir( 
        name="[COLORgoldenrod]Thanksgiving Food Recipes[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="https://cbsla.files.wordpress.com/2015/11/o12.jpg")

    Add_Dir( 
        name="[COLORgoldenrod]Thanksgiving Drink Recipes[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="http://clv.h-cdn.co/assets/15/42/640x351/gallery-1444835809-thanksgiving-drinks-1115-1.jpg")

    Add_Dir( 
        name="[COLORgoldenrod]Thanksgiving Decorations[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
        icon="http://clv.h-cdn.co/assets/cm/15/08/54eaa9c4db4f9_-_thanksgiving-table-7-de.jpg")

    Add_Dir( 
        name="[COLORgoldenrod]Thanksgiving Games[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
        icon="https://i.ytimg.com/vi/wAsV8dSzKJU/maxresdefault.jpg")

    Add_Dir( 
        name="[COLORgoldenrod]Thanksgiving Music[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
        icon="http://4.bp.blogspot.com/-6F_nKdSPG_s/UnT_4sMK_YI/AAAAAAAAIOo/Q2nQ0qtcJEA/s500/Thanksgiving+playlist.jpg")

    Add_Dir( 
        name="[COLORgoldenrod]Thanksgiving Funny Videos[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_15+"/", folder=True,
        icon="https://i.imgur.com/Q7qDQKG.png")
        
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#
if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
