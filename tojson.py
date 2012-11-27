import pickle
import time
teams = {}

files = ["test.txt","test2.txt"]

while(True):
    for f in files:
        with open(f, "r") as myfile:
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
    for team in teams.keys():
        fout = open(team ,"w+")
        fout.write(repr(teams[team]))
        fout.flush()
        fout.close()
    files = {}
    files["array"] = teams.keys()
    
    fout = open("array","w+")
    fout.write(repr(files))
    fout.flush()
    fout.close()
        
