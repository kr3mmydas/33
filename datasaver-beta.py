import yoinker
import sqlite3
class Datasaver():
    def __init__(self, targetyoinker,):
        self.targetyoinker = targetyoinker
        self.sql = '''CREATE TABLE IF NOT EXISTS Εργασίες (
	Τίτλος text NOT NULL PRIMARY KEY,
	Τίτλος(Μετάφραση) text NOT NULL,
	Συγγραφέας text NOT NULL,
	Λέξεις-κλειδιά text NOT NULL,
	Λέξεις-κλειδιά(Μετάφραση) text NOT NULL,
	Περίληψη text NOT NULL,
	Περίληψη(Μετάφραση) text NOT NULL,
	Σύνδεσμος text NOT NULL
);

CREATE TABLE IF NOT EXISTS Σχολές (
	Όνομα σχολής text NOT NULL PRIMARY KEY,
	Σύνδεσμος εργασιών text NOT NULL
);

CREATE TABLE IF NOT EXISTS "Σχολή της εργασίας" (
	Όνομα σχολής text NOT NULL,
	Τίτλος text NOT NULL
);
'''
        self.sxoles = (('Αρχιτεκτόνων Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/59'),('Ηλεκτρολόγων Μηχανικών και Τεχνολογίας Υπολογιστών','https://nemertes.library.upatras.gr/jspui/handle/10889/65'),('Μηχανικών Περιβάλλοντος','https://nemertes.library.upatras.gr/jspui/handle/10889/6553'),('Μηχανικών Η/Υ και Πληροφορικής','https://nemertes.library.upatras.gr/jspui/handle/10889/68'),('Μηχανολόγων και Αεροναυπηγών Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/69'),('Πολιτικών Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/71'),('Χημικών Μηχανικών','https://nemertes.library.upatras.gr/jspui/handle/10889/75'))
    def initiate_save(self):
        conn = sqlite3.connect('postgraduatework.db')
        c = conn.cursor()
        


