import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

df = pd.read_csv('C:/users/conno/OneDrive/Documents/personal projects/power 5 bball/5seasbig10.csv')
# 2015 - 2023 seasons
df['Away_P_Diff'] = df['Away_P'] - df['Home_P']
df['Home_P_Diff'] = df['Home_P'] - df['Away_P']

away_p_diff = df.groupby('Away')['Away_P_Diff'].mean()
home_p_diff = df.groupby('Home')['Home_P_Diff'].mean()

def colors(team):
    color = {
        'Illinois': (19, 41, 75),
        'Indiana': (153, 0, 0),
        'Iowa': (255, 205, 0),
        'Maryland': (224, 58, 62),
        'Michigan': (0, 39, 76),
        'Michigan State': (24, 69, 59),
        'Minnesota': (122,0,25),
        'Nebraska': (227, 25, 55),
        'Northwestern': (78, 42, 132),
        'Ohio State': (187, 0, 0),
        'Penn State': (4, 30, 66),
        'Purdue': (206, 184, 136),
        'Rutgers': (204,0,51),
        'Wisconsin': (197, 5, 12) 
    }
    r, g, b = color[team]
    return mcolors.rgb2hex((r/255, g/255, b/255))

sns.scatterplot(x = away_p_diff.values, y = home_p_diff.values, style = away_p_diff.index,
                s = 89, hue = away_p_diff.index, 
                palette = sns.color_palette([colors(t) for t in away_p_diff.index]))
plt.ylabel('Mean Home Game Points Difference', fontname = 'Times New Roman')
plt.xlabel('Mean Away Game Points Difference', fontname = 'Times New Roman')
plt.title('Big 10 Basketball Mean Away Game Point Difference vs Mean Home Game Point Difference',
          fontsize = 16, fontweight = 'demibold', y = 1.08,
          fontname = 'Times New Roman')
plt.suptitle('Data from 2015-2023 Seasons (sports-reference.com). No Conference Tournament Games.',
             fontsize = 9, y = 0.94, fontname = 'Times New Roman')
plt.text(0.9, -0.1, 'Graph by Connor Stanley.', fontsize = 8,
         transform = plt.gca().transAxes, fontname = 'Times New Roman')
plt.axhline(y = 0, color = 'black', linewidth = 0.29)
plt.axvline(x = 0, color = 'black', linewidth = 0.29)
plt.gca().get_legend().set_title('Teams')
plt.grid(True, linewidth = 0.14)
plt.show()
