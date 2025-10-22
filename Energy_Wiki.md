
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

