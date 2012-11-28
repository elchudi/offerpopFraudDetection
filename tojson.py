import pickle
import time
import scipy.interpolate as sp
from scipy.misc import derivative
import numpy as np
files = ["data_complete.ready"]

    

def sort_array(teams):  
    array = []
    team_names = teams.keys()
    for t_name in teams.keys():
        """
        times = teams[t_name].keys()
        times = map(int, times)
        """
        votes = teams[t_name].values()
        votes = map(int, votes)
        #print t_name
        #print votes
        total_votes = 0
        if votes:
            total_votes = max(votes)
            array.append((t_name, total_votes)) 
    array = sorted(array, key=lambda votes: votes[1])
    array = [item[0] for item in array]
    return array[::-1]
    

def read_files_into_json():
    teams = {}
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
    return teams
       

def interpolatef(data):
    data = sorted(data.items())
    #print data
    #times = data.keys()
    times = [d[0] for d in data]
    times = map(int, times)
    #votes = data.values()
    votes = [d[1] for d in data]
    votes = map(int, votes)
    #print "min", min(times), " max ", max (times)
    fc = sp.interp1d(times,votes,bounds_error=False,fill_value=0,kind=5)
    return fc

def write_non_fancy(teams):
    #print teams
    for team in teams.keys():
        fout = open(team+".d0" ,"w+")
        fout.write(repr(teams[team]))
        fout.flush()
        fout.close()
    filesa = {}
    sorted_array = sort_array(teams)
    #print sorted_array
    filesa["array"] = [f + ".d0" for f in sorted_array]

    fout = open("array","w+")
    fout.write(repr(filesa))
    fout.flush()
    fout.close()


def write_fancy(teams):
    print "for"
    for team in teams.keys():
        print team
        fout = open(team ,"w+")
        foutd1 = open(team+".d1" ,"w+")
        foutd2 = open(team+".d2" ,"w+")
        fc = interpolatef(teams[team])
        from_fc = {}
        from_fcd1 = {}
        from_fcd2 = {}
        for k in teams[team].keys():
            #print k
            #print dir(fc(int(k)))
            value = int(k)
            from_fc[k] = fc(value).item()
            v1 =  derivative(fc,(value),dx=60,order=5) 
            #from_fcd1[k] = v1 if v1 > 0.0001 else 0
            from_fcd1[k] = str(v1)
            v2 =  derivative(fc,(value),dx=60,order=5, n=2)
            #from_fcd2[k] =  v2 if v2 > 0.0001 else 0
            from_fcd2[k] =  str(v2)
            
        #fout.write(repr(teams[team]))
        fout.write(repr(from_fc))
        fout.flush()
        fout.close()
        foutd1.write(repr(from_fcd1))
        foutd1.flush()
        foutd1.close()
        foutd2.write(repr(from_fcd2))
        foutd2.flush()
        foutd2.close()
    filesa = {}
    sorted_array = sort_array(teams)     
    #print sorted_array
    filesa["array"] = sorted_array
   


 
    fout = open("array","w+")
    fout.write(repr(filesa))
    fout.flush()
    fout.close()
    
 
while(True):
    teams = read_files_into_json()
    write_non_fancy(teams)
    #print teams
