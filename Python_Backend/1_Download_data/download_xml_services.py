"""
DESCRIPTION:
XML downloader for SciTech Connect XML Services. 
Downloads metadata XML for all found search results, 
taking in account multiple pages with search results.

INSTRUCTIONS:
Find the search qurery which equals the following <link> by following this manual: 
http://www.osti.gov/home/sites/www.osti.gov.home/files/SciTechXMLDataServices.pdf

USAGE:
Locate file in Terminal and type:
python download_xmls_services.py --download <link> <ResultFolder>

EXAMPLE:
python download_xmls_services.py --download http://www.osti.gov/scitech/scitechxml?searchFor=batter* batter

AUTHOR:
Simon Engelke (engelke.co)

LICENSE:
MIT

VERSION:
1.0
"""

# -*- coding: utf-8 -*-
import time, requests, codecs, re, sys, os

def download_xmls_services(search_link, folder):
  """this function will download XMLs from SciTech Connect XML services"""
  
  # Define folder to store files in
  path_folder = os.path.join(os.getcwd(), folder, 'xml_services')
  if not os.path.exists(path_folder):
    os.makedirs(path_folder)

  # Presets
  more_pages = True
  index = 0

  # Title
  print '=============' + ' Download XML Services ' + '============='

  # Loop while there are more pages which can be dowloaded
  while more_pages == True:

    # Download XML
    endpoint = search_link + '&SortBy=publication_date&nrows=1000&page=' + str(index)
    xml_encoded = requests.get(endpoint)
    textstring = xml_encoded.content.decode('utf-8').encode('utf-8')

    # Save XML file 
    path_xml_file = os.path.join(path_folder, str(index) + '.xml')
    text_file = codecs.open(path_xml_file, "w")
    text_file.write(textstring)
    text_file.close()

    # Check if there are more pages
    more_pages_check = re.search(r'\"\smorepages=\"true\"\s', textstring)
    if not more_pages_check:
      more_pages = False

    # Add log
    now = time.strftime("%c")
    log = str(index) + ' | ' + str(now)
    with open(os.path.join(path_folder, 'log.txt'), 'a') as file:
      file.write(log + '\n')
  
    # Print and add index
    print '| ' + str(index) + ' | ' + str(now) + ' | '
    index = index + 1

    # Add some break time for the server
    seconds = 1
    time.sleep(seconds)

def main():
  if len(sys.argv) != 4:
    print 'usage: python download_xmls_services.py {--download} <link> <ResultFolder>'
    sys.exit(1)
  
  option = sys.argv[1]
  link = sys.argv[2]
  folder = sys.argv[3]
  if option == '--download':
    download_xmls_services(link, folder)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
