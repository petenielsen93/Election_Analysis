# Election_Analysis

## Overview of Election Audit
In this fictitious event, we helped Seth and Tom submit election audit results to a local election commission for an election in Colorado. After learning the basics of python syntax, looping, if statements, and connecting to csv and txt files, we wrote some code to import the election data, calculate important metrics, and determine the winner. The findings were then written onto the election_analysis.txt file, where they are clearly readable for the election commission.

## Election-Audit Results
There were many metrics that we calculated from the data to give insight into the results:

- Total Votes Cast
The total votes cast in the election was calculated by first creating a total vote counter and setting that variable to 0. Next, while looping through the CSV file to convert it into a list of dictionaries, we added each row as a vote. We then printed the variable for total votes and edited it to include a comma at its necessary locations. There were 369,711 votes total. 

    #Initialize a total vote counter.
        total_votes = 0
    #Add to the total vote count
        total_votes = total_votes + 1 (This was placed inside the loop)
    #the code responsible for listing the total vote count on the election_analysis document. 
     f"Total Votes: {total_votes:,}\n"

- County Breakdown
The number of votes and percentage of total votes was calculated for each county. This was first done by creating a county list, to hold the names of the counties, and a county dictionary, which we used to hold the vote counts and match them with their respective county. When looping through the CSV file, we took the name of each county down, and created an if statement saying if the county was already in the list, to skip it. This led us to build our list. We totaled the county votes by adding a vote for every time the name was listed. We then wrote another loop in order to retrieve our info from the dictionary we created, and to then total our count for each county and calculate our percentage of votes per county. This led to our county votes breakdown available in the election_analysis document. 

    #The code below was placed inside the first loop to retrieve the county names.
    county_name = row[1]
    #This conditional was written to gather only unique names for our list, and to count those votes for every time the county name was listed.
    
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
    #This code was the loop that calculated the vote count per county and percentage per county based on our dictionary information, and printed the results. 
        for county_name in county_votes:
            # 6b: Retrieve the county vote count.
            county_vc = county_votes[county_name]
            # 6c: Calculate the percentage of votes for the county.
            county_percentage = float(county_vc) / float(total_votes) * 100

            # 6d: Print the county results to the terminal.
            county_results = (f'{county_name}: {county_percentage:.1f}% ({county_vc:,})\n')

- The county with the largest amount of votes was Denver county by far, with 82.8% of the vote count. This is not surprising, because Denver county takes up the most population-dense parts of the city of Denver. 

- Candidate Breakdown
The candidate breakdown was calculated almost identically to the county breakdown. We created a candidate list and dictionary, which we used to hold the candidate names and match them with their vote counts. We used the same method of taking unique candidate names and vote counts as we did with the county information. Again, we wrote another loop in order to retrieve our info from the dictionary, and to then total our count and calculate our percentage. This led to our candidate votes breakdown available in the election_analysis document. 

    #Get the candidate name from each row.
        candidate_name = row[2]
    #This loop was written to gather our unique names and vote count
    
    if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    #This code took our list and dictionary info, and let us display them as we wanted. 
        for candidate_name in candidate_votes:

            # Retrieve vote count and percentage
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate's voter count and percentage to the
            # terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

- As shown on the election_analysis document, the winner of the election is Diana DeGette, with 73.8% of the vote and receiving 272,892 votes total. She won by a landslide. 


## Election-Audit Summary
Elections are a very important democratic process in this country, and auditing this election was critical to ensuring that as an election commission, you were successful preventing any foul play and bringing forth a clear and concise victor. This code was a critical part of the audit, and I believe it could be applied to other elections as well. In order to do that, we would firstly need to modify the part of the code that is relative to importing the file, and update it to the location and format of the next file. Maybe that even includes new information we could use to draw conclusions about election outcomes. Secondly, we could update the for loop to include options for calculating the vote counts for districts, cities, and even states. 