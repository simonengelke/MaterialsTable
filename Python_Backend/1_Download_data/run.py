import sys, os

from download_xml_services import download_xmls_services
from extract_links_osti_xml import extract_identifier_links
from download_osti_files import download

def main():
  if len(sys.argv) != 3:
    print 'usage: python run.py <link> <folder>'
    sys.exit(1)
  
  link = sys.argv[1]
  folder = sys.argv[2]

  download_xmls_services(link, folder)
  extract_identifier_links(folder)
  download(os.path.join('identifier_links', 'identifier_links_all.txt'), folder + '_files', 'txt+xml')

if __name__ == '__main__':
  main()