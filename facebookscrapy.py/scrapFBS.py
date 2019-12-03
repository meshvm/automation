
import os
import time
import re
import time
import requests
import fileRdWr
#
import urllib.request
from bs4 import BeautifulSoup
#
def tag_visible(element):
    '''This function is a helper function to removes all the html tags from the element
            it finds all visible text excluding scripts, comments, css etc.
            return:True or False
    '''
    #function to remove html tags
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    # if isinstance(element,comment):
    #     return False
    return True
def text_from_html(body):
    ''' 
    This function is used to extract text from html page ,it uses function tag_visible() as a helper funciton 
    parameter:html content of page return:String of all visible text
    '''
    #function to extract text from html page
    soup = BeautifulSoup(body, 'html.parser')
    #print(soup.text)
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts) 
    #print(visible_texts,"visible text") 
    return u" ".join(t.strip() for t in visible_texts)
def scrap_operation(url):    
    link = url
   
    page = requests.get(link)
    main_contact=page.content
    
    main_contact_soup = BeautifulSoup(main_contact, 'html.parser')  #Parse html code
    text_of_main_contact = main_contact_soup.findAll(text=True)
    visible_texts = filter(tag_visible, text_of_main_contact)
    main_contact_html_text=u" ".join(t.strip() for t in visible_texts)

    file_append=open("oyt.txt", "a")
    if file_append.mode == 'a':
       #print(main_contact_html_text)
       file_append.write(main_contact_html_text)
       file_append.close()
    #fileRdWr.fileReadWr()

       

   
    
if __name__ == "__main__":
    url=''
    scrap_operation(url)
    
       
    
