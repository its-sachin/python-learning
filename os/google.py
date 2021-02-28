import sys
import webbrowser

sys.argv
if len(sys.argv) > 1:
    tosearch = '+'.join(sys.argv[1:])
    address = 'http://www.google.co.in/search?q={}'.format(tosearch)
    webbrowser.open(address)