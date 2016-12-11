#Play Trending Videos

from bs4 import BeautifulSoup
import requests
import webbrowser
import subprocess

response = requests.get("https://www.youtube.com/feed/trending")

data = response.text
soup = BeautifulSoup(data,"lxml") 

#Find all h3 tags
i=0 
cond=True
while cond==True:
      list1=[]
      for link in soup.find_all("h3",{"class":"yt-lockup-title"}):
          for var in link.find_all("a"):
              title = var.get("title")
              href  = var.get("href")
              print("Title[%s] = %s\n"%(i,title))
              list1.insert(i,href)
              i=i+1

      choice = int(raw_input("Want to play video enter your choice else -1 "))
      select =list1[choice]
      link = "https://www.youtube.com"+select
      
      if choice!=-1:
         option = raw_input("VLC(v) or Youtube(y) ")
         if option=='y':
            webbrowser.open(link)
         else:
            myprocess = subprocess.call(['vlc','-vvv',link])
      choice=raw_input("want to continue y/n ")
      if choice=='n':
         cond=False
      i=0   
           
     
