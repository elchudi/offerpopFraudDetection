import data
import urllib2
import time

with open("test.txt", "a") as myfile:
    while(True):
        for k,v in data.urls.items():
            try:
                response = urllib2.urlopen(v)
                html = response.read()
                pos = html.find('"VoteCount"')
                html_piece = html[pos: pos +20]
                #print k,",", html_piece[html_piece.find(">") + 1: html_piece.find("<")],",", time.time()
                toapp = ",".join([ k, html_piece[html_piece.find(">") + 1: html_piece.find("<")],str( time.time())])
                myfile.write(toapp)
                myfile.write("\n")
            except:
                time.sleep(2)

