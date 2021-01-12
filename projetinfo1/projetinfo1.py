##importations
import sqlite3
from math import * 

##principal

conn = sqlite3.connect('INFO')
cursor = conn.cursor()
#cursor.execute("""
#CREATE TABLE IF NOT EXISTS Identifiants(
#  NomDeCompte VARCHAR(45) NOT NULL,
 # MotDePasse VARCHAR(45) NOT NULL,
 # Personne_idPersonne INT NOT NULL,
#  PRIMARY KEY (NomDeCompte, MotDePasse)

#)
#""")
conn.commit()
cursor.execute("""
INSERT INTO Identifiants(Personne_idPersonne, NomDeCompte, MotDePasse) VALUES(?, ?, ?)""", (34041, "carolilou", "Chocolat"))
cursor.execute("""SELECT Personne_idPersonne,MotDePasse  FROM Identifiants""")
user1 = cursor.fetchone()
print(user1)

print("entrer votre identifiant")
id=input()

print("entrer votre mot de passe")
motdepasse=input()

def comparaison(id, motdepasse):
    cursor.execute("SELECT * FROM Identifiants WHERE Personne_idPersonne = " + str(id))
    resultat = list(cursor)
    if len(resultat) == 0 :
        return "identifiant ou mot de passe incorrect"
    elif resultat[0][1]==str(motdepasse) :
        return "Bonjour" , resultat[0][0]
    return "identifiant ou mot de passe incorrect"

print(comparaison(id,motdepasse))