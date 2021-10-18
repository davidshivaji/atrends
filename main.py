import sys
from datetime import date
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='en_US', tz=360)

# https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories

all_keywords = sys.argv[1:]

today = date.today()
frame = f'2004-01-01 {today.strftime("%Y-%m-%d")}'

# cat=31 = programming
pytrends.build_payload(all_keywords, timeframe=frame, geo='')


df = pytrends.interest_over_time()
df.head(20)

plt.style.use('dark_background')
plt.figure().patch.set_facecolor('#121212')
plt.axes().set_facecolor('#080808')
linewidth = 1

colors = ['orange', 'teal', 'crimson', 'magenta', 'skyblue']

for i, x in enumerate(all_keywords):
    plt.plot(df[x], color=colors[i], label=x, linewidth=linewidth)

plt.legend()
plt.grid(color='#303030')

# wherever you run this from, it will save the image there.
plt.savefig(f'{"_".join(x for x in all_keywords)}.png', dpi=120)
plt.show()
