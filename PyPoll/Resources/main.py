import os
import csv 

ELECTION_DATA_PATH = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates = {}
winner = None

with open(ELECTION_DATA_PATH) as election_data_file:
    csvreader = csv.reader(election_data_file, delimiter=',')
    next(csvreader)

    for row in csvreader:
        candidate = row[2]
        total_votes += 1

        if candidate not in candidates:
            candidates[candidate] = 1
        else:  
            candidates[candidate] += 1

winner = max(candidates, key=candidates.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")