#PyPoll Homework Final Matthew Berning

#import dependancies
import pathlib

import os

import pandas as pd

#read in csv

file = 'Resources/election_data.csv'

election_df = pd.read_csv(file)

#find total votes

total_votes = election_df['Voter ID'].count()

# find votes per candidate

election_df_group = election_df.groupby(['Candidate'])

election_df_count = election_df_group.count()

#locate results by loc

correy_votes = election_df_count.loc["Correy", "Voter ID"]
khan_votes = election_df_count.loc["Khan", "Voter ID"]
li_votes = election_df_count.loc["Li", "Voter ID"]
otooley_votes = election_df_count.loc["O'Tooley", "Voter ID"]

#print results to terminal

print("Election Results") 
print("--------------------")
print("Total Votes: " + str(total_votes))
print("--------------------")
print("Khan: " + str(round((khan_votes/total_votes * 100),3))+'%'+' ('+str(khan_votes)+')')
print("Correy: " + str(round((correy_votes/total_votes * 100),3))+'%'+' ('+str(correy_votes)+')')
print("Li: " + str(round((li_votes/total_votes * 100),3))+'%'+' ('+str(li_votes)+')')
print("O'Tooley: " + str(round((otooley_votes/total_votes * 100),3))+'%'+' ('+str(otooley_votes)+')')
print("--------------------")
if (khan_votes > li_votes and khan_votes > otooley_votes and khan_votes > correy_votes):
    print('Winner: Khan')
    
elif (correy_votes > li_votes and correy_votes > khan_votes and correy_votes > otooley_votes):
    print('Winner: Correy')
    
elif (li_votes > correy_votes and li_votes > khan_votes and li_votes > otooley_votes):
    print('Winner: Li')
    
elif (otooley_votes > li_votes and otooley_votes > correy_votes and otooley_votes > khan_votes):
    print('Winner: O\'Tooley')
	
	
#create variables to hold each output then print each variable to .txt file 
eres = ("Election Results") 
line = ("--------------------")
tot = ("Total Votes: " + str(total_votes))
# print("--------------------")
khan = ("Khan: " + str(round((khan_votes/total_votes * 100),3))+'%'+' ('+str(khan_votes)+')')
corey = ("Correy: " + str(round((correy_votes/total_votes * 100),3))+'%'+' ('+str(correy_votes)+')')
li = ("Li: " + str(round((li_votes/total_votes * 100),3))+'%'+' ('+str(li_votes)+')')
otoo = ("O'Tooley: " + str(round((otooley_votes/total_votes * 100),3))+'%'+' ('+str(otooley_votes)+')')
# print("--------------------")
if (khan_votes > li_votes and khan_votes > otooley_votes and khan_votes > correy_votes):
    winner = ('Winner: Khan')
    
elif (correy_votes > li_votes and correy_votes > khan_votes and correy_votes > otooley_votes):
    winner = ('Winner: Correy')
    
elif (li_votes > correy_votes and li_votes > khan_votes and li_votes > otooley_votes):
    winner = ('Winner: Li')
    
elif (otooley_votes > li_votes and otooley_votes > correy_votes and otooley_votes > khan_votes):
    winner = ('Winner: O\'Tooley')

#export results to text file using pathlib

pathlib.Path("C:/Users/OI/Desktop/Homework/Results.txt").write_text(str(eres + '\n' + line +'\n' + tot +'\n' + line +'\n' + khan +'\n' + corey +'\n' + li +'\n' + otoo +'\n' + line +'\n' + winner))
  
