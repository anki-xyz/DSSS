import sys  # System-specific parameters and functions

from PyQt5.QtWidgets import (QApplication, QFileDialog, QPushButton, QWidget,QMainWindow,
                             QLabel, QVBoxLayout, QShortcut, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QKeySequence, QImage
import imageio as io

# Preparing the environment for the image:
class ImageWidget(QLabel):
    def __init__(self):
        super().__init__() #super() is used to refer the superclass from the subclass.
        # In this case "ImageL" is a subclass of QLabel
    
        self.setAlignment(Qt.AlignCenter)   # The widget will be displayed in the center
        self.setText('Drop an image here')  # Text to help the user
        self.setStyleSheet('''
           QLabel{
                border-style: dashed;
                border-width: 2px;
                border-radius: 10px;
                border-color: #aaa;
                font: 14px
           }
        '''
        ) # style of the QLabel


    def setPixmap(self, im):
        super().setPixmap(im)




#Let's define our widget
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Drag and drop app')
        self.setMinimumSize(250, 300)

        ## ADD A MENU BAR
        self.menu = self.menuBar()

        # Main top menu
        self.file = self.menu.addMenu("&File")
        self.file.addAction("Open", self.open)
        self.file.addAction("Save", self.save)
        self.file.addAction("Close", self.close)


        ### SAVE YOUR IMAGE in self.im!
        self.im = None 

        
        # CREATE A CENTRAL WIDGET TO SHOW IMAGE
        w = QWidget(self)
        self.setCentralWidget(w)
        self.mainLayout = QVBoxLayout()
        w.setLayout(self.mainLayout)
        
  
        self.displayPicture = ImageWidget() #we configure the widget to add
        self.mainLayout.addWidget(self.displayPicture) # we add the widget to the window


        # TODO 
        # We want to bind the typical "Ctrl+S" to the save function:
        # self.ctrls_shortcut = QShortcut(QKeySequence("Your shortcut binding goes here"), self)
        # self.ctrls_shortcut.... <-- now bind the shortcut to the saving routine


    def setImage(self, im):
        self.displayPicture.setPixmap(QPixmap(im))

    def open(self):
        fn, _ = QFileDialog.getOpenFileName(filter="*.png;*.jpg")

        if fn:
            print(fn)
            self.im = io.imread(fn)
            self.setImage(fn)

    ###
    # TODO
    # Add code for drag & drop, use Google search
    ##

    def save(self):
        # TODO
        # Here comes the saving routine

        # If succeeded show a popup window/message box with information layout
        # otherwise a popup window/message box with critical layout
        pass
    

def main():

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()