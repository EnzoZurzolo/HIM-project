# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:43:45 2023

@author: EZ2
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
import sys
#from txtbox import * 
import requests  
import csv

from PyQt5.QtCore import pyqtSlot




url = "https://raw.githubusercontent.com/devw/spen/main/src/Multiple-Choice-Quiz.csv"

lign =1
def read_csv_from_internet(url):
    response = requests.get(url)
    lines = response.text.splitlines()
    reader = csv.reader(lines)
    return reader

def check_question_type(url,lign):
    
    reader = read_csv_from_internet(url) 
    c=0
    for row in reader:

        if c == lign:
            if row[0]== 'radio':
                return 1

            elif  row[0]== 'checkbox':
                return 2

            elif  row[0]== 'text':
                return 3

        elif c == row[-1]:
            return 4
        else :
            c+=1

def questionask(url,lign):
    reader = read_csv_from_internet(url)
    c=0
    for raw in reader:
        if c == lign:
            question_ask = raw[1]
            return question_ask  
        else :
            c+=1
def trueAnswer(url,lign):
    reader = read_csv_from_internet(url)
    c=0
    for raw in reader:
        if c == lign:
            true_answer = raw[3]
            return true_answer  
        else :
            c+=1

        
class GUI(QWidget):  
    def __init__(self):

        super().__init__()
        
          
        if check_question_type (url,lign) == 2 :
            self.checkbox()

        elif check_question_type (url,lign) == 1:
            self.radiobutton()

        elif check_question_type (url,lign) == 3:
            self.txt()

        else:
            sys.exit()
          
    
        
    def checkbox(self):
        self.title = 'PyQt absolute positioning - pythonspot.com'

        self.setWindowTitle(self.title)
        
        label = QLabel(questionask(url,lign), self)
        label.move(10,0)

        vbox = QVBoxLayout()
        checkbox1 = QCheckBox('paris')
        checkbox2 = QCheckBox('lille')
        checkbox3 = QCheckBox('bordeau')
        checkbox4 = QCheckBox('tour')
        vbox.addWidget(label)
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(checkbox3)
        vbox.addWidget(checkbox4)

        button = QPushButton('verify', self)
        button.setToolTip('This is an example button')
        vbox.addWidget(button)
        button.clicked.connect(self.on_click)
        self.setLayout(vbox)
        self.show()
    
    
    def radiobutton(self):  
        layout = QGridLayout()     
        
        self.title = 'PyQt absolute positioning - pythonspot.com'

        self.setWindowTitle(self.title)
        
        label = QLabel(questionask(url,lign), self)
        layout.addWidget(label, 0, 0)
        
        radiobutton = QRadioButton("Australia")
        radiobutton.setChecked(True)
        radiobutton.country = "Australia"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 1, 0)

        radiobutton = QRadioButton("China")
        radiobutton.country = "China"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 2, 0)
            
        radiobutton = QRadioButton("Japan")
        radiobutton.country = "Japan"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 3, 0)
        
        radiobutton = QRadioButton("Japan")
        radiobutton.country = "Japan"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 4, 0)
        
        button = QPushButton('verify', self)
        button.clicked.connect(self.on_click)
        layout.addWidget(button, 5, 0)       
        self.setLayout(layout)
        self.show()


    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Country is %s" % (radioButton.country))

    
    def txt(self):
     
        e4 = QLineEdit()
        e4.textChanged.connect(self.textchanged)
        flo = QFormLayout()
        button = QPushButton('verify', self)
        flo.addRow(questionask(url,lign),e4)
        flo.addRow(button)
        e4.editingFinished.connect(self.enterPress)
        button.clicked.connect(self.on_click)
        self.setLayout(flo)
        self.setWindowTitle("QLineEdit Example")
        self.show()   
    
 
    def textchanged(self,text):
        print("Changed: " + text)


    def enterPress(self):
        print ('test enter')
                
        
    def checkboxStateChanged(self):
        sender = self.sender()
        if sender.isChecked():
            print(sender.text() + ' checked')
        else:
            print(sender.text() + ' unchecked')
                

    def radioButtonToggled(self):
        sender = self.sender()
        if sender.isChecked():
            print(sender.text() + ' selected')


    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        app.exec()
        
while lign <6:
    print(questionask(url,lign))
    print(trueAnswer(url,lign))
    app = QApplication([])
    gui = GUI()
    app.exec()
    lign +=1
