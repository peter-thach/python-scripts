# Python Scripts

A collection of scripts made with Python made for fun in order to automate tasks.

## mapIt.py

A script that allows the user to open a Google Maps page to an address provided either in the command line or from the user's clipboard. 
Optionally, instead of using

```
webbrowser.open('http://www.google.com/maps/place/' + address)
```

the user can opt to use 

```
webbrowser.open('http://www.google.com/maps/dir/yourAddress/ + address)
```

after having replaced 'yourAddress' in the URL with their address to open up a Google Maps page with the directions from their origin to their destination.