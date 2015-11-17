from distutils.core import setup
import py2exe
import gio
setup(
           name = 'ValOpciones',
           description = 'Herramienta para valuar Opciones de Compra y Venta',
           version = '1.0',
           windows = [
                         {
                             'script': 'interfaz.py',
                             'icon_resources': [(1, "escudo.ico")],
                         }
                     ],
           options = {
                         'py2exe': {
                             'packages':'encodings',
                             'includes': 'cairo, pango, pangocairo, atk, gobject, gio',
                         }
                     },

                  data_files=[
                               'escudo.png',
                               'libreria.py',
                               'libreria.pyc'
                             ]
             )

