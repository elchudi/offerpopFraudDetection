import matplotlib.pyplot as plt
teams = {}
with open("test.txt", "r") as myfile:
    for line in myfile.readlines():
        sp =  line.split(",")
        if (len(sp) > 2):
            team =  line.split(",")[0]
            votes =  line.split(",")[1]
            times =  line.split(",")[2]
            if team not in teams.keys():
                teams[team] = {}
            teams[team][times[:times.find(".")]] = votes

for team,values in teams.items():
    with open(team+".data", "wr+") as outTeam:
        print teams[team]
        for k,v in teams[team].items():
            if(len(str(k))==10):
                outTeam.write(k)
                outTeam.write('\t')
                outTeam.write(v)
                outTeam.write('\n')
    print values.keys()
    times = values.keys()
    times = map(int, times)
    votes = values.values()
    votes = map(int, votes)
    plt.plot(times, votes, "ro")
    print min(times), max(times), min(votes), max(votes)
    plt.axis([min(times), max(times), min(votes) -10, max(votes)+10])
    plt.show()
    """
    """
    
