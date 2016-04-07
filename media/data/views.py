#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, render_to_response, RequestContext
from django.utils import timezone
from django.core.urlresolvers import reverse
from urllib import urlretrieve
from django.core.files import File
from subprocess import call
import os, time, json, threading

from .models import GzipFile, Station, History

def status(request):
	fetchfile()
	# Handle file upload
	stations = Station.objects.all()
	historyls = History.objects.all()
	d = time.strftime('%y-%m-%d')
	t = time.strftime('%H:%M:%S')
	return render_to_response(
		'status.html',
		{'stations': stations, 'historylist': historyls, 'date': d, 'time': t},
		context_instance=RequestContext(request),
	)
	

def fetchfile():
	# Use time as file name
	d = time.strftime('%y%m%d')
	t = time.strftime('%H%M%S')
	# Create file for day
	if call(['mkdir media/data/'+ d], shell = True):
		print "File already exist"
	# Delete File after 1 day
	if call(['rm -r media/data/'+ str(int(d)-1)], shell = True):
		print "Cannot remove file"
	else:
		expired_status_file = GzipFile.objects.filter(zipfile__contains = 'data/'+str(int(d)-1))
		expired_status_file.delete()
		expired_history = History.objects.filter(mday = )

	path = os.path.join('media/data', d, t)
	# Fetch gzip file from website
	statusfile = urlretrieve("http://data.taipei/youbike", path+'.gz')
	# Compare the previous status
	# Save file path to database
	newstatus = GzipFile(zipfile = statusfile[0].replace('media/', ''))
	newstatus.save()

	#Rename the old status
	filepath = os.path.join('media/data', d)
	renamecmd = ['mv '+ filepath + '/newtmp.json '+ filepath + '/oldtmp.json']
	call(renamecmd, shell = True)
	# Unzip file
	cmd = ['gunzip -k .'+ newstatus.zipfile.url]
	call(cmd, shell = True)
	# Name as new temp	
	renamecmd = ['mv '+ path +' ' + filepath +'/newtmp.json']
	call(renamecmd, shell = True)

	# Tranform JSON Object to Python Dictionary
	jsonpath = filepath+'/newtmp.json'
	with open(jsonpath) as j:
		stationdic = json.load(j)

	stationdic = stationdic['retVal']
	# Import data to model
	for x in stationdic.keys():
		date = time.strptime(stationdic.get(x)['mday'], "%Y%m%d%H%M%S")
		date = time.strftime('%Y-%m-%d %H:%M:%S', date)
		print date
		#date = timezone.make_aware(date)
		newstation = Station(sno = stationdic.get(x)['sno'], sna = stationdic.get(x)['sna'], tot = stationdic.get(x)['tot'], sbi = stationdic.get(x)['sbi'], sarea = stationdic.get(x)['sarea'], mday = date, lat = stationdic.get(x)['lat'], lng = stationdic.get(x)['lng'], ar = stationdic.get(x)['ar'], sareaen = stationdic.get(x)['sareaen'], snaen = stationdic.get(x)['snaen'], aren = stationdic.get(x)['aren'], bemp = stationdic.get(x)['bemp'], act = int(stationdic.get(x)['act']), source_path = GzipFile.objects.latest('id'))
		newstation.save()
		newhistory = History(sno = newstation, mday = newstation.mday, sbi = newstation.sbi)
		newhistory.save()
		#createchart(newstation)

	# Auto update the data in 60 seconds
	threading.Timer(60, fetchfile).start()

	return "File Fetched"

'''
def createchart(adn):
	ds = DataPool(
			series=[{
				'options': {'source': History.objects.filter(sno = adn)},
				'terms': ['mday', 'sbi']
			}]
		)

	cht = Chart(
			datasource = ds,
			series_options = [{
				'options':{'type': 'line', 'stacking': False},
				'terms':{'mday': ['sbi']}
			}],
			chart_options = {
				'title': {'text': 'Weather Data of Boston and Houston'},
				'xAxis': {'title': {'text': 'Time'}}
			}
		)
'''
# Create your views here.
