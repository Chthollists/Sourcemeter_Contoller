import sys,re
from PyQt5 import QtCore, QtGui, QtWidgets

from bsp_visa import Visa_Bridge

import numpy as np
import time
import os

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


def frange(x, y, jump):
    while x <= y:
        yield x
        x += jump

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 594)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 341, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.splitter_6 = QtWidgets.QSplitter(self.formLayoutWidget)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.Online_Plt_checkBox = QtWidgets.QCheckBox(self.splitter_6)
        self.Online_Plt_checkBox.setObjectName("Online_Plt_checkBox")
        self.Meas_pushButton = QtWidgets.QPushButton(self.splitter_6)
        self.Meas_pushButton.setObjectName("Meas_pushButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.splitter_6)
        self.Input_Splitter = QtWidgets.QSplitter(self.formLayoutWidget)
        self.Input_Splitter.setOrientation(QtCore.Qt.Vertical)
        self.Input_Splitter.setObjectName("Input_Splitter")
        self.splitter_1 = QtWidgets.QSplitter(self.Input_Splitter)
        self.splitter_1.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_1.setObjectName("splitter_1")
        self.Input_Lab_1 = QtWidgets.QLabel(self.splitter_1)
        self.Input_Lab_1.setObjectName("Input_Lab_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.splitter_1)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.splitter_2 = QtWidgets.QSplitter(self.Input_Splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.Input_Lab_2 = QtWidgets.QLabel(self.splitter_2)
        self.Input_Lab_2.setLineWidth(0)
        self.Input_Lab_2.setObjectName("Input_Lab_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.splitter_3 = QtWidgets.QSplitter(self.Input_Splitter)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.lineEdit_3 = QtWidgets.QLabel(self.splitter_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Input_Lab_3 = QtWidgets.QLineEdit(self.splitter_3)
        self.Input_Lab_3.setText("")
        self.Input_Lab_3.setObjectName("Input_Lab_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Input_Splitter)
        self.Mode_Sel_Splitter = QtWidgets.QSplitter(self.formLayoutWidget)
        self.Mode_Sel_Splitter.setOrientation(QtCore.Qt.Horizontal)
        self.Mode_Sel_Splitter.setObjectName("Mode_Sel_Splitter")
        self.Step_radioButton = QtWidgets.QRadioButton(self.Mode_Sel_Splitter)
        self.Step_radioButton.setObjectName("Step_radioButton")
        self.Step_radioButton.setChecked(True)
        self.Num_radioButton = QtWidgets.QRadioButton(self.Mode_Sel_Splitter)
        self.Num_radioButton.setObjectName("Num_radioButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Mode_Sel_Splitter)
        self.MeasProgressBar = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.MeasProgressBar.setProperty("value", 0)
        self.MeasProgressBar.setObjectName("MeasProgressBar")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.MeasProgressBar)
        self.splitter_5 = QtWidgets.QSplitter(self.formLayoutWidget)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter = QtWidgets.QSplitter(self.splitter_5)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.lineEdit_AvfTime = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_AvfTime.setObjectName("lineEdit_AvfTime")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_2 = QtWidgets.QLabel(self.splitter_4)
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.splitter_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.splitter_5)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 210, 761, 341))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_plot = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_plot.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_plot.setObjectName("horizontalLayout_plot")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(379, 9, 401, 191))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_data = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_data.setContentsMargins(0, 0, 0, 0)
        self.formLayout_data.setObjectName("formLayout_data")
        self.tableWidget = QtWidgets.QTableWidget(self.formLayoutWidget_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.formLayout_data.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tableWidget)
        self.splitter_7 = QtWidgets.QSplitter(self.formLayoutWidget_2)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.data_save = QtWidgets.QPushButton(self.splitter_7)
        self.data_save.setObjectName("data_save")
        self.data_clear = QtWidgets.QPushButton(self.splitter_7)
        self.data_clear.setObjectName("data_clear")
        self.formLayout_data.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.splitter_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.redefineUiEvents()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.volt=None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Online_Plt_checkBox.setText(_translate("MainWindow", "Plot"))
        self.Meas_pushButton.setText(_translate("MainWindow", "Measure"))
        self.Input_Lab_1.setText(_translate("MainWindow", "Start"))
        self.Input_Lab_2.setText(_translate("MainWindow", "Step"))
        self.lineEdit_3.setText(_translate("MainWindow", "End"))
        self.Step_radioButton.setText(_translate("MainWindow", "Step"))
        self.Num_radioButton.setText(_translate("MainWindow", "Num"))
        self.label.setText(_translate("MainWindow", "Avg Times"))
        self.lineEdit_AvfTime.setText(_translate("MainWindow", "16"))
        self.label_2.setText(_translate("MainWindow", "dt"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.01"))
        self.data_save.setText(_translate("MainWindow", "Save"))
        self.data_clear.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.horizontalLayout_plot.addWidget(dynamic_canvas)

        self._dynamic_ax = dynamic_canvas.figure.subplots()
        #self._timer = dynamic_canvas.new_timer(
        #    50, [(self._update_canvas, (), {})])
        #self._timer.start()


    def _update_canvas(self):
        if self.Online_Plt_checkBox.isChecked():
            self._dynamic_ax.clear()
            '''
            t = np.linspace(0, 10, 101)
            # Shift the sinusoid as a function of time.
            self._dynamic_ax.plot(t, np.sin(t + time.time()))
            '''
            if self.volt:
                self._dynamic_ax.plot(self.volt, self.sour_curr)
                self._dynamic_ax.figure.canvas.draw()
        else:
            self._dynamic_ax.clear()
            self._dynamic_ax.figure.canvas.draw()


    def redefineUiEvents(self):
        self.Num_radioButton.toggled.connect(self.mode_selectEvent_Num)
        self.Meas_pushButton.clicked.connect(self.measure_Event)
        self.data_clear.clicked.connect(self.clear_Event)
        self.data_save.clicked.connect(self.save_Event)


    def mode_selectEvent_Num(self,b):
        if b==True:
            self.Input_Lab_2.setText('Points')
        else:
            self.Input_Lab_2.setText('Step')


    def measure_Event(self):
        #print('Measure')
        try:
            self.inputparam=[]
            self.inputparam.append(float(self.lineEdit_1.text()))
            self.inputparam.append(float(self.lineEdit_2.text()))
            self.inputparam.append(float(self.Input_Lab_3.text()))
            self.inputparam.append(float(self.lineEdit_4.text()))
            self.inputparam.append(float(self.lineEdit_AvfTime.text()))
            #print(self.inputparam)
            if self.Step_radioButton.isChecked()==True:
                self.volt=list(frange(self.inputparam[0],self.inputparam[2],self.inputparam[1]))
            if self.Num_radioButton.isChecked()==True:
                self.volt=list(np.linspace(self.inputparam[0],self.inputparam[2],int(self.inputparam[1])))

            if self.volt:
                #print(self.volt)
                self.Meas_pushButton.setEnabled(False)
                self.tableWidget.clear()
                self.tableWidget.setRowCount(len(self.volt))
                self.tableWidget.setColumnCount(3)
                self.tableWidget.setHorizontalHeaderLabels(['Voltage','Source_Current','Gate_Current'])
                #progress=0
                self.dt=self.inputparam[3]
                self.avg_time=int(self.inputparam[4])
                self.gate_curr=[]
                self.sour_curr=[]

                '''
              Open a sub-thread to measure 
              and a handler in main thread to update the UI
                '''
                self.thread=MyThread(volt=self.volt,dt=self.dt,avg_time=self.avg_time)
                self.thread.thread_update_signal.connect(self.threadupdate) # 线程发过来的信号挂接到槽：update
                self.thread.start()



                self.data_save.setEnabled(True)
                self.Meas_pushButton.setEnabled(True)

        except ValueError:
            print('Value Error')


    def threadupdate(self,index,volt_length,volt,gate_curr,sour_curr):

        self.tableWidget.setItem(index,0,QtWidgets.QTableWidgetItem('%.4f' %volt))
        self.tableWidget.setItem(index,1,QtWidgets.QTableWidgetItem('%e' %sour_curr))
        self.tableWidget.setItem(index,2,QtWidgets.QTableWidgetItem('%e' %gate_curr))

        self.gate_curr.append(gate_curr)
        self.sour_curr.append(sour_curr)

        self.MeasProgressBar.setValue(int((index+1)*100/volt_length))
        if index==len(self.volt)-1:
            self.thread.terminate()
            self._update_canvas()




    def clear_Event(self):
        self.tableWidget.clear()
        self.volt=None
        self.gate_curr=None
        self.sour_curr=None
        self.data_save.setEnabled(False)


    def save_Event(self):
        try:
            fileName1, filetype = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget,
                                                                        "选取文件",
                                                                        "./",
                                                                        "Coma Split Files (*.csv)")
            if fileName1:
                f=open(fileName1,'w')
                f.write('Average_times:%d,dt=%f(s)\n' %(self.avg_time,self.dt))
                f.write('Volt(V),Gate_Current(A),Source_Current(A)\n')
                for i in range(len(self.volt)):
                    f.write('%s,%s,%s\n' %(self.volt[i],self.gate_curr[i],self.sour_curr[i]))
        except IOError:
            print('Wirte Data File Error.')
        finally:
            if f:
                f.close()

class MyThread(QtCore.QThread):

    thread_update_signal = QtCore.pyqtSignal(int,int,float,float,float) # 信号类型：int

    def __init__(self, volt=None, dt=0.1, avg_time=16, parent=None):
        super().__init__(parent)
        self.avg_time=avg_time
        self.volt=volt
        self.dt=dt
        self.avg_time=avg_time
        self.Visa_Bridge=Visa_Bridge()

    def run(self):
        for index in range(len(self.volt)):
            sour_curr_sum=0.0
            gate_curr_sum=0.0
            try:
                for cnt in range(self.avg_time):
                    res=self.Visa_Bridge.gate_test(volt=self.volt[index])
                    print(res)
                    if isinstance(res,list):
                        sour_curr_sum=sour_curr_sum+res[0];
                        gate_curr_sum=gate_curr_sum+res[1];
                    time.sleep(round(self.dt/self.avg_time,4))
                self.thread_update_signal.emit(index,len(self.volt),
                    self.volt[index],gate_curr_sum/self.avg_time,sour_curr_sum/self.avg_time)  #发射信号
            except Exception as e:
                print(e)


            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    UI = QtWidgets.QMainWindow()
    MainUI = Ui_MainWindow()
    MainUI.setupUi(UI)
    UI.show()
    sys.exit(app.exec_())

