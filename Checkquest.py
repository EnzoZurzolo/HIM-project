# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:43:45 2023

@author: EZ2
"""



import requests  # python3.10 -m pip install requests
import csv

def read_csv_from_internet(url):
    response = requests.get(url)
    lines = response.text.splitlines()
    reader = csv.reader(lines)
    return reader

def check_question_type(url,lign):
    
    reader = read_csv_from_internet(url) 
    c=0
    for row in reader:
        print(row[0])
        if c == lign:
            if row[0]== 'radio':
                return 1
                print("radio")
            elif  row[0]== 'checkbox':
                return 2
                print ("checkbox")
            elif  row[0]== 'text':
                return 3
                print('text')
        elif c == row[-1]:
            return 4
        else :
            c+=1

# Replace with the actual CSV file URL
#csv_url = "https://raw.githubusercontent.com/devw/spen/main/src/Multiple-Choice-Quiz.csv"
#read_csv_from_internet(csv_url) 

#check_question_type(csv_url,1)
