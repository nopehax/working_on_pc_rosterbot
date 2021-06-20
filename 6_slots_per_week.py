#! python3

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import ctypes

driver_path = "D:/Downloads/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
user = 'Hca-98933600'
password = '0923-Vcs'
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


next_month = 'Jul'
result = ''
got_it = False

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--headless")
option.add_argument('--log-level=3')
option.add_argument('--incognito')

browser = webdriver.Chrome(executable_path=driver_path, options=option)
browser.get("https://abs.rafflesmedical.com.sg/eroster")


def ok():
    ok_btn = browser.find_element_by_id('btn-ok')
    ok_btn.click()


def main():
    
    user_element = browser.find_element_by_name("userId")
    user_element.send_keys(user)

    pass_element = browser.find_element_by_name("password")
    pass_element.send_keys(password)

    location = Select(browser.find_element_by_name('Cluster_Id'))
    location.select_by_value('3')

    login = browser.find_element_by_css_selector('button')
    login.click()

    ok()


def check():
    global result
    tab = []
    table = browser.find_elements_by_tag_name("td")
    for cell in table:
        word = cell.text.split()
        for i in word:
            if i in MONTHS:
                tab.append(i)
    print(tab)
    
    if next_month in tab:
        print("E-Roster slots for %s are open!" % next_month)
        return True
    elif not tab:
        return True
    else:
        print("E-Roster slots for %s has not been released" % next_month)
        return False


def chope():
    global got_it
    choped = 0

    browser.refresh()
    ok()
    
    time.sleep(0.5)
    try:
        box = browser.find_elements_by_xpath("//tr")
    except NoSuchElementException:
        print('no checkbox found???')
        got_it = True
        return
    
    
    for each in box:
        wanted_row = each.find_elements_by_tag_name("td")
        date = wanted_row[0].text
        day = date[date.find("(")+1:date.find(")")]
        if day in DAYS:
            checkbox = wanted_row[1].find_elements_by_xpath(".//*")[0]
            if not checkbox.is_selected() and checkbox.is_enabled():
                checkbox.click()                
                choped += 1
                print('Open slot selected')

    if choped != 0:
        submit = browser.find_element_by_id('btnSubmit')
        submit.click()

        time.sleep(0.5)
        obj = browser.switch_to.alert
        print(obj.text)
        obj.accept()
        time.sleep(0.5)
        ok()
        got_it = True
        print("Yay, %d slot(s) has been choped for you!" % choped)
        ctypes.windll.user32.MessageBoxW(0, "Pls check the slot(s) booked", "ALERT", 0)
    else:
        print('nothing')


def exit():
    browser.get("https://abs.rafflesmedical.com.sg/eroster/Account/Logout")
    browser.quit()


main()
time.sleep(0.5)             #idk why i have to put this buffer, but if i don't, then at times it will give an empty array
check()
while got_it == False:
    chope()
    time.sleep(5)
exit()
