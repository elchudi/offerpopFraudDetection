import pickle
import time
teams = {}

while(True):
    with open("test.txt", "r") as myfile:
        for line in myfile.readlines():
            if(len(line.split(",") ) > 2):
                team =  line.split(",")[0]
                votes =  line.split(",")[1]
                times =  line.split(",")[2]
                if team not in teams.keys():
                    teams[team] = {}
                t = times[:times.find(".")]
                if (len(str(t)) == 10):
                    teams[team][times[:times.find(".")]] = votes
    fout = open("json.log","w+")
    fout.write(repr(teams))
    fout.flush()
    fout.close()
    time.sleep(10)
