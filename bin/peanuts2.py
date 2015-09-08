import urllib
import os
import shutil
import time
import datetime

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


#Move old picture to /media/Daten/Bilder/Comics/Peanuts/ (wenn vom Sonntag, dann als jpg
timestr = time.strftime("%Y-%m-%d")
now = datetime.datetime.now()
if now.isoweekday() == 1:
    shutil.copyfile("/home/joecool/.fluxbox/backgrounds/peanuts.gif","/media/Daten/Bilder/Comics/Peanuts/peanuts_{0}.jpg".format(timestr))
else:
    shutil.copyfile("/home/joecool/.fluxbox/backgrounds/peanuts.gif","/media/Daten/Bilder/Comics/Peanuts/peanuts_{0}.gif".format(timestr))

#Read Source Code
myopener = MyOpener()
#page = myopener.open ("http://www.gocomics.com/peanuts")
page = myopener.open ("https://www.peanuts.com")
source = page.readlines()
page.close()

#Get Source Code line
for i, line in enumerate(source):
    if "feature_item" in line:
        l = line
words = l.split()

#Get Url
pic_list=[]
for i, word in enumerate(words):
    if "src" in word:
        pic_list.append(word)
url = pic_list[1].strip('src="')

#Download Picture
img = urllib.urlopen("{0}".format(url))
localFile = open('/home/joecool/.fluxbox/backgrounds/peanuts.gif',"wb")
localFile.write(img.read())
localFile.close()

#Make Background
os.system("DISPLAY=:0.0 feh --bg-center ~/.fluxbox/backgrounds/peanuts.gif")
