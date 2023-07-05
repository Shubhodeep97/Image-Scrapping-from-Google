#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import requests


# In[4]:


from bs4 import BeautifulSoup


# In[9]:


Google_Image_Link = 'https://www.google.com/imghp?hl=en&authuser=0&ogbl'


# In[6]:


user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}


# In[7]:


Image_Folder = 'Google Images'


# In[11]:


def main():
    if not os.path.exists(Image_Folder):
        os.mkdir(Image_Folder)
    download_images()    


# In[13]:


def download_images():
    data = input('Enter your search keyword: ')
    num_images = 50
    
    print('Searching Images...')
    
    
    url = Google_Image_Link + 'q=' + data
    
    response_html = requests.get(url, headers = user_agent)
    response_text = response_html.text
    
    
    b_soup = BeautifulSoup(response_text, 'response.parser')
    results = b_soup.findAll('img', {'class': 'gb_k gbii'})
    
    
    
    count = 0
    imagelinks = []
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count = count + 1
            if (count >= num_images):
                break
                
                
        except KeyError:
            continue
            
            
    print(f'Found {len(imagelinks)} images')
    print('Start Downloading...')
    
    
    for i, imagelink in enumerate(imagelinks):
        response = requests.get(imagelink)
        
        imagename = Image_Folder + '/' + data + str(i+1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)
            
            
    print('Download Completed!')
    
    
if __name__ == '__main__':
    main()


# In[ ]:




