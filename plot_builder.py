#Author Samuel Arwood sarwood@bu.edu

import plotly
import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot
import plotly.graph_objs as go

def plot_div(DNS : int, TCP : int, SSL : int, SERVER : int, TRANS : int, name : int, conn : int, pre : int, trans : int, tot : int):
	init_notebook_mode(connected=True)

	if SSL == 0:
		x = ['DNS Lookup', 'namelookup', 'TCP Connection', 'connect', 'Server Processing', 
				'starttransfer', 'Content Transfer', 'total']
		y = [DNS, name, TCP, conn, SERVER, trans, TRANS, tot]

		data = [go.Bar(
				x=x,y=y,
			    marker=dict(
        		    color=['rgb(158,202,225)','rgb(234,12,9)',
        		    	   'rgb(158,202,225)','rgb(234,12,9)',
        		    	   'rgb(158,202,225)','rgb(234,12,9)',
			        	   'rgb(158,202,225)','rgb(234,12,9)'],
            		line=dict(
                		color='rgb(8,48,107)',
                		width=1.5),
        		),
        		opacity=0.6
			)]

	else:
		x = ['DNS Lookup', 'namelookup', 'TCP Connection', 'connect', 'SSL Handshake', 
				'pretransfer', 'Server Processing', 'starttransfer', 'Content Transfer', 
				'total']
		y = [DNS, name, TCP, conn, SSL, pre, SERVER, trans, TRANS, tot]

		data = [go.Bar(
				x=x,y=y,
			    marker=dict(
        		    color=['rgb(158,202,225)','rgb(234,12,9)',
        		    	   'rgb(158,202,225)','rgb(234,12,9)',
        		    	   'rgb(158,202,225)','rgb(234,12,9)',
        		    	   'rgb(158,202,225)','rgb(234,12,9)',
			        	   'rgb(158,202,225)','rgb(234,12,9)'],
            		line=dict(
                		color='rgb(8,48,107)',
                		width=1.5),
        		),
        		opacity=0.6
			)]	

	layout = go.Layout(
		height=600,
	    annotations=[
    	    dict(x=xi,y=yi,
        	    text=str(yi),
            	xanchor='center',
            	yanchor='bottom',
            	showarrow=False,
        	) for xi, yi in zip(x, y)]
	)

	fig = go.Figure(data=data, layout=layout)
	#py.iplot(fig, filename='grouped-bar')

	#return plotly.offline.plot([Box(y = np.random.randn(50), showlegend=False) for i in range(45)], show_link=False, include_plotlyjs=False, output_type='div')
	return plotly.offline.plot(fig, show_link=False, include_plotlyjs=False, output_type='div')

if __name__ == '__main__':
	plot_div()