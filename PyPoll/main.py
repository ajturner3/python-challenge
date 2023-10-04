import os
import csv 

ELECTION_DATA_PATH = os.path.join('Resources', 'election_data.csv')
ANALYSIS_FILE_PATH = os.path.join('Analysis', 'results.txt')

total_votes = 0
candidate_votes = {}
candidate_list=[]

with open(ELECTION_DATA_PATH) as election_data_file:

        
        csvreader = csv.reader(election_data_file, delimiter=',')

        next(csvreader)

        for row in csvreader:
                total_votes += 1

                candidate_name = row[2]
                if candidate_name not in candidate_list:
                        candidate_list.append(candidate_name)
                        candidate_votes[candidate_name] = 0

                candidate_votes[candidate_name] += 1
winner = ""
winner_votes = 0
candidate_output_list = []
candidate_votes_output = []
candidate_percentage_votes = []

for candidate_name, votes in candidate_votes.items():
                percentage = round(votes/total_votes*100, 3)
                candidate_output_list.append(candidate_name)
                candidate_votes_output.append(votes)
                candidate_percentage_votes.append(percentage)
                
                if votes > winner_votes:
                        winner = candidate_name
                        winner_votes = votes

output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"  
        f"{candidate_output_list[0]}: {candidate_percentage_votes[0]}% ({candidate_votes_output[0]})\n"
        f"{candidate_output_list[1]}: {candidate_percentage_votes[1]}% ({candidate_votes_output[1]})\n"
        f"{candidate_output_list[2]}: {candidate_percentage_votes[2]}% ({candidate_votes_output[2]})\n"
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
print(output)


# Export the results to text file
with open(ANALYSIS_FILE_PATH, "w") as txt_output:
    txt_output.write(output)
# Print the output (to terminal)