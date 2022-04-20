import random
import webbrowser
import pyautogui
import time
import csv 

dict = []

with open('dictionary.csv') as csvfile:    
	csvReader = csv.reader(csvfile)    
	for row in csvReader:        
		dict.append(row[0])
# Import a dictionary file for generating random words

while True:
    url = "https://engine.presearch.org/search?q="
    num = random.randint(1,10)
    words = ''
    # Prepare the string to be editted and opened, make sure you are signed in to your presearch account

    for i in range (0,num):
        word = random.choice(dict)
        url = url + '+' + word
    # Create a search term with random length and random words from the dictionary
    
    webbrowser.open_new_tab(url)
    time.sleep(2)
    pyautogui.hotkey('command', 'w')
    sleep_time = random.uniform(3, 10)
    time.sleep(sleep_time)
    # Open the search term in a new tab, close it, and wait for a random amount of time