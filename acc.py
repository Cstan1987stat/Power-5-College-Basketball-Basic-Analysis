import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

df = pd.read_csv('C:/users/conno/OneDrive/Documents/personal projects/power 5 bball/5seasacc.csv')

df['Away_P_Diff'] = df['Away_P'] - df['Home_P']
df['Home_P_Diff'] = df['Home_P'] - df['Away_P']
df.loc[df['Home'] == 'Miami (FL)', 'Home'] = 'Miami'
df.loc[df['Away'] == 'Miami (FL)', 'Away'] = 'Miami'

away_p_diff = df.groupby('Away')['Away_P_Diff'].mean()
home_p_diff = df.groupby('Home')['Home_P_Diff'].mean()

def colors(team):
    color = {
        'Boston College': (115, 0, 10),
        'Clemson': (245, 102, 0),
        'Duke': (0, 48, 135),
        'Florida State': (120, 47, 64),
        'Georgia Tech': (179,163,105),
        'Louisville': (227, 27, 35),
        'Miami': (244, 115, 33),
        'NC State': (204, 0, 0),
        'North Carolina': (123, 175, 212),
        'Notre Dame': (12, 35, 64),
        'Pittsburgh': (0, 53, 148),
        'Syracuse': (247, 105, 0),
        'Virginia': (35, 45, 75),
        'Virginia Tech': (99, 0, 49),
        'Wake Forest': (158, 126, 56)
    }
    r, g, b = color[team]
    return mcolors.rgb2hex((r/255, g/255, b/255))
sns.scatterplot(x = away_p_diff.values, y = home_p_diff.values, style = away_p_diff.index,
                s = 90, hue = away_p_diff.index,
                palette = sns.color_palette([colors(t) for t in away_p_diff.index]))
plt.ylabel('Mean Home Game Points Difference', fontname = 'Times New Roman')
plt.xlabel('Mean Away Game Points Difference', fontname = 'Times New Roman')
plt.title('ACC Basketball Mean Away Game Points Difference vs Mean Home Game Points Difference',
          fontsize = 16, fontweight = 'demibold', y = 1.08,
          fontname = 'Times New Roman')
plt.suptitle('Data from 2015-2023 Seasons (sports-reference.com). No Conference Tournament Games.',
             fontsize = 9, y = 0.94, fontname = 'Times New Roman')
plt.text(0.9, -0.1, 'Graph by Connor Stanley.', fontsize = 8,
         transform = plt.gca().transAxes, fontname = 'Times New Roman')
plt.grid(True, linewidth = 0.14)
plt.axhline(y = 0, color = 'black', linewidth = 0.29)
plt.axvline(x = 0, color = 'black', linewidth = 0.29)
plt.gca().get_legend().set_title('Teams')
plt.grid(True, linewidth = 0.14)
plt.show()

