import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

from ressources.ui import Ui_MainWindow as CompiledUiWindow
from forms.c_local_gui import LocalDialog

from classes.c_student import Etudiant

class MainForm(QtWidgets.QMainWindow, CompiledUiWindow):
    def __init__(self, parent = None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Etudiant Manager")

        self.Programme_comboBox.addItem("Programmation et securiter")
        self.Programme_comboBox.addItem("Science nat")
        self.Programme_comboBox.addItem("Science humaine")
        self.Programme_comboBox.addItem("idk")


    def str_list_students(self):
        text = ""
        for student in Etudiant.lst_Etudiant:
            text += student.__str__()
        return text

    @pyqtSlot()
    def on_Modifier_pushButton_clicked(self):
        pass

    @pyqtSlot()
    def on_Supprimer_pushButton_clicked(self):
        pass

    @pyqtSlot()
    def on_Add_pushButton_clicked(self):
        nom = self.Nom_lineEdit.text().capitalize()
        prenom = self.Prenom_lineEdit.text().capitalize()
        matricule = self.MatriculelineEdit.text()
        naissance = self.Naissance_dateEdit.date()
        programme = self.Programme_comboBox.currentText()

        #instance
        et = Etudiant()

        try:
            # attribut setter
            et.nom = nom
            et.prenom = prenom
            et.matricule = matricule
            et.date_naissance = naissance
            et.programme = programme

            # ajouter a la liste quand toute les attributs sont set
            et.lst_ajouter()

        # handle les erreurs d'input parser dans la classe
        except ValueError as e:
            self.Error_label.setText(f"Erreur de valeur: {e}")

        else: # aucune erreur

            # ajouter la liste
            self.Etudiant_plainTextEdit.setPlainText(self.str_list_students())

            # clear out les textbox
            self.Nom_lineEdit.clear()
            self.Prenom_lineEdit.clear()
            self.MatriculelineEdit.clear()
            self.Naissance_dateEdit.clear()

    @pyqtSlot()
    def on_localmanager_open_clicked(self):
        local = LocalDialog(self)
        local.show()


