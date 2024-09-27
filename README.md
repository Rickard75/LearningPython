# Random Notes
- added something to try pull
- se faccio una modifica a un file interno in una sottocartella, bisogna prima fare add+commit in quella sottocartella e solo dopo fare add+commit nella cartella del livello superiore; alternativamente posso eseguire l'add+commit solo nella cartella del livello superiore

**VOCABULARY**
- track		:	collegare modifiche tra locale e github
- staging area	:	file that stores info about next commit
- commit		: 	snapshot of state of repository
- repo		:	ordered set of commits
- hash		:	fingerprint of a commmit, its personal "ID code"
- branch		:	isolated set of commits (useful to not ruin working state of project, to experiment new code, not interfering with other developers)
- merge		:	to unify two different branches with a third unifying commit
- tag		:	alias to commit hash, simple name to mark important commits such as releases
- remote		:	repository in a different place (usually online)

# TUTORIALS
**COME INIZIALIZZARE GIT IN UNA CARTELLA LOCALE**
- Imposta il nome dell'autore
`git config --global user.name Rickard75`	
- Imposta la mail dell'autore**
git config --global user.email pino@gmail.com		
- Rende la cartella corrente una repository git; ora 'master' è il branch corrente**
git init 						

----------COME CREARE UN NUOVO BRANCH---------------
# Assicurati di essere sul branch principale
git checkout main
# Aggiorna il branch principale
git pull origin main
# Crea e spostati sul nuovo branch
git checkout -b nome-del-nuovo-branch
# Pusha il nuovo branch sul repository remoto
git push origin nome-del-nuovo-branch

-----------COME ELIMINARE UN BRANCH------------------
# Eliminare un branch localmente
git branch -d nome-branch || git branch -D nome-branch
# Eliminare un branch da remoto
git push origin --delete nome-branch

-----------COME FARE IL MERGE DI UN BRANCH SECONDARIO NEL PRINCIPALE (main)----------
git checkout main
git pull origin main
git checkout feature-branch
git pull origin feature-branch
git checkout main
git merge feature-branch
git push origin main

-------------COME RIPRISITINARE UN COMMIT ATTRAVERSO IL CODICE HASH------------
#Ripristina e mantiene la cronologia successiva 
git revert <commit-hash>
#Hard reset: Elimina tutti i commit successivi al commit specificato e cambia anche il contenuto del tuo working directory
git reset --hard <commit-hash>
#Mantiene le modifiche nel tuo working directory, ma sposta il puntatore al commit specificato.
git reset --soft <commit-hash>
# Ripristina il contenuto di un singolo file/directory a uno specifico commit
git checkout <commit-hash> -- <path/to/file>
# Mostra la cronologia dei commit (quelli più recenti: consigliato prima del ripristino)
git log

