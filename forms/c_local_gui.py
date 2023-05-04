import json
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot

from ressources.local_compiled import Ui_Dialog

from classes.c_locaux import Local_Normal, Local_Technique, lst_locals
from classes.c_local import Local

class LocalDialog(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, parent = None) -> None:

        super(LocalDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Local manager")

        self.comboBox.addItems(["Technique", "Normal"])
        self.comboBox.activated[str].connect(self.onActivatedText)

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

    @pyqtSlot(str)
    def onActivatedText(self, text):
        if text == "Normal":
            self.lineEdit_6.hide()
            self.lineEdit_7.hide()

        else:
            self.lineEdit_6.show()
            self.lineEdit_7.show()

    #save
    @pyqtSlot()
    def on_pushButton_3_clicked(self):

        for local in lst_locals:
            local.serialiser()
    
    #load
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        with open("ressources/classes.json", "r") as e:
            data = json.load(e)

        lst_locals.clear()
        
        for dict_class in data:

            if data[dict_class]["_type"] == "Normal":
                c_classe = Local_Normal()
                c_classe.deserialiser(dict_class)
            else:
                c_classe = Local_Technique()
                c_classe.deserialiser(dict_class)

            lst_locals.append(c_classe)

            str_classestr = str(c_classe).split("\n")
            for x in str_classestr:
                self.model.appendRow(QtGui.QStandardItem(x))

            self.model.appendRow(QtGui.QStandardItem("************************************************"))


    @pyqtSlot()
    def on_pushButton_clicked(self):

        gui_type_de_local = self.comboBox.currentText()
        gui_numero = self.lineEdit_2.text()
        gui_lieu = self.lineEdit_3.text()
        gui_dimension = self.lineEdit_4.text()
        gui_places = self.lineEdit_5.text()
        gui_marque = self.lineEdit_6.text()
        gui_nombre_ordi = self.lineEdit_7.text()

        if gui_type_de_local == "Technique":

            et = Local_Technique()

            try:
                et.type = gui_type_de_local
                et.numero = gui_numero
                et.lieu = gui_lieu
                et.dimension = int(gui_dimension)
                et.places = int(gui_places)
                et.marque_ordinateur = gui_marque
                et.nb_ordinateur = int(gui_nombre_ordi)

            except ValueError as e:
                self.label_8.setText(f"Erreur de valeur: {e}")
                return

        elif gui_type_de_local == "Normal":

            et = Local_Normal()

            try:

                et.type = gui_type_de_local
                et.numero = gui_numero
                et.lieu = gui_lieu
                et.dimension = int(gui_dimension)
                et.places = int(gui_places)

            except ValueError as e:
                self.label_8.setText(f"Erreur de valeur: {e}")
                return

        else:
            self.label_8.setText(f"Erreur de type de local")
            return

        str_classestr = str(et).split("\n")
        for x in str_classestr:
            self.model.appendRow(QtGui.QStandardItem(x))

        #self.model.appendRow(QtGui.QStandardItem("************************************************"))
        ## ajouter la liste
        #self.model.appendRow(QtGui.QStandardItem(f"Type: {et.type}"))
        #self.model.appendRow(QtGui.QStandardItem(f"Numero: {et.numero}"))
        #self.model.appendRow(QtGui.QStandardItem(f"Lieu: {et.lieu}"))
        #self.model.appendRow(QtGui.QStandardItem(f"Dimension: {str(et.dimension)}"))
        #self.model.appendRow(QtGui.QStandardItem(f"Places: {str(et.places)}"))
#
        #if et.type == "Technique":
        #    self.model.appendRow(QtGui.QStandardItem(f"Marque ordinateur: {str(et.marque_ordinateur)}"))
        #    self.model.appendRow(QtGui.QStandardItem(f"Nombre ordinateurs: {str(et.nb_ordinateur)}"))
#
        #self.model.appendRow(QtGui.QStandardItem("************************************************"))

        #save to lst
        lst_locals.append(et)
