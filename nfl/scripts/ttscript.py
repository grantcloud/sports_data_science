# write team-total .csv for analysis 

import pandas as pd

df = pd.read_csv('data/spreadspoke_scores.csv')

# include only year 2000 through 2018
df = df[(df.schedule_season.astype('int') >= 2000) & (df.schedule_season.astype('int') < 2019)]

# dropping unnecessary columns
df = df.loc[:,['schedule_season','score_home','score_away','over_under_line']]

# calculating total score in the game
df['total_score'] = df.score_home + df.score_away

# floating columns to calculate which covered
df['total_score'] = df['total_score'].astype('float')
df['over_under_line'] = df['over_under_line'].astype('float')

# helper function to calculate if the over or under hit (or push)
def overunder(row):
    if row.total_score > row.over_under_line:
        return 'over'
    elif row.total_score < row.over_under_line:
        return 'under'
    elif row.total_score == row.over_under_line:
        return 'push'
    
df['cover'] = df.apply(overunder, axis=1)

df.to_csv('data/nfl_over_unders.csv', index=False)