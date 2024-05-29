import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

df = pd.read_csv('C:/users/conno/OneDrive/Documents/personal projects/power 5 bball/5seasbig12.csv')

df['Away_P_Diff'] = df['Away_P'] - df['Home_P']
df['Home_P_Diff'] = df['Home_P'] - df['Away_P']

away_p_diff = df.groupby('Away')['Away_P_Diff'].mean()
home_p_diff = df.groupby('Home')['Home_P_Diff'].mean()


def colors(team):
    color = {
        'Kansas State': (81, 40, 136),
        'Texas': (191, 87, 0),
        'Kansas': (0, 81, 186),
        'Baylor': (21, 71, 52),
        'Texas Tech': (204, 0, 0),
        'West Virginia': (0, 40, 85),
        'Iowa State': (200, 16, 46),
        'TCU': (77, 25, 121),
        'Oklahoma': (132, 23, 25),
        'Oklahoma State': (255, 124, 25)
    }
    r, g, b = color[team]
    return mcolors.rgb2hex((r/255, g/255, b/255))



sns.scatterplot(x = away_p_diff.values, y = home_p_diff.values, 
                style = away_p_diff.index, s = 75, 
                hue = away_p_diff.index,
                palette = sns.color_palette([colors(t) for t in away_p_diff.index]))
plt.ylabel('Mean Home Game Points Difference', fontname = 'Times New Roman')
plt.xlabel('Mean Away Game Points Difference', fontname = 'Times New Roman')
plt.axhline(y = 0, color = 'black', linewidth = 0.29)
plt.axvline(x = 0, color = 'black', linewidth = 0.29)
plt.title('Big 12 Basketball Mean Away Game Points Difference vs Mean Home Game Points Difference',
          fontname = 'Times New Roman', fontsize = 16, fontweight = 'demibold',
          y = 1.08)
plt.suptitle('Data from 2013-2023 Seasons (sports-reference.com). No Conference Tournament Games.',
             fontname = 'Times New Roman', fontsize = 9, y = 0.94)
plt.text(0.9, -0.1, 'Graph By Connor Stanley.', fontsize = 9,
         transform = plt.gca().transAxes, fontname = 'Times New Roman')
plt.gca().get_legend().set_title('Teams')
plt.grid(True, linewidth = 0.14)
plt.axvline(x = 0, color = 'black', linewidth = 0.2)
plt.legend(loc = 'upper left')
plt.gca().get_legend().set_title('Teams')
plt.show()
