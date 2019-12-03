''' 
    1. This file remove tags from oyt.txt if present into required strings if tags present, otherwise   
    and also checks for email, url , phone number using REGEX 
    2. if email phone number found send it to DB using API using update2 and apisndat.py file
    3. If website found send it using otherAPI update3 and apisndat.py file
'''
import re
import os

import pdb
import apisndat
new_contact=[]
number=[]
eml=[]
url_sc=[]
def fileReadWr():
    print("*"*40)
    f= open("oyt.txt", "r")
    if f.mode == "r":
        content = f.read()
        contents= cleanhtml(content)
        #print(contents)
        datafilter(contents)

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


''' In function datafilter() REGEX is used to filter PHONE NUMBER, WEBSITE LINK, EMAILS  from the traversed facebookpage
"contents" is the text container of each page'''

def datafilter(contents):
        try:
            if (
                contents.endswith('.gov') or
                contents.endswith('.org') or
                contents.endswithk.endswith('.net') or
                contents.endswith('.com') or
                contents.endswith('.in') or
                contents.endswith('.me')):
                eml.append(contents)
        except:        
            eml =re.findall(r'\w+@\w+\.{1}\w+', contents) 
        emails = list(set(eml))
        #phone number
        try:
            number =re.findall(r'[\+]{0,1}(\d{10,13}|[\(][\+]{0,1}\d{2,}[\13)]*\d{5,13}|\d{2,6}[\-]{1}\d{2,13}[\-]*\d{3,13})',contents)
        except: 
            pass   
        #unique number
        contact = list(set(number))
        #pdb.set_trace()
        #print(contact)
        #to filter indian numbers starting with +91,0 or ten digit which donot start from 1|2|3|
        for numbr in contact:      
            if (( len(numbr) < 13 or (numbr[0] == '+' or numbr[0]=='0')) and (numbr[0]!='1' and numbr[0]!='2'and numbr[0]!='3')):
                new_contact.append(numbr) 

        # print(new_contact)    
        #appending-websites
        try:
            url_sc = re.findall(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})',contents)
            websites = list(set(url_sc))
        except:
            pass
        updatedata(emails,new_contact)
        updatewebsite(websites)
        os.remove("oyt.txt")

def updatedata(emails,new_contact):
        api2_update=''
        phon=''
        emil=''
        urlink=''
        if len(new_contact) !=0:
            phon= (','.join(new_contact))
            phon ="&phone1=" + phon 

        if len(emails) != 0:
            emil = (','.join(emails))
            emil = "&email1=" + emil

        
            # urlink = (','.join(url))
        urlink = "&url1=" + "fb_url" 

        api2_update= phon + emil +urlink
        print(api2_update)   
        apisndat.new_api(api2_update)

def updatewebsite(websites):
        api3_update=''
        if len(websites) != 0:
            api3_update =(','.join(websites))
            api3_update = "&website=" + api3_update  
            print(api3_update)      
            apisndat.website_data_api(api3_update)   
            # '''    
         
     
if __name__ == "__main__":

    fileReadWr()  
