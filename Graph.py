from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import requests
import json
import matplotlib.pyplot as plt
import numpy as np


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        #hour = [1,2,3,4,5,6,7,8,9,10]
        #temperature = [30,32,34,32,33,31,29,32,35,45]

        time = requests.get('http://localhost:8000/time')
        ini_pos1 = requests.get('http://localhost:8000/ini_pos1')
        ini_pos2 = requests.get('http://localhost:8000/ini_pos2')
        #Fin_LDR1 = requests.get('http://localhost:8000/Fin_LDR1')
        #Fin_LDR2 = requests.get('http://localhost:8000/Fin_LDR2')
        #Fin_LDR3 = requests.get('http://localhost:8000/Fin_LDR3')
        #Fin_LDR4 = requests.get('http://localhost:8000/Fin_LDR4')
        #VIn_AADAT = requests.get('http://localhost:8000/VIn_AADAT')

        #print(x.text)

        ini_pos1_y = json.loads(ini_pos1.text)
        #print(s.replace('a', ''))
        ini_pos1_y = ini_pos1_y.replace('{', '')
        ini_pos1_y = ini_pos1_y.replace('}', '')
        ini_pos1_y = ini_pos1_y.replace('[', '')
        ini_pos1_y = ini_pos1_y.replace(']', '')
        ini_pos1_y = ini_pos1_y.replace('"ini_pos1":', '')
        ini_pos1_y = ini_pos1_y.replace('"', '')

        ini_pos1_y_list = ini_pos1_y.split(",")
        #print(ini_pos1_y_list.__len__())


        ######
        ini_pos2_y = json.loads(ini_pos2.text)
        #print(s.replace('a', ''))
        ini_pos2_y = ini_pos2_y.replace('{', '')
        ini_pos2_y = ini_pos2_y.replace('}', '')
        ini_pos2_y = ini_pos2_y.replace('[', '')
        ini_pos2_y = ini_pos2_y.replace(']', '')
        ini_pos2_y = ini_pos2_y.replace('"ini_pos2":', '')
        ini_pos2_y = ini_pos2_y.replace('"', '')

        ini_pos2_y_list = ini_pos2_y.split(",")




        ####

        y = json.loads(time.text)
        #print(s.replace('a', ''))
        y = y.replace('{', '')
        y = y.replace('}', '')
        y = y.replace('[', '')
        y = y.replace(']', '')
        y = y.replace('"Time":', '')
        y = y.replace('"', '')

        letter_list = y.split(",")

        #print(y)
        # plot data: x, y values
    
        for i in range(0, len(ini_pos2_y_list)):
            ini_pos2_y_list[i] = int(ini_pos2_y_list[i])

        plt.plot(letter_list, ini_pos2_y_list)
        plt.show()
        #self.graphWidget.plot(letter_list,  ini_pos2_y_list)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()