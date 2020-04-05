import csv
import pprint
import datetime
import urllib.parse
import urllib.request
import os

from Parameter_containers import Countries, Keys_eu

eu_corona_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv"
corona_file_name = 'corona_data.csv'

def download_corona_data_to_file(url,corona_file_name):
	print("Download corona data...")
	dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
	urllib.request.urlretrieve(url, dir_path + corona_file_name)
	print("Download corona data successful" + "data written to file " + corona_file_name)

def dict_list_from_csv_file(variables_file):
    print("Converting csv data to list of dictionarys")
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
    reader = csv.DictReader(open(variables_file, 'rt'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    print("Converting csv data to list of dictionarys successful")
    return dict_list

def elements_of_actual_day(dict_list):
    print("Parse corona data for today")
    date_today = datetime.datetime.now()
    actual_day_elemets = elements_of_day(dict_list,date_today)
    print("Parse corona data for today successful")
    return actual_day_elemets

def elements_of_day(dict_list, date):
    date_today_str = date.strftime("%d/%m/%Y")
    print("Parse Corona data for day: " + date_today_str)
    day_elements = []
    for element in dict_list:
        if element.get(Keys_eu.DateRep) == date_today_str:
            day_elements.append(element)
    print("Parse Corona data for day sucessful")
    return day_elements

def elements_of_country(dict_list, country):
    print("Parse Corona data for country: " + country)
    country_elements = []
    for element in dict_list:
        if element.get(Keys_eu.CountriesAndTerritories) == country:
            country_elements.append(element)
    print("Parse Corona data for country sucessful")
    return country_elements

def print_Countries(dict_list):
    print("All available Countries: ")
    Countries = []
    temp_elements = elements_of_actual_day(dict_list)#returns also country unique elements
    for element in temp_elements:
        print(element.get(Keys_eu.CountriesAndTerritories))
        

print("-- Corona Analysis start --")

#download from eu server
download_corona_data_to_file(eu_corona_data_url, corona_file_name)

#convert csv data to list of dictionarys
# keys in dicts will be:dateRep,day,month,year,cases,deaths,countriesAndTerritories,geoId,countryterritoryCode,popData2018
corona_data_dictlist = dict_list_from_csv_file(corona_file_name)

#filter for data of current day
actual_day_data_dictlist = elements_of_actual_day(corona_data_dictlist)

#filter for country
country_data_dictlist = elements_of_country(actual_day_data_dictlist, Countries.Germany)

#show all Countries
#print_countrys(corona_data_dictlist)

#print info for today germany
pprint.pprint(elements_of_country(actual_day_data_dictlist, Countries.Germany))	






 





