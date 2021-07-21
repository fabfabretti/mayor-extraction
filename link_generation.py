import csv

debug = False

def create_table():
    """ Crea un dizionario codice:None, con tutti i codici da esaminare.
    :return dizionario codice->None (verrà riempito poi)"""
    codici = __find_codes()
    table = {}
    for e in codici:
        table[e] = None
    __print_debug(table)
    return table


def __find_codes():
    """ Funzione interna usata da create_table. Prende il file della professoressa e ricava tutti i codici ISTAT.
    Ritorna una lista di codici ISTAT.

    :return insieme dei codici estratti"""

    # 1. Recupero i codici ISTAT dal file della prof
    codici_istat_0 = set()
    with open("abitanti_2019_2020.csv") as csvfile:
        reader = csv.reader(csvfile,delimiter=";")
        for entry in reader:
            codici_istat_0.add(entry[0])

    codici_istat = []
    for element in codici_istat_0:
        num_str = str(element)
        while len(num_str) < 6:
            num_str = "0" + num_str
        if num_str not in codici_istat:
            codici_istat.append(num_str)
    return codici_istat

def get_link(codice):
    """A partire da un codice ISTAT, genera il link al sito.
    :param codice: codice ISTAT del comune
    :return stringa con il link alla pagina di amministrazione del comune"""
    return "******" + codice[0:3] + "/" + codice[3:7] + "/amm.html"

def __print_debug(print_db):
    """Esegue una stampa solamente se la variabile debug è a True.
    :param stringa da stampare"""
    if debug is True:
        print(print_db)