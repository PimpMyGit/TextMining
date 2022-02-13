00__Preprocessing:

preprocess iniziale: fasi di cleaning, tokenize, lemmatize, analisi luhn e estrazione bigrammi costrutti

01a__ClassificationTask_Preprocess:

contiene i metodi per il preprocess partendo dal dataset generato dal primo preprocess iniziale.
e' necessario per la creazione dei dataset che sono poi in input ai modelli di classificazione, vengono fatte semplici analisi come ad esempio la filtratura dei termini non presenti nel dataset SenticNet delle polarita'.

01b__ClassificationTask_Algorithm: 

partendo dai dataset preprocessati, diversi modelli, suddivisi in capitoli, vengono costruiti e testati.
e' diviso in una prima parte di import, una seconda di lettura dei file e poi nello specifico ogni capitolo consente di costruire ed utilizzare il relativo modello. vengono infine stampate le performance relative al test set.

02__ClusteringTask:

partendo da dataset preprocessato, si applicano gli algoritmi di clustering alle frasi nelle forme preprocessate, luhn e bigrammi
per poi visualizzare i risultati ottenuti.