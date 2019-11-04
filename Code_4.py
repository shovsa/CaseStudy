#Startups with seed funding or crowd funding.
from collections import Counter
import pandas as pd
a = pd.read_csv('startup_funding.csv')
b = a.copy()
b['StartupName'].replace('Flipkart.com','Flipkart',inplace=True)
b['StartupName'].replace('Ola Cabs','Ola',inplace=True)
b['StartupName'].replace('Olacabs','Ola',inplace=True)
b['StartupName'].replace('Oyo Rooms','Oyo',inplace=True)
b['StartupName'].replace('OyoRooms','Oyo',inplace=True)
b['StartupName'].replace('Oyorooms','Oyo',inplace=True)
b['StartupName'].replace('OYO Rooms','Oyo',inplace=True)
b['StartupName'].replace('Paytm Marketplace','Paytm',inplace=True)
b['InvestmentType'].replace('SeedFunding','Seed Funding',inplace=True)
b['InvestmentType'].replace('PrivateEquity','Private Equity',inplace=True)
b['InvestmentType'].replace('Crowd funding','Crowd Funding',inplace=True)
b = b[b['InvestorsName']!='undisclosed investors']
b = b[(b['InvestmentType']=='Seed Funding') | ((b['InvestmentType']=='Crowd Funding'))] 
d = {}
f = {}
for i in b['InvestorsName']:
    for j in str(i).split(','):
        temp = j.strip()
        if temp in d:
            d[temp] += 1
        else:
            d[temp] = 1
for i in d:
    for j in range(len(b['StartupName'])):
        try:
            if str(i) in str(b['InvestorsName'][j]):
                if b['StartupName'][j] in f:
                    f[b['StartupName'][j]]+=1
                else:
                    f[b['StartupName'][j]]=1
        except:
            pass
    d[i] = d[i] - (sum(f.values()) - len(f))
    f = {}
e = {}
e = Counter(d).most_common(5)
for i in e:
    print(i[0],i[1])