# The data we need to retrieve
# 1. Total # of votes cast
# 2. Complete list of candidates that received votes
# 3. Percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on pop. vote

#dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path    
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0 #total vote counter
candidate_options = [] #initialize variable as list
candidate_votes = {}    #initialize variable as dict
#Winning candidate and winning count tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and read the file
with open(file_to_load) as election_data:
    #Read and analyze the data here
    file_reader = csv.reader(election_data)
# Read and print the header row.
    headers = next(file_reader)
    
    
#print each row in csv/count votes
    for row in file_reader:
        total_votes += 1  #find total votes
        candidate_name = row[2] #grab candidate name from row
        
        if candidate_name not in candidate_options: # list candidate options
            candidate_options.append(candidate_name) #add to list if not already on list
            candidate_votes[candidate_name] = 0 #begin count of votes for candidate
        candidate_votes[candidate_name] += 1 #add vote to candidate count
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"--------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------\n"
            )
        
        print(election_results, end="")
        txt_file.write(election_results)
        
        for candidate_name in candidate_votes: #starting a loop for each candidate's vote count
            votes = candidate_votes[candidate_name] #assigned count of candidate's vote to variable votes
            vote_percentage = float(votes)/float(total_votes) * 100 #created vote percentage variable
            candidate_results = (
                    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)
            txt_file.write(candidate_results)    

                #print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n') #print statement inside loop to create multiple statements with each percentage
            if (votes > winning_count) and (vote_percentage > winning_percentage): #if statement to decide winner while looping through all candidates
                winning_count = votes #highest number is winning_count
                winning_percentage = vote_percentage 
                winning_candidate = candidate_name 
        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
    

