# Vaxxdater
Custom script that scrapes the web for dates available for vaccination against COVID-19

The scripts scrapes https://www.vgregion.se/ov/vaccinationstider/bokningsbara-tider/ and emails preset
email if the number of available spots is bigger than 10.

Usage:
  Edit credentials.py to return your chosen email and password. If used in a cloud service i recommens setting these
  as enviromental variables for greater security. 
  Note that to use email you have to  may have to change permissions in your accounts security settings.
