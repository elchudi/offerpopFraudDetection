import pickle
import time
teams = {}

while(True):
    with open("offer.log", "r") as myfile:
        for line in myfile.readlines():
            team =  line.split(",")[0]
            votes =  line.split(",")[1]
            times =  line.split(",")[2]
            if team not in teams.keys():
                teams[team] = {}
            teams[team][times[:-4]] = votes
    fout = open("json.log","w+")
    fout.write(repr(teams))
    fout.flush()
    fout.close()
    time.sleep(10)
