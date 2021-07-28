# OpenclassroomsProjet

### Scripts d'installation de logiciels sur Windows et sur Linux. ###

## Scenario :

  Entreprise de plus de 50 salariés, ordinateurs et pc portable multi-marques. 


## Objectif principal :

  
  - Installation de logiciels récurrents en mode silence
  - Gains de temps
  

## Utilisation :

  L'outil est utilisable sur Windows 10 ou sur un système Unix.
Il peut être lancé par le plannificateur de tâche, une tâche cron ou un script personnalisé.



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


- Téléchargez et décompressez le répertoire 2.Win_install.zip (https://cloudlasalle-my.sharepoint.com/:f:/g/personal/henri_kahudi_unilasalle_fr/Elg9YPTjsYFJsscTRTjIvzwB-DyOWrPgcJ-pTbKa7CyFaQ?e=zOTtPd) 

- Lancez installation : 

```
ouvrir un Invite de commande en tant qu'administrateur

> cd 2.Win_install/
> python software.py
> 
```

