#Take CSV and create a data frame with desired information
#Create a second dataframe with 10 (variable to change) day moving averages of statistics that also includes runs scored for that game for home and away team
#Simulate game using Monte Carlo
#Compare winners and determine success of predicting game outcomes with a Monte Carlo
import dataFrameGen as frame

def generateProbabilities(seasonFrame, days, team):

    tf = frame.generateTeamFrame(seasonFrame, team)

    stats = frame.generateSumFrame(tf, days, team, 0)
    totalABs = stats['ABs']


    probs = {'Strikeouts': stats['Strikeouts']/totalABs,
             'Walks': stats['Walks']/totalABs,
             'HBP': stats['HBP']/totalABs,
             'Error': stats['Error']/totalABs,
             'Single': stats['Single']/totalABs,
             'Double': stats['Double']/totalABs,
             'Triple': stats['Triple']/totalABs,
             'HR': stats['HR']/totalABs,
             'Double Play': stats['Double Play']/totalABs,
             'Sac Flies': stats['Sac Flies']/totalABs,
             'Sac Hits': stats['Sac Hits']/totalABs}

    probs['Forced Outs'] = 1 - sum(probs.values())
    probs['Team'] = team

    return probs

def gameSearch(seasonFrame, days):
    games = []
    for index, row in seasonFrame.iterrows():
        if row['Home Game Number'] > days and row['Away Game Number'] > days:
            games.append(index)

    return games

def runMonteCarlo(game, probabilityHome, probabilityAway, iterations):
    print(game)
    #Return Home Score, Away Score, Spread

def main(seasonFile, days):

    mf = frame.generateMainFrame(seasonFile)
    #Generate list of games that the teams have played the required number of games
    games = gameSearch(mf, 10)
    #Loop through each game and run the Monte Carlo
    testGame = mf.iloc[144]

    #Calculate probabilities
    probabilityHome = generateProbabilities(mf, days, testGame['Home Team'])
    probabilityAway = generateProbabilities(mf, days, testGame['Away Team'])

    #Feed into Monte Carlo

    #Return probability of each team winning



main('GL2010.csv', 10)