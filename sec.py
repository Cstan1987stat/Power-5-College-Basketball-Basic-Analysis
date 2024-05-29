import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

df = pd.read_csv('C:/users/conno/OneDrive/Documents/personal projects/power 5 bball/5seassec.csv')



def bar_colors(team):
    color = {
        'Alabama': (158, 27, 50),
        'Arkansas': (157, 34, 53),
        'Auburn': (12, 35, 64),
        'Florida': (0, 33, 165),
        'Georgia': (186, 12, 47),
        'Kentucky': (0, 51, 160),
        'Louisiana State': (70, 29, 124),
        'Mississippi': (204, 9, 47),
        'Mississippi State': (102, 0, 0) ,
        'Missouri': (0,0,0),
        'South Carolina': (115,0,10),
        'Tennessee': (255, 130, 0),
        'Texas A&M': (80, 0, 0),
        'Vanderbilt': (134,109,75)
    }
    r, g, b = color[team]
    return mcolors.rgb2hex((r/255, g/255, b/255))

df['Away_P_Diff'] = df['Away_P'] - df['Home_P']
df['Home_P_Diff'] = df['Home_P'] - df['Away_P']        
away_p_diff = df.groupby('Away')['Away_P_Diff'].mean()
home_p_diff = df.groupby('Home')['Home_P_Diff'].mean()

sns.scatterplot(x = away_p_diff.values, y = home_p_diff.values, style = away_p_diff.index,
                s = 95, hue = away_p_diff.index, 
                palette = sns.color_palette([bar_colors(t) for t in away_p_diff.index]))
plt.ylabel('Mean Home Game Points Difference', fontname = 'Times New Roman')
plt.xlabel('Mean Away Game Points Difference', fontname = 'Times New Roman')
len_x = len(away_p_diff)
plt.axhline(y = 0, color = 'black', linewidth = 0.29)
plt.axvline(x = 0, color = 'black', linewidth = 0.29)
plt.title('SEC Basketball Mean Away Game Points Difference vs Mean Home Game Points Difference',
          fontsize = 16, fontweight = 'demibold', y = 1.09,
          fontname = 'Times New Roman')
plt.suptitle('Data from 2013-2023 Seasons (sports-reference.com). No Conference Tournament Games.',
             fontsize = 9, y = 0.94, fontname = 'Times New Roman')
plt.text(0.9, -0.1, 'Graph by Connor Stanley.', fontsize = 8,
         transform = plt.gca().transAxes, fontname = 'Times New Roman')
plt.grid(True, linewidth = 0.14)
plt.gca().get_legend().set_title('Teams')
plt.show()

print(df)
