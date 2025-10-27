import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = np.genfromtxt('Moores_Law.csv', delimiter=',', skip_header=1, usecols=(1, 2), dtype=float, filling_values=np.nan)
data = data[~np.isnan(data).any(axis=1)]

aar = data[:, 1]
transistor_antal = data[:, 0]

# Her beregner vi den naturlige logaritme af transistor antal, ja.. simpelthen simpelthen
log_transistor_antal = np.log(transistor_antal)

# Og her udfører vi så en lineær regression
slope, intercept, r_value, p_value, std_err = stats.linregress(aar, log_transistor_antal)

# Her laver vi så "forudsigelsen" for den linære regression, ved at tegne 100 punkter som er jævnt fordelt mellem minimum og maksimum af år
aar_tilpasset = np.linspace(aar.min(), aar.max(), 100)
log_transistor_tilpasset = slope * aar_tilpasset + intercept

# Her definierer vi konstanterne for Moore's lov, altså en fordobling hvert andet år hvor det starter med 2250 transistorer
a = 2250 # Startværdi i år 1971
b = 2 # Fordobling hvert andet år
c = 1971 # Startår

# Vi udregner AM og BM konstanterne
AM = np.log(b) / 2
BM = np.log(a) - AM * c

# Nu laver vi lambda funktionen for moore's lov
moores_lov = lambda year: np.exp(AM * year + BM)

# nu beregner moore's lov værdierne for alle årstallene
moores_vaerdier = moores_lov(aar)

# Og til sidst plotter vi det hele
plt.figure(figsize=(10, 6))
plt.yscale('log')
plt.scatter(aar, transistor_antal, color='blue', label='Datapunkter')
plt.plot(aar_tilpasset, np.exp(log_transistor_tilpasset), 'r-', label=f'Eksponentiel regression (R^2 = {r_value**2:.3f})')
plt.plot(aar, moores_vaerdier, 'g--', linewidth=2, label="Moore's lov (fordobling hvert 2 år)")
plt.xlabel('År')
plt.ylabel('Antal transistorer')
plt.title("Moore's lov vs. Datapunkter med regressioner")
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.show()