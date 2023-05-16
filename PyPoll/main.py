#Importiing relevant packages
import os
import csv

#Establishing path to the data
csvpath = os.path.join(".","Resources","election_data.csv")

#Holds total number of votes
n = 0

#Holds the number of votes
vote_counter = 0

#Key is Candidate Name; Value is number of votes
votes = {}

#Keeps the highest number of votes (by candidate)
winner_votes = 0

#Stores the name of the candidate with the highest vote
current_winner = ""


#Opening CSV file to read data
with open(csvpath, encoding  = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Skips CSV headers
    header = next(csvreader)

    #Looping row by row in the sheet
    for row in csvreader:
        n += 1
        if row[2] in votes:
            votes[row[2]] += 1 
        else:
            votes[row[2]] = 1

#Printing and Creating textfile
text = open("election_results.txt", "w")
text.write("Election Results\n")
text.write("-------------------------\n")
text.write(f"Total Votes: {n}\n")
text.write("-------------------------\n")

#Prints list of candidates, the precentage of votes obtained, and total votes obtained
for name in votes:
    text.write(f"{name}: {round(votes[name]*100/n, 3)}% ({votes[name]})\n")

    #Checks for candidate with highest number of votes and stores their name
    if votes[name] > winner_votes:
        winner_votes = votes[name]
        current_winner = name

text.write("-------------------------\n")
text.write(f"Winner: {current_winner}\n")
text.write("-------------------------\n")
text.close()
        