# ****************
# PyAero settings
# ****************

# path to PyAero installation
PYAEROPATH = '.'

# set locale for decimal separators
# can be either 'C' or ''
# if string is empty than system default locale is used
LOCALE = 'C'

# airfoil chord length
CHORDLENGTH = 1.

# path to icons
ICONS = '../icons/'
ICONS_S = ICONS + '16x16/'
ICONS_L = ICONS + '24x24/'

# path to data (e.g. airfoil coordinate files)
# path can be absolute or relative (to position where starting PyAero)
AIRFOILDATA = '../data'

# set the filter for files to be shown in dialogs
DIALOGFILTER = 'Airfoil contour files (*.dat *.txt);;STL files (*.stl)'

# set the filter for files to be shown in the airfoil browser
FILEFILTER = ['*.dat', '*.txt', '*.msh']

# set anchor for zooming
# 'mouse' means zooming wrt to mouse pointer location
# 'center' means zooming wrt to the view center
ZOOMANCHOR = 'mouse'

# visibility of scroolbars in graphicsview (True, False)
SCROLLBARS = False

# background of graphicsview ('solid', 'gradient')
VIEWSTYLE = 'gradient'

# set zoom limits so that scene is always in meaningful size
MINZOOM = 100.0
MAXZOOM = 10000.

# scale increment
SCALEINC = 1.1

# logging color
LOGCOLOR = '#1763E7'
