'''
Created on 2012-7-29

@author: Administrator
'''
import sys
import ctypes
from ctypes import wintypes
import win32com
from PyQt4 import QtGui,QtCore
import hotkey
import pyHook

class Mtext(QtGui.QTextEdit):
    def mouseReleaseEvent(self,event):
        QtGui.QTextEdit.mouseDoubleClickEvent(self,event)
        #super(QtGui.QTextEdit,self).mouseDoubleClickEvent(event)
        if self.textCursor().hasSelection():
            self.copy()
        event.accept()
        
class MTExample(QtGui.QMainWindow): 
    def __init__(self):
        super(QtGui.QMainWindow,self).__init__()
        self.initUI()
        QtGui.QShortcut("Ctrl+Alt+1",self,self.trayClick)
       

    def closeEvent(self,event):
        
        if not self.trayIcon.realc:
            self.hide()
            event.ignore()
            
    def center(self):
        sg = self.frameGeometry()
        scg =  QtGui.QDesktopWidget().screenGeometry().center()
        sg.moveCenter(scg)
        self.move(sg.topLeft())
    
    def file_dialog(self):
        print 1
    def initUI(self):
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        '''Text Editor'''
        textEdit= Mtext()# QtGui.QTextEdit()
        QtCore.QObject.connect(textEdit,QtCore.SIGNAL("clicked"), self.file_dialog)
        self.setCentralWidget(textEdit)
        #widget = LayoutManagement.MTExample(self)
        #self.setCentralWidget(widget)
        ''' position & basic conf'''
        self.setGeometry(400,300,310,310)
        self.center()
        #self.statusBar().showMessage('&Ready')
        self.setWindowIcon(QtGui.QIcon('app.png'))
        self.setWindowTitle("P-ad")
        ''' menu bar action'''
        exitAction = QtGui.QAction("&Exit",self)
        #exitAction.triggered.connect(QtGui.qApp.quit)
        exitAction.triggered.connect( QtCore.QCoreApplication.instance().quit)
        #exitAction.triggered.connect(self.close_)
        exitAction.setStatusTip("Quit()")
        exitAction.setShortcut("Ctrl+Q")
        
        ''' menu bar'''
        #menubar = self.menuBar()
        #fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(exitAction)
        ''' about action'''
        aboutaction = QtGui.QAction('&About',self)
        aboutaction.triggered.connect(self.popabout)
        
        ''' tool bar'''
        self.comm_bar = self.addToolBar("comm_bar")
        self.comm_bar.addAction(aboutaction)
        
        ''''tray'''
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setIcon(QtGui.QIcon("app.png"))
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.trayClick) 
        self.trayIcon.setToolTip(u"front pad")
        self.trayIcon.realc = False
        ''' tray action'''
        traymenu = QtGui.QMenu()
        exitAction = traymenu.addAction("Exit")
        exitAction.triggered.connect(self.tray_close)
        self.trayIcon.setContextMenu(traymenu)
    def tray_close(self):
        self.trayIcon.realc = True
        QtCore.QCoreApplication.instance().quit()
    
    def close_(self):
        QtCore.QCoreApplication.instance().quit();

    def trayClick(self,reason='default'):
        #if reason==QtGui.QSystemTrayIcon.DoubleClick: 
        self.show()
        self.showNormal()
        #elif reason==QtGui.QSystemTrayIcon.MiddleClick: 
            #self.show()
    def quickd(self,mes):
        self.show()
        self.showNormal()
    def popabout(self):
        qd = QtGui.QDialog()
        qd.setWindowTitle('about')
        qd.setModal(True)
        qd.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        qd.setGeometry(400,400,200,100)
        lb = QtGui.QLabel(qd)
        lb.setText("qcpad:<b>00</b>")
        
        sg = qd.frameGeometry()
        scg =  QtGui.QDesktopWidget().screenGeometry().center()
        sg.moveCenter(scg)
        qd.move(sg.topLeft())
        
        qd.exec_()
        
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv);
    '''
    trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon("app.png"), app)
    menu = QtGui.QMenu()
    exitAction = menu.addAction("Show")
    trayIcon.setContextMenu(menu)
    '''
    mte = MTExample()
    mte.show();
    mte.trayIcon.show();
    
    hk = hotkey.hotkeyer(mte.quickd,mte)
    hm = pyHook.HookManager()
    hm.KeyDown = hk.OnKeyboardEvent
    hm.HookKeyboard()

    sys.exit(app.exec_());
    
