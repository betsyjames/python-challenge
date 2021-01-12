# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


import os
import csv

# Define Variables
total_votes = 0
candidate_dict = {}
candidate_list = []
vote_count_list = []
vote_percent_list = []
winner_list = []



# Path of file to read data
csvpath = os.path.join("Resources", "election_data.csv")

# Open the csv file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Loop through each row 
    for row in csvreader:

        #find the total number of votes i.e total number of rows 
        total_votes += 1

        #Check if key exists in dic and add it
        if row[2] in candidate_dict.keys():
            candidate_dict[row[2]] = candidate_dict[row[2]] + 1
        else:
            candidate_dict[row[2]] = 1 
       

    
    # Add the candidate name, vote count
    for key, value in candidate_dict.items():
         candidate_list.append(key)
         vote_count_list.append(value)

    #print(f"{vote_count_list}")
  
    # Percentage of votes. For each value in vote count list, finding the percent
    for count in vote_count_list:
        vote_percent_list.append(round(count/total_votes * 100,3))
 
    # Finding the winner. Add all data with name, vote count and percent change to list
    election_data = list(zip(candidate_list, vote_percent_list, vote_count_list))

    #Finding the max vote count and the name and appending it to winner list
    for name in election_data:
         if max(vote_count_list) == name[2]: # Comapring Max vote value to vote count list and then getting the name
            winner_list.append(name[0])
    #Adding Winner name to a list
    winner = winner_list[0]

# Print all data
    print("Election Results")
    print("---------------------------------------")    
    print(f"Total Votes : {total_votes}")
    print("---------------------------------------")  
    print(f"{election_data[0][0]}: {election_data[0][1]}% ({election_data[0][2]})")
    print(f"{election_data[1][0]}: {election_data[1][1]}% ({election_data[1][2]})")
    print(f"{election_data[2][0]}: {election_data[2][1]}% ({election_data[2][2]})")
    print(f"{election_data[3][0]}: {election_data[3][1]}% ({election_data[3][2]})")
    print("---------------------------------------")
    print(f"Winner : {winner}")
    print("---------------------------------------")


#Export to a text file
# Specify the file to write to
output_path = os.path.join("analysis","output_text.txt")

with open(output_path, 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("---------------------------------------\n")    
    textfile.write(f"Total Votes : {total_votes}\n")
    textfile.write("---------------------------------------\n")  
    textfile.write(f"{election_data[0][0]}: {election_data[0][1]}% ({election_data[0][2]})\n")
    textfile.write(f"{election_data[1][0]}: {election_data[1][1]}% ({election_data[1][2]})\n")
    textfile.write(f"{election_data[2][0]}: {election_data[2][1]}% ({election_data[2][2]})\n")
    textfile.write(f"{election_data[3][0]}: {election_data[3][1]}% ({election_data[3][2]})\n")
    textfile.write("---------------------------------------\n")
    textfile.write(f"Winner : {winner}\n")
    textfile.write("---------------------------------------\n")  