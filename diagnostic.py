from itom import dataIO
from itom import ui
from itom import dataObject
from itom import *
import numpy as np
import matplotlib.pyplot as plt
from itomUi import ItomUi

spectrometer = dataIO("AvantesAvaSpec", 6546, 1641)
camera =  dataIO("OpenCVGrabber") #change the camera depending on which ones we are using
win = ui("completeInterface.ui", ui.TYPEWINDOW, childOfMainWindow=True)


def show(self, modalLevel=0):
    self.gui.show(modalLevel)
    
def integrationTime_changed():
    time =win.timelineEdit["text"]
    spectrometer.setParam("integration_time",time)
        # if win.radio1["checked"]:
           # spectrometer.setParam("integration_time", 0.005)
        # elif win.radio2["checked"]:
           # spectrometer.setParam("integration_time", 0.010)
#   
        # spectrometer.setParam("integration_time", 0.060)


def snap():
    data = dataObject()
    spectrometer.startDevice()
    spectrometer.acquire()
    spectrometer.getVal(data)
    dataCopy = data.copy()
    

    plot(data, properties={"title": "Spectrometer snapshot","valueLabel":'Counts',"axisLabel":"Wavelength / nm"})

    data2 = dataObject()
    camera.startDevice()
    camera.acquire()
    camera.getVal(data2)
    dataCopy2 = data2.copy()
    plot(data2)
  
def live():
       d = dataObject()
       spectrometer.startDevice()
       spectrometer.acquire()
       spectrometer.getVal(d)
       liveImage(spectrometer)
       # properties={"title": "Spectrometer snapshot","valueLabel":'Counts',"axisLabel":'Wavelength / nm'} )

       d2 = dataObject()
       camera.startDevice()
       camera.acquire()
       camera.getVal(d2)
       liveImage(camera)# properties={"title": "Camera snapshot","valueLabel":'y position',"axisLabel":"x position"})
  
  

# initialize all signal/slots
# win.radio1.connect("clicked()", integrationTime_changed)
# win.radio2.connect("clicked()", integrationTime_changed)
# win.radio3.connect("clicked()", integrationTime_changed)

win.btnSnap.connect("clicked()", snap)
win.btnLive.connect("clicked()", live)
win.connectBtn.connect("clicked()", integrationTime_changed)


win.show(0)