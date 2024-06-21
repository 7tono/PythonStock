import requests
import datetime
import tkinter as tk
import tkinter.ttk as ttk

def get_share():
	ticker = tex.get( 0., tk.END )
	ticker = ticker.rstrip('\n')
	asi = str(variable.get())
	interval = "?interval="+asi
	nagasa = "&range="+str(variable_range.get())

   # Yahoofinance URL
	url = 'https://query1.finance.yahoo.com/v8/finance/chart/'+ticker+".T"+interval+nagasa

	#データ取ってくる
	r = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})
	#r = requests.get(url)
	# json化
	stocks = r.json()
	#print(r)
	c =len(stocks['chart']['result'][0]['timestamp'])
	with open(ticker+".csv", 'w') as f:
		for i in range(c):
			dt = datetime.datetime.fromtimestamp(stocks['chart']['result'][0]['timestamp'][i])
			if asi=="1m" or asi=="5m" or asi=="1h":
				date = dt.strftime('%Y-%m-%d %H:%M')
			elif asi=="1mo":
				date = dt.strftime('%Y-%m')	
			else:
				date = dt.strftime('%Y-%m-%d')
			print(date, end=",",file=f)
			print(stocks['chart']['result'][0]['indicators']['quote'][0]['open'][i], end=",",file=f)
			print(stocks['chart']['result'][0]['indicators']['quote'][0]['high'][i], end=",",file=f)
			print(stocks['chart']['result'][0]['indicators']['quote'][0]['low'][i], end=",", file=f)
			print(stocks['chart']['result'][0]['indicators']['quote'][0]['close'][i], end=",", file=f)
			print(stocks['chart']['result'][0]['indicators']['quote'][0]['volume'][i], file=f)

root = tk.Tk()
root.title("株価ダウンロード")
root.geometry("300x300")
button = tk.Button(root, text="スタート",command=get_share)
button.place( x = 10, y = 250, width = 230, height = 30 )
lab = tk.Label( text = u'ティッカー' )
lab.place( x = 0, y = 10, width = 60, height = 30 )
lab = tk.Label( text = u'.T' )
lab.place( x = 130, y = 10, width = 60, height = 30 )
tex = tk.Text( )
tex.place( x = 50, y = 10, width = 100, height = 20 )

asi_list = ['1m', '5m', '1h','1d','1mo']
range_list = ['1d','30d', '60d','365d','730d']
variable = tk.StringVar()
variable.set("1d")
lab2 = tk.Label( text = u'足' )
lab2.place( x = 0, y = 50, width = 60, height = 30 )
combo_asi=ttk.Combobox(root,values=asi_list,textvariable=variable)
combo_asi.place( x = 50, y = 50, width = 50, height = 30 )

lab3 = tk.Label( text = u'期間' )
lab3.place( x = 0, y = 90, width = 60, height = 30 )
variable_range = tk.StringVar()
variable_range.set("60d")
combo_range=ttk.Combobox(root,values=range_list,textvariable=variable_range)
combo_range.place( x = 50, y = 90, width = 50, height = 30 )

root.mainloop()