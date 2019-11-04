#Program to find out the list of top 5 investors.
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
a = pd.read_csv('startup_funding.csv')
b = a.copy()
b = b[b['InvestorsName']!='undisclosed investors']
d = {}
for i in b['InvestorsName']:
    for j in str(i).split(','):
        temp = j.strip()
        if temp in d:
            d[temp] += 1
        else:
            d[temp] = 1
e = {}
e = Counter(d).most_common(5)
for i in e:
    print(i[0],i[1])
plt.scatter([e[0][0],e[1][0],e[2][0],e[3][0],e[4][0]],[e[0][1],e[1][1],e[2][1],e[3][1],e[4][1]],)
plt.title('Plot of Investor Name vs Number Of Investments')
plt.xlabel('Investor Name')
plt.ylabel('Number Of Investments')
plt.grid()
plt.show()