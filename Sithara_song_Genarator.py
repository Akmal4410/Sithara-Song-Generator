import re
import urllib.request
import markovify

orginal_lyrics = open("Lyrics.txt", "w")

url = "https://www.malayalachalachithram.com/listsongs.php?g=1414"

artist_html = urllib.request.urlopen(url)
artist_html_str = str(artist_html.read())
# To find the links on the page, we’ll be using the re library we imported
# which will find all a link.

links = re.findall('href="([^"]+)"', artist_html_str)
# print(links)

song_link = []

for x in links:
    if "song.php" in x:
        x = x.replace("..", "")
        x = "https://www.malayalachalachithram.com/" + x
        song_link.append(x)
print(song_link)


for x in song_link:
    song_html = urllib.request.urlopen(x)
    song_html_str = str(song_html.read())
    split = song_html_str.split('Lyrics submitted by: Viji', 1)
    split_html = split[1]
    split = split_html.split('</div>', 1)
    lyrics = split[1]


print(lyrics)