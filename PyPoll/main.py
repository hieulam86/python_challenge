import csv
import os

#Read data from the CSV file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) #Skip the header row

    #Create variables
    candidates = {}
    total_votes = 0
    winner = ""
    winner_votes = 0

    #Loop through each row in the CSV
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]

        #Count vote for each candidate
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1

        #Check the winner
        if candidates[candidate] > winner_votes:
            winner = candidate
            winner_votes = candidates[candidate]

    #Calculate the percentages
    percentage_votes = {}
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        percentage_votes[candidate] = percentage

    #Print the results
    print("Election Results")
    print("--------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------")
    for candidate, votes in candidates.items():
        percentage = percentage_votes[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("--------------------------------")
    print(f"Winner: {winner}")
    print("--------------------------------")

    #Output the results to a text file
    output_path = os.path.join('..', 'analysis', 'PyPoll.txt')
    with open(output_path, 'w') as output_file:
        output_file.write("Election Results\n")
        output_file.write("------------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("------------------------------\n")
        for candidate, votes in candidates.items():
            percentage = percentage_votes[candidate]
            output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        output_file.write("------------------------------\n")
        output_file.write(f"Winner: {winner}\n")
        output_file.write("------------------------------\n")