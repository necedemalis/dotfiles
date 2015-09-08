import urllib
import os
import shutil
import time
import datetime

class MyOpener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"


#Move old picture to /media/Daten/Bilder/Comics/Peanuts/ (wenn vom Sonntag, dann als jpg
timestr = time.strftime("%Y-%m-%d")
now = datetime.datetime.now()
shutil.copyfile("/home/joecool/.fluxbox/backgrounds/peanuts.gif","/media/Daten/Bilder/Comics/Peanuts/peanuts_{0}.jpg".format(timestr))

#Read Source Code
#myopener = MyOpener()
#page = myopener.open ("http://www.gocomics.com/peanuts")
#page = myopener.open ("https://www.peanuts.com")
#source = page.readlines()
#page.close()

#Get Source Code line
#for i, line in enumerate(source):
    #if "feature_item" in line:
        #l = line
#words = l.split()

#Get Url
#pic_list=[]
#for i, word in enumerate(words):
    #if "src" in word:
        #pic_list.append(word)
#url = pic_list[1].strip('src="')

#Download Picture
if now.isoweekday() == 1:
    day="/Sundays/pe"
    end="comb_hs"
else:
    day="daily/pe_c"
    end=""
url = time.strftime("%y%m%d")

img = urllib.urlopen("http://www.peanuts.com/wp-content/comic-strip/color-low-resolution/desktop/2015/{1}{0}{2}.jpg".format(url,day,end))
print(img)
localFile = open('/home/joecool/.fluxbox/backgrounds/peanuts.gif',"wb")
localFile.write(img.read())
localFile.close()

#Make Background
os.system("DISPLAY=:0.0 feh --bg-center ~/.fluxbox/backgrounds/peanuts.gif")
