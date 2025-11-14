#!/usr/bin/env python3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path

html = '<html><body><p>Lorem ipsum<p>äöü ...</body></html>'
subj = 'Mail mit Foto äöü'
frm  = 'Sender mit äöü <bla@bla.com>'
to   = 'Empfänger mit äöü <bla@blabla.com>'
frm  = 'Michael <michael.kofler@gmx.com>'         
to   = 'Kontakt <kontakt@kofler.info>'


try:
    # E-Mail zusammenstellen
    mail = MIMEMultipart()
    mail['Subject'] = subj
    mail['From']    = frm
    mail['To']      = to
    mail.attach(MIMEText(html, 'html'))

    # Datei mit Foto hinzufügen; foto.jpg aus dem Verzeichnis lesen, 
    # in dem sich auch die Code-Datei befindet
    srcpath = Path(__file__).parent.absolute()
    fname = srcpath.joinpath('foto.jpg')
    with open(fname, 'rb') as f:
        img = MIMEImage(f.read())
    mail.attach(img)

    # E-Mail mit lokalem Mail-Server versenden
    # ersetzen Sie hostname, login und password
    # durch geeignete Zeichenketten!
    #smtp = smtplib.SMTP('hostname')
    #smtp.starttls()
    #smtp.login('login', 'password')

    smtp = smtplib.SMTP('mail.gmx.net')
    smtp.smtpport = 465
    smtp.starttls()
    smtp.login('michael.kofler@gmx.com', 'rHgmxnet1234')  


    smtp.sendmail(frm, [to], mail.as_string())
    smtp.quit()
except BaseException as ex:
    print('Fehler:', ex)
    
