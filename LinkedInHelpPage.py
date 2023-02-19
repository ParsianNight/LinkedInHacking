from urllib.request import urlopen
import re
import urllib.request
import os
import sys
import datetime
def download_webpage(url):
    fileName = url.find("answer/a")
    fileName = url[fileName+len("answer/a"):]+".txt"

    if os.path.exists(fileName):
        print("File already exists")
        compare_webpage(url)
    else:
        fileName = url.find("answer/a")
        fileName = url[fileName+len("answer/a"):]
        urllib.request.urlretrieve(url, fileName)
        print("File downloaded")

def compare_webpage(url):
    if os.path.exists(url):
        
        fileName = url[fileName+len("answer/a"):]
        urllib.request.urlretrieve(url, fileName+"Tax")
        print("File downloaded")
        with open(fileName+'Tex', 'r') as f:
            with open(fileName, 'r') as f1:
                for line in f:
                    for line1 in f1:
                        if line != line1:
                            print(line +"\n"+line1+"\n\n")
                        else:
                            print("There is no difference in content")
with open('URLS.txt', 'w') as f:
    f.write(f"{datetime.date.today()}" + "------\n")

data ={}
for i in range(1500000):
    url = f"https://www.linkedin.com/help/linkedin/answer/a{i}"
    print(url)
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    start_index = html.find('"subText":"') +  len('"subText":"')
    end_index = html.find('","lastModifiedTimestamp":')
    date = re.findall("(.*days|.*hour).*",html[start_index:end_index],re.IGNORECASE)
    if len(date) != 0 :
        data[url] = date
        download_webpage(url)
        with open('URLS.txt', 'w') as f:
            f.write(url +"  " + date[0])
    date={}
    



