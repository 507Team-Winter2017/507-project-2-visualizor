#proj2.py
from bs4 import BeautifulSoup as bs
import requests as rq 


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here

res = rq.get('https://nytimes.com')
soup = bs(res.text,'html.parser')
headlines = soup.find_all(class_='story-heading')
ct,i=0,0
while ct<10:
    if headlines[i].span:
        i += 1
        continue
    else:
        print(headlines[i].a.text)
        i+=1
        ct+=1


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here

res=rq.get('https://www.michigandaily.com/')
soup = bs(res.text,'html.parser')
lst = soup.find_all('ol')[0]
for i in lst:
    temp = bs(str(i),'html.parser')
    print(temp.text.strip())


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here

res = rq.get('http://newmantaylor.com/gallery.html')
soup=bs(res.text,'html.parser')
img=soup.find_all('img')
for i in img:
    try: print(i['alt'])
    except: print('No alternative text provided!!')

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here

url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'

def emails(url,indx=0):
    res=rq.get(url,headers={'User-Agent':'Mozilla/5.0'})
    soup = bs(res.text,'html.parser')
    lst = soup.find_all('div','field field-name-contact-details field-type-ds field-label-hidden')
    for i in lst:
        indx+=1
        node = i.find('a')['href']
        r = rq.get('https://www.si.umich.edu'+node,headers={'User-Agent':'Mozilla/5.0'})
        s = bs(r.text,'html.parser')
        e = s.find(class_='field field-name-field-person-email field-type-email field-label-inline clearfix')
        print (str(indx) + ' ' + e.find('a').get_text())
    p = soup.find('li','pager-current').get_text().split()
    
    if p[0] != p[-1]:
        url = 'https://www.si.umich.edu'+soup.find('li','pager-next last').a['href']
        emails(url,indx)

emails(url)