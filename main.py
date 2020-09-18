FILE_NAME = 'c:/Users/sakaw/Downloads/TCMG 412/local_copy.txt'

beginyear = '12/Oct/1994' #beginning of year
beginmonth = 'Oct/1994' #beginning month
endyear = '12/Oct/1995' #end of year
clean=[] #creating a list for all the dates

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



####finding the number of orders in the last year 

#finding the start of the year

startyear = clean.count(beginyear)
  
#if the beginning of the year doesn't appear in the list then start on the first avalible date of october 1994
if startyear > 0:
  for x in clean:
    if x == beginyear:
      start = (clean.index(x))
      break
if startyear == 0:
  for x in clean:
    simpdate = x[7:11]
    if simpdate == '1994':
      start = (clean.index(x))
      break


#finding the end of the year      

finishyear = clean.count(endyear)
if finishyear > 0:
  for x in clean:
    #if end of year exists find the index and subtract 1 so it ends at a year
    if x == endyear:
      end = (clean.index(x)-1)
      break
else:
  end = len(clean)
 
  
#determining number of orders total and last year  
total_log = len(clean)
total_year = end - start

print('There were ', total_year,' amount of orders in the last year')
print('There were ', total_log,' orders in the log')
        
