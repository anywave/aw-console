import pyqtgraph as pg
from pyqtgraph.console import ConsoleWidget
import pickle

# make the app first
app = pg.mkQApp()

# just example of setting up some useful variables
namespace = {
    'data_path': '/foo/bar/c,rfDC',
}

# nice words
welcome_message = """
Welcome to the AnyWave console. Here you can experiment, using and
programming with the AnyWave API.
"""

# editor, could be useful, could be a preference?
editor = "gvim {fileName} +{lineNum}"

# make the widget
cw = ConsoleWidget(
    namespace=namespace,
    text=welcome_message,
    editor=editor,
)

# show it
cw.show()

# run
app.exec_()
