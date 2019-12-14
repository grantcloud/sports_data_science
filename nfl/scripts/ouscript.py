# write over/under .csv for analysis

import pandas as pd

# import all NFL teams
tdf = pd.read_csv('data/nfl_teams.csv')

# dropping teams no longer in the NFL
tdf = tdf[~tdf.team_name.isin(['Phoenix Cardinals','St. Louis Cardinals','Baltimore Colts','San Diego Chargers','St. Louis Rams','Boston Patriots','Los Angeles Raiders','Houston Oilers','Tennessee Oilers'])]

# import scores, favorites, and spreads from 1966
df = pd.read_csv('spreadspoke_scores.csv')

# removing unneeded columns
df = df.loc[:,['schedule_season','schedule_playoff',
              'team_home','score_home','score_away',
              'team_away','spread_favorite','stadium_neutral',
              'over_under_line','team_favorite_id']]

# grab only games from 2015 to 2019
df = df[(df.schedule_season.astype('int') >= 2015) & (df.schedule_season.astype('int') < 2019)]

# grab only regular season games
df = df[df['schedule_playoff'] == False]

# create dictionary of team name to team id mappings
idDict = {tdf[tdf['team_name'] == team].team_id.reset_index(drop=True)[0]:team for team in tdf.team_name.unique()}

# create a new column for favorites with team names instead of team id's
df['favorite'] = df['team_favorite_id'].map(idDict)

# write the cleaned df to csv
df.to_csv('data/nfl_spread_covers.csv', index=False)