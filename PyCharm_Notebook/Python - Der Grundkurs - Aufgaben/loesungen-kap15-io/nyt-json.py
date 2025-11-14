#!/usr/bin/env python3
import json
import urllib.request
# bitte besorgen Sie sich auf 
# https://developer.nytimes.com/signup einen
# eigenen Key!
url      = 'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=QlgA0FsRxaB2hDP4QGKjmaD2OOCaBrf0'
response = urllib.request.urlopen(url)
binary   = response.read()        # binäre Daten
txt      = binary.decode('utf-8') # als Text interpretieren
top15    = json.loads(txt)
books    = top15['results']['books']
for book in books:
    print('Title:\t', book['title'])
    print('Author:\t', book['author'])
    print('ISBN:\t', book['primary_isbn13'])
    print()

