#/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Author: Goncalo Bejinha 13428
#

import sys
import re
import GeoIP

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

from collections import OrderedDict

import sqlite3
import csv

import os

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors

class Firewall_Data():
	'''Class that allows to process the firewall log (/var/log/ufw.log).''' 

	def read_firewall_log(self):
		'''Method to read the firewall log and obtain data from it.
		   @return info -> Data obtained from the log.
		   @return ip_list -> List of number of attacks by IP.'''
		ip_list = dict()
		info = []
		location = None
		ip = None
		date = None
		time = None

		#file_object = open('/var/log/ufw.log', 'r') 
		file_object = open('ufw.log', 'r') 
		gi = GeoIP.open("GeoIP.dat", GeoIP.GEOIP_STANDARD)
		for line in file_object:
			if not re.search("SRC=192.", line):
				lista = line.split("SRC=")
				if not re.search(":", lista[1].split(' ')[0]):
					ip = lista[1].split(' ')[0]
					date = line[0:6]
					time = line[7:15]

					if ip_list.has_key(ip):
						ip_list[ip] = ip_list[ip] + 1

					else:
						ip_list[ip] = 1
				        
					try:
						location = gi.country_name_by_addr(ip)
					except:
						continue

					finally:
						info.append([ip, date, time, location])

		return info, ip_list


	def geo_ip_lookup(self, ip_address):
		'''Method to seach the coordinates of a given IP address.
		   @param ip_address -> IP to search.
		   @return record_list -> List containing the latitude and longitude.'''
		gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)

		gir = gi.record_by_addr(ip_address)

		record_list = []

		if gir is not None:
			record_list.append([gir['city'], gir['latitude'], gir['longitude'], ip_address])

		return record_list


	def build_bars_graph(self, ip_list):
		'''Method to create a simple horizontal bar chart.
		   @param ip_list -> List of all IP's read from the log.
		   @reference: http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html'''
		new_ip_list = OrderedDict(sorted(ip_list.items(), key=lambda x: x[1]))
		ip = [None] * len(ip_list)
		attempts = [None] * len(ip_list)
		i = 0

		for k in new_ip_list:
			ip[i] = k
			attempts[i] = new_ip_list[k]
			i = i + 1

		y_pos = np.arange(len(ip))

		plt.barh(y_pos, attempts, align='center', color='green')
		plt.yticks(y_pos, ip)
		plt.xlabel('Number of attempts')
		plt.title('Attack Attempts per IP')

		plt.show()


m = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
		llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='aqua') 
plt.title("Equidistant Cylindrical Projection")
plt.show()



