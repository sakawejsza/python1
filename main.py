beginyear = '12/Oct/1994' #beginning of year
beginmonth = 'Oct/1994' #beginning month
endyear = '12/Oct/1995' #end of year
clean=[] #creating a list for all the dates










# finding the number of orders in the last year 

#finding the start of the year
startyear = count(beginyear)
#if the beginning of the year doesn't appear in the list then start on the first avalible date of october 1994
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
#if end of year exists find the index and subtract 1 so it ends at a year
if finishyear > 0
  for x in clean:
    if x == endyear
      end = (clean.index(x)-1)
      break
 #if end does not exist then the end of the year is just the end of the file
else
  end = clean.length()
  
#determining number of orders total and last year  
total_log = clean.length()
total_year = end - start

print('There were ', total_year,' amount of orders in the last year')
print('There were ', total_log,' orders in the log')
        
