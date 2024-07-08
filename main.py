import requests 
import json
###Creating HTML###


#Functions
def fetchtofile(url,path):
    response = requests.get(url)
    with open (path,"w",encoding="utf-8") as f:
        f.write(response.text)

 #Variables       
category=["food","travel","beauty","sports and fitness","lifestly","parenting","business","music","photography","fashion","Animals"]


#Scaping data and storing in html file
user_input = input(f"Enter a category: {category}")

if user_input == category[0]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/food",f"{category[0]}.html")
elif user_input == category[1]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/travelling",f"{category[1]}.html")
elif user_input == category[2]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/beauty",f"{category[2]}.html")
elif user_input == category[3]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/health-fitness",f"{category[3]}.html")
elif user_input == category[4]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/lifestyle",f"{category[4]}.html")
elif user_input == category[5]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/parenting",f"{category[5]}.html")
elif user_input == category[6]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/business",f"{category[6]}.html")
elif user_input == category[7]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/music",f"{category[7]}.html")
elif user_input == category[8]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/photography",f"{category[8]}.html")
elif user_input == category[9]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/fashion",f"{category[9]}.html")
elif user_input == category[10]:
    
    fetchtofile("https://www.notjustanalytics.com/instagram-influencers/animals",f"{category[10]}.html")
else:
    print("Invalid category")

###################

###Extracting Data###

from bs4 import BeautifulSoup

with open (f"{user_input}.html","r",encoding="utf-8") as f:
        text=(f.read())
        

def extract_usernames(html):
   
    soup = BeautifulSoup(html, 'html.parser') 
    divs = soup.find_all('div', class_='text-md font-bold flex flex-row items-center font-montserrat truncate max-w-md')
    usernames = []

    for div in divs:
        username = div.get_text().strip()
        if username.startswith('@'):
            usernames.append(username)
    
    return usernames




username = extract_usernames(text)
for i in username:
    print(i)
                   
#########################################

