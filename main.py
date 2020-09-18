beginyear = '12/Oct/1994'
beginmonth = 'Oct/1994'
endyear = '12/Oct/1995'
clean=[]

#put line into list
elements = line.split()
#collect date data
date = elements[3]
#clean up date
clean.append(date[1:12])
# have a list named clean full of dates day/month/year

