

from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from plotly import graph_objs as go, offline as po, tools
import plotly.graph_objs as go
from plotly.graph_objs import Scatter,Line,Layout,Box,Bar,Histogram
from flask import Flask,render_template,request,redirect,url_for
import plotly.offline as offplot
import pandas as pd
import numpy as np
import json
from range import plot


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
def plot():
	df = pd.read_csv('/home/haritha/final/data/kannansfile.csv')

	

	Year = list(df['year(BillDate)'])
	IPD = list(df['ipd'])
	REV = list(df['revenue'])
	BOR= list(df['BOR'])
	OP = list(df['op'])
	dfyear = df.groupby('year(BillDate)')
	
	curve1 = Scatter( x=IPD, y=REV, name='Plot', mode = 'markers',text=BOR,marker=dict(color=REV,colorscale='Viridis'))
	curve2 = Scatter( x=IPD,y=REV, name='Plot',xaxis='x2')
	x1=request.args.get("x1")
	x2=request.args.get("x2")

	
	

	data = [curve1,curve2]
	
	layout = Layout(
	   xaxis=dict(
		domain=[0,0.5],title=x1
	    ),
	    xaxis2=dict(
		domain=[0.6,1],title=x2
	    ),
	   
	    yaxis2=dict(
		anchor='x2'
	    ),
	    
	  updatemenus = [
	    dict(
	      x=-0.25, y=0.8,
	      yanchor='top',
	  
	      direction='up',

		# Y value
	      buttons = [
		dict( args= [dict(y=[IPD])],	  label='IPD',     method='restyle' ),
		dict( args= [dict(y=[REV])],       label='REV',      method='restyle' ),
		dict( args= [dict(y=[BOR])],       label='BOR',     method='restyle' ),
		dict( args= [dict(y=[OP])],       label='OP',          method='restyle' ),
		]


	    ),
	      dict(
	      x=-0.48, y=0.8,
	      yanchor='top',

		#X value
	      buttons = [
	      	dict( args= [dict(x=[IPD])],	  label='IPD',     method='restyle' ),
		dict( args= [dict(x=[REV])],       label='REV',      method='restyle' ),
		dict( args= [dict(x=[BOR])],       label='BOR',     method='restyle' ),
		dict( args= [dict(x=[OP])],       label='OP',          method='restyle' ),
		dict( args= [dict(x=[Year])],       label='Year',          method='restyle' ),

		
		]


	    ),
	     dict(
	      x=-0.25, y=0.7,
	      yanchor='top',

		#Hover text
	      buttons = [
		dict( args= [dict(text=[Year])],	label='Year',     method='restyle' ),
		dict( args= [dict(text=[IPD])],	        label='IPD',      method='restyle' ),
		dict( args= [dict(text=[OP])],          label='OP',     method='restyle' ),
		dict( args= [dict(text=[REV])],         label='REV',          method='restyle' ),
		dict( args= [dict(text=[BOR])],       	label='BOR',          method='restyle' ),
		]


	    ),
	    dict(
	      x=-0.25, y=0.6,
	      yanchor='top',

		#ColorScale
	      buttons = [
		dict( args= [dict(marker=dict(color=Year,colorscale='Viridis'),line=dict(color=Year,colorscale='Viridis'))],	  label='YEAR',method='restyle' ),
		dict( args= [dict(marker=dict(color=REV,colorscale='Rainbow'))],       label='REV',      method='restyle' ),
		dict( args= [dict(marker=dict(color=IPD,colorscale='Electric'))],       label='IPD',     method='restyle' ),
		dict( args= [dict(marker=dict(color=OP,colorscale='Greens'))],       label='OP',          method='restyle' ),
			]
	    ),	    
	  
	  ],
	  annotations = [
	    dict(text='X:',x= -0.54,xref='paper',height=25,y=0.88,yref='paper',showarrow=False,font=dict(size=15)),
	    dict(text='Y:',x= -0.32,xref='paper',height=25,y=0.88,yref='paper',showarrow=False,font=dict(size=15)),
	    dict(text='HoverText',x= -0.54,xref='paper',height=25,y=0.68,yref='paper',showarrow=False,font=dict(size=15)),
	    dict(text='Color',x= -0.54,xref='paper',height=25,y=0.58,yref='paper',showarrow=False,font=dict(size=15)),
	    dict(text='Graph your data',x= 0.50,xref='paper',height=25,y=1.15,yref='paper',showarrow=False,font=dict(size=20)),
	    dict(text='Enter choices',x= -0.50,xref='paper',height=25,y=1.15,yref='paper',showarrow=False,font=dict(size=20))],
	

	  sliders = [dict(
	   
	    x = -0.60,y=0.5,
	    borderwidth=3,
	    len=0.5,
	    currentvalue= dict(
	      xanchor = 'right',
	      prefix ='Revenue vs OP:',
	      font= dict(
		color= 'black',
		size= 14
	      )
	    ),
	   
	    steps= [dict(
	      label='2014',
	      method= 'restyle',
	      args= [dict(y=[dfyear['revenue'].get_group(2014)],x=[dfyear['op'].get_group(2014)],text='2014')]
	      
	    ), 
	    dict(
	      label= '2015',
	      method= 'restyle',
	      args= [dict(y=[dfyear['revenue'].get_group(2015)],x=[dfyear['op'].get_group(2015)],text='2015')]
	    ), 
	    dict(
	      label= '2016',
	      method= 'restyle',
	      args= [dict(y=[dfyear['revenue'].get_group(2016)],x=[dfyear['op'].get_group(2016)],text='2016')]
	    ),
	    dict(
	      label= '2017',
	      method= 'restyle',
	      args= [dict(y=[dfyear['revenue'].get_group(2017)],x=[dfyear['op'].get_group(2017)],text='2017')]
	    ),
	    dict(
	      label= '2018',
	      method= 'restyle',
	      args= [dict(y=[dfyear['revenue'].get_group(2018)],x=[dfyear['op'].get_group(2018)],text='2018')]
	    )]
	  )],
	  )	



	figure = go.Figure(data=data, layout=layout)
	div1 = offplot.plot(figure, show_link=False, output_type="div", include_plotlyjs=False)
	return div1
	

class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))

	def __init__(self, username, password):
		self.username = username
		self.password = password


@app.route('/', methods=['GET', 'POST'])
def home():
	div1=plot()
	""" Session control"""
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			
			return render_template('index.html', div1=div1)
		return render_template('index.html',div1=div1)


@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login Form"""
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		passw = request.form['password']
		try:
			data = User.query.filter_by(username=name, password=passw).first()
			if data is not None:
				session['logged_in'] = True
				return redirect(url_for('home'))
			else:
				return 'Incorrect username or password'
		except:
			return "Incorrect username or password"

@app.route('/register/', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
		new_user = User(username=request.form['username'], password=request.form['password'])
		db.session.add(new_user)
		db.session.commit()
		return render_template('index.html')
	return render_template('register.html')

@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.debug = True
	db.create_all()
	app.secret_key = "123"
	app.run(host='0.0.0.0')
	
