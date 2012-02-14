import sys
from PySide import QtCore, QtGui
from PySide.phonon import Phonon

def main():

    app = QtGui.QApplication([])
    app.setApplicationName('test_PySide_phonon')

    print "Qt plugin paths: " + unicode(list(app.libraryPaths()))
    print 'Qt Libraries path: ' + unicode(QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.LibrariesPath))

    try:
        media_source = Phonon.MediaSource('test_PySide_phonon.wav')

        media_object = Phonon.MediaObject()
        media_object.setCurrentSource(media_source)
        media_object.finished.connect(app.quit)

        audio_output = Phonon.AudioOutput(Phonon.NotificationCategory)

        Phonon.createPath(media_object, audio_output)

        media_object.play()
    
        status = app.exec_()

    except:
        status = 1

    return status

if __name__ == "__main__":
    sys.exit(main())
