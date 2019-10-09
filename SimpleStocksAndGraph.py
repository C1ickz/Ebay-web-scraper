import pandas_datareader.data as web
import matplotlib.pyplot as plt

ticker = input("input ticker (NOTE: This is not being error checked): ").upper()
f = web.DataReader(ticker, 'stooq') # if ticker does not work add ^ in front aka ^tkr

print(f[:10]) # prints first 10 lines of stock data
print("-----------")
print(f['Close'])

#try to graph
wantToSee = input("Do you want to see the graph?(y or n): ")
if wantToSee == 'y': 
	f["Close"].plot()
	plt.title("Stock Prices of {}".format(ticker))
	plt.ylabel("Price ($)")
	plt.show()
else:
	print("exiting program...")