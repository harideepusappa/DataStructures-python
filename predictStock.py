import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

global dates,prices
dates = []
prices = []

def get_data(filename):
	with open(filename,'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		count = 1
		for row in csvFileReader:
			# dates.append(int(row[0].split('-')[2]))
			dates.append(count)
			count = count+1
			prices.append(float(row[1]))
			if count >6 :
				break

	# print dates
	return

def predict_prices(dates,prices,x):
	prices.reverse()
	print prices
	dates = np.reshape(dates,(len(dates),1))
	print '-----------'
	svr_len = SVR(kernel='linear',C=1e3)
	print '-----------1'
	svr_poly = SVR(kernel='poly',C=1e3,degree = 2)
	print '-----------2'
	svr_rbf = SVR(kernel='rbf',C=1e3,gamma = 0.1)
	print '-----------3'

	svr_len.fit(dates,prices)
	print '-----------4'
	# svr_poly.fit(dates,prices)
	print '-----------5'
	svr_rbf.fit(dates,prices)
	print '-----------6'

	plt.scatter(dates,prices,color='black',label = 'Data')
	print '-----------7'
	plt.plot(dates,svr_rbf.predict(dates),color='red',label='RBF model')
	print '-----------8'
	plt.plot(dates,svr_len.predict(dates),color='green',label='Linear mode')
	print '-----------9'
	# plt.plot(dates,svr_poly.predict(dates),color='blue',label='RBF polynomial')
	print '-----------10'
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Support vectoir regression')
	plt.legend()
	plt.show()
	return svr_rbf.predict(x)[0], svr_len.predict(x)[0]
get_data('aapl.csv')
print '-----------'
predicted_price = predict_prices(dates,prices,200)
print '-----------'
print(predicted_price)