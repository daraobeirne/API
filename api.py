from __future__ import print_function
import requests


CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'




"""
class Human(object):
	def __init__(self, name, birthday):
		self.name = name
		self.birthday = birthday
	def get_sleep_time(self):
		return "8 hours"
"""	

class CPIData(object):
	"""Abstraction of the CPI data provided by FRED.
	
	This stores internally only one value per year.
	
	"""
	
	def __init__(self):
		self.year_cpi = {}
		self.last_year = None
		self.first_year = None
		
	def load_from_url(self, url, save_as_file=None):
		"""Loads data from a given url.
		
		The downloaded file can also be saved into a location for later
		re-use with the "save_as_file" parameter specifying a filename.
		
		After fetching the file this implementation uses load_from_file
		internally. 
		
		"""
	
	def load_from_file(self, fp):
		"""Loads CPI data from a given file-like object."""
		
	def get_adjusted_price(self, price, year, current_year=None):
		"""Returns the adapted price from a given year compared to what current
		year has been specified.
		
		"""
		
		


def main():
	"""This function handles the actual logic of this script"""
	
	# Grab CPI/Inflation data.
	
	#Grab API/game platform data.
	
	
	
	# Figure out the current price of each platform.
	# This will require looping through each platform we received.
	# calculate the adjusted price based on the CPI data we also received
	# During this point, we should also validate our data so we do not skew
	# our results.
	
	
	#Gnerate a plot/bar graph for the adjusted price data. 
	
	
	#Generate a CSV file to save for the adjusted price data. 
	
	
	
	