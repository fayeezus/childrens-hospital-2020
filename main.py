import random
import colorama
from colorama import Fore, Back
from seleniumwire import webdriver
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#catchall = input("Catchall: ") #enter your catchall domain
colorama.init(autoreset=True)

#PROXY = (random.choice(list(open('proxies.txt'))))
while True:

    print(Fore.CYAN + "Starting Browser")
    first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria', 'Alfonso','Mannix','Peter','Dante','Deborah','Xanthus','Lester','Jolie','Forrest','Orli','Adele','Shad','Mufutau','Hamish','Kirk','Wesley','Shad','Candace','Zachery','Maxine','Candace','Fitzgerald','Blythe','Margaret','Drew','Sawyer','Nomlanga','Ulla','Daniel','Ethan','Clayton','Veda','Yasir','Ashely','Mufutau','Leo','Flavia','Dante','Brielle','Nell','Ariana','Ashely','Jason','Patrick','Brennan','Mallory','Hyatt','Reuben','Uta','Althea','Mara','Megan','Lara','Jena','Carissa','September','Courtney','Pearl','Joelle','Chloe','Charles','Sigourney','Lyle','Ashton','Nell','Giacomo','Jemima','Brandon','Elmo','Lois','Brody','Malcolm','Blair','Gisela','Orson','Lila','Madeson','Dustin','Plato','Pearl','Althea','Slade','Iris','Burton','Dahlia']
    last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
    first = random.choice(first_names)
    last = random.choice(last_names)
    options = Options()
    options.add_argument('ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--enable-javascript")
    options.add_argument("incognito")
 #   options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome("C:/Users/User/Desktop/2020Valentines/chromedriver", options=options)
    driver.get("https://secure1.chla.org/site/SPageNavigator/2020_Valentines.html")
    #driver.set_window_position(0,0)
    #driver.set_window_size(500,500)
    print(Fore.RED + Back.BLACK + "Children's Hospital LA 2020 Valentines Script by Fayeezus")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/main/section/div/form/div[1]/div[2]/ul/li[1]').click()
    #first name
    fn = driver.find_element_by_xpath('//*[@id="cons_first_name"]')
    fn.send_keys(first)
    print(Fore.CYAN + "Using first name: " + Fore.GREEN + first) 
    #last name
    ln = driver.find_element_by_xpath('//*[@id="cons_last_name"]')
    ln.send_keys(last)
    print(Fore.CYAN + "Using last name: " + Fore.GREEN + last)
    #emails
    data = (random.choice(list(open('emails.txt'))))
    x11 = driver.find_element_by_xpath('//*[@id="cons_email"]')
    x11.send_keys(data)
    print(Fore.CYAN + "Using Email: " + Fore.GREEN + data)

    time.sleep(2)
    #message
    #message = (random.choice(list(open('message.txt'))))
    #sendmessage = driver.find_element_by_xpath('/html/body/main/section/div/form/div[2]/div[2]/div/div[3]/label/textarea')
    #sendmessage.send_keys(message)
 #   driver.find_element_by_xpath('//*[@id="ACTION_SUBMIT_SURVEY_RESPONSE"]').click()
    time.sleep(2)
    print(Fore.CYAN + "Successfully sent a Card with email: " + Fore.GREEN + data) 

    driver.quit()