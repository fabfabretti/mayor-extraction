# Read Me

* **Autrice**
  \---- 

* **Titolo del progetto**
  *Progetto Web Scraping: i sindaci d'Italia*

* **Descrizione**
  Il programma permette di estrarre in automatico l'elenco di nomi dei sindaci e codice ISTAT del relativo comune sfruttando la tecnica del web scraping.

  Il file `main` chiede all'utente le impostazioni da usare per l'estrazione, gestisce il ciclo di estrazione e restituisce delle statistiche sull'esecuzione.

  Il file `link_generation.py` contiene una serie di funzioni per generare una tabella con tutti i codici ISTAT estraibili, e una funzione che dato il codice ISTAT di un comune genera il link corrispondente nel sito che stiamo usando per l'estrazione.

  Il file `mayor_extraction.py` contiene una serie di funzioni che permettono di estrarre e ripulire il nome del sindaco di un singolo comune.

  Il file `log.py` contiene tutte le funzioni relative alla scrittura e alla lettura dei due log (log delle estrazioni e log degli errori)

* **Input**
  All'utente viene chiesto via terminale se vuole svuotare il log prima di iniziare, e se vuole fare un'estrazione completa o parziale.
  Il file `abitanti_2019_2020.csv` è usato come input per generare la lista dei codici, ed è già situato nella cartella. 

* **Output**

  * Un **file** `log.txt` dove vengono memorizzati i codici istat seguiti dal relativo nome del sindaco.
  * Un **file** `log_errors.txt` dove vengono memorizzati i codici istat che non sono stati estratti correttamente nell'ultima esecuzione di codice, insieme a una stringa che descrive l'errore riscontrato.
  * Su **console**, per ogni accesso al sito viene visualizzato il codice ISTAT e il nome del sindaco in caso di estrazione con successo, la stringa di errore altrimenti.
    A fine estrazione vengono visualizzati alcuni dati statistici sull'esecuzione del programma: tempo di esecuzione, numero di sindaci estratti, numero di comuni skippati, numero di comuni che hanno ritornato errore.

* **Esempio di invocazione del codice**:

  \> L'utente avvia il programma premendo "play" sull'IDE, oppure avviando `py main.py` da terminale.

  \> Al momento della richiesta, l'utente risponde "y" oppure "n" per settare le impostazioni

  \> L'estrazione avviene in automatico, producendo un output su terminale simile al seguente:

  > \>102050: Francesco Galati
  > [...]
  > \> 028001: Federico Barbierato
  > Tempo di esecuzione: 10 minuti 59.79 secondi
  > Estratti: 7449
  > Skippati: 0
  > Errori: 530

  \> Nella cartella saranno presenti un file log.txt con tutte le estrazioni e un log_errors.txt con tutte le estrazioni non andate a buon fine.