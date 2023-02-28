import os
import csv 

#set path for file
dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, "Resources/election_data.csv")

#define variables
votes_list = []
candidates_list = []
candidate_votes_dict = {}

#open and read CSV
with open(filepath) as election_data_file:
    csv_reader = csv.reader(election_data_file, delimiter=',')

    #read the header row 
    csv_header = next(election_data_file)

    #find total votes
    for row in csv_reader:
        votes_list.append(int(row[0]))
        total_votes = len(votes_list)

        #create a list of candidate names column
        candidate_names = str(row[2])

        #add new candidate names to list
        if candidate_names not in candidates_list:
            candidates_list.append(candidate_names)
            candidate_votes_dict[candidate_names] = 1

        #count votes of candidates in the list
        else: 
            candidate_votes_dict[candidate_names] = candidate_votes_dict[candidate_names] + 1

#determine winner
winner_votes = max(candidate_votes_dict.values())
winner_candidate = max(candidate_votes_dict, key=candidate_votes_dict.get)

#print final values
print("Election Results:")
print("---------------------------")
print(f"Total votes: {total_votes}")
print("---------------------------")
print(f"{candidates_list[0]}: {round((candidate_votes_dict[candidates_list[0]]/total_votes)*100, 3)}% ({candidate_votes_dict[candidates_list[0]]})")
print(f"{candidates_list[1]}: {round((candidate_votes_dict[candidates_list[1]]/total_votes)*100, 3)}% ({candidate_votes_dict[candidates_list[1]]})")
print(f"{candidates_list[2]}: {round((candidate_votes_dict[candidates_list[2]]/total_votes)*100, 3)}% ({candidate_votes_dict[candidates_list[2]]})")
print("---------------------------")
print(f"Winner: {winner_candidate}")


#create path for output file
dirname = os.path.dirname(__file__)
output_file = os.path.join(dirname, "Analysis/election_data.txt")

#open output file and fill it with information
with open(output_file, "w") as outfile:

    outfile.write("Election Results:\n")
    outfile.write("---------------------------\n")
    outfile.write(f"Total votes: {total_votes}\n")
    outfile.write("---------------------------\n")
    outfile.write(f"{candidates_list[0]}: {round((candidate_votes_dict[candidates_list[0]]/total_votes)*100, 3)}% ({candidate_votes_dict[candidates_list[0]]})\n")
    outfile.write(f"{candidates_list[1]}: {round((candidate_votes_dict[candidates_list[1]]/total_votes)*100, 3)}% ({candidate_votes_dict[candidates_list[1]]})\n")
    outfile.write(f"{candidates_list[2]}: {round((candidate_votes_dict[candidates_list[2]]/total_votes)*100, 3)}% ({candidate_votes_dict[candidates_list[2]]})\n")
    outfile.write("---------------------------\n")
    outfile.write(f"Winner: {winner_candidate}")
