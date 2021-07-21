# Import di moduli di default
import time

#Import delle mie funzioni
import log
from link_generation import get_link
from link_generation import create_table
from mayor_extraction import find_mayorname

# Impostazioni

print("Benvenut* nella utility di estrazione dei sindaci d'Italia. \n---")

reset = False
response = ""
while response != "y" and response != "n":
    response = input("Vuoi svuotare il log dalle estrazioni precedenti prima di iniziare? (y/n) ")
    if response == "y":
        reset = True
    if response == "n":
        reset = False

small_sample = False
response = ""
while response != "y" and response != "n":
    response = input("Vuoi eseguire un numero di richieste ridotto? (y/n) ")
    if response == "y":
        small_sample = True
    if response == "n":
        small_sample = False # Impostazione mia di debug: mentre scrivevo il codice ho preferito cercare pochi sindaci assieme
                             # per non sovraccaricare i server con le mie richieste

# Statistiche
n_examined = 0
n_skipped = 0
n_errors = 0
tick = time.time() # Uso successivamente per misurare il tempo di esecuzione

# --- Esecuzione

# Setup
if reset is True:
    log.clear()
already_examined = log.load() # Crea un set con i codici già letti
current_extraction = create_table() # Crea un dizionario con codici del file --> empty

# Per ogni codice di result guarda se hai già trovato il risultato di quel codice;
# if false, scrapalo dalla pagina.
count = 0
for entry in current_extraction.keys():
    # 1. Controllo se era già stata esaminata
    if entry in already_examined:
        print("[-] {}: skip".format(entry))
        n_skipped += 1
    else:
        count += 1
        mayor = find_mayorname(get_link(entry))
        current_extraction[entry] = mayor
        if "[!]" not in mayor:
            log.add(entry,mayor)
            n_examined += 1
        else:
            print("[!] {}: {}".format(entry,mayor))
            log.adderror(entry,mayor)
            n_errors += 1
        if small_sample is True and count > 50:
            break

tock = time.time() - tick
if tock < 60:
    print("Tempo di esecuzione: {:.2f} secondi".format(tock))
else:
    print("Tempo di esecuzione: {} minuti {:.2f} secondi".format(int(tock/60), tock%60))
print("Estratti: {}\nSkippati: {}\nErrori: {}".format(n_examined,n_skipped,n_errors))