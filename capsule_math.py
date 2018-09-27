import numpy as np
import csv

capsules = {'timefog':{'gold':{0:33.0/34,3:0.35/34,5:0.25/34,8:0.20/34,10:0.15/34,30:0.05/34},
                           'silver':{0:296.8/3,1:4.8/9,3:4.8/9}},
            'rising':{'inferno':{0:0.89,5:0.05,10:0.03,20:0.02,80:0.01},
                      'squirrel girl':{0:0.73,10:0.17,20:0.08,80:0.02},
                      'spider-gwen':{0:0.73,10:0.17,20:0.08,80:0.02},
                      'captain marvel':{0:0.9,10:0.075,80:0.025},
                      'ms. marvel':{0:0.9,10:0.075,80:0.025},
                      'quake':{0:0.9,10:0.075,80:0.025}},
            'inferno':{'inferno':{0:0.05,1:0.73,2:0.145,3:0.0275,4:0.015,5:0.01,6:0.0075,7:0.005,8:0.005,9:0.0025,10:0.0025}}
               }

"""
capsules = {'timefog':{'gold':{0:28.0/29,3:0.35/29,5:0.25/29,8:0.20/29,10:0.15/29,30:0.05/29},
						'silver':{0:296.8/3,1:4.8/9,3:4.8/9}},
			'infinity':{'strange':{0:0.87,10:0.09,20:0.04},'teen groot':{0:0.9,10:0.06,20:0.04},
						'spider-man':{0:0.87,10:0.09,20:0.04},'starlord':{0:0.87,10:0.09,20:0.04},
						'killmonger':{0:0.9,10:0.06,20:0.04},'nebula':{0:0.87,10:0.09,20:0.04},
						'punisher':{0:0.9,10:0.06,20:0.04},'scarlet witch':{0:0.9825,80:0.0175}
						'thane':{0:0.96,10:0.0225,80:0.0175}},
			'strange':{'strange':{0:0.34, 1:0.32, 3:0.26, 5:0.08},'teen groot':{0:0.96,1:0.04}},
			'spider-man':{'spider-man':{0:0.34,1:0.32,3:0.26,5:0.08},'teen groot':{0:0.96,1:0.04}},
			'starlord':{'starlord':{0:0.34,1:0.32,3:0.26,5:0.08},'killmonger':{0:0.96,1:0.04}},
			'nebula':{'nebula':{0:0.27,1:0.4,3:0.25,5:0.08},'killmonger':{0:0.96,1:0.04},
						'punisher':{0:0.92,1:0.08}},
			'captain marvel':{'captain marvel':{0:0.27,1:0.4,3:0.25,5:0.08},'thane':{0:0.98,1:0.02},
						'punisher':{0:0.94,1:0.04,3:0.02}},

			}
"""
print sorted(capsules.keys())
cap = capsules[raw_input("Choose a capsule from the above list: ").lower()]

print sorted(cap.keys())
cdist = cap[raw_input("Choose a character from the above list: ").lower()]

N = input("Enter number of character shards you want: ")
prob = min(input("Enter the probability (between 0 and 1) you'd like to stop at: "),0.995)


dist = np.zeros(sorted(cdist.keys())[-1]+1)

for i in cdist.keys():
	dist[i] = cdist[i]
	print i, dist[i]

prev = dist[:]
k = 1

csvfile = open(raw_input("Give this csv a file name: ")+".csv","w")
writer = csv.writer(csvfile)

writer.writerow(["Capsules", "Chance"])

#while k < 2100:
while len(prev) <= N or sum(prev[N:]) < prob:
	if len(prev) > N:
		writer.writerow([k,sum(prev[N:])])
	prev = np.convolve(prev, dist)
	k += 1
	print k, sum(prev[N:])

