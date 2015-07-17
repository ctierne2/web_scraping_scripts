#! python2
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()
	
webbrowser.open('http://maps.google.com/maps/place/' + address)
	
# TODO: Get address from clipboard