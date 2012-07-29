'''
Created on 2012-7-29

@author: Administrator
'''
import sys
from PyQt4 import QtGui,QtCore

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
        self.setWindowTitle("Menu & Toolkit")
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
        ''' tool bar'''
        #self.comm_bar = self.addToolBar("comm_bar")
        #self.comm_bar.addAction(exitAction)
        
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

    def trayClick(self,reason):
        if reason==QtGui.QSystemTrayIcon.DoubleClick: 
            self.show()
        elif reason==QtGui.QSystemTrayIcon.MiddleClick: 
            self.show()
          
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
    sys.exit(app.exec_());
    
