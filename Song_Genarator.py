import re #REGEX library
import urllib.request #Open URLs
import markovify #Generate a Markov chain
import random
from time import sleep #Needed to avoid ban from alyrics


originalLyrics = open('lyrics.txt', 'w')

url = "https://www.azlyrics.com/c/coldplay.html"
artistHtml = urllib.request.urlopen(url)
artistHtmlStr = str(artistHtml.read())
# To find the links on the page, we’ll be using the re library we imported which will find all a link.

links = re.findall('href="([^"]+)"', artistHtmlStr)

print(links)
