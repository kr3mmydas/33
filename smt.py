from calendar import c
import tkinter as tk
from webbrowser import Opera
from PIL import ImageTk, Image, ImageSequence
from tkinter import *
from tkinter import messagebox,ttk
import threading
import yoinker
import datasaver
import time

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
    

        

    def Button1():
        
        if clicked.get() == "Chrome" : datasaver.Datasaver().initiate_save()
       
        if clicked.get() == "Edge" :datasaver.Datasaver('Edge').initiate_save()
        
        if clicked.get() == "Safari" :datasaver.Datasaver('Safari').initiate_save()
            
        if clicked.get() == "Opera" :datasaver.Datasaver('Opera').initiate_save()
            
        if clicked.get() == "Mozilla" :datasaver.Datasaver('Firefox').initiate_save()
        
        

            



    b1 = tk.Button(root,text='Ξεκινήστε την ενημέρωση ◕',font=('',13),command=lambda: [threading.Thread(target=Button1).start(),threading.Thread(target=messagi()).start()]).pack(expand=1,anchor="nw",pady=7)

    


    button_eksodos=tk.Button(root,text='-Έξοδος-',font=('',10),command=root.destroy).pack(expand=1,anchor="se")
    
    root.mainloop()

def w2():
    master =tk.Tk()
    #master.config(bg="#000000")
    master.title('team.33')
    master.geometry("700x450")
    master.iconbitmap("C:\Program Files (x86)\icon.ico")


    lbl1 = tk.Label(master, text='Επιλέξτε το πολυτεχνικό τμήμα που σας ενδιαφέρει',font=("",15)).pack(pady=20)
    
    b3 = tk.Button(master,text='Τμήμα Ηλεκτρολόγων Μηχανικών και Τεχνολογίας Υπολογιστών ◕',font=('',13),command=lambda:[listokouti('Ηλεκτρολόγων Μηχανικών και Τεχνολογίας Υπολογιστών')]).pack(expand=1,anchor="nw",pady=7)

    b4 = tk.Button(master,text='Τμήμα Μηχανικών Ηλεκτρονικών Υπολογιστών και Πληροφορικής ◕',font=('',13),command=lambda:[listokouti('Μηχανικών Ηλεκτρονικών Υπολογιστών και Πληροφορικής')]).pack(expand=1,anchor="nw",pady=7)

    b5 = tk.Button(master,text='Τμήμα Πολιτικών Μηχανικών ◕',font=('',13),command=lambda:[listokouti('Πολιτικών Μηχανικών')]).pack(expand=1,anchor="nw",pady=7)

    b6 = tk.Button(master,text='Τμήμα Χημικών Μηχανικών ◕',font=('',13),command=lambda:[listokouti('Χημικών Μηχανικών')]).pack(expand=1,anchor="nw",pady=7)

    b7 = tk.Button(master,text='Τμήμα Μηχανολόγων και Αεροναυπηγών Μηχανικών ◕',font=('',13),command=lambda:[listokouti('Μηχανολόγων και Αεροναυπηγών Μηχανικών')]).pack(expand=1,anchor="nw",pady=7)

    b1 = tk.Button(master,text='Τμήμα Μηχανικών Περιβάλλοντος ◕',font=('',13),command=lambda:[listokouti('Μηχανικών Περιβάλλοντος')]).pack(expand=1,anchor="nw",pady=7)

    b2 = tk.Button(master,text='Τμήμα Αρχιτεκτόνων Μηχανικών ◕',font=('',13),command=lambda:[listokouti('Αρχιτεκτόνων Μηχανικών')]).pack(expand=1,anchor="nw",pady=7)



        
    b8 = tk.Button(master,text="< Έξοδος >",font=("",10),command=master.destroy).pack(expand=1)


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
        # i5=IntVar()
        # i6=IntVar()
        # i7=IntVar()

        # checkbuttons

        check1 = tk.Checkbutton(rain,text="Τίτλος",font=('',13),variable=i1,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        check2 = tk.Checkbutton(rain,text="Θέμα",font=('',13),variable=i2,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        check3 = tk.Checkbutton(rain,text="Συγγραφέας",font=('',13),variable=i3,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        check4 = tk.Checkbutton(rain,text="Ημερομηνία Δημοσίευσης",font=('',13),variable=i4,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        #check5 = tk.Checkbutton(master,text="Τμήμα Πολιτικών Μηχανικών",font=('',13),variable=i5,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        # check6 = tk.Checkbutton(master,text="Τμήμα Χημικών Μηχανικών",font=('',13),variable=i6,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        # check7 = tk.Checkbutton(master,text="Τμήμα Μηχανολόγων και Αεροναυπηγών Μηχανικών",font=('',13),variable=i7,onvalue=1,offvalue=0).pack(expand=1,anchor="nw")
        




        #def pupop():
         #   if  i1.get()== 0 and i2.get()== 0 and i3.get()== 0 and i4.get()== 0 :
          #      response=messagebox.showwarning("messagebox","Παρακαλώ επιλέξτε φίλτρα")
           # else:
            #    b1.config(command=listokouti)

        b1 = tk.Button(rain,text="< Υποβολή >",font=("",10),command=listokouti).pack(expand=1)

        rain.mainloop()
            

      


def listokouti(sxolh):
    ddd = datasaver.Datasaver().selector(sxolh)
    money=tk.Tk()
    money.title("team.33")
    # money.config(bg="#000000")
    frame=tk.Frame(money)
    scrollarw1=ttk.Scrollbar(frame,orient=VERTICAL)
    


    my_listbox= tk.Listbox(frame,yscrollcommand=scrollarw1.set,height=15, width=175, selectmode=SINGLE)
    scrollarw1.config(command=my_listbox.yview)
    scrollarw1.pack(side=RIGHT,fill= Y)

    scrollarw2=ttk.Scrollbar(frame,orient=HORIZONTAL)
    scrollarw2.config(command=my_listbox.xview)
    scrollarw2.pack(side=BOTTOM,fill= X)
    

    frame.pack()
    
    
    my_listbox.pack(pady=20)
    # to item einai akyro to evala mono gia na leitoyrgei to scrollbar
    for pleiada in ddd:
        my_listbox.insert(END,pleiada[0]+','+pleiada[8])
    butt =tk.Button(money,text="< Υποβολή >",command=ergasia).pack()
     
    money.mainloop()

def ergasia():
    yolo = tk.Tk()
    # κώδικας που θα εμφανίζει εργασία
    yolo.mainloop()



def begin():
    root = tk.Tk()
    root.title("team.33")
    root.geometry("400x600")
    # root.config(bg="#000000")
    root.iconbitmap("C:\Program Files (x86)\icon.ico")

    enimerwsi=tk.Button(root,text="Λήψη εργασιών",command=suma,font=('',15)).pack(pady=20)

    img_for_scrape = tk.PhotoImage(file="C:\Program Files (x86)\web-sc.png")
    label1= tk.Label(root,image=img_for_scrape).pack()#,bg="#000000"

    button_start=tk.Button(root,text="Κλικ για να ξεκινήσετε",command=w2,font=('',15)).pack(pady=20)

    root.mainloop()

begin()







