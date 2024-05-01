import sys
import pandas_datareader.data as dr
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd
import mplfinance as mpf
import tkinter as tk

pyear=2
fday =1
simble =""

def get_share():
	global pyear,fday,simble
	simble = tex.get( 0., tk.END )[:-1]
	#simble ='2127.T'
	my_share = share.Share(simble)
	symbol_data = None
	try:
		symbol_data = my_share.get_historical(
			share.PERIOD_TYPE_YEAR, pyear, 
			share.FREQUENCY_TYPE_DAY, fday)
	except YahooFinanceError as e:
		print(e.message)
		sys.exit(1)

	df = pd.DataFrame(symbol_data)
	df["timestamp"] = pd.to_datetime(df.timestamp, unit="ms")
	df["open"]=round(df["open"], 1)
	df["high"]=round(df["high"], 1)
	df["low"]=round(df["low"], 1)
	df["close"]=round(df["close"], 1)
	print("------------------------")
	df.columns = ['Date','Open', 'High', 'Low', 'Close', 'Volume']
	df.set_index('Date', inplace = True)
	print(df)
	df.to_csv(simble+".csv", index=True,date_format='%Y-%m-%d')

def get_share2():
	s = tex.get( 0., tk.END )
	lab["text"]  = s

root = tk.Tk()
root.title("株価ダウンロード")
root.geometry("400x300")
button = tk.Button(root, text="スタート",command=get_share)
button.place( x = 0, y = 80, width = 230, height = 30 )
lab = tk.Label( text = u'ティッカー' )

lab.place( x = 0, y = 10, width = 60, height = 30 )
tex = tk.Text( )
tex.place( x = 100, y = 10, width = 230, height = 30 )
root.mainloop()