# OpenclassroomsProjet

### Scripts d'installation de logiciels sur Windows et sur Linux. ###


## Scenario :

  Entreprise de plus de 50 salariés, ordinateurs et pc portable multi-marques. 


## Objectif principal :

  
  - Installation de logiciels récurrents en mode silence
  - Gains de temps
  

## Utilisation :

  L'outil est utilisable sur Windows 10 ou sur un système Unix.
Il peut être lancé par une tâche cron ou un script personnalisé.



## Conditions :

Python3 doit être installé sur le client s'il est automatisé.

Les scripts tournent sous Linux et Windows.

Dans le repertoire d'installation doivent figurer :

  * googlechromestandaloneenterprise64.msi
  * setup.exe
  * Teams_windows_x64.exe
  * OperaSetup.exe
  * ZoomInstaller.exe
  * winrar-x64-XXXfr.exe
  * vlc-X.X.XX-win64.exe
  * LibreOffice_X.X.X-Win_64.msi
  * AcroRdrDC2100520048_fr_FR.exe
  * jre-8u291-windows-x64.exe
  * npp.X.X.Installer.exe
  * Configuration.xml
  * 7zXXX-x64.exe
  
et le répertoire :
  * Office/
    

## Installation :


- Téléchargez et décompressez le répertoire 2.Win_install.zip

- Lancez installation : 

```
ouvrir un Invite de commande en tant qu'administrateur

> cd 2.Win_install/
> python software.py
> 
```


## Méthode :

*olCheckSeq.py* peut être exécuté au niveau de la séquence.
Vous devez spécifier le nom des plans que vous souhaitez vérifier :
```
> python3 olCheckSeq.py P1 P2 P3
> python3 olCheckSeq.py P*
> python3 olCheckSeq.py *
```
*olCheckShot.py* peut être exécuté au niveau du plan.
Il n'a pas besoin d'argument :
```
> python3 olCheckShot.py
```


## Resultats :

- S'ils sont lancés manuellement, checkSeq et checkShot afficheront les résultats dans la console.

>Cette méthode est recommandée pour un usage ponctuel.

- Le ministe HTML se trouve dans $PROJ/$SEQ/.web/index.htm

>seqreport.htm est affiché dans le cadre de gauche.

>Les rapports de plans sont écrits dans $PROJ/$SEQ/$SHOT/report.htm

>Ils seront affichés dans le cadre de droite du minisite.

>Des versions archivées de report.htm sont copiées dans report_$PROJ_$SEQ_$SHOT_DATE_TIME.htm

- Les fichiers globaux de log sont dans $PROJ/LOGS/ (olCheckSeqlog.DATE-TIME.txt)

>Ils contiennent des versions courtes des retours console.

