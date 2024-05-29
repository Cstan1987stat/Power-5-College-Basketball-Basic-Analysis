import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

df = pd.read_csv('C:/users/conno/OneDrive/Documents/personal projects/power 5 bball/5seaspac12.csv')

df['Away_P_Diff'] = df['Away_P'] - df['Home_P']
df['Home_P_Diff'] = df['Home_P'] - df['Away_P']

away_p_diff = df.groupby('Away')['Away_P_Diff'].mean()
home_p_diff = df.groupby('Home')['Home_P_Diff'].mean()
def colors(team):
    color = {
        'Arizona': (204, 0, 51),
        'Arizona State': (140, 29, 64),
        'California': (0, 50, 98) ,
        'Colorado': (207, 184, 124),
        'Oregon': (18, 71, 52),
        'Oregon State': (220, 68,5),
        'Southern California': (153, 27, 30),
        'Stanford': (140, 21, 21),
        'UCLA': (45,104,96),
        'Utah': (204, 0, 0),
        'Washington': (51, 0, 111),
        'Washington State': (152, 30, 50) 
    }
    r, g, b = color[team]
    return mcolors.rgb2hex((r/255, g/255, b/255))

sns.scatterplot(x = away_p_diff.values, y = home_p_diff.values, style = away_p_diff.index,
                s = 80, hue = away_p_diff.index,
                palette = sns.color_palette([colors(t) for t in away_p_diff.index]))
plt.ylabel('Mean Home Game Points Difference', fontname = 'Times New Roman')
plt.xlabel('Mean Away Game Points Difference', fontname = 'Times New Roman')
plt.title('Pac 12 Basketball Mean Away Game Points Difference vs Mean Home Game Points Difference.',
          fontsize = 16, fontweight = 'demibold', y = 1.08,
          fontname = 'Times New Roman')
plt.suptitle('Data from 2012-2023 Seasons (sports-reference.com). No Conference Tournament Games.',
             fontsize = 9, y = 0.94, fontname = 'Times New Roman')
plt.text(0.9, -0.1, 'Graph by Connor Stanley.', fontsize = 8,
         transform = plt.gca().transAxes, fontname = 'Times New Roman')
plt.axhline(y = 0, color = 'black', linewidth = 0.29)
plt.axvline(x = 0, color = 'black', linewidth = 0.29)
plt.gca().get_legend().set_title('Teams')
plt.grid(True, linewidth = 0.14)
plt.show()


