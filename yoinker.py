from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.common.exceptions
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
    def yoinkbot(self, linksies,range_limiter): #Για την ώρα, αποθηκεύει όλο το html των υποσελίδων με τις μεμονωμένες εργασίες.
        textlist = []
        for i in range(2,range_limiter):
            sneakystring = ''
            pinakion = '//*[@id="content"]/div[3]/div/div[1]/table/tbody/tr[{}]/td[2]/strong/a'.format(i) #μεταβλητό xpath, κάντε το google search αν δεν ξέρετε τι είναι
            pinakas = self.currentBrowser.find_element(By.XPATH, pinakion) #το browser δεν έχει οριστεί, θα γίνει self.currentBrowser όταν μπει στο class, ΜΗΝ ΤΟ ΤΡΕΞΕΤΕ ΑΚΟΜΑ
            pinakas.send_keys(Keys.RETURN)
            for i in range(1,8):
                mplhrofories = '//*[@id="content"]/div[3]/table/tbody/tr[{}]/td[1]'.format(i)
                mpinakas = '//*[@id="content"]/div[3]/table/tbody/tr[{}]/td[2]'.format(i) #ξανά, μεταβλητό XPATH
                try:
                    infokeimeno = self.currentBrowser.find_element(By.XPATH, mplhrofories).text
                    if 'Title:' in infokeimeno:infokeimeno = infokeimeno.replace('Title:', 'Τίτλος:')
                    elif 'Other Titles:' in infokeimeno:infokeimeno = infokeimeno.replace('Other Titles:', 'Τίτλος (Μετάφραση):')
                    elif 'Authors:' in infokeimeno:infokeimeno = infokeimeno.replace('Authors:', 'Συγγραφέας:')
                    elif 'Keywords:' in infokeimeno:infokeimeno = infokeimeno.replace('Keywords:', 'Λέξεις Κλειδιά:')
                    elif 'Keywords (translated):' in infokeimeno:infokeimeno = infokeimeno.replace('Keywords (translated):', 'Λέξεις Κλειδιά (Μετάφραση):')
                    elif 'Abstract:' in infokeimeno:infokeimeno = infokeimeno.replace('Abstract:', 'Περίληψη:')
                    elif 'Abstract (translated):' in infokeimeno:infokeimeno = infokeimeno.replace('Abstract (translated):', 'Περίληψη (Μετάφραση) :')   
                    if 'Τμήμα' and '(ΜΔΕ)' not in self.currentBrowser.find_element(By.XPATH, mpinakas).text: sneakystring += (infokeimeno + '///' + self.currentBrowser.find_element(By.XPATH, mpinakas).text + '\t')#εδώ βάζουμε στη λίστα textlist το κείμενο που παίρνουμε από το element το οποίο εντοπίσαμε με το μεταβλητό XPATH
                    else: sneakystring += 'Δε βρέθηκε άλλο στοιχείο\t'
                except selenium.common.exceptions.NoSuchElementException:
                    sneakystring += 'Δε βρέθηκε τέτοιο στοιχείο\t'
            sneakystring += ('Σύνδεσμος εργασίας:///' + self.currentBrowser.find_element(By.XPATH,'//*[@id="content"]/div[3]/div[2]/table/tbody/tr[2]/td[1]/a').get_attribute('href'))
            self.currentBrowser.get(linksies)
            textlist.append(sneakystring)
        return(textlist)
    def beginYoink(self): #ετοιμάζει τη λίστα με το κείμενο που θα στείλουμε στα sql bois
       self.currentBrowser.get(self.l1nk)
       self.currentBrowser.minimize_window()
       psopsontent = self.currentBrowser.page_source #να μην τα ξαναπώ, πασάρει στο bs4 το source
       rangesoup = BeautifulSoup(psopsontent)
       rangetext = str(rangesoup.get_text())
       rangelist = [] #αυτό το θέλουμε για να πάρουμε το νούμερο που θα οριοθετήσει την κλεψά
       l0ine = tuple(rangetext.split('\n')) #γραμμές του text.
       for i in l0ine:
            if 'Φθίνουσα σειρά' in i and 'Descending order' not in i or 'Φθίνουσα σειρά' not in i and 'Descending order' in i:
                i = i.split(' ')
                rangelist.extend(i)       
       maxrange =  int(rangelist[-1])
       if type(maxrange/20) != int: rangeOp = maxrange//20 + 1
       else: rangeOp = maxrange/20
       masterlist = []
       for i in range(rangeOp + 1):#ΚΑΠΟΥ ΣΤΟ HTML ΒΓΑΖΕΙ ERROR, ΒΡΕΙΤΕ ΤΙ ΦΤΑΙΕΙ ΚΑΙ ΦΤΙΑΞΤΕ ΤΟ ΠΛΣ ΘΕΛΩ ΝΑ ΑΥΤ
           lynk = self.l1nk + '?offset={}'.format(20*(i))
           if maxrange - 20*i >=20: powerRanger = 22 #Το powerRanger είναι στην ουσία ο αριθμός των στοιχείων που πρέπει να βουτήξουμε, το έκανα έτσι γιατί κουράστηκα να φτιάχνω σούπες,
           else: powerRanger = maxrange - 20*i +2
           masterlist.extend(self.yoinkbot(lynk, powerRanger))
       return masterlist
    