import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4", "Problem 5"]
#group = ["A", "B", "C", "D", "E"]
#group = ["A", "B", "C", "D"]
group = ["A", "B"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","restore","time","sess", "confidence"]
userlist =  ['S3', 'S5', 'S10', 'S11', 'S12', 'S16', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S25', 'S26', 'S27', 'S28', 'S30', 'S31', 'S33', 'S34', 'A1', 'A4', 'A6', 'A7', 'A9', 'A12', 'A13', 'A14', 'A19', 'A21', 'A22', 'B4', 'B12', 'B14', 'B15', 'B17', 'B21', 'B23', 'B24', 'B27', 'B29', 'B32', 'B33', 'B34', 'B35', 'B40', 'B41', 'B42', 'B46', 'S43', 'S46', 'S47', 'S48', 'S51', 'S52']

groupN = 2
col = 12

for p in prob:
	with open('AB.csv', 'rb')as csvfile:
       		firstrow = True
		spamreader = csv.reader(csvfile, delimiter=',')
		avg_list = [None]*groupN
		group_num = [None]*groupN
		for n in range(groupN):
			avg_list[n] = [None] * col
			group_num[n] = 0
		for i in range(groupN):
			for j in range(col):
				avg_list[i][j] = 0.0
		
		for row in spamreader:
			if firstrow:
				firstrow = False
			else:
#				if row[2] in userlist:
#				if row[11] == "1" : # accuracy
				if True :
					if p == row[0]:
        	        	                g = ord(row[1])-65
						if g == 4: g=2 #g=3 when _withC.csv
                        		        group_num[g] += 1
						for j in range(col):
                                        	        if j==0 : avg_list[g][j] += float(row[j+3])
							elif j == 1:
								avg_list[g][j] = 0
							elif j == 11:
                	                                        t = time.strptime(row[j+2],'%H:%M:%S')
                        	                                s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
	                                                        avg_list[g][j] += s
							elif j == 13:
								avg_list[g][j] = 0
                        	                        else:
								if j == 12:	
									avg_list[g][j] += float(row[j+3])
								else:
									avg_list[g][j] += float(row[j+2])
		for m in range(groupN):
			for k in range(col):
				if group_num[m] != 0:
					avg_list[m][k] /= group_num[m]
	#		if p == "Problem 5":
	#		avg_list[m][1] = avg_list[m][0] / avg_list[m][2]
 #                       avg_list[m][13] = avg_list[m][12] / avg_list[m][9]

		for i in range(groupN):
			print "Group "+chr(i+65) + " : " +str(group_num[i])
		

	                for l in range(col):
                        	if l == 11:
                        	        seconds = avg_list[i][l]
                                	minutes = seconds // 60
                       	        	print "%02d:%02d" % (minutes, seconds % 60)
                        	else:
                                	print avg_list[i][l]
	
