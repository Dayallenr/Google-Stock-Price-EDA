import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


google = pd.read_csv('/Users/dayallenragunathan/Downloads/googl_data_2020_2025.csv')


print(google.duplicated().sum())
print(google.isna().sum())


print(google.head())


google.dropna(subset='Adj Close', inplace=True)
print(google.isna().sum())


print(google.head())


pd.options.display.max_columns = 20
'''or
pd.set_option('max_columns', 20)'''

#clean first two rows
google.drop(index = 0, inplace = True)

#change col names
google.rename(columns={'Price':'Date'}, inplace = True)

#change date column to proper format
google['Date'] = pd.to_datetime(google['Date']).dt.strftime('%Y-%m-%d')

print(google.head())


numeric_cols = ["Adj Close", "Close", "High", "Low", "Open", "Volume"]

# Convert columns to float
google[numeric_cols] = google[numeric_cols].apply(pd.to_numeric, errors="coerce")


print(google.dtypes)


#Compute daily price change (%)

google["Price Change (%)"] = google["Close"].pct_change() * 100
google.dropna(inplace=True)

print(google.head())

correlation = google['Close'].corr(google['Price Change (%)'])
print(f'Correlation between Closing Price and Price Change is {correlation:.3f}')

if correlation >= 0.5:
    print('Correlation is positive')
elif correlation <= -0.5:
    print('Correlation is negative')
else:
    print('No Correlation')

#Plot 1
plt.subplot(2, 1, 1)
plt.plot(google.index, google['Close'], label = 'Closing Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Google Stock Closing Price over Time')
plt.legend()

#Plot 2
plt.subplot(2, 1, 2)
plt.hist(google['Price Change (%)'], bins = 50, color = 'hotpink')
plt.xlabel('Price Change')
plt.ylabel('Frequency')
plt.title('Google Stock Price Change Distribution')


plt.tight_layout()
plt.show()


#Plot 2
plt.plot(google.index, google['High'], label = 'Highest Price', color = 'hotpink')
#Plot 1
plt.plot(google.index, google['Close'], label = 'Closing Price', alpha = 0.7)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Google Stock Price over Time')
plt.legend()

plt.show()


#hello there
#test