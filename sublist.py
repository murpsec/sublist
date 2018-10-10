#! python3
#  sublist v1.0
#  Authors:
#  Brent Murphy - twitter.com/brent_murphy
#  Biran Patel - twitter.com/_nopreserveroot
  
import requests
import types
import sys
from bs4 import BeautifulSoup
 
print("""
 __       _       __ _     _   
/ _\_   _| |__   / /(_)___| |_ 
\ \| | | | '_ \ / / | / __| __|
_\ \ |_| | |_) / /__| \__ \ |_ 
\__/\__,_|_.__/\____/_|___/\__|
                                
# Created By @brent_murphy and @_nopreserveroot
    """ )

#remove duplicates
def quickRemoveDuplicates(lst):
	d={}
	for elem in lst:
		if elem not in d.keys():
			d[elem]=1
		else:
			d[elem]+=1
	return d.keys()

# user specified input
url = input( "Please enter a valid domain (example: test.com): ")

r = requests.get('https://crt.sh?q=%25.'+url)
html_content = r.text
  
# parse the html using beautiful soup
soup = BeautifulSoup(html_content,"html.parser")
  
#data from correct table
secondtable = soup.findAll('table')[1]
out=[] 
for row in secondtable.findAll("tr"):
  data = []
  if type (row) is list:
    data.append(row.findAll("td"))
  else:
    data += row
  if len(data) < 13:
    continue
  out.append (str(data[9]).strip("<td></td><th></th>"))

out = list(quickRemoveDuplicates(out))
if len(out) <= 0:
    print ("Oops, invalid domain! Re-run with a valid domain.")
    sys.exit()
else:
  question = input("Would you like to output a file? y/n: ")
  if question.lower() != "y" and question.lower() != "n":
    print ("You did not enter a valid answer, please re-run.")
    sys.exit()

  if question.lower() == "y":
    outfile = open(url+".txt","w")
  while "Identity" in out:
	  out.remove("Identity")
for i in out:
  print (i)
  if question.lower() == "y":
    outfile.write(i + "\n")
if question.lower() == "y":
  outfile.close()
print ("============================")
print ("There were "+ str(len(out)) +" unique domains!")
