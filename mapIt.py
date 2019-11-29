# Launches a map in the broswer using an address from the command line or clip board.
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)

# Remove the above line and uncomment the below line after replacing 'yourAddress' with your address to obtain the directions to
# address from your address instead. 

# webbrowser.open('http://www.google.com/maps/dir/yourAddress/ + address)