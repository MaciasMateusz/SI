import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

#input
currency1 = 'USD'
currency2 = 'DKK'
dateFrom = '2019-01-01'
dateTo = '2019-01-10'

#stworzenie metody do sprawdzenia waluty i użycie jej
def checkCurrency(currency,beg,end):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + currency + "/" + dateFrom + "/" + dateTo + "/"
    currency_req = requests.get(url)
    currency_data = currency_req.json()
    return currency_data['rates']
rate1 = checkCurrency(currency1,dateFrom,dateTo)
rate2 = checkCurrency(currency2,dateFrom,dateTo)

# Ograniczenie do pierwszych 10 wpisów i ustawienie indexu na date
rateData1 = pd.DataFrame.from_dict(rate1).head(10)
rateData2 = pd.DataFrame.from_dict(rate2).head(10)
plotData1 = rateData1.set_index(['effectiveDate'])['mid']
plotData2 = rateData2.set_index(['effectiveDate'])['mid']

# Użycie funkcji obliczającej korelację dwóch kursów, oraz narysowanie wykresu
correlation = np.corrcoef (plotData1, plotData2)[0][1]
plt.plot(plotData1, 'g--', plotData2,'b--')
plt.ylim(ymin=0)
plt.title('Korelacja {} do {} = {}'.format(currency1, currency2, correlation))
plt.ylabel('PLN')
plt.xlabel('Data')
plt.legend([currency1, currency2], loc='lower right')
plt.show()