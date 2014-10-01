"""
DESCRIPTION:
Extracts SciTech links and OSTI identifiers from XML files. 

INSTRUCTIONS:
First download XML files into a folder with download_xml_services.py. 
To obtain a text file with all links out of the downloaded files, use the 
--identifier_links option, as this one is more reliable than the direct
extraction of the links. If one wants to extract and save the identifiers, 
one can use the --identifier option. The links are saved in a subfolder
with the respective option name in individual files for each XML file 
and as a collected file with all identifiers or links extracted out of
a folder.

USAGE:
Locate file in Terminal and type:
python download_xmls_services.py --option <XMLFolder>
options are --identifier_links, --identifiers, --links

EXAMPLE:
python download_xmls_services.py --identifier_links batter

AUTHOR:
Simon Engelke (engelke.co)

LICENSE:
MIT

VERSION:
1.0
"""

# -*- coding: utf-8 -*-
import sys, codecs, re, os, glob

def file_opener(filename):
  """Opens the files"""
  textstring = ''
  input_file = codecs.open(filename, encoding='utf-8')
  textstring = input_file.read()
  input_file.close()
  return textstring

def extract_identifiers(folder):
  """Extracts osti identifiers out of XMLs and saves links."""
  os.chdir(os.path.join(os.getcwd(), folder)) # change directory to folder directory

  print '=============' + ' Extract Links OSTI XML ' + '============'

  for filename_xml in sorted(glob.glob("*.xml")):
    textstring = file_opener(filename_xml)
    identifier_tuple = re.findall(r'<dc:ostiId>(\d+)</dc:ostiId>',textstring,re.DOTALL)
    if not identifier_tuple:
      sys.stderr.write('Couldn\'t find the identifier!\n')
      sys.exit(1)
    for identifier in identifier_tuple:
      save_file(folder, filename_xml, identifier, 'identifiers')
    print 'Extracted links from: ' + filename_xml
  os.chdir(os.pardir) #back to parent directory

def extract_identifier_links(folder):
  """Extracts osti identifiers out of XMLs and saves links."""
  os.chdir(os.path.join(os.getcwd(), folder, 'xml_services')) # change directory to folder directory

  print '=============' + ' Extract Links OSTI XML ' + '============'

  for filename_xml in glob.glob("*.xml"):
    textstring = file_opener(filename_xml)
    identifier_tuple = re.findall(r'<dc:ostiId>(\d+)</dc:ostiId>',textstring,re.DOTALL)
    if not identifier_tuple:
      sys.stderr.write('Couldn\'t find the identifier!\n')
      sys.exit(1)

    # Create links
    for identifier in identifier_tuple:
      #print identifier
      identifier_link = 'http://www.osti.gov/scitech/servlets/purl/' + identifier
      #print identifier_link
      save_file('identifier_links', filename_xml, identifier_link, 'identifier_links')
    print 'Extracted links from: ' + filename_xml
  os.chdir(os.pardir) #back to parent directory

def extract_links(folder):
  """Imports an Unicode file and extracts Links."""
  os.chdir(os.path.join(os.getcwd(), folder)) # change directory to folder directory

  print '=============' + ' Extract Links OSTI XML ' + '============'

  for filename_xml in glob.glob("*.xml"):
    textstring = file_opener(filename_xml)
    links_tuple = re.findall(r'\>(http://www.osti.gov/scitech/servlets/purl/\d+)\<',textstring,re.DOTALL)
    if not links_tuple:
      sys.stderr.write('Couldn\'t find the links!\n')
      sys.exit(1)
    for link in links_tuple:
      save_file(os.path.join(os.pardir, folder), filename_xml, link, 'links')
    print 'Extracted links from: ' + filename_xml
  os.chdir(os.pardir) #back to parent directory


def save_file(folder, filename, extract, type_extract):
  """Adds the extracted links line by line to a text file"""
  path_type_extract = os.path.join(os.pardir, type_extract)
  if not os.path.exists(path_type_extract):
    os.makedirs(path_type_extract)
  filename_extract = filename[:-4] + '_' + type_extract + '.txt'
  with open(os.path.join(os.pardir, type_extract, filename_extract), "ab") as extract_file:
    extract_file.write(extract + "\n")
  filename_extract_all = type_extract + '_all.txt'
  with open(os.path.join(os.pardir, type_extract, filename_extract_all), "ab") as extract_file:
    extract_file.write(extract + "\n")

def main():
  if len(sys.argv) != 3:
    print 'usage: python extract_links_osti.py {--links|--identifier|--identifier_links} file'
    sys.exit(1)

  option = sys.argv[1]
  folder = sys.argv[2]
  if option == '--links':
    extract_links(folder)
  elif option == '--identifiers':
    extract_identifiers(folder)
  elif option == '--identifier_links':
    extract_identifier_links(folder)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
