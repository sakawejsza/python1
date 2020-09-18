FILE_NAME = 'c:/Users/sakaw/Downloads/TCMG 412/local_copy.txt'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)
clean = []
# Loop through the file 
for line in fh:
  #put line into list
  elements = line.split(" ")
  #collect date data
  date = elements[3]
  #clean up date
  clean.append(date[1:12])
  # have a list named clean full of dates day/month/year



beginyear = '12/Oct/1994'
beginmonth = 'Oct/1994'
endyear = '12/Oct/1995'


# finding the number of orders in the last year 

#finding the start of the year
startyear = count(beginyear)
if startyear = 0
  start = 0
if count > 0
  for x in clean:
    simpdate = x[3:11]
    if simpdate == 'Oct/1994'
      start = (clean.index(x))
      break
      
#finding the end of the year      
finishyear = count(endyear)
if finishyear > 1
  for x in clean:
    if x == endyear
      end = (clean.index(x))
      break
else
  end = clean.length()
  
#determining number of orders total and last year  
total_log = clean.length()
total_year = end - start
        
print( total_log)
print(total_year)
