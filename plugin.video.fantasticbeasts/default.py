# -*- coding: utf-8 -*-

# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Fantastic Beasts
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

YOUTUBE_CHANNEL_ID_1 = "PL0A4JBMYjGZCV7oXmvFfl85YBv08bWQyI"
YOUTUBE_CHANNEL_ID_2 = "PL0A4JBMYjGZD15kDhkqu_fkl_2WlWJPvM" 
YOUTUBE_CHANNEL_ID_3 = "PL0A4JBMYjGZBU5dMwZrlWEspKcDGRd2F9" 
YOUTUBE_CHANNEL_ID_4 = "PL0A4JBMYjGZDXTLrL8ns9eS0RbuhFBeQF"     
YOUTUBE_CHANNEL_ID_5 = "PL0A4JBMYjGZBTCP92DHrgczZf10TMgbN6" 
YOUTUBE_CHANNEL_ID_6 = "PL0A4JBMYjGZAhOEf_GTF4u3dM-hkyIajD"
YOUTUBE_CHANNEL_ID_7 = "PL0A4JBMYjGZB_L2ES5tvSubf-W0V5zv-5"
YOUTUBE_CHANNEL_ID_8 = "PL0A4JBMYjGZCb7yWH3ii2qg_K2llgZpMq"     

@route(mode='main_menu')
def Main_Menu():
    Add_Dir( 
        name="[COLORgold]African Animals[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://i.pinimg.com/736x/e4/fd/88/e4fd8875ecb4e92055ea4bd6d0b3b21f--african-elephant-african-safari.jpg")
        
    Add_Dir( 
        name="[COLORgold]North American Animals[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="http://whackstarhunters.com/wp-content/uploads/2017/04/mule-deer.jpg")
    
    Add_Dir( 
        name="[COLORgold]South American Animals[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://media1.britannica.com/eb-media/88/156388-004-19085593.jpg")
        
    Add_Dir( 
        name="[COLORgold]European Animals[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://treesforlife.org.uk/docs/079_360__lynx_1404309607_standard.jpg")
    
    Add_Dir( 
        name="[COLORgold]Australian Animals[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="http://www.natureaustralia.org.au/wp-content/uploads/2015/02/Thorny-Devil-%C2%A9-Carolyn-Larcombe-tile-800x510.jpg")

    Add_Dir( 
        name="[COLORgold]Asian Animals[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://huntnewsnu.com/wp-content/blogs.dir/1/files/2017/04/BornInChina5890f4f965a3e.jpg")

    Add_Dir( 
        name="[COLORgold]Animals in Antarctica[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="http://1.bp.blogspot.com/-cpUlygaKoHI/UjUu-TnQ9LI/AAAAAAAAAW0/hzihCui3TIM/s1600/Elephant%20Seal%20Antarctica.jpg")

    Add_Dir( 
        name="[COLORgold]Animals of the Ocean[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="https://i.pinimg.com/736x/81/be/1f/81be1f3c47388ff1fdeb08c5cc360b92--sea-dragon-rainbows.jpg")
        
        
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
