import os
import csv

# Lists to store data elements
election=[]
results={}
sorted_candidates={}
dashes = "---------------------------\n"
count = 0

# Get current work directory
cwd = os.getcwd()

election_csv = os.path.join(cwd, 'Resources', 'election_data.csv')

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #read header
    csv_header = next(csvreader)    
    
    # Store candidate from csv file into election list
    for row in csvreader:
        election.append(row[2])
    
    
    total_votes = len(election)
    
    # Sort candidates in list
    election = sorted(election)
    
    # Get unique candidates from list using set method
    candidates = set(election)
    #print(candidates)
    
    # Loop through candidates and calculate vote tallies
    for pol in candidates:
        #print(can, election.count(can))
        #Build dictionary of candidates/votes
        results.update({pol:election.count(pol)})
    
    # Create new dictionary with the candidates 
    # sorted by vote tally greatest to smallest
    sorted_candidates = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
    
    
    # Build analysis report and store in string variable 
    # to print to terminal and save to file
    report_analysis = "Election Results\n" + \
        dashes + \
        f"Total Votes: {total_votes}\n" + \
        dashes
    
    # Dynamically build analysis report by looping through sorted_candidates dictionary    
    for name, vote in sorted_candidates.items():
        count += 1
        if (count == 1):
            winner_name = name
            
        pct_calc = round((vote / total_votes) * 100, 3)
        report_analysis += f"{name}: {pct_calc}% ({vote})\n"
    
    report_analysis = report_analysis + \
        dashes + \
        f"Winner: {winner_name}\n" + \
        dashes
    
    # Show report in terminal
    print(report_analysis)
    
    # Save report to text file
    analysis_file = os.path.join(cwd, "analysis", "election_data.txt")
    with open(analysis_file, "w") as outfile:
        outfile.write(report_analysis)
        
