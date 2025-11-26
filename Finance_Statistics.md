# Compound Annual Growth Rate (durchschnittliche jährliche Wachstumsrate):$$
\text{CAGR} = \left( \frac{P_{\text{End}}}{P_{\text{Start}}} \right)^{\frac{1}{\frac{T_{\text{End}} - T_{\text{Start}}}{365.25}}} - 1
$$
Die Compound Annual Growth Rate (CAGR) bezeichnet auf Deutsch die durchschnittliche jährliche Wachstumsrate. Sie gibt an, wie viel ein Wert (z. B. Umsatz, Investment oder Unternehmenswert) im Durchschnitt pro Jahr über einen bestimmten Zeitraum gewachsen ist, wobei Schwankungen innerhalb der Jahre durch die CAGR geglättet werden. 

- in Python: (Tabelle.Preisspalte.iloc[-1]/Tabelle.Preisspalte.iloc[0])**(1/((Tabelle.index[-1]-Tabelle.index[0]).days/365.25))-1


# Simple Return (Einfache Rendite):  $$R=\left( \frac{P_{neu}-P_{alt}}{P_{alt}}\right)

$$
- Es ist zu beachten, dass die prozentuale Änderung nicht additiv ist. Unterschiedliche Perioden sind durch Addition, somit nicht zu vergleichen.
# Logarithmic Return (Logarithmische Rendite):  $$ r = \ln \left( \frac{P_{\text{neu}}}{P_{\text{alt}}} \right) $$
- Anders als die einfache Rendite (Simple Return) ist die logarithmische Rendite Additiv. Gerade die Addition führt zu den richtigen prozentualen Änderungen wohingegen r für sich alleingesehen ein falsches Ergebnis liefert und nicht die eigentliche prozentuale Änderung anzeigt, lediglich nur den logarithmischen Wert.
# Eulerische Zahl: $$( e = \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n ) $$
# Prozentuale Veränderung der Log-Perioden: $$e^r-1$$
- Der Logarithmic Return "r" gibt nicht die reale prozentuale Veränderung an, weshalb die eulerische Zahl mit r potenziert wird und anschließend die Eins subtrahiert werden muss.

# Zinseszins (without frequency):$$Future~Value=Present~Value*\left( 1+r\right)^{(n)}$$
# Barwert$$Present~Value=\frac{Future~Value}{(1+r)^n}$$
# Effective Annual Rate (Effektiver Jahreszins):$$r=\left( \frac{Future~Value}{Present~Value} \right)^{1/n}-1$$
# Laufzeit-Umstellung / Periodenformel:$$n=\frac{\log\left( \frac{Future~Value}{Present~Value} \right)}{\log(1+r)}$$
