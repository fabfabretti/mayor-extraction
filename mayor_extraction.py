import requests
from bs4 import BeautifulSoup

debug = False

# Definisco fuori le stringhe di errore per cambiarle facilmente in caso di necessità.
err_404 = "[!] Error 404"
err_nomayor = "[!] No mayor in page"

def find_mayorname(link):
    """ Dato un link, fa web scraping per ricavare il nome del sindaco.
    Ritorna una stringa con il nome del sindaco.
    Se la pagina non è presente o non c'è un campo sindaco ritorna una stringa di errore.
    :param link: Link alla pagina in cui estrarre il nome
    :return Nome: ripulito del sindaco, oppure stringa di errore."""

    # Scarico la pagina; se non esiste, ritorno errore
    r = requests.get(link)
    if r.ok is False:
        __print_debug(link, err_404)
        return err_404

    # Parso la pagina trovo tutti i td "intestazione", ovvero con classe "itit"
    # (ho notato dal sito che tutte le intestazioni in tabella hanno questo attribute!)
    soup = BeautifulSoup(r.text, "html.parser")
    page_html = soup.findAll('td', attrs={"class": "itit"})

    # Cerco dentro i td trovati quello con scritto "Sindaco"
    td_titolosindaco = None
    for td in page_html:
        if 'Sindaco' in td:
            td_titolosindaco = td
            break

    # Se non ha trovato il titolo "Sindaco", likely non è presente sul sito
    # (vicesindaco reggente or smth) e quindi skippo tutto il resto.
    if td_titolosindaco is None:
        __print_debug(link, err_nomayor)
        return err_nomayor

    # Altrimenti vado avanti e cerco di raggiungere il nome del sindaco.
    else:
        # Trovo il nodo con il titolo "Sindaco":
        found_row = td_titolosindaco.parent.nextSibling.nextSibling
                    # .parent: salgo alla table row di "Sindaco"
                    # .nextSibling.nextSibling: passo alla riga successiva;
                    #                           ce ne vogliono due perché il primo è un carattere vuoto.
        found = found_row.find("b")
                    # Il nome del sindaco è sempre l'unica cosa in bold della riga,
                    # quindi mi basta cercare ciò che è in bold.

        __print_debug(link, found.text)
        return __mayor_clean(found.text)

def __mayor_clean(mayor):
    """
    Trova la posizione della stringa in cui si trova un punto (se esiste) e sostituisce i caratteri da 0 a quel
    punto + 2 (per cancellare anche lo spazio) con "".
    In pratica cancella i titoli del tipo "Avv. ", "Dott. ", ...
    :param mayor: nome del sindaco
    :return: nome del sindaco senza titoli
    """
    if "." in mayor:
        mayor = mayor.replace(mayor[0:mayor.index(".")+2],"")
    return mayor

def __print_debug(link, res):
    """
    Semplice stampa che si attiva solo se la modalità debug è attivata.
    :param link: link analizzato
    :param res: nome del sindaco o stringa di errore
    """
    if debug is True:
        print("{}: {}".format(link,res))
    return
