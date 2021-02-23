import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

page=requests.get('https://www.iplt20.com/')
soup=BeautifulSoup(page.content,'html.parser')
# print(soup)

# lead=soup.findAll(class_='match-item__score--runs')

# lead=soup.findAll(id='main-content')

players=[]

results=[]

ranks=[]

lead=soup.findAll(class_='leaderBackdrop')


caders=[1,2,3,4,5]


try:
    for k in range(int(input('enter up to five :'))):
    
        ci=lead[k].find(class_='leaderHeader')
        a1=ci.text.strip()
        ranks.append(a1)
        p=lead[k].find(class_='digits')
        a2=p.text.strip()
        results.append(a2)
        h=lead[k].find('h1')
        a3=h.text.strip()
        players.append(a3)

except:
    raise 'please enter the up to 5 numbers'


print(players,results,ranks)
# lead1=soup.findAll('div')
# print(lead1)



# matplotlib scenario


cader=[ i for i in range(int(input('enter a value up to 5 numbers :')))]

print(plt.plot(cader,results))
print(plt.xlabel(' ranks '))
print(plt.ylabel(' results'))
print(plt.title('ipl prediction'))
print(plt.show())