from tkinter import *


#%% Modèle
def dec_to_bits(dec):
    """
    Convertit en binaire un entier

    Parameters
    ----------
    dec :un entier entre 0 et 255

    Returns
    -------
    Représentation binaire de l'entier sous forme de liste de 8 bits

    """
    assert 0 <= dec <= 255 #vérification de la valeur du décimal
    bits = [0 for i in range(8)] #création d'une suite de 8 bits
    i  = 7  #index de bit du poids faible
    while dec > 0 :  #vérification qu'il reste des bits à calculer
        bits[i] = dec % 2 #calcul du bit
        dec = dec // 2 #division pour passer au bit suivant
        i = i -1 #changement de bit dans la liste
    return bits


def test_dec_to_bits():
    assert dec_to_bits(15) == [0, 0, 0, 0, 1, 1, 1, 1]
    assert dec_to_bits(132) == [1, 0, 0, 0, 0, 1, 0, 0]


def bits_to_dec(bits):
    """
    Convertit une liste de bits en décimal

    Parameters
    ----------
    bits : liste de 8 bits

    Returns
    -------
    entier entre 0 et 255

    """
    dec = 0
    puissance = 0
    for i in range (len(bits)-1,-1,-1) : #parcours de la liste bit par bit
        dec = dec + bits[i] * 2**puissance #calcul de la valeur décimale bit par bit
        puissance = puissance + 1 #changement de poids du bit
    return dec
    


def test_bits_to_dec():
    assert bits_to_dec([0, 0, 0, 0, 1, 1, 1, 1]) == 15
    assert bits_to_dec([1, 0, 0, 0, 0, 1, 0, 0]) == 132


def ip_to_bits(ip):
    """
    Convertit une adresse ip sous forme de str en liste de 32 bits

    Parameters
    ----------
    ip : adresse ip sous forme de str comme '172.17.232.6'

    Returns
    -------
    adresse ip sous forme de liste de 32 bits

    """
    parties = ip.split (".") #division de l'adresse en 4 valeur str
    bits = [] #création de la liste de bits
    for valeure in parties : #parcours des 4 valeurs str
        bits = bits + dec_to_bits(int(valeure)) #transformation de str en décimal puis ajout du bits à la liste
    return bits


def test_ip_to_bits():
    assert ip_to_bits("172.17.232.6") == [
        1,
        0,
        1,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
    ]


def bits_to_ip(ip_bits):
    """
    Convertit une adresse ip sous forme de str en liste de 32 bits


    Parameters
    ----------
    ip_bits : adresse ip sous forme de liste de 32 bits

    Returns
    -------
    adresse ip sous forme de str comme '172.17.232.6'

    """
    ip = "" #création de l'ip en str
    for i in range (4) : #parcours des 4 parties de l'ip
        partie = ip_bits [i*8 : (i+1)*8 ] 
        valeur = bits_to_dec(partie)
        ip = ip + str(valeur) #ajout de la valeur décimale de la partie à l'ip
        if i < 3 : #vérifie qu'il y a encore des parties à ajouter
            ip = ip + "." #ajout du séparateur de chaque valeur
    return ip


def test_bits_to_ip():
    assert (
        bits_to_ip(
            [
                1,
                0,
                1,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                1,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
            ]
        )
        == "172.17.232.6"
    )

 


def verifier_ip(ip):
    """
    Vérifie si une adresse ip sous forme de  str comme '172.17.232.6'
    est valide

    Parameters
    ----------
    ip : adresse ip sous forme de str comme '172.17.232.6'
    Returns
    -------
    booléen
    """
    try:
        parties1 = ip.split(".") #division de l'adresse en 4 valeur str
        if len(parties1) != 4: #vérification du nombre de parties
            return False #arrêt de la vérification
        for p in parties1: #parcours des 4 parties
            n = int(p) #conversion de la partie en entier
            if n < 0 or n > 255: #vérification de la valeur de chaque partie
                return False #si une partie n'est pas valide, arrête la vérification
        return True
    except:
        return False

def test_verifier_ip():
    assert verifier_ip("172.17.232.6") == True
    assert verifier_ip("172.17.256.6") == False
    assert verifier_ip("172.17.256") == False
    assert verifier_ip("172.17.256") == False


def prefixe_reseau(ip_bits, mask):
    """
    Renvoie le préfixe réseau d'une adresse IP sous forme de liste de 32 bits
    à partir de la longueur du masque réseau

    Parameters
    ----------
    ip_bits : liste de bits (0 ou 1)
    masque : entier entre 1 et 31 bits

    Returns
    -------
    Renvoie une liste de 32 bits

    """
    prefixe = [0 for i in range(32)] #création de la liste du préfixe réseau
    ip_masque = [1 for i in range(mask)] + [0 for j in range(32 - mask)] #création du masque sous forme de liste de bits
    for i in range(32): #parcours des 32 bits
        prefixe[i] = ip_bits[i] * ip_masque[i] #calcul du préfixe bit par bit
    return prefixe


def test_prefixe_reseau():
    assert prefixe_reseau(
        [
            1,
            0,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1,
            0,
        ],
        21,
    ) == [
        1,
        0,
        1,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]


def calcul_ip():
    """Fonction de rappel du bouton bouton_calcul
    Récupère l'adresse IP  de la variable de contrôle  adresse_ip
    Vérifie si cette adresse est valide avec verifier_ip
    Si elle est valide, convertit l'adresse en liste de 32 bits,
    puis calcule le préfixe réseau, la première adresse, la dernière adresse
    et l'adresse de broadcast (dernière adresse de la plage)
    Modifie pour cela les variables de contrôles liées aux étiquettes
    d'affichage de ces différents éléments
    """
    ip = adresse_ip.get()
    if not verifier_ip(ip): #vérification de l'adresse ip
        message_erreur.set("Adresse non conforme") #affichage du message d'erreur
    else:
        message_erreur.set("") #efface le message d'erreur
        ip_bits = ip_to_bits(ip) #conversion de l'adresse ip en bits
        adresse = prefixe_reseau(ip_bits, masque.get()) #calcul du préfixe réseau
        adresse_reseau.set("Adresse  réseau : " + bits_to_ip(adresse)) #affichage de l'adresse réseau
        adresse[31] = 1 #calcul de la première adresse
        premiere_adresse.set("Première adresse : " + bits_to_ip(adresse)) #affichage de la première adresse
        broadcast = adresse.copy() #copie de l'adresse réseau pour la broadcast
        for i in range(masque.get(), 32): #parcours des bits hors masque
            broadcast[i] = 1 #calcul de l'adresse broadcast
        adresse_broadcast.set("Adresse broadcast : " + bits_to_ip(broadcast)) #affichage de l'adresse broadcast
        derniere_ip = broadcast.copy() #copie de l'adresse broadcast pour la dernière adresse
        derniere_ip[31] = 0 #calcul de la dernière adresse
        derniere_adresse.set("Dernière adresse : " + bits_to_ip(derniere_ip)) #affichage de la dernière adresse
        nombre = 2**(32 - masque.get()) - 2 #calcul du nombre d'adresses ip
        nombre_adresses_ip.set("Nombre d'adresses IP : " + str(nombre)) #affichage du nombre d'adresses ip disponibles
#%% Vue : interface graphique


# Fenêtre racine
fen = Tk() #ouveeture de la fenêtre graphique
fen.title("Calculateur d'adresses IP") #titre de la fenêtre
fen.geometry("600x400") #taille de la fenêtre

### Variables de contrôles
adresse_ip = StringVar()
premiere_adresse = StringVar()
premiere_adresse.set("Première adresse : ")
adresse_reseau = StringVar()
adresse_reseau.set("Adresse réseau : ")
derniere_adresse = StringVar()
derniere_adresse.set("Dernière adresse : ")
adresse_broadcast = StringVar()
adresse_broadcast.set("Adresse broadcast : ")
message_erreur = StringVar()
nombre_adresses_ip = StringVar()
nombre_adresses_ip.set("Nombre d'adresses IP : ")
masque = IntVar()

# Cadre adresse
cadre_adresse = Frame(fen) #création du cadre adresse
etiq_adresse = Label(cadre_adresse, text="Adresse IP : ", font=("Arial", 20)) #caractérisation de l'étiquette adresse
saisie_adresse = Entry(
    cadre_adresse, textvariable=adresse_ip, font=("Arial", 20)
)
etiq_adresse.pack(side=LEFT)
saisie_adresse.pack(side=LEFT)
cadre_adresse.pack() #création et caractérisation de l'entrée adresse

# Cadre masque
cadre_masque = Frame(fen) #création du cadre masque
etiq_masque = Label(cadre_masque, text= "Masque réseau : ", font=("Arial", 20)) #caractérisation de l'étiquette masque
saisie_masque = Scale(
    cadre_masque,
    from_=1,
    to=31,
    orient=HORIZONTAL,
    variable=masque,
    tickinterval=15,
    font=("Arial", 14),) #caractérisation de l'entrée en échelle du masque
etiq_masque.pack(side=LEFT) #placement de l'étiquette masque
saisie_masque.pack(side=LEFT) #placement de l'entrée en échelle du masque
cadre_masque.pack() #création du cadre masque

# Cadre calcul
cadre_calcul = Frame(fen) #création du cadre d'affichage des résultats
bouton_calcul = Button(
    cadre_calcul,
    text="Calculer",
    font=("Arial", 16),
    command=calcul_ip) #caractérisation du bouton de calcul
bouton_calcul.pack(pady=10)  #placement du bouton de calcul
cadre_calcul.pack() #placement du cadre calcul

Label(cadre_calcul, textvariable=adresse_reseau, font=("Arial", 14)).pack()
Label(cadre_calcul, textvariable=premiere_adresse, font=("Arial", 14)).pack()
Label(cadre_calcul, textvariable=derniere_adresse, font=("Arial", 14)).pack()
Label(cadre_calcul, textvariable=adresse_broadcast, font=("Arial", 14)).pack()
Label(cadre_calcul, textvariable=nombre_adresses_ip, font=("Arial", 14)).pack()
# implémentation des résultats dans le cadre calcul


#%% Boucle infinie , réceptionnaire d'événement
fen.mainloop()
