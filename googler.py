from googlesearch import search
import requests
from bs4 import BeautifulSoup

def file_searcher(name_of_seriese,season,quality):
	s=search("intitle index of?mkv "+name_of_seriese+" "+season+" "+quality,stop=1)
	s=list(s)
	#print(s)
	return s[0]
def get_video_links(archive_url,quality):
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content,'html5lib')
    links = soup.findAll('a')
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mkv')]
    #print(video_links) 
    return video_links
def download_video_series(video_links,name):
    i=1
    for link in video_links:
        file_name =name+str(i)
        i=i+1 
        #print(file_name)   
        print ("Downloading file:",file_name)
        # create response object
        r = requests.get(link, stream = True)	
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
         
        print("%s downloaded!\n"%file_name)
 
    print ("videos downloaded!")
    return

name=input("enter seriese name:")
season=input("enter season:")
quality=input("enter quality:")
download_video_series(get_video_links(file_searcher(name,season,quality),quality),name)
