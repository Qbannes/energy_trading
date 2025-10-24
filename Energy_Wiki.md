
# **Merit-Order**

Die Merit-Order ist die Einsatzreihenfolge stromproduzierender Kraftwerke auf einem Stromhandelsplatz. Die Merit-Order orientiert sich nach den niedrigsten Grenzkosten. 
Kraftwerke mit den niedrigsten Grenzkosten werden zuerst zugeschaltet. Das letzte berücksichtigte oder auch zugeschaltete Kraftwerk ist das sogenannte Grenzkraftwerk.

| Kraftwerk    | Grenzkosten (€/MWh) | Angebotsmenge (MWh) |
| ------------ | ------------------- | ------------------- |
| Windpark     | 0                   | 30                  |
| Braunkohle   | 20                  | 40                  |
| Steinkohle   | 40                  | 20                  |
| Gaskraftwerk | 60                  | 10                  |
Würden nun 90 MWh benötigt, so würden der Höhe ihre Grenzkosten, der Windpark, dann das Braunkohlekraftwerk und zuletzt als sogenanntes Grenzkraftwerk das Steinkohlekraftwerk zugeschaltet werden.  
## **Preisbildung**

Die Schnittstelle von Angebot und Nachfrage bilden den Börsenpreis an der Strombörse. Beim sogenannten Market-Clearing-Price bzw. Markträumungspreis erhält das letzte Angebot den Zuschlag. Das Kraftwerk mit den teuersten Grenzkosten definiert den Börsenpreis für alle eingesetzten Kraftwerke. Nach der obigen Tabelle und einem Strombedarf von 100MWh/h würde das Grenzkraftwerk hier den Preis definieren. 
## **Merit-Order-Effekt**

Dieser Effekt ändert die herkömmliche Reihenfolge der Kraftwerke durch das stetige Sinken von Stromproduktionskosten. Die Wachsende Einspeisung von erneuerbarer Energie (Photovoltaik, Windenergie, Biomasse) verdrängt die konventionellen Spitzenlastkraftwerke nach hinten und diese werden dadurch weniger gebraucht. Dieser Effekt wird als Merit-Order-Effekt bezeichnet. 
Lediglich die [Residuallast](C:\Users\bedla\Documents\Ausbildung_Informatik\1_Praktikum\Praktikum_Daten-_und_Prozessanalyse\energy_trading\Energiewirtschaft_Wörterbuch.md) - der verbleibende Stromverbrauch nach Abzug der erneuerbaren Energien - muss durch konventionelle Spitzenlastkraftwerke ausgeglichen werden.
![[energy_trading/Bilder/Merit-Order-Effekt_Diagramm.jpg]] 

Quelle: https://www.next-kraftwerke.de/wissen/merit-order
# **Strombörse**

In Europa gibt es zwei wesentliche Börsen für den Stromhandel. Einmal die EEX (European Energy Exchange AG) mit Sitz in Leipzig und die Tochter der EEX die EPEX (European Power Exchange) mit sitz in Paris. 
Ander EEX (Terminmarkt) werden Termingeschäfte getätigt, das bedeutet, dass dort langfristig Energie ein- und verkauft wird. Dort werden Energiemengen langfristig - monats-, quartals- und jahrweise - eingekauft, um zum Beispiel günstige Preise erzielen zu können. Neben dem Erzielen eines möglichst niedrigen Preises, wird durch den Kauf von Grundlastenergie (base) und Spitzenlastenergie (peak) der Bedarf gedeckt. Weiter gibt es auch Zwischenprodukte (Zwischenverlauf), die auch weiter außerbörslich gehandelt werden können.

An der EPEX (Spotmarkt) findet der kurzfristige Handel statt. Hier wird grundsätzlich in zwei Varianten des Handels unterschieden. Zum Einen zwischen day-ahead (ein Tag vor Nutzung) und intraday (am selben Tag -> halbe Stunde vor Nutzung). Somit kann Energie viertel- und stundenweise eingekauft werden. Die Preise sind hier deutlich höher als auf den Terminmärkten. 

Eine dritte Möglichkeit Strom zu handeln, besteht im OTC-Handel (over the couter). Hier wird der Strom mit einem Vertragspartner außerhalb der Strombörse geschlossen. Die Vertragspartner sind nicht an die Termine und Preise der Börse gebunden und können ihre Verträge individuell gestalten. Weiter können OTC-Geschäfte bis kurz vor Lieferung abgeschlossen werden, was gegenüber Börsen mehr Flexibilität bietet. Allerdings besteht bei dem OTC Kauf- und Liefergeschäft ein direktes Kontrahentenrisiko z.B. durch kurzfristigen Zahlungs- oder Lieferausfall.
OTC-Geschäfte müssen 15 Minuten vor Lieferung gemeldet werden. Bei regelzoneninterne Verträge (innerhalb der Bilanzzone) reicht die Meldung bis unmittelbar vor Lieferung.


![[handelsfristen_an_strommaerkten_NXK_021_ba54109f63.webp]]
Quelle:     https://www.youtube.com/watch?v=cmvuYbUjyxA 
	    https://www.next-kraftwerke.de/wissen/spotmarkt-epex-spot

# Arbitrage

Als Arbitrage wird das gleichzeitige Ausnutzen von Preisunterschieden des einen und desselben Guts auf unterschiedlichen Märkten bezeichnet. Voraussetzung hier ist, dass die Preisunterschiede auf den Teilmärkten die Transaktions- und Transformationskosten übersteigen, damit sich Gewinne realisieren lassen. Eine zentrale Eigenschaft der Arbitrage ist die des risikolosen Handels nahezu gleichzeitiger Ausführung von Kauf und Verkauf, was organisatorisch und technisch herausfordernd sein kann. Die Arbitrage trägt zur Harmonisierung der Preisunterschiede unter den Teilmärkten bei.

# Ask-Preis und Bid-Preis

Der Ask-Preis (Briefkurs) ist der niedrigste Preis, zudem ein Verkäufer bereit ist zu verkaufen. Der Bid-Preis (Geldkurs) ist der höchste Preis, zudem ein Käufer bereit ist zu kaufen.
Der Ask-Preis ist grundsätzlich immer höher als der Bid-Preis und die Spanne (spread) dazwischen beträgt in der Regel 1-2% je nach Volatilität und Liquidität des Marktes.

# Negative Strompreise

Negative Strompreise entstehen, wenn die Stromproduktion (Angebot) den Stromverbrauch (Nachfrage) übersteigt. Diese Preise treten meist bei einer zu hohen Einspeisung von Solar- und Windenergie auf. 

# 50hz-Netz

Das europäische Stromnetz hat eine Frequenz von 50 Herz. Das bedeutet, dass der Wechselstrom 50 mal in der Sekunde seine Richtung ändert. Die Einhaltung der 50 Herz sind ist entscheidend für die Netzstabilität. Um diesen Wert zu erhalten muss der Verbrauch in jedem Moment der Erzeugung entsprechen. 

## 49,8 und 50,2-Hertz-Problematik

Liegt ein Strommangel im Netz vor, sinkt die Frequenz und genauso umgekehrt. Das Verhältnis von Stromverbrauch und Stromerzeugung ist die Ursache für Schwankungen im Herzbereich. AB Werten von 49,8 und 50,2 greifen Sicherheitsmechanismen, die die Frequenz wieder auf 50 Herz zurückbringen.

### Abkopplung bei Unterfrequenz (Frequenz zu niedrig)

- Unter 49,80 Hz: Aktivierung zusätzlicher Erzeugungsleistung und Maßnahmen zur Frequenzstabilisierung.
    
- Unterschreitet die Frequenz 49,50 Hz, liegt die untere Grenze der im Normalbetrieb geduldeten Frequenzabweichung.
    
- Weiteres Sinken auf 49,00 Hz löst frequenzabhängigen Lastabwurf von ca. 10-15% der Verbraucher aus (Teil-Blackout).
    
- Bei 48,70 Hz und 48,40 Hz folgen weitere Lastabwürfe von jeweils 10-15%.
    
- Bei 47,50 Hz erfolgt gezielte Abtrennung von Netzsegmenten und Kraftwerken, was einem regionalen Blackout entspricht.
    

## Abkopplung bei Überfrequenz (Frequenz zu hoch)

- Ab 50,20 Hz beginnen viele regelbare Erzeugungsanlagen (z.B. PV, BHKW) ihre Leistung zu reduzieren.
    
- Die obere Grenze im Normalbetrieb liegt bei 50,50 Hz.
    
- Ab 51,00 Hz müssen neuere Kraftwerke mindestens 90 Minuten einsatzfähig bleiben, ältere Kraftwerke gehen vom Netz.
    
- Ab 51,50 Hz müssen alle regelbaren Kraftwerke ihre Stromerzeugung komplett einstellen.
    
- Ab 52,00 Hz gilt der Betriebszustand als unzulässig.

# Netzbetreiber

Als wichtiger Aktuer in der Energiewirtschaft ist der Netzbetreiber verantwortlich für den sicheren Betrieb. Sie überwachen das Stromnetz und stellen sicher, dass das Netz stets innerhalb seiner Kapazität arbeitet und die Nachfrage immer gedeckt ist. Auf den Märkten spielen sie eine ROlle für Ausgleichs- und Systemdienstleistungen.
## Übertragungsnetzbetreiber (ÜNB)


## Verteilungsnetzbetreiber (VNB)


# 4- bzw. 6-Stunden-Regel

Die 4- bzw. 6-Stunden-Regel führt dazu, dass EEG-geförderte Anlagen für die Zeiträume mit mindestens 4 bzw. 6 Stunden negativer Strompreise keine Marktprämie erhalten. Das beeinflusst sowohl, wann Anlagenbetreiber keine Einnahmen haben, als auch wann sie aus wirtschaftlichen Gründen eventuell den Strom nicht mehr einspeisen wollen.