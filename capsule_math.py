import numpy as np
import csv

strange = {0:0.34, 1:0.32, 3:0.26, 5:0.08}

N = input("Enter number of thing wanted: ")
prob = min(input("Enter the probability you'd like to stop at: "),0.995)

dist = [0.34, 0.32, 0, 0.26, 0, 0.08]
cumu = 0
i = 1

prev = dist[:]

csvfile = open(raw_input("Give this csv a file name: ")+".csv","w")
writer = csv.writer(csvfile)

writer.writerow(["Capsules", "Chance"])

while len(prev) <= N or sum(prev[N:]) < prob:
	prev = np.convolve(prev, dist)
	i += 1
	print i, sum(prev[N:])
	if len(prev) > N:
		writer.writerow([i,sum(prev[N:])])
