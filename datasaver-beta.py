# -*- coding: utf-8 -*- 
import yoinker
import sqlite3
class Datasaver():
    def __init__(self, desired_browser='Chrome'):
        self.browser = desired_browser
        self.conn = sqlite3.connect('postgraduatework2.db')
        self.c = self.conn.cursor()
        self.sqlmaker_ergasies = '''CREATE TABLE IF NOT EXISTS ergasies (
	title text NOT NULL,
	engtitle text NOT NULL,
	authors text NOT NULL,
	kwds text NOT NULL,
	engkwds text NOT NULL,
	abstracc text NOT NULL,
	engabstracc text NOT NULL,
	linksey text NOT NULL,
    PRIMARY KEY(title,engtitle,authors,kwds,engkwds,abstracc,engabstracc,linksey)
);'''

        self.sqlmaker_sxoles = '''CREATE TABLE IF NOT EXISTS sxoles (
	sxolhname text NOT NULL PRIMARY KEY,
	mainlink text NOT NULL
);'''

        self.sqlmaker_ergsxolh = '''CREATE TABLE IF NOT EXISTS ergsxolh (
    sxolhname NOT NULL,
    title text NOT NULL,
    FOREIGN KEY(sxolhname) REFERENCES sxoles(sxolhname),
    FOREIGN KEY(title) REFERENCES ergasies(title)   
);
'''
       
        self.sxoles = (('Αρχιτεκτόνων Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/59'),('Μηχανικών Περιβάλλοντος','https://nemertes.library.upatras.gr/jspui/handle/10889/6553'),('Χημικών Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/75'),('Ηλεκτρολόγων Μηχανικών και Τεχνολογίας Υπολογιστών','https://nemertes.library.upatras.gr/jspui/handle/10889/65'),('Πολιτικών Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/71'),('Μηχανολόγων και Αεροναυπηγών Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/69'),('Μηχανικών Ηλεκτρονικών Υπολογιστών και Πληροφορικής','https://nemertes.library.upatras.gr/jspui/handle/10889/68'))
        self.sqlremover = ''' DELETE FROM ergasies WHERE linksey=NULL;'''
    def initiate_save(self):
        self.c.execute(self.sqlmaker_ergasies)
        self.c.execute(self.sqlmaker_sxoles)
        self.c.execute(self.sqlmaker_ergsxolh)
        self.c.execute(self.sqlremover)
        for i in self.sxoles:
            self.c.execute('''INSERT INTO sxoles VALUES (?,?);''',(i[0],i[1]))
       # self.c.execute(self.selector)
        self.upd8r()
        self.c.execute('''COMMIT''')
        self.c.close()
    def upd8r(self):
        for sxolh in self.sxoles:
            rammer = yoinker.MasterYoinker(self.browser, sxolh[1]).beginYoink()
            for ergasia in rammer:
                titlos = ''
                transl8d_titlos = ''
                syggrafeas = ''
                keywordz = ''
                eng_keywordz = ''
                abstracc = ''
                eng_abstracc = ''
                elpis_xorterou_syndesmos = ''
                metavlhtes = [titlos,transl8d_titlos,syggrafeas,keywordz,eng_keywordz,abstracc,eng_abstracc,elpis_xorterou_syndesmos]                
                for stoixeio in ergasia.split('\t'):
                    axrhsto_info = stoixeio.split('///')
                    if axrhsto_info[0] == 'Τίτλος (Μετάφραση): ': transl8d_titlos = axrhsto_info[1]
                    if axrhsto_info[0] == 'Τίτλος: ':titlos = axrhsto_info[1]
                    if axrhsto_info[0] == 'Συγγραφέας: ': syggrafeas = axrhsto_info[1]
                    if axrhsto_info[0] == 'Λέξεις Κλειδιά: ': keywordz = axrhsto_info[1]
                    if axrhsto_info[0] == 'Λέξεις Κλειδιά (Μετάφραση): ': eng_keywordz = axrhsto_info[1]
                    if axrhsto_info[0] == 'Περίληψη: ': abstracc = axrhsto_info[1]
                    if axrhsto_info[0] == 'Περίληψη (Μετάφραση) : ': eng_abstracc = axrhsto_info[1]
                    if axrhsto_info[0] == 'Σύνδεσμος εργασίας:': elpis_xorterou_syndesmos = axrhsto_info[1]
                    for var in metavlhtes:
                        if not var: var = 'Το στοιχείο δε βρέθηκε'
                try:
                    self.c.execute('''INSERT INTO ergasies VALUES(?,?,?,?,?,?,?,?);''',(titlos,transl8d_titlos,syggrafeas,keywordz,eng_keywordz,abstracc,eng_abstracc,elpis_xorterou_syndesmos))
                except sqlite3.IntegrityError : pass
                self.c.execute('''INSERT INTO ergsxolh VALUES(?,?);''',(sxolh[0],titlos))       