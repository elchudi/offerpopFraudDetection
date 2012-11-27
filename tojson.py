import pickle
import time
teams = {}

files = ["test.txt","test2.txt","test3.txt"]

    

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
    sorted_array = sort_array(teams)     
    files["array"] = sorted_array
    
    fout = open("array","w+")
    fout.write(repr(files))
    fout.flush()
    fout.close()
