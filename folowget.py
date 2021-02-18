from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pickle
from pyautogui import scroll as s
from pyautogui import moveTo as m
PATH = r'D:\Python\Afilescodedbyme\Automator\chromedriver.exe'
driver= webdriver.Chrome(PATH)
oldfollowers=[]
newfollowers=[]
def configure(ame):
    global name
    name=ame
    print(name)
def login(email,password):
    driver.get("https://www.instagram.com/")
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")).send_keys(email)
    driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input").send_keys(password)
    driver.find_element_by_css_selector("#loginForm > div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div:nth-child(3) > button > div").click()
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")).click()

def getfollowers():
    #try:
     #   oldfollowers=pickle.load(open('followerlist/{}.pickle'.format(name),'rb'))
    #except:
     #   oldfollowers=[]
    #print(oldfollowers)
    driver.get("https://instagram.com/{}/".format(name)) 
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a")).click()

def getnewfollowers():
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name("g47SY").text)
    try:
        oldfollowers=pickle.load(open('followerlist/{}.pickle'.format(name),'rb'))
    except:
        oldfollowers=[]
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name("PZuss")) 
    x=-1
    m(673,534)
    while (True):
        try:
            x=x+1
            s(-60)
            WebDriverWait(driver, 5).until(lambda y: y.find_elements_by_class_name("_0imsa")[x])
            currentname=driver.find_elements_by_class_name("_0imsa")[x].text
            fsatate=binary_search(oldfollowers,currentname)
            if(fsatate=="false"):
                print(currentname,"is a new follower!")
                newfollowers.append(currentname)
        except:
            break

def binary_search(arr, elem):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2

        if arr[mid] < elem:
            low = mid + 1
        elif arr[mid] > elem:
            high = mid - 1
        else:
            return "true"
    return "false"
def save():
    oldfollowers.sort()
    print(newfollowers)
    
def message(name,message):
    driver.get("https://www.instagram.com/direct/inbox/") 
    WebDriverWait(driver, 5).until(lambda y: y.find_element_by_class_name("QBdPU").find_elements_by_class_name("_8-yf5")[0]).click()
    time.sleep(0.1)
    driver.find_elements_by_class_name("M5V28")[0].send_keys(name)
    WebDriverWait(driver, 5).until(lambda y: y.find_element_by_class_name("dCJp8 "))
    driver.find_elements_by_class_name("dCJp8 ")[0].click()
    driver.find_elements_by_class_name("rIacr")[0].click()       
    while True:
        try:
            driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN")
            time.sleep(0.1)
        except:
            break             
    WebDriverWait(driver, 5).until(lambda y: y.find_element_by_css_selector("#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea")).send_keys(message)     
    driver.find_element_by_css_selector("#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea").send_keys('\n')     
def messagefollowers(name,accname,password,messages):
    configure(name)
    login(accname,password)
    getfollowers()
    getnewfollowers()
    try:
        oldfollowers=pickle.load(open('followerlist/{}.pickle'.format(name),'rb'))
    except:
        oldfollowers=[]
    for names in newfollowers:
        time.sleep(0.5)
        oldfollowers.append(names)
        pickle.dump(oldfollowers,open("followerlist/{}.pickle".format(name),"wb"))
        message(names,messages)
        print(names,messages)
    save()
messagefollowers("shreyarao.music","vineethrao50@gmail.com","####","hello")
