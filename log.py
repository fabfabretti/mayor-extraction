import csv

debug = True
logfile = "log.txt"
errlogfile = "log_errors.txt"

def add(codice, mayor):
    """ Aggiunge un file al log, scrivendolo immediatamente.
    :param codice Codice ISTAT del comune
    :param mayor Nome pulito del sindaco"""
    log = open(logfile,"a") # Se non esiste lo crea!
    log.write(codice + "," + mayor + "\n")
    if debug is True:
        print("> {}: {}".format(codice,mayor))
    log.close()

def adderror(codice,error):
    """Aggiunge un errore al log, scrivendolo immediatamente.
    :param codice Codice ISTAT del comune
    :param error Stringa di errore
    """
    log = open(errlogfile,"a")
    log.write(codice + "," + error[4:] + "\n")
    log.close()

def load():
    """Carica tutti i codici già esaminati correttamente  - ovvero presenti sul log - e ne restituisce un set.
    Dato che è sempre chiamato a inizio estrazione, lo uso anche per ripulire il log.
    :return Insieme dei codici ISTAT già visitati e presenti nel log."""
    __clearerrlog()
    already_examined = set()
    with open(logfile) as csvfile:
        reader = csv.reader(csvfile)
        for entry in reader:
            already_examined.add(entry[0])
    return already_examined


def clear():
    """Svuota il log."""
    log = open(logfile,"r+")
    log.seek(0)
    log.truncate()
    log.close()

def __clearerrlog():
    """Ripulisce il log degli errori."""
    errlog = open(errlogfile,"r+")
    errlog.seek(0)
    errlog.truncate()
    errlog.close()