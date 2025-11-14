#!/usr/bin/env python3

import urllib.request
import sys

try:
    # Leseprobe Hacking-Buch
    url       = 'https://s3-eu-west-1.amazonaws.com/gxmedia.galileo-press.de/leseproben/5841/leseprobe_rheinwerkverlag_datenbanksysteme_%E2%80%93_das_umfassende_lehrbuch.pdf'
    chunksize = 64 * 1024  # 64 kByte
    response  = urllib.request.urlopen(url)
    with open('leseprobe.pdf', 'wb') as f:
        while True:
            chunk = response.read(chunksize)
            if not chunk: break
            f.write(chunk)
            # Feedback
            print('+', end='')
            sys.stdout.flush()
        print()

except BaseException as ex:
    print('Fehler:', ex)
    




