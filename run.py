import data
import urllib2


for k,v in data.urls.items():
    response = urllib2.urlopen(v)
    html = response.read()
    pos = html.find('"VoteCount"')
    html_piece = html[pos: pos +20]
    print k, html_piece[html_piece.find(">") + 1: html_piece.find("<")]
