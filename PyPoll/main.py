#import the necessary modules
import os
import csv

#create the file path for the election data 
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

#create variables to hold the number of votes, the full list of candidates, a list for each unique candidate
#a total votecount that adds together all the votes for each unique candidate
#and a percentage of the total vote pool for each unique candidate
votecount = 0
candidates = []
unique_candidate = []
votecount1 = []
votepercent = []

#read the csv file and loop through the table
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        #increase the total number of votes cast as the loop iterates 
        votecount += 1
       
        #add every candidate name to the candidates list
        candidates.append(row[2])

#create a set and append every unique name to the unique_candidate name (ending up with a list of 4 people)
for i in set(candidates):
    #use filler variables to calculate the total amount of votes cast for each unique candidate
    unique_candidate.append(i)
    j = candidates.count(i)
    votecount1.append(j)
    
    #calculate the percentage of all votes cast (rounded), and add these to the votepercent list
    k = round((j/votecount)*100, 3)
    votepercent.append(k)
    
#zip together the 3 lists so that each candidate is tied to their vote count and percentage
#sort the zip (making sure it is in reverse order) by the vote percentage (hence why it is the first row)
finallist = sorted(zip(votepercent, unique_candidate, votecount1), reverse=True)

#calculate the winner by using the max method to look through the votecount1 list
# the winner is the unique_candidate index that matches the the same index value as the winningvote
#this may not be necessary after zipping the lists together but this was written before finding the zip solution, and it still works
winningvote = max(votecount1)
winner = unique_candidate[votecount1.index(winningvote)]

#print the analysis table, and now the candidates should appear in descending order of how many votes they got
print(f"Election Results")
print(f"-"*28)
print(f"Total Votes: {votecount}")
print(f"-"*28)
#printing the zipped together list of candidates and their votes/percentages (inspired by Justin Co from gitlab)
for row in finallist:
    print(f"{row[1]}: {row[0]}00% ({row[2]})")
print(f"-"*28)
print(f"Winner: {winner}")
print(f"-"*28)

#write the results to a text file in the same format as the output above
with open("analysis.txt", "w") as text:
    text.write(f"Election Results \n")
    text.write(f"-"*28)
    text.write(f"\n")
    text.write(f"Total Votes: {votecount} \n")
    text.write(f"-"*28)
    text.write(f"\n")
    for row in finallist:
        text.write(f"{row[1]}: {row[0]}00% ({row[2]}) \n")
    text.write(f"-"*28)
    text.write(f"\n")
    text.write(f"Winner: {winner} \n")
    text.write(f"-"*28)