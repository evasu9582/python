import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt


page=requests.get('https://www.iplt20.com/stats/2020/most-runs')

soup=BeautifulSoup(page.content,'html.parser')

lead=soup.findAll('div' ,attrs={'class':'stats-table'})
player=lead[0].findAll('span',attrs={'class':'top-players__last-name'})
score=lead[0].findAll('td',attrs={'class':'top-players__r is-active'})

player_names=[]

player_scores=[]


for i in range(0,int(input('enter required numer of scores :'))):

    	# player=lead[0].findAll('span',attrs={'class':'top-players__last-name'})

    	player_names.append(player[i].text.strip())

    	# score=lead[0].findAll('td',attrs={'class':'top-players__r is-active'})

    	player_scores.append(score[i].text.strip())


print(player_scores,player_names)

print(plt.bar(player_names[::-1],player_scores[::-1],width=0.3,color='orange'))

print(plt.xlabel('Players Names'))

print(plt.ylabel('Players Scores'))
 
print(plt.title('Ipl Top playres'))

print(plt.show())

	# index=[j for j in range(int(input('enter a value :')))]
	# print(len(lead))
	# print(player[9].get_text())
	# print(score[9].get_text())

	# p=lead.find(class_="top-players__r is-active")

	# s=lead.find(class_="top-players__last-name")

	
	
	
	
	
	
	
	
	
	
	


