import tkinter as tk
from PIL import ImageTk, Image, ImageSequence
from tkinter import *
from tkinter import messagebox,ttk
import threading
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions

def suma():


    root = tk.Tk()
    #root.config(bg='#000000')
    root.iconbitmap('C:\Program Files (x86)\icon.ico')
    root.title("team33")

    options = ["Chrome", "Mozilla", "Opera", "Edge", "Safari"]

    clicked = tk.StringVar()
    clicked.set("   browsers  ")# auto den typwnetai
    drop = tk.OptionMenu(root, clicked, *options)
    brr = tk.Label(root,text="Επιλέξτε Browser",font=("",15)).pack(anchor='n',expand=1)#fg="#FFFFFF",bg="#000000"
    #imAgin = tk.PhotoImage(file="C:\Program Files (x86)\lrower-logos.png") #error den vriskei eikona
    #lAbel = tk.Label(root,image=imAgin).pack()
    drop.pack(expand=1)

    def messagi():
        if  clicked.get()!= "Chrome" and clicked.get()!="Mozilla" and clicked.get()!="Opera" and clicked.get()!="Edge" and clicked.get()!="Safari" :
            response=messagebox.showwarning("mess","Παρακαλώ επιλέξτε browser!\n\t✧٩(•́⌄•́๑)و ✧")
    


    class MasterYoinker():  # το κύριο class για να αρχίζει το scraping
        def __init__(self, browser_input, l1nk, currentBrowser=''):
            PATH = "C:\Program Files (x86)\chromedriver.exe"
            PATH1 = "C:\Program Files (x86)\geckodriver.exe"
            PATH2 = "C:\Program Files (x86)\msedgedriver.exe"
            PATH3 = "C:\Program Files (x86)\operadriver.exe"
            PATH4 = "C:\Program Files (x86)\safaridriver.exe"

            if browser_input == 'Chrome':
                self.currentBrowser = webdriver.Chrome(PATH)  # από δω και κάτω ετοιμάζουμε browsers που υποστηρίζονται
            elif browser_input == 'Firefox':
                self.currentBrowser = webdriver.Firefox(PATH1)
            elif browser_input == 'Edge':
                self.currentBrowser = webdriver.Edge(PATH2)
            elif browser_input == 'Opera':
                self.currentBrowser = webdriver.Opera(PATH3)
            elif browser_input == 'Safari':
                self.currentBrowser = webdriver.Safari(PATH4)
            self.l1nk = l1nk  # το link του site από nemertes που θέλουμε να ζουλέψουμε, για όποιον κάνει τη main

        def yoinkbot(self, linksies,
                    range_limiter):  # Για την ώρα, αποθηκεύει όλο το html των υποσελίδων με τις μεμονωμένες εργασίες.
            textlist = []
            for i in range(2, range_limiter):
                pinakion = '//*[@id="content"]/div[3]/div/div[1]/table/tbody/tr[{}]/td[2]/strong/a'.format(
                    i)  # μεταβλητό xpath, κάντε το google search αν δεν ξέρετε τι είναι
                pinakas = self.currentBrowser.find_element(By.XPATH,
                                                        pinakion)  # το browser δεν έχει οριστεί, θα γίνει self.currentBrowser όταν μπει στο class, ΜΗΝ ΤΟ ΤΡΕΞΕΤΕ ΑΚΟΜΑ
                pinakas.send_keys(Keys.RETURN)
                for i in range(1, 8):
                    mpinakas = '//*[@id="content"]/div[3]/table/tbody/tr[{}]/td[2]'.format(i)  # ξανά, μεταβλητό XPATH
                    try:
                        textlist.append(self.currentBrowser.find_element(By.XPATH,
                                                                        mpinakas).text)  # εδώ βάζουμε στη λίστα textlist το κείμενο που παίρνουμε από το element το οποίο εντοπίσαμε με το μεταβλητό XPATH
                    except selenium.common.exceptions.NoSuchElementException:
                        textlist.append('Δε βρέθηκε τέτοιο στοιχείο')
                self.currentBrowser.get(linksies)
            for item in textlist:
                if 'Τμήμα' and '(ΜΔΕ)' in item: textlist.remove(item)
            return (textlist)

        def beginYoink(self):  # ετοιμάζει τη λίστα με το κείμενο που θα στείλουμε στα sql bois
            self.currentBrowser.get(self.l1nk)
            self.currentBrowser.minimize_window()
            psopsontent = self.currentBrowser.page_source  # να μην τα ξαναπώ, πασάρει στο bs4 το source
            rangesoup = BeautifulSoup(psopsontent)
            rangetext = str(rangesoup.get_text())
            rangelist = []  # αυτό το θέλουμε για να πάρουμε το νούμερο που θα οριοθετήσει την κλεψά
            l0ine = tuple(rangetext.split('\n'))  # γραμμές του text.
            for i in l0ine:
                if 'Φθίνουσα σειρά' in i and 'Descending order' not in i or 'Φθίνουσα σειρά' not in i and 'Descending order' in i:
                    i = i.split(' ')
                    rangelist.extend(i)
            maxrange = int(rangelist[-1])
            if type(maxrange / 20) != int:
                rangeOp = maxrange // 20 + 1
            else:
                rangeOp = maxrange / 20
            masterlist = []
            for i in range(rangeOp + 1):  # ΚΑΠΟΥ ΣΤΟ HTML ΒΓΑΖΕΙ ERROR, ΒΡΕΙΤΕ ΤΙ ΦΤΑΙΕΙ ΚΑΙ ΦΤΙΑΞΤΕ ΤΟ ΠΛΣ ΘΕΛΩ ΝΑ ΑΥΤ
                lynk = self.l1nk + '?offset={}'.format(20 * (i))
                if maxrange - 20 * i >= 20:
                    powerRanger = 22  # Το powerRanger είναι στην ουσία ο αριθμός των στοιχείων που πρέπει να βουτήξουμε, το έκανα έτσι γιατί κουράστηκα να φτιάχνω σούπες,
                else:
                    powerRanger = maxrange - 20 * i + 2
                masterlist.extend(self.yoinkbot(lynk, powerRanger))
            return masterlist





    class Gif():
        def __init__(self, meg):
            self.meg = meg
            self.canvas = tk.Canvas(meg, width=200, height=200)
            self.canvas.pack()
            self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                    Image.open("C:\Program Files (x86)\gif1.gif"))]
            self.image = self.canvas.create_image(100, 100, image=self.sequence[0])
            self.animate(1)

        def animate(self, counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.meg.after(50, lambda: self.animate((counter + 1) % len(self.sequence)))


    def gif():
        top1 = tk.Toplevel()
        top1.title("loading...")
        top1.iconbitmap("C:\Program Files (x86)\icon.ico")
        gif1 = Gif(top1)
        top1.mainloop()

    
        

    def Button1():
        if clicked.get() == "Chrome" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Chrome',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/6553').beginYoink()))
                f.close()
        if clicked.get() == "Edge" :
                with open('textlist.txt', 'w', encoding='utf-8') as f:
                    f.write(str(MasterYoinker('Edge',
                                            'https://nemertes.library.upatras.gr/jspui/handle/10889/6553').beginYoink()))
                    f.close()
        if clicked.get() == "Safari" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Safari',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/6553').beginYoink()))
                f.close()
        if clicked.get() == "Opera" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Opera',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/6553').beginYoink()))
                f.close()
        if clicked.get() == "Mozilla" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Mozilla',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/6553').beginYoink()))
                f.close()



    def Button3():
        if clicked.get() == "Chrome" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Chrome',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/65').beginYoink()))
                f.close()
        if clicked.get() == "Edge" :
                with open('textlist.txt', 'w', encoding='utf-8') as f:
                    f.write(str(MasterYoinker('Edge',
                                            'https://nemertes.library.upatras.gr/jspui/handle/10889/65').beginYoink()))
                    f.close()
        if clicked.get() == "Safari" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Safari',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/65').beginYoink()))
                f.close()
        if clicked.get() == "Opera" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Opera',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/65').beginYoink()))
                f.close()
        if clicked.get() == "Mozilla" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Mozilla',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/65').beginYoink()))
                f.close()


    def Button6():
        if clicked.get() == "Chrome" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Chrome',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/75').beginYoink()))
                f.close()
        if clicked.get() == "Edge" :
                with open('textlist.txt', 'w', encoding='utf-8') as f:
                    f.write(str(MasterYoinker('Edge',
                                            'https://nemertes.library.upatras.gr/jspui/handle/10889/75').beginYoink()))
                    f.close()
        if clicked.get() == "Safari" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Safari',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/75').beginYoink()))
                f.close()
        if clicked.get() == "Opera" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Opera',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/75').beginYoink()))
                f.close()
        if clicked.get() == "Mozilla" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Mozilla',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/75').beginYoink()))
                f.close()



    def Button4():
        if clicked.get() == "Chrome" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Chrome',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/68').beginYoink()))
                f.close()
        if clicked.get() == "Edge" :
                with open('textlist.txt', 'w', encoding='utf-8') as f:
                    f.write(str(MasterYoinker('Edge',
                                            'https://nemertes.library.upatras.gr/jspui/handle/10889/68').beginYoink()))
                    f.close()
        if clicked.get() == "Safari" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Safari',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/68').beginYoink()))
                f.close()
        if clicked.get() == "Opera" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Opera',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/68').beginYoink()))
                f.close()
        if clicked.get() == "Mozilla" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Mozilla',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/68').beginYoink()))
                f.close()



    def Button5():
        if clicked.get() == "Chrome" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Chrome',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/69').beginYoink()))
                f.close()
        if clicked.get() == "Edge" :
                with open('textlist.txt', 'w', encoding='utf-8') as f:
                    f.write(str(MasterYoinker('Edge',
                                            'https://nemertes.library.upatras.gr/jspui/handle/10889/69').beginYoink()))
                    f.close()
        if clicked.get() == "Safari" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Safari',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/69').beginYoink()))
                f.close()
        if clicked.get() == "Opera" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Opera',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/69').beginYoink()))
                f.close()
        if clicked.get() == "Mozilla" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Mozilla',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/69').beginYoink()))
                f.close()




    def Button7():
        if clicked.get() == "Chrome" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Chrome',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/71').beginYoink()))
                f.close()
        if clicked.get() == "Edge" :
                with open('textlist.txt', 'w', encoding='utf-8') as f:
                    f.write(str(MasterYoinker('Edge',
                                            'https://nemertes.library.upatras.gr/jspui/handle/10889/71').beginYoink()))
                    f.close()
        if clicked.get() == "Safari" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Safari',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/71').beginYoink()))
                f.close()
        if clicked.get() == "Opera" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Opera',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/71').beginYoink()))
                f.close()
        if clicked.get() == "Mozilla" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Mozilla',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/71').beginYoink()))
                f.close()




    def Button2():
        if clicked.get() == "Chrome" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Chrome',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/59').beginYoink()))
                f.close()
        if clicked.get() == "Edge" :
                with open('textlist.txt', 'w', encoding='utf-8') as f:
                    f.write(str(MasterYoinker('Edge',
                                            'https://nemertes.library.upatras.gr/jspui/handle/10889/59').beginYoink()))
                    f.close()
        if clicked.get() == "Safari" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Safari',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/59').beginYoink()))
                f.close()
        if clicked.get() == "Opera" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Opera',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/59').beginYoink()))
                f.close()
        if clicked.get() == "Mozilla" :
            with open('textlist.txt', 'w', encoding='utf-8') as f:
                f.write(str(MasterYoinker('Mozilla',
                                        'https://nemertes.library.upatras.gr/jspui/handle/10889/59').beginYoink()))
                f.close()



    l=tk.Label(root,text='Επιλέξτε πολυτεχνικό τμήμα',font=("",15)).pack(expand=1,pady=10)#,bg="#000000"

    b3 = tk.Button(root,text='Τμήμα Ηλεκτρολόγων Μηχανικών και Τεχνολογίας Υπολογιστών ◕',font=('',13),command=lambda: [threading.Thread(target=Button3).start(),threading.Thread(target=messagi()).start(),threading.Thread(target=gif).start()]).pack(expand=1,anchor="nw",pady=7)

    b4 = tk.Button(root,text='Τμήμα Μηχανικών Ηλεκτρονικών Υπολογιστών και Πληροφορικής ◕',font=('',13),command=lambda: [threading.Thread(target=Button4).start(),threading.Thread(target=messagi()).start(),threading.Thread(target=gif).start()]).pack(expand=1,anchor="nw",pady=7)

    b5 = tk.Button(root,text='Τμήμα Πολιτικών Μηχανικών ◕',font=('',13),command=lambda: [threading.Thread(target=Button5).start(),threading.Thread(target=messagi()).start(),threading.Thread(target=gif).start()]).pack(expand=1,anchor="nw",pady=7)

    b6 = tk.Button(root,text='Τμήμα Χημικών Μηχανικών ◕',font=('',13),command=lambda: [threading.Thread(target=Button6).start(),threading.Thread(target=messagi()).start(),threading.Thread(target=gif).start()]).pack(expand=1,anchor="nw",pady=7)

    b7 = tk.Button(root,text='Τμήμα Μηχανολόγων και Αεροναυπηγών Μηχανικών ◕',font=('',13),command=lambda: [threading.Thread(target=Button7).start(),threading.Thread(target=messagi()).start(),threading.Thread(target=gif).start()]).pack(expand=1,anchor="nw",pady=7)

    b1 = tk.Button(root,text='Τμήμα Μηχανικών Περιβάλλοντος ◕',font=('',13),command=lambda: [threading.Thread(target=Button1).start(),threading.Thread(target=messagi()).start(),threading.Thread(target=gif).start()]).pack(expand=1,anchor="nw",pady=7)

    b2 = tk.Button(root,text='Τμήμα Αρχιτεκτόνων Μηχανικών ◕',font=('',13),command=lambda: [threading.Thread(target=Button2).start(),threading.Thread(target=messagi()).start(),threading.Thread(target=gif).start()]).pack(expand=1,anchor="nw",pady=7)


    button_eksodos=tk.Button(root,text='-Έξοδος-',font=('',10),command=root.destroy).pack(expand=1,anchor="se")
    
    root.mainloop()

def w2():
    master =tk.Tk()
    #master.config(bg="#000000")
    master.title('team.33')
    master.geometry("700x450")
    master.iconbitmap("C:\Program Files (x86)\icon.ico")

    s1=IntVar()
    s2=IntVar()
    s3=IntVar()
    s4=IntVar()
    s5=IntVar()
    s6=IntVar()
    s7=IntVar()

    # checkbuttons

    lbl1 = tk.Label(master, text='Επιλέξτε τα πολυτεχνικά τμήματα που σας ενδιαφέρουν',font=("",15)).pack(pady=20)
    c1 = tk.Checkbutton(master,text="Τμήμα Μηχανικών Περιβάλλοντος",font=('',13),variable=s1,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
    c2 = tk.Checkbutton(master,text="Τμήμα Αρχιτεκτόνων Μηχανικών",font=('',13),variable=s2,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
    c3 = tk.Checkbutton(master,text="Τμήμα Ηλεκτρολόγων Μηχανικών και Τεχνολογίας Υπολογιστών",font=('',13),variable=s3,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
    c4 = tk.Checkbutton(master,text="Τμήμα Μηχανικών Ηλεκτρονικών Υπολογιστών και Πληροφορικής",font=('',13),variable=s4,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
    c5 = tk.Checkbutton(master,text="Τμήμα Πολιτικών Μηχανικών",font=('',13),variable=s5,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
    c6 = tk.Checkbutton(master,text="Τμήμα Χημικών Μηχανικών",font=('',13),variable=s6,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
    c7 = tk.Checkbutton(master,text="Τμήμα Μηχανολόγων και Αεροναυπηγών Μηχανικών",font=('',13),variable=s7,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
     


# ΥΠΑΡΧΕΙ ΠΡΟΒΛΛ
    #def mesw3():
        #if  s1.get()== 0 and s2.get()== 0 and s3.get()== 0 and s4.get()== 0 and s5.get()== 0 and s6.get()== 0 and s7.get()== 0 :
           # response=messagebox.showwarning("mess","Παρακαλώ επιλέξτε πολυτεχνικά τμήματα!")
        
    
        
    b1 = tk.Button(master,text="< Υποβολή >",font=("",10),command=w3).pack(expand=1)


    master.mainloop()


def w3():
        rain = tk.Tk()
        rain.iconbitmap('C:\Program Files (x86)\icon.ico')
        # rain.config(bg="#000000")
        rain.title("team33")
        rain.geometry('400x300')
        e1=tk.Entry(rain, width=60, borderwidth=7)
        e1.insert(0,"Αvαζήτηση για...")
        e1.pack(expand=1, anchor="n",pady=10)
        lbl=tk.Label(rain,text="Φίλτρα για αναζήτηση εργασιών",font=("",15)).pack(anchor="nw",expand=1)

        
        i1=IntVar()
        i2=IntVar()
        i3=IntVar()
        i4=IntVar()
        i5=IntVar()
        #i6=IntVar()
        #i7=IntVar()

        # checkbuttons

        check1 = tk.Checkbutton(rain,text="Τίτλος",font=('',13),variable=i1,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        check2 = tk.Checkbutton(rain,text="Θέμα",font=('',13),variable=i2,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        check3 = tk.Checkbutton(rain,text="Συγγραφέας",font=('',13),variable=i3,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        check4 = tk.Checkbutton(rain,text="λέξεις κλειδιά",font=('',13),variable=i4,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        check5 = tk.Checkbutton(rain,text="περίληψη",font=('',13),variable=i5,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        # check6 = tk.Checkbutton(master,text="Τμήμα Χημικών Μηχανικών",font=('',13),variable=i6,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        # check7 = tk.Checkbutton(master,text="Τμήμα Μηχανολόγων και Αεροναυπηγών Μηχανικών",font=('',13),variable=i7,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        




        #def pupop():
         #   if  i1.get()== 0 and i2.get()== 0 and i3.get()== 0 and i4.get()== 0 and i5.get()== 0 :
          #      response=messagebox.showwarning("messagebox","Παρακαλώ επιλέξτε φίλτρα")
           # else:
            #    b1.config(command=listokouti)

        b1 = tk.Button(rain,text="< Υποβολή >",font=("",10),command=listokouti).pack(expand=1)

        rain.mainloop()
            

      


def listokouti():

    money=tk.Tk()
    money.title("team.33")
    # money.config(bg="#000000")
    frame=tk.Frame(money)
    scrollarw1=ttk.Scrollbar(frame,orient=VERTICAL)



    my_listbox= tk.Listbox(frame,yscrollcommand=scrollarw1.set,width=50)
    scrollarw1.config(command=my_listbox.yview)
    scrollarw1.pack(side=RIGHT,fill= Y)

    scrollarw2=ttk.Scrollbar(frame,orient=HORIZONTAL)
    scrollarw2.config(command=my_listbox.xview)
    scrollarw2.pack(side=BOTTOM,fill= X)


    frame.pack()
    
    my_listbox.pack(pady=20)
    # to item einai akyro to evala mono gia na leitoyrgei to scrollbar
    for item in range(1,101):
        my_listbox.insert(END,item)
    butt =tk.Button(money,text="< Υποβολή >",command=ergasia).pack()


    money.mainloop()

def ergasia():
    yolo = tk.Tk()
    # κώδικας που θα εμφανίζει εργασία
    yolo.mainloop()



def begin():
    root = tk.Tk()
    root.title("team.33")
    root.geometry("400x300")
    # root.config(bg="#000000")
    root.iconbitmap("C:\Program Files (x86)\icon.ico")

    enimerwsi=tk.Button(root,text="Λήψη εργασιών",command=suma,font=('',15)).pack(pady=20)

    img_for_scrape = tk.PhotoImage(file="C:\Program Files (x86)\web-sc.png")
    label1= tk.Label(root,image=img_for_scrape).pack()#,bg="#000000"

    button_start=tk.Button(root,text="Κλικ για να ξεκινήσετε",command=w2,font=('',15)).pack(pady=20)

    root.mainloop()

begin()







