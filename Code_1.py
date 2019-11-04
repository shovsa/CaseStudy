# Code for finding the best location for startups in India
import pandas as pd
import matplotlib.pyplot as plt
a = pd.read_csv('startup_funding.csv')
b = a.copy()
c = b['CityLocation'].value_counts()
d = {}
l = 0
co = 0
p = list(c.index.copy())
q = list(c.values.copy())
for i in c.index[0:10]:
    d[i] = c.values[l]
    l +=1
    for j in range(10,len(c.index)):
        if i.lower() in ((c.index[j].split('/'))[0]).lower():
            d[i] += c.values[j]
            p.remove(c.index[j])
for i in range(10,len(c.index)):
    if c.index[i].lower() == 'delhi':
        co += c.values[i]
        p.remove(c.index[i])
d['New Delhi'] += co   
d['NCR'] = d['New Delhi'] + d['Gurgaon'] + d['Noida']
bangalore = d['Bangalore']
mumbai = d['Mumbai']
ncr = d['NCR']
plt.bar(['Bangalore','Mumbai','NCR'],[bangalore,mumbai,ncr])
plt.title('Bar graph of location vs number of fundings')
plt.xlabel('LOCATION')
plt.ylabel('NUMBER OF FUNDINGS')
plt.show()
print('NCR',d['NCR'])