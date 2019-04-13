__author__ = 'Kevin'

from tkinter import *
from tkinter import StringVar
from time import sleep
from urllib.request import urlopen
from urllib.request import URLError
from bs4 import BeautifulSoup
from selenium import webdriver
from splinter import Browser
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import datetime
from threading import Thread
import socket


try:
    f = open('essentialFiles\\file.dat','w')
    f.close()
    os.remove('essentialFiles\\file.dat')
except Exception as e:
    def closeWindow():
        noRightsWindow.destroy()
    noRightsWindow = Tk()
    noRightsWindow.resizable(width=False, height=False)
    noRightsWindow.title("Ultra Cop")
    noRightsWindow.geometry("200x80")
    failureLabel = Label(noRightsWindow, text="Must be used with Admin Rights.")
    failureLabel.place(relx=0.5, rely=0.25, anchor=CENTER)
    closeButton = Button(noRightsWindow, text="OK", command=closeWindow)
    closeButton.place(relx=0.5, rely=0.65, anchor=CENTER)
    noRightsWindow.mainloop()
    quit()


try: #Try to connect to the internet
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    ip = str(s.getsockname()[0])
    s.close()
except: #If can't connect to the internet...Quit
    def closeWindow():
        noInternetWindow.destroy()
    noInternetWindow = Tk()
    noInternetWindow.resizable(width=False, height=False)
    noInternetWindow.title("Ultra Cop")
    noInternetWindow.geometry("200x80")
    failureLabel = Label(text="Failed to connect to internet.")
    failureLabel.place(relx=0.5, rely=0.25, anchor=CENTER)
    closeButton = Button(text="OK", command=closeWindow)
    closeButton.place(relx=0.5, rely=0.65, anchor=CENTER)
    noInternetWindow.mainloop()
    quit()


try: #Try to open file with first IP address
    with open ("essentialFiles\\file.txt", "r") as myfile:
        data=myfile.readlines()
    savedIP = data[0][157:]
    if ip != savedIP:
        try:
            with open ("essentialFiles\\file2.txt", "r") as myfile:
                data=myfile.readlines()
            savedIP2 = data[0][157:]
            if ip != savedIP2:
                def closeWindow():
                    invalidIPWindow.destroy()
                invalidIPWindow = Tk()
                invalidIPWindow.resizable(width=False, height=False)
                invalidIPWindow.title("Ultra Cop")
                invalidIPWindow.geometry("200x80")
                failureLabel = Label(text="Only 2 IP addresses allowed to use bot.")
                failureLabel.place(relx=0.5, rely=0.25, anchor=CENTER)
                closeButton = Button(text="OK", command=closeWindow)
                closeButton.place(relx=0.5, rely=0.65, anchor=CENTER)
                invalidIPWindow.mainloop()
                quit()

        except:
            f = open('essentialFiles\\file2.txt','w')
            f.write("‹L$\‰‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ" + str(ip))
            f.close()

except Exception as e: # If the first IP address file is not present
    f = open('essentialFiles\\file.txt','w')
    f.write("‹L$\‰‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ‹L$\‰óÁÎ" + str(ip))
    f.close()

executable_path = "essentialFiles\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = executable_path
chrome_options = Options()
chrome_options.add_extension('autofill.crx')
driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
root = Tk()
root.resizable(width=False, height=False)
root.title("Ultra Cop")
root.geometry("400x525")
wait = WebDriverWait(driver, 1000)


keyword    = StringVar()
color      = StringVar()
size       = StringVar()
name       = StringVar()
email      = StringVar()
phone      = StringVar()
address    = StringVar()
address2   = StringVar()
address3   = StringVar()
zip        = StringVar()
city       = StringVar()
cc         = StringVar()
cvc        = StringVar()



def loadScreen():
    loadScreen = PhotoImage(file=r"images\\loading1.png")


    try:
        global screen
        screen = Label(root, image=loadScreen)
        screen.image = loadScreen
        screen.place(x=0, y=0)

    except Exception as e:
        pass

def newWindow():
    root.geometry("300x120")
    for widget in widgetList:
        widget.place_forget()
    finalItemLabel = Label(text="Keyword: " + keywordconfirm, fg="Red", font="-weight bold")
    finalItemLabel.place(x=20, y=20)
    finalColorLabel = Label(text="Color: " + colorconfirm, fg="Red", font="-weight bold")
    finalColorLabel.place(x=20, y=40)
    finalSizeLabel = Label(text="Size: " + sizeconfirm, fg="Red", font="-weight bold")
    finalSizeLabel.place(x=20, y=60)

    runButton = Button(text = "RUN", command = run)
    runButton.place(x = 250, y = 40)






def confirm():
    def fillInfo():
        global keywordconfirm
        keywordconfirm = keyword.get()
        global colorconfirm
        colorconfirm   = color.get()
        global sizeconfirm
        sizeconfirm    = listboxF.get(ACTIVE)
        global nameconfirm
        nameconfirm    = name.get()
        global emailconfirm
        emailconfirm   = email.get()
        global phoneconfirm
        phoneconfirm   = phone.get()
        global addressconfirm
        addressconfirm = address.get()
        global addressconfirm2
        addressconfirm2 = address2.get()
        global addressconfirm3
        addressconfirm3 = address3.get()
        global zipconfirm
        zipconfirm     = zip.get()
        global cityconfirm
        cityconfirm    = city.get()
        global stateconfirm
        stateconfirm   = listbox.get(ACTIVE)
        global ccTypeconfirm
        ccTypeconfirm  = listboxCC.get(ACTIVE)
        global ccconfirm
        ccconfirm      = cc.get()
        global monthconfirm
        monthconfirm   = listboxE.get(ACTIVE)
        global yearconfirm
        yearconfirm    = listboxE2.get(ACTIVE)
        global cvcconfirm
        cvcconfirm     = cvc.get()
        global styleconfirm
        styleconfirm   = listboxS.get(ACTIVE)


        card = 0
        if ccTypeconfirm == 'Visa':
            card = 0
        elif ccTypeconfirm == 'American Express':
            card = 1
        elif ccTypeconfirm == 'Mastercard':
            card = 2
        driver.get('chrome-extension://nlmmgnhgdeffjkdckmikfpnddkbbfkkk/options.html')
        while True:
            try:
                driver.find_element_by_id('button-close').click()
                break
            except:
                pass

        entrynumber = 0
        entryType = ['^order\[billing_name\]$', '^order\[email\]$', '^order\[tel\]$', '^order\[billing_address\]$', '^order\[billing_address_2\]$',
                     '^order\[billing_address_3\]$', '^order\[billing_zip\]$', '^order\[billing_city\]$', '^credit_card\[cnb\]$', '^credit_card\[vval\]$',
                     '^order\[billing_state\]$', '^credit_card\[month\]$', '^credit_card\[type\]$']
        entryConfirm = [nameconfirm, emailconfirm, phoneconfirm, addressconfirm, addressconfirm2, addressconfirm3, zipconfirm, cityconfirm, ccconfirm,
                        cvcconfirm, stateconfirm, monthconfirm, card]

        while entrynumber != 13:
            entrynumber += 1
            while True:
                try:
                    driver.find_element_by_id("button-add").click()
                    break
                except:
                    pass
            driver.find_element_by_id("n_" + str(entrynumber)).send_keys(entryType[entrynumber - 1])
            driver.find_element_by_id("v_" + str(entrynumber)).send_keys(entryConfirm[entrynumber - 1])
            driver.find_element_by_id("s_" + str(entrynumber)).send_keys("supremenewyork.com")

            if entryType[entrynumber - 1] == "^credit_card\[type\]$" or entryType[entrynumber - 1] == "^credit_card\[month\]$"\
                    or entryType[entrynumber - 1] == "^credit_card\[year\]$" or entryType[entrynumber - 1] == "^order\[billing_state\]$":
                Select(driver.find_element_by_id('t_' + str(entrynumber))).select_by_visible_text('Select')

        driver.find_element_by_id("button-save").click()
        driver.get("http://www.supremenewyork.com/shop/all")

        sleep(1)

        screen.destroy()

        newWindow()



    fillThread = Thread(target=fillInfo)
    fillThread.start()

    gifThread = Thread(target=loadScreen)
    gifThread.start()



def run():

    def chooseYear():
        while True:

            try:
                Select(driver.find_element_by_id("credit_card_year")).select_by_visible_text(str(yearconfirm))
            except:
                pass


    def accessoriesScrape():
        while True:
            html = connectToSupreme("accessories")
            soup = BeautifulSoup(html, 'html.parser')
            tableStats = soup.findAll('h1')
            for section in tableStats:
                section = cleanCode(section)
                if keywordconfirm in section:
                    link = section[36:]
                    link = link[:32]
                    link = "http://supremenewyork.com/shop" + link


                    if len(colorconfirm) > 0:
                        colorPick = Thread(target=colorCheck(link))
                        colorPick.start()
                    else:
                        driver.get(link)
                        checkoutThread = Thread(target=checkout)
                        checkoutThread.start()
                    return

    def pantsScrape():
        while True:
            html = connectToSupreme("pants")
            soup = BeautifulSoup(html, 'html.parser')
            tableStats = soup.findAll('h1')
            for section in tableStats:
                section = cleanCode(section)
                if keywordconfirm in section:
                    link = section[36:]
                    link = link[:30]
                    link = "http://supremenewyork.com/shop" + link
                    link = link.strip('"')


                    if len(colorconfirm) > 0:
                        colorPick = Thread(target=colorCheck(link))
                        colorPick.start()
                    else:
                        driver.get(link)
                        checkoutThread = Thread(target=checkout)
                        checkoutThread.start()
                    return

    def shirtsScrape():
        while True:
            html = connectToSupreme("shirts")
            soup = BeautifulSoup(html, 'html.parser')
            tableStats = soup.findAll('h1')
            for section in tableStats:
                section = cleanCode(section)
                if keywordconfirm in section:
                    link = section[36:]
                    link = link[:27]
                    link = "http://supremenewyork.com/shop" + link
                    link = link.strip('"')

                    if len(colorconfirm) > 0:
                        colorPick = Thread(target=colorCheck(link))
                        colorPick.start()
                    else:
                        driver.get(link)
                        checkoutThread = Thread(target=checkout)
                        checkoutThread.start()
                    return

    def tshirtscrape():
        while True:
            html = connectToSupreme("t-shirts")
            soup = BeautifulSoup(html, 'html.parser')
            tableStats = soup.findAll('h1')
            for section in tableStats:
                section = cleanCode(section)
                if keywordconfirm in section:
                    link = section[36:]
                    link = link[:29]
                    link = "http://supremenewyork.com/shop" + link
                    link = link.strip('"')

                    if len(colorconfirm) > 0:
                        colorPick = Thread(target=colorCheck(link))
                        colorPick.start()
                    else:
                        driver.get(link)
                        checkoutThread = Thread(target=checkout)
                        checkoutThread.start()
                    return

    def jacketscrape():
        while True:
            html = connectToSupreme("jackets")
            soup = BeautifulSoup(html, 'html.parser')
            tableStats = soup.findAll('h1')
            for section in tableStats:
                section = cleanCode(section)
                if keywordconfirm in section:
                    link = section[36:]
                    link = link[:29]
                    link = "http://supremenewyork.com/shop" + link
                    link = link.strip('"')

                    if len(colorconfirm) > 0:
                        colorPick = Thread(target=colorCheck(link))
                        colorPick.start()
                    else:
                        driver.get(link)
                        checkoutThread = Thread(target=checkout)
                        checkoutThread.start()
                    return

    def sweatshirtscrape():
        while True:
            html = connectToSupreme("sweatshirts")
            soup = BeautifulSoup(html, 'html.parser')
            tableStats = soup.findAll('h1')
            for section in tableStats:
                section = cleanCode(section)
                if keywordconfirm in section:
                    link = section[36:]
                    link = link[:32]
                    link = "http://supremenewyork.com/shop" + link
                    link = link.strip('"')

                    if len(colorconfirm) > 0:
                        colorPick = Thread(target=colorCheck(link))
                        colorPick.start()
                    else:
                        driver.get(link)
                        checkoutThread = Thread(target=checkout)
                        checkoutThread.start()
                    return

    def topsweatersscrape():
        while True:
            html = connectToSupreme("tops_sweaters")
            soup = BeautifulSoup(html, 'html.parser')
            tableStats = soup.findAll('h1')
            for section in tableStats:
                section = cleanCode(section)
                if keywordconfirm in section:
                    link = section[36:]
                    link = link[:34]
                    link = "http://supremenewyork.com/shop" + link
                    link = link.strip('"')

                    if len(colorconfirm) > 0:
                        colorPick = Thread(target=colorCheck(link))
                        colorPick.start()
                    else:
                        driver.get(link)

                    return

    def connectToSupreme(type):
        attemptCount = 0
        while True:
            try:
                html = urlopen('http://www.supremenewyork.com/shop/all/' + type, timeout=1.5)
                return html
            except:
                attemptCount += 1

    def cleanCode(dirtyHTML):
        cleanHTML = str(dirtyHTML).replace("<", " ").replace(">", " ")
        return cleanHTML

    def colorCheck(itemLink):
        while True:
            try:
                    html = urlopen(itemLink, timeout=5)
                    break
            except:
                    pass

        soup = BeautifulSoup(html, 'html.parser')
        tableStats = soup.findAll('a')
        for section in tableStats:
            color = str(section)
            color = color.replace('"', " ")

            if colorconfirm in color:
               colorlink = section['href']
               checkoutThread = Thread(target=checkout)
               checkoutThread.start()
               driver.get('http://supremenewyork.com' + colorlink)


    def sizePick():
        triedSize = False
        while True:
            try:
                if sizeconfirm == "No Size":
                    break
                if sizeconfirm == "Small":
                    driver.find_element_by_xpath("//select[@id='size']/option[text()='Small']").click()
                    break
                if sizeconfirm == "Medium":
                    driver.find_element_by_xpath("//select[@id='size']/option[text()='Medium']").click()
                    break
                if sizeconfirm == "Large":
                    driver.find_element_by_xpath("//select[@id='size']/option[text()='Large']").click()
                    break
                if sizeconfirm == "XLarge":
                    driver.find_element_by_xpath("//select[@id='size']/option[text()='XLarge']").click()
                    break
                if sizeconfirm == "34":
                    driver.find_element_by_xpath("//select[@id='size']/option[text()='34']").click()
                    return
            except:
                if triedSize == False:
                    triedSize = True
                    pass


    def checkout():
        sleep(0.25)
        sizePick()
        triedToAdd = False
        while True:
            try:
                driver.find_element_by_xpath(".//*[@value='add to cart']").click()
                WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='cart-remove']/fieldset[1]/b")))
                driver.find_element_by_xpath(".//*[@id='cart-remove']/fieldset[1]/b").click()
                break
            except Exception as e:
                try:
                    driver.find_element_by_xpath(".//*[@id='add-remove-buttons']/input").click()
                    break
                except:
                    sleep(1)
                    pass
                if triedToAdd == False:
                    triedToAdd = True

        triedToGo = False
        while True:
            try:
                driver.find_element_by_xpath(".//*[@id='cart']/a[2]").click()
                break
            except:
                if triedToGo == False:
                    triedToGo = True

        try:
            driver.find_element_by_xpath(".//*[@id='cart-cc']/fieldset/p[2]/label/div/ins").click()
        except:
            driver.find_element_by_xpath(".//*[@id='cart-cc']/fieldset/p/label/div/ins").click()

        autoFill = Thread(target=chooseYear)
        autoFill.start()

        sleep(1.1)

        while True:
            try:
                driver.find_element_by_xpath(".//*[@id='pay']/input").click()
                break
            except:
                pass

    root.withdraw()

    if styleconfirm == "T-Shirts":
        tshirtscrape()

    if styleconfirm == "Jackets":
        jacketscrape()

    if styleconfirm == "Sweatshirts":
        sweatshirtscrape()

    if styleconfirm == "Tops/Sweaters":
        topsweatersscrape()

    if styleconfirm == "Pants":
        pantsScrape()

    if styleconfirm == "Shirts":
        shirtsScrape()

    if styleconfirm == "Accessories":
        accessoriesScrape()


confirmButton = Button(text = "CONFIRM", command = confirm)
confirmButton.place(x = 325, y = 475)


itemNameLabel = Label(text = "Keyword")
itemNameLabel.place(x=10,y = 20)
itemNameEntry = Entry(width = 15, textvariable = keyword)
itemNameEntry.place(x = 75, y = 22)


colorLabel    = Label(text = "Color")
colorLabel.place(x = 200, y = 20)
colorEntry    = Entry(width = 15, textvariable = color)
colorEntry.place(x = 250, y =22)

sizeLabel     = Label(text = "Size")
sizeLabel.place(x = 10, y = 70)


nameLabel    = Label(text = "Name")
nameLabel.place(x=200,y = 70)
nameEntry    = Entry(width = 15, textvariable = name)
nameEntry.place(x = 250, y = 72)

emailLabel   = Label(text = "Email")
emailLabel.place(x=10,y = 120)
emailEntry   = Entry(width = 15, textvariable = email)
emailEntry.place(x=75, y=122)

phoneLabel   = Label(text = "Phone")
phoneLabel.place(x=200,y = 120)
phoneEntry   = Entry(width = 15, textvariable = phone)
phoneEntry.place(x=250,y = 122)

addressLabel = Label(text = "Address")
addressLabel.place(x = 10, y = 170)
addressEntry = Entry(width = 15, textvariable = address)
addressEntry.place(x = 75, y=172)
addressEntry2 = Entry(width = 15, textvariable = address2)
addressEntry2.place(x = 75, y=192)
addressEntry3 = Entry(width = 15, textvariable = address3)
addressEntry3.place(x = 75, y=212)

zipLabel     = Label(text = "Zip")
zipLabel.place(x = 200, y = 170)
zipEntry     = Entry(width = 15, textvariable = zip)
zipEntry.place(x = 250, y =172)

cityLabel    = Label(text = "City")
cityLabel.place(x = 10, y = 260)
cityEntry = Entry(width = 15, textvariable = city)
cityEntry.place(x = 75, y = 262)

stateLabel   = Label(text = "State")
stateLabel.place(x = 200, y = 260)

ccTypeLabel  = Label(text = "CC Type")
ccTypeLabel.place(x = 10, y = 310)

ccnumberLabel= Label(text = "CC#")
ccnumberLabel.place(x = 200, y =310)
ccnumberEntry= Entry(width = 15, textvariable = cc)
ccnumberEntry.place(x = 250, y = 312)

expDateLabel = Label(text = "Exp. Date")
expDateLabel.place(x = 10, y = 360)

cvcLabel     = Label(text = "CVC")
cvcLabel.place(x = 10, y = 410)
cvcEntry     = Entry(width = 15, textvariable = cvc)
cvcEntry.place(x = 75, y = 412)

styleLabel   = Label(text = "Style")
styleLabel.place(x = 200, y = 410)

listboxF = Listbox(height = 1, width = 15) #Size
listboxF.insert(1, "No Size")
listboxF.insert(2, "Small")
listboxF.insert(3, "Medium")
listboxF.insert(4, "Large")
listboxF.insert(5, "XLarge")
listboxF.insert(6, "28")
listboxF.insert(7, "30")
listboxF.insert(8, "32")
listboxF.insert(9, "34")
listboxF.place(x = 75, y = 72)

listboxS  = Listbox(height = 1, width = 20) #STYLE
listboxS.insert(1, "Jackets" )
listboxS.insert(2, "Shirts")
listboxS.insert(3, "Tops/Sweaters")
listboxS.insert(4, "Sweatshirts")
listboxS.insert(5, "Pants")
listboxS.insert(6, "T-Shirts")
listboxS.insert(7, "Hats")
listboxS.insert(8, "Accessories")
listboxS.place(x = 250, y = 412)

listboxE = Listbox(height = 1, width = 4) #MONTH
listboxE.insert(1, "01")
listboxE.insert(2, "02")
listboxE.insert(3, "03")
listboxE.insert(4, "04")
listboxE.insert(5, "05")
listboxE.insert(6, "06")
listboxE.insert(7, "07")
listboxE.insert(8, "08")
listboxE.insert(9, "09")
listboxE.insert(10, "10")
listboxE.insert(11, "11")
listboxE.insert(12, "12")
listboxE.place(x = 75, y = 362)

listboxE2 = Listbox(height = 1, width = 6) #YEAR
listboxE2.insert(1, "2016")
listboxE2.insert(2, "2017")
listboxE2.insert(3, "2018")
listboxE2.insert(4, "2019")
listboxE2.insert(5, "2020")
listboxE2.insert(6, "2021")
listboxE2.insert(7, "2022")
listboxE2.insert(8, "2023")
listboxE2.insert(9, "2024")
listboxE2.place(x = 200, y = 362)

listboxCC = Listbox(height = 1, width = 17) #CC Type
listboxCC.insert(1, "Visa")
listboxCC.insert(2, "American Express")
listboxCC.insert(3, "Mastercard")
listboxCC.place(x = 75, y =312)

listbox = Listbox(height = 1, width = 10) #states
listbox.place(x = 250, y = 262)
listbox.insert(1, "AL")
listbox.insert(2, "AK")
listbox.insert(3, "AZ")
listbox.insert(4, "AR")
listbox.insert(5, "CA")
listbox.insert(6, "CO")
listbox.insert(7, "CT")
listbox.insert(8, "DE")
listbox.insert(9, "FL")
listbox.insert(10, "GA")
listbox.insert(11, "HI")
listbox.insert(12, "ID")
listbox.insert(13, "IL")
listbox.insert(14, "IN")
listbox.insert(15, "IA")
listbox.insert(16, "KS")
listbox.insert(17, "KY")
listbox.insert(18, "LA")
listbox.insert(19, "ME")
listbox.insert(20, "MD")
listbox.insert(21, "MA")
listbox.insert(22, "MI")
listbox.insert(23, "MN")
listbox.insert(24, "MS")
listbox.insert(25, "MO")
listbox.insert(26, "MT")
listbox.insert(27, "NE")
listbox.insert(28, "NV")
listbox.insert(29, "NH")
listbox.insert(30, "NJ")
listbox.insert(31, "NM")
listbox.insert(32, "NY")
listbox.insert(33, "NC")
listbox.insert(34, "ND")
listbox.insert(35, "OH")
listbox.insert(36, "OK")
listbox.insert(37, "OR")
listbox.insert(38, "PA")
listbox.insert(39, "RI")
listbox.insert(40, "SC")
listbox.insert(41, "SD")
listbox.insert(42, "TN")
listbox.insert(43, "TX")
listbox.insert(44, "UT")
listbox.insert(45, "VT")
listbox.insert(46, "VA")
listbox.insert(47, "WA")
listbox.insert(48, "WV")
listbox.insert(49, "WI")
listbox.insert(50, "WY")

root.iconbitmap('essentialFiles\\icon.ico')

widgetList = [confirmButton, itemNameLabel, itemNameEntry, colorLabel, colorEntry, sizeLabel, nameLabel, nameEntry,
              emailEntry, emailLabel, phoneLabel, phoneEntry, addressLabel, addressEntry, addressEntry2, addressEntry3,
              zipLabel, zipEntry, cityLabel, cityEntry, stateLabel, listbox, listboxF]

root.mainloop()
quit()