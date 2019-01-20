import requests
import re

base_url = "http://www.heroes3maps.com/?fulltext=Allies&author=&version%5B%5D=1&size%5B%5D=2&size%5B%5D=3&players%5B%5D=1&players%5B%5D=2&players%5B%5D=3&players%5B%5D=4&players%5B%5D=5&players%5B%5D=6&players%5B%5D=7&players%5B%5D=8&humans%5B%5D=1&humans%5B%5D=2&humans%5B%5D=3&humans%5B%5D=4&humans%5B%5D=5&humans%5B%5D=6&humans%5B%5D=7&humans%5B%5D=8&language%5B%5D=5&language%5B%5D=17&language%5B%5D=21&language%5B%5D=31&language%5B%5D=33&language%5B%5D=56&language%5B%5D=62&language%5B%5D=64&language%5B%5D=65&language%5B%5D=85&language%5B%5D=89&language%5B%5D=95&teams%5B%5D=1&teams%5B%5D=2&teams%5B%5D=3&teams%5B%5D=4&teams%5B%5D=5&teams%5B%5D=6&teams%5B%5D=7&teams%5B%5D=8&difficulty%5B%5D=1&difficulty%5B%5D=2&difficulty%5B%5D=3&difficulty%5B%5D=4&difficulty%5B%5D=5&underworld%5B%5D=0&underworld%5B%5D=1&victory%5B%5D=1&victory%5B%5D=2&victory%5B%5D=3&victory%5B%5D=4&victory%5B%5D=5&victory%5B%5D=6&victory%5B%5D=7&victory%5B%5D=8&victory%5B%5D=9&victory%5B%5D=10&victory%5B%5D=11&victory%5B%5D=12&victory%5B%5D=13&victory%5B%5D=14&loss%5B%5D=1&loss%5B%5D=2&loss%5B%5D=3&loss%5B%5D=4&year%5B%5D=2018&year%5B%5D=2017&year%5B%5D=2016&year%5B%5D=2015&year%5B%5D=2014&year%5B%5D=2013&year%5B%5D=2012&year%5B%5D=2011&year%5B%5D=2010&year%5B%5D=2009&year%5B%5D=2008&year%5B%5D=2007&year%5B%5D=2006&year%5B%5D=2005&year%5B%5D=2004&year%5B%5D=2003&year%5B%5D=2002&year%5B%5D=2001&year%5B%5D=2000&year%5B%5D=1999&offset="
offset = 0
counter = 0

def findmaps(url):
  r = requests.get(url)
  p = re.compile('http.*?.h3m')
  maps = set(p.findall(r.text))
  return maps

def downloadcmd(maps):
  for m in maps:
    print("iwr -outf %s %s" % (m.split("/")[-1],m))

while True:
  maps = findmaps(base_url + str(offset))
  if len(maps) == 0:
    break
  counter += len(maps)
  downloadcmd(maps)
  offset += 10 # pagging - 10 maps per page 

print("Fetch done. Explored %d maps." % (counter))