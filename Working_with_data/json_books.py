import xml.dom.minidom as md
import json
from xml.dom import minidom
import xml.dom.minidom
import os

import csv 

def json_book():
    action=0
    while action!=4:
        file=open("Book_list.json","r")
        file_json=json.load(file)
        print("\nChoose the action: \n1.Display books\n2.Add new book\n3.Remove the book\n4.Exit")
        action=int(input("\nEnter the number from 1 to 4: "))
        if action==1:
            print("Information about books: ")
            pretty_json = json.dumps(file_json, indent=4)
            file.close()
            print(pretty_json)
            
        elif action==2:
            title=input("Enter the book's title:")
            author=input("Enter the book's author:")
            year=int(input("Enter the year of release date:"))
            informations = {"Title" : title, "Author" : author, "Year" : year}
            file_json['Books'].append(informations)
            with open('Book_list.json', 'w') as file:
                json.dump(file_json, file, indent=4)

        elif action==3:
            to_delate=input("Which book do you want to remove? Write a tittle of the book:")
            j=0
            for i in file_json['Books']:
                if i['Title'] == to_delate:
                    del file_json['Books'][j]
                j=j+1
            with open('Book_list.json', 'w') as file:
                json.dump(file_json, file, indent=4)
        else:
            break

json_book()