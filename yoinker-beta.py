import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class MasterYoinker(): #το κύριο class για να αρχίζει το scraping
    def __init__(self, browser_input, l1nk, currentBrowser = '' ):
        if browser_input == 'Chrome': self.currentBrowser = webdriver.Chrome() #από δω και κάτω ετοιμάζουμε browsers που υποστηρίζονται
        elif browser_input == 'Firefox': self.currentBrowser = webdriver.Firefox()
        elif browser_input == 'Edge': self.currentBrowser = webdriver.Edge()
        elif browser_input == 'Opera': self.currentBrowser = webdriver.Opera()
        elif browser_input == 'Safari': self.currentBrowser = webdriver.Safari()
        self.l1nk = l1nk # το link του site από nemertes που θέλουμε να ζουλέψουμε, για όποιον κάνει τη main
    def beginYoink(self): #μέχρι στιγμής δοκίμαζα πώς να αυτοματοποιήσουμε ως πού θα βουτάμε το html
        self.currentBrowser.get(self.l1nk)
        rangesource = self.currentBrowser.find_element(By.CLASS_NAME,'browse_range')
        rangesoup = BeautifulSoup(rangesource)
        rangetext = str(rangesoup.get_text())
        rangetup = tuple(rangetext.split(' '))
        

        return rangetup(-1) 

print(MasterYoinker('Chrome','https://nemertes.library.upatras.gr/jspui/handle/10889/65').beginYoink()) #έμεινε από το test, αν λυθεί το πρόβλημα του range πρέπει να πάει στο διάολο


        
    



for i in range(2,22): #χύμα κώδικας που πρέπει να ενσωματωθεί στο class αργότερα, γι' αυτό συμφέρει να το βάλετε σε κανα notepad αν δεν υπάρχει vscode. Αποθηκεύει όλο το html των υποσελίδων με τις μεμονωμένες εργασίες.
    pinakion = '//*[@id="content"]/div[3]/div/div[1]/table/tbody/tr[{}]/td[2]/strong/a'.format(i)
    pinakas = browser.find_element(By.XPATH, pinakion) #το browser δεν έχει οριστεί, θα γίνει self.currentBrowser όταν μπει στο class, ΜΗΝ ΤΟ ΤΡΕΞΕΤΕ ΑΚΟΜΑ
    pinakas.send_keys(Keys.RETURN)
    psontent = browser.page_source
    soupa = BeautifulSoup(psontent)
    print(soupa.prettify)
    browser.get('https://nemertes.library.upatras.gr/jspui/handle/10889/65')
   