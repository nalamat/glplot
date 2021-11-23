#!/usr/bin/env python

'''Run demo.


This file is part of glplot <https://github.com/nalamat/glplot>
Copyright (C) 2017-2021 Nima Alamatsaz <nima.alamatsaz@gmail.com>
'''

import sys
import logging
import glplot      as     glp
from   PyQt5       import QtCore, QtGui, QtWidgets

log = logging.getLogger(__name__)

def masterExceptionHook(exctype, value, traceback):
    if exctype in (SystemExit, KeyboardInterrupt):
        log.info('Exit requested with "%s"' % exctype.__name__)
    else:
        log.exception('Uncaught exception occured',
            exc_info=(exctype, value, traceback))
    log.info('Exiting application')
    sys.exit(1)
sys._excepthook = sys.excepthook
sys.excepthook  = masterExceptionHook

glp.setSurfaceFormat()

app = QtWidgets.QApplication([])
app.setApplicationName = 'GLPlot Demo'
# app.setWindowIcon(QtGui.QIcon(config.APP_LOGO))

demo = glp.DemoWindow()
demo.show()

app.exec_()
