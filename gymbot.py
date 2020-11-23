import os
import sys
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": "C:/Users/Michael/MLS", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
browser = webdriver.Chrome(os.path.join(sys.path[0], 'chromedriver'), options=options)

def login(username, password):
    
    login_url = 'https://myfit4less.gymmanager.com/portal/login.asp'
    browser.get(login_url)
    username_css = browser.find_element_by_css_selector('#emailaddress')
    username_css.send_keys(username)
    password_css = browser.find_element_by_css_selector('#password')
    password_css.send_keys(password)
    browser.find_element_by_css_selector('#loginButton').click()
    time.sleep(7)


def navigate(select_times):
    '''
    navigates through the page and books an appointment with your desired time.
    param: select_times - array of size 3
    insert the desired times as a string in an array in order of preference e.g. ["4:00 PM". "5:00PM", "7:00AM"]
    '''
    time.sleep(3)
    # browser.find_element_by_xpath('//*[(@id = "btn_date_select")]').click() # don't know why css isn't working lol
    element = browser.find_element_by_css_selector("#btn_date_select")
    browser.execute_script("arguments[0].click();", element)
    time.sleep(3)
    date = (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d')
    browser.find_element_by_css_selector('#date_'+ date ).click() # picks a date 2 days in the future
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    slots = soup.find_all("div", {"class": "time-slot-data-line"})
    print(slots)
    my_times = ["at " + s for s in select_times]
    id_tag = None
    found_first = False
    found_second = False
    for idx,slot in enumerate(slots): # check if first preference is found. If not try the next preference
        if slot.text == my_times[0]:
            id_tag = slots[idx].parent.parent.get('id')
            print('You got a booking at', my_times[0])
            found_first = True
            break
    if not (found_first or found_second): # check if second preference is found. If not try the third preference
        for idx,slot in enumerate(slots):
            if slot.text == my_times[1]:
                id_tag = slots[idx].parent.parent.get('id')
                print('You got a booking at', my_times[1])
                found_second = True
                break

    if not (found_first or found_second):
        for idx,slot in enumerate(slots):
            if slot.text == my_times[2]:
                id_tag = slots[idx].parent.parent.get('id')
                print('You got a booking at', my_times[2])
                found_second = True
                break
    if id_tag:
        browser.find_element_by_id(id_tag).click()
    else:
        print("Couldn't find a booking :(")
    time.sleep(2)
    element = browser.find_element_by_css_selector("#dialog_book_yes")
    browser.execute_script("arguments[0].click();", element)

if __name__ == "__main__":
    print("Starting bot...")
    login('username','password') # enter your credentials to log into myfit4less
    print("You sir (or madam) are logged in and ready to book")
    navigate(["7:00 AM", "8:00 AM", "8:00 PM"]) # insert the time you wanna book for