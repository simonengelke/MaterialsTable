"""
DESCRIPTION:
Plain text and XML downloader for SciTech Connect. 
Downloads plain text files and XML metadata files from identifiers or links listed in text file.

INSTRUCTIONS:
Prepare identifier or link list and batch download plain text or XML files into folder.
Either download only the plain text files with option --txt or plain text files and respective XML
metadata files with option --txt+xml

USAGE:
Locate file in Terminal and type:
python download_osti_files.py --option <file> <folder>
options are --txt and --txt+xml

EXAMPLE:
python download_osti_files.py --txt+xml identifier_links_all.txt batter_files

AUTHOR:
Simon Engelke (engelke.co)

LICENSE:
MIT

VERSION:
1.0
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, codecs, re, sys, cookielib, os, time

def download(links_identifiers, folder, filetype):
  """This function can be used to download plain text and XML metadata files from SciTech Connect by OSTI."""
  # Open text file with links or identifiers

  with open(links_identifiers, 'r') as f:

    # Presets
    osti_txt_file = ''
    downloads = 0
    not_downloaded = 0
    osti = int
    path_folder = os.path.join(os.getcwd(), folder)
    if not os.path.exists(path_folder):
      os.makedirs(path_folder)
    path_errors = os.path.join(os.getcwd(), folder, 'errors')
    if not os.path.exists(path_errors):
      os.makedirs(path_errors)
    print '=============' + ' Download OSTI files ' + '==============='
    print '| ' + '#' + ' | ' + 'identifier          date and time' + ' |'

    # Determine if links or identifiers in file
    first_line = f.readline()
    if first_line.startswith("http://www.osti.gov/scitech/servlets/purl/"):
      re_search = r'http://www.osti.gov/scitech/servlets/purl/(\d*)'
    else:
      re_search = r'(\d*)'
    f.seek(0)

    # Downloads files line by line / link by link
    for line in f:
      extract_osti = re.search(re_search,line)
      osti = extract_osti.group(1)
      osti_txt_file = str(osti) + '.txt'
      path_osti_txt_file = os.path.join(path_folder, osti_txt_file)
      endpoint_txt = 'http://www.osti.gov/scitech/servlets/purl/' + str(osti)    
      txt_encoded = requests.get(endpoint_txt, headers={ 'Accept': 'text/plain'} )

      # Expected encoding for full-text
      if txt_encoded.encoding == 'UTF-8':
        log_encoding = txt_encoded.encoding
        txt_utf = txt_encoded.content
        
        # Uncomment try when want to use utf-8 encoding for files (does not work for all files)
        #try:

        text_file = codecs.open(path_osti_txt_file, "wb")

        # Alternatively files can be saved with utf-8, but the exceptions will occur
        #text_file = codecs.open(path_osti_txt_file, "wb", "utf-8")
        text_file.write(txt_utf)
        text_file.close()
        log('log', '', osti, log_encoding, path_folder)
        downloads = downloads + 1
        now = time.strftime("%c")
        print '| ' + str(downloads) + ' | ' + str(osti) + ' | ' + str(now) + ' |'

        if downloads % 10 == 0:
          print '================== ' + str(downloads) + ' =================='

        # Download XML if specified in filetype
        if filetype == 'txt+xml':
          endpoint_xml = 'http://www.osti.gov/scitech/scitechxml?osti_id=' + str(osti)
          xml_utf = requests.get(endpoint_xml).content
          xml_file = codecs.open(os.path.join(path_folder, osti + '.xml'), "wb")

          # Alternatively, utf-8 encoding can be used, but then have to uncomment try and except,
          # as some files cannot be saved in utf-8
          # xml_file = codecs.open(os.path.join(path_folder, osti + '.xml'), "wb", "utf-8")
          # xml_file = codecs.open(os.path.join(path_errors, 'not_correct_encoding', osti + '.xml'), "wb", "utf-8")
          
          xml_file.write(xml_utf)
          xml_file.close()

        # Have to uncomment these exceptions when using utf-8 encoding for TXT and XML
        """
        # Some files cannot be saved as utf-8
        except UnicodeDecodeError: 
          if not os.path.exists(os.path.join(path_errors, 'not_correct_encoding')):
            os.makedirs(os.path.join(path_errors, 'not_correct_encoding'))
          text_file = codecs.open(os.path.join(path_errors, 'not_correct_encoding', osti_txt_file), "wb")
          text_file.write(txt_utf)
          text_file.close()
          log('not_correct_encoding', 'not correct encoding', osti, log_encoding, path_errors)
          log('log', 'not_correct_encoding', osti, log_encoding, path_folder)
          not_downloaded = not_downloaded + 1

          # Download XML if specified in filetype
          if filetype == 'xml' or 'txt+xml':
            endpoint_xml = 'http://www.osti.gov/scitech/scitechxml?osti_id=' + str(osti)
            xml_utf = requests.get(endpoint_xml).content
            xml_file = codecs.open(os.path.join(path_errors, 'not_correct_encoding', osti + '.xml'), "wb")
            xml_file.write(xml_utf)
            xml_file.close()

        except:
          print 'Unknown error during writing'
          log('writing_errors', 'writing errors', osti, log_encoding, path_errors)
          log('log', 'writing_errors', osti, log_encoding, path_folder)
          not_downloaded = not_downloaded + 1

        """
      # Returned HTML errors are encoded in 'utf-8', 
      # means these documents cannot be downloaded as full-text
      elif txt_encoded.encoding == 'utf-8':
        log_encoding = txt_encoded.encoding
        log('no_full_text', 'not downloaded because no full text', osti, log_encoding, path_errors)
        log('log', 'not downloaded because no full text', osti, log_encoding, path_folder)
        not_downloaded = not_downloaded + 1

      # Should not happen, as all files were converted to UFT-8 following to OSTI
      else:
        log_encoding = txt_encoded.encoding
        log('log', 'unknown_encoding_errors', osti, log_encoding, path_folder)
        log('unknown_encoding_errors', '', osti, log_encoding, path_errors)
        not_downloaded = not_downloaded + 1

      # Take a break for the servers
      #time.sleep(1)

  log('log', '\n' + 'Total downloads: ' + str(downloads), '', '', '')
  log('log', 'Total not downloads: ' + str(not_downloaded), '', '', '')
  print 'Total downloads: ' + str(downloads)
  print 'Total not downloads: ' + str(not_downloaded)

def log(log_name, comments, osti, log_encoding, path_folder):
  """ Records logs"""
  with open(os.path.join(path_folder, log_name + '.txt'), 'a') as file:
    now = time.strftime("%c")
    file.write(str(osti) + ' | ' + str(log_encoding) + ' | ' + str(now) + ' | ' + comments + '\n')

def main():
  if len(sys.argv) != 4:
    print 'usage: python download_osti_files.py {--txt|txt+xml} <file> <folder>'
    sys.exit(1)
  
  option = sys.argv[1]
  filename = sys.argv[2]
  folder = sys.argv[3]
  filetype = sys.argv[3]
  if option == '--txt':
    download(filename, folder, 'txt')
  elif option == '--txt+xml':
    download(filename, folder, 'txt+xml')
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
	