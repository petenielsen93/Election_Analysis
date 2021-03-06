# The data we need to retrieve
# 1. Total # of votes cast
# 2. Complete list of candidates that received votes
# 3. Percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on pop. vote


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path    
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open election results and read the file
with open(file_to_load) as election_data:
    #Read and analyze the data here
    file_reader = csv.reader(election_data)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)



# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

