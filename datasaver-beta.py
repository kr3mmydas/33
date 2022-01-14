import yoinker
import sqlite3
import time
class Datasaver():
    def __init__(self, desired_browser='Chrome'):
        self.browser = desired_browser
        self.conn = sqlite3.connect('postgraduatework.db')
        self.c = self.conn.cursor()
        self.sqlmaker_ergasies = '''CREATE TABLE IF NOT EXISTS ergasies (
	title text NOT NULL PRIMARY KEY,
	engtitle text NOT NULL,
	authors text NOT NULL,
	kwds text NOT NULL,
	engkwds text NOT NULL,
	abstracc text NOT NULL,
	engabstracc text NOT NULL,
	linksey text NOT NULL
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
        self.sqlsaver = '''INSERT INTO sxoles VALUES ('{}','{}'); '''
        self.sxoles = (('Αρχιτεκτόνων Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/59'),('Χημικών Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/75'))
        self.sqlremover = ''' DELETE FROM sxoles;'''
    def initiate_save(self):
        self.c.execute(self.sqlmaker_ergasies)
        self.c.execute(self.sqlmaker_sxoles)
        self.c.execute(self.sqlmaker_ergsxolh)
        self.c.execute(self.sqlremover)
        for i in self.sxoles:
            self.c.execute(self.sqlsaver.format(i[0],i[1]))
        self.upd8r()
        self.c.execute('''COMMIT''')
        self.c.close()
    def upd8r(self):
        for sxolh in self.sxoles:
            rammer = yoinker.MasterYoinker(self.browser, sxolh[1]).beginYoink()
            for ergasia in rammer:
                
                for stoixeio in ergasia.split('\t'):
                    titlos = ''
                    transl8d_titlos = ''
                    syggrafeas = ''
                    keywordz = ''
                    eng_keywordz = ''
                    abstracc = ''
                    eng_abstracc = ''
                    elpis_xorterou_syndesmos = ''
                    metavlhtes = [titlos,transl8d_titlos,syggrafeas,keywordz,eng_keywordz,abstracc,eng_abstracc,elpis_xorterou_syndesmos]
                    axrhsto_info = stoixeio.split('///')
                    if axrhsto_info[0] == 'Τίτλος: ':titlos = axrhsto_info[1]
                    elif axrhsto_info[0] == 'Τίτλος (Μετάφραση): ': transl8d_titlos = axrhsto_info[1]
                    elif axrhsto_info[0] == 'Συγγραφέας: ': syggrafeas = axrhsto_info[1].replace("'","´")
                    elif axrhsto_info[0] == 'Λέξεις Κλειδιά: ': keywordz = axrhsto_info[1].replace('\n',',')
                    elif axrhsto_info[0] == 'Λέξεις Κλειδιά (Μετάφραση): ': eng_keywordz = axrhsto_info[1].replace('\n',',')
                    elif axrhsto_info[0] == 'Περίληψη: ': abstracc = axrhsto_info[1].replace("'","´")
                    elif axrhsto_info[0] == 'Περίληψη (Μετάφραση) : ': eng_abstracc = axrhsto_info[1].replace("'","´")
                    elif axrhsto_info[0] == 'Σύνδεσμος εργασίας:': elpis_xorterou_syndesmos = axrhsto_info[1]
                    for var in metavlhtes:
                        if not var: var = 'Το στοιχείο δε βρέθηκε'
                    try:self.c.execute(''' INSERT INTO ergasies VALUES('{}','{}','{}','{}','{}','{}','{}','{}');'''.format(titlos,transl8d_titlos,syggrafeas,keywordz,eng_keywordz,abstracc,eng_abstracc,elpis_xorterou_syndesmos))
                    except sqlite3.IntegrityError: pass
                    except sqlite3.OperationalError:pass
                    try:self.c.execute('''INSERT INTO ergsxolh VALUES('{}','{}'); '''.format(titlos, sxolh[0]))
                    except sqlite3.IntegrityError: pass
                    except sqlite3.OperationalError:pass        



Datasaver().initiate_save()

    
        


