#################################################################################
#      Installation des logiciels de base                                       #
#             Juin 2021                                                         #
#            Henri KAHUDI                                                       #
#################################################################################

import os                                                                                        #importation du module "os"


def test_vlc():                                                                                  #definition de fonction
    os.chdir(r"C:\Program Files")                                                   #méthode utilisé pour changer le répertoire de travail actuel
    if(os.path.exists(liste1[0])):                                                               #test à l'aide du module "os" et des méthodes "path" et "exists" si dans la liste1, à l'argument "0", le fichier existe
        print("***************************VLC EXISTE DÉJA*********************************")     #affiche la chaine de caractere entre les parentheses
    else:
        print("*************************INSTALLATION VLC EN COURS*************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("vlc-3.0.14-win64 /S")                                                         #méthode utilisé pour interagir avec le systeme d'exploitation
        print("#############################VLC INSTALLÉ##################################")

def test_notepadd():
    os.chdir(r"C:\Program Files (x86)")
    if(os.path.exists(liste1[1])):
        print("***************************NOTEPADD++ EXISTE DÉJA**************************")
    else:
        print("*****************INSTALLATION NOTEPAD++ EN COURS***************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("npp.8.0.Installer.exe /S")
        print("##########################NOTEPAD++ INSTALLÉ###############################")

def test_winrar():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[2])):
        print("***************************WINRAR EXISTE DÉJA*********************************")
    else:
        print("*****************INSTALLATION WINRAR EN COURS*********************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("winrar-x64-602fr.exe /S")
        print("#############################WINRAR INSTALLÉ###############################")
        
def test_zip7():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[3])):
        print("***************************7ZIP EXISTE DÉJA********************************")
    else:
        print("*****************INSTALLATION 7ZIP EN COURS********************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("7z1900-x64.exe /S")
        print("##############################7ZIP INSTALLÉ################################")

def test_zoom():
    os.chdir(r"C:\Users\henri\AppData\Roaming")
    if(os.path.exists(liste1[4])):
        print("***************************ZOOM EXISTE DÉJA********************************")
    else:
        print("*****************INSTALLATION ZOOM EN COURS********************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("ZoomInstaller.exe /S")
        print("#############################ZOOM INSTALLÉ#################################")

def test_chrome():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[5])):
        print("***************************CHROME EXISTE DÉJA******************************")
    else:
        print("*****************INSTALLATION CHROME EN COURS******************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("MsiExec.exe /i googlechromestandaloneenterprise64.msi /qn")
        print("##############################CHROME INSTALLÉ##############################")

def test_opera():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[6])):
        print("***************************OPÉRA EXISTE DÉJA*******************************")
    else:
        print("*****************INSTALLATION OPÉRA EN COURS*******************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("OperaSetup.exe /silent /allusers=1 /launchopera=0 /setdefaultbrowser=0")
        print("#############################OPÉRA INSTALLÉ################################")

def test_adobe_reader():
    os.chdir(r"C:\Program Files (x86)")
    if(os.path.exists(liste1[7])):
        print("***********************ADOBE READER EXISTE DÉJA****************************")
    else:
        print("*****************INSTALLATION ADOBE READER EN COURS************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("AcroRdrDC2100520048_fr_FR/sAll /rs /msi EULA_ACCEPT=YES")
        print("############################ADOBE READER INSTALLÉ##########################")

def test_office365():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[8])):
        print("*************************OFFICE365 EXISTE DÉJA*****************************")
    else:
        print("*****************INSTALLATION OFFICE365 EN COURS***************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("setup.exe /configure Configuration.xml")
        print("#############################OFFICE365 INSTALLÉ############################")

def test_teams():
    os.chdir(r"C:\Users\henri\AppData\Local")
    if(os.path.exists(liste1[9])):
        print("***************************TEAMS EXISTE DÉJA*******************************")
    else:
        print("*****************INSTALLATION TEAMS EN COURS*******************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("Teams_windows_x64.exe /S")
        print("#############################TEAMS INSTALLÉ################################")

def test_java():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[10])):
        print("*****************************JAVA EXISTE DÉJA******************************")
    else:
        print("**********************INSTALLATION JAVA EN COURS***************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("start /wait jre-8u291-windows-x64.exe /s REBOOT=Suppress")
        print("##############################JAVA INSTALLÉ################################")

def test_libreoffice():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[11])):
        print("*************************LIBRE OFFICE EXISTE DÉJA**************************")
    else:
        print("*****************INSTALLATION LIBRE OFFICE EN COURS************************")
        os.chdir(r"C:\toto\2.Win_install")
        os.system("MsiExec.exe /i LibreOffice_7.1.4_Win_x64.msi RebootYesNo=No /qn")
        print("###########################LIBRE OFFICE INSTALLÉ###########################")



 
print("##########################INSTALLATION DES LOGICIELS DE BASE#################################")


liste1 = ["vlc","notepad","winrar","zip7","zoom","chrome","opera","adobeReader","office365","teams","java","libreoffice"]                       
liste2 = ["VideoLAN","Notepad++","WinRAR","7-Zip","Zoom","Google","Opera","Adobe","Microsoft Office","Microsoft","Java","LibreOffice"]

liste1 = liste2


test_vlc()  #Appel de la fonction défini plus haut
test_notepadd()
test_winrar()
test_zip7()
test_zoom()
test_chrome()
test_opera()
test_adobe_reader()
test_teams()
test_java()
test_office365()
test_libreoffice()

print("##########################INSTALLATION DES LOGICIELS TERMINÉ#################################")
