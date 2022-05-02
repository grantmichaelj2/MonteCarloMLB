import pandas as pd

def generateMainFrame(csvFile):

    df = pd.read_csv(csvFile, usecols = ['Date', 'Away Team', 'Home Team', 'Away Game Number', 'Home Game Number', 'Away Score', 'Home Score', 'Away ABs', 'Away Hits', 'Away Doubles', 'Away Triples', 'Away HRs', 'Away Sac Hits', 'Away Sac Flies', 'Away HBP', 'Away Walks', 'Away Strikeouts', 'Away Stolen Bases', 'Away Caught Stealing', 'Away Double Plays', 'Away Errors', 'Home ABs', 'Home Hits', 'Home Doubles', 'Home Triples', 'Home HRs', 'Home Sac Hits', 'Home Sac Flies', 'Home HBP', 'Home Walks', 'Home Strikeouts', 'Home Stolen Bases', 'Home Caught Stealing', 'Home Double Plays', 'Home Errors'])

    return df

def generateTeamFrame(pdFrame, team):

    teamStats = pdFrame.loc[(pdFrame['Home Team'] == team) | (pdFrame['Away Team'] == team)]

    return teamStats

def generateSumFrame(teamFrame, days, team, iteration):
    stats = {'ABs': 0,
             'Strikeouts': 0,
             'Walks': 0,
             'HBP': 0,
             'Error': 0,
             'Single': 0,
             'Double': 0,
             'Triple': 0,
             'HR': 0,
             'Double Play': 0,
             'Sac Flies': 0,
             'Sac Hits': 0}

    #Select first N rows of data
    test = teamFrame.iloc[iteration:days]
    #Sum it (will need unique function)
    for index, row in test.iterrows():
        if row['Home Team'] == team:
            stats['ABs'] += row['Home ABs']
            stats['Strikeouts'] += row['Home Strikeouts']
            stats['Walks'] += row['Home Walks']
            stats['HBP'] += row['Home HBP']
            stats['Error'] += row['Away Errors']
            stats['Single'] += (row['Home Hits'] - row['Home Doubles'] - row['Home Triples'] - row['Home HRs'])
            stats['Double'] += row['Home Doubles']
            stats['Triple'] += row['Home Triples']
            stats['HR'] += row['Home HRs']
            stats['Double Play'] += row['Home Double Plays']
            stats['Sac Flies'] += row['Home Sac Flies']
            stats['Sac Hits'] += row['Home Sac Hits']

        elif row['Away Team'] == team:
            stats['ABs'] += row['Away ABs']
            stats['Strikeouts'] += row['Away Strikeouts']
            stats['Walks'] += row['Away Walks']
            stats['HBP'] += row['Away HBP']
            stats['Error'] += row['Home Errors']
            stats['Single'] += (row['Away Hits'] - row['Away Doubles'] - row['Away Triples'] - row['Away HRs'])
            stats['Double'] += row['Away Doubles']
            stats['Triple'] += row['Away Triples']
            stats['HR'] += row['Away HRs']
            stats['Double Play'] += row['Away Double Plays']
            stats['Sac Flies'] += row['Away Sac Flies']
            stats['Sac Hits'] += row['Away Sac Hits']

    return stats


