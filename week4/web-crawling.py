import HTMLParser
import urllib

urlText = []

#Define HTML Parser
class parseText(HTMLParser.HTMLParser):
    def handle_data(self, data):
        if data != '\n':
            urlText.append(data)

#Create instance of HTML parser
lParser = parseText()

thisurl = "https://www.youtube.com/watch?v=bGZZxgixkew"
#Feed HTML file into parser
lParser.feed(urllib.urlopen(thisurl).read().decode('UTF-8'))
lParser.close()

with open('crawl_test.txt', 'wb') as file:
    for item in urlText:
        file.write(item.encode('UTF-8') + '\n')

    file.close()