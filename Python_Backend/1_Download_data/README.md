## Description

### Run.py

Batch download Department of Energy plain text and XML metadata files from SciTech Connect

### Individual files

1. XML downloader for SciTech Connect XML Services. 
Downloads metadata XML for all found search results, 
taking in account multiple pages with search results.
2. Extracts SciTech links and OSTI identifiers from XML files. 
3. Downloads plain txt (and optional XML) for each link or identifier

## Instructions

### Run.py

Use run.py to automatically download the document links, extract them and download
the plain text files and XML files

### Individual files

Use the three individual files to download links, extract them and download plain text and
metadata or only plain text files

1. First find the search qurery which equals the following <link> by following this manual: 
http://www.osti.gov/home/sites/www.osti.gov.home/files/SciTechXMLDataServices.pdf
and download XML files with download_xml_services.py into a subfolder called <xml_services> 
in the specified parent folder. 
2. To obtain a text file with all links out of the downloaded files, use the 
--identifier_links option. Have the mail folder with the downloaded XML service XMLs in a 
<xml_services> subfolder. The links are saved in a subfolder with the respective option name, 
identifiers, identifier_links, or links in individual files for each XML file and as a collected 
file with all identifiers or links extracted out of a folder.
3. Prepare identifier or link list and batch download plain text or XML files into folder.
Either download only the plain text files with option --txt or plain text files and respective XML
metadata files with option --txt+xml

## Usage

Locate file in Terminal and type:

### Run.py

python run.py *link* *folder*

### Individual files

1. python download_xmls_services.py --download link *ResultFolder*
2. python extract_links_osti_xml.py {--identifier_links|--identifiers|--links} *XMLFolder*
3. python download_osti_files.py {--txt|txt+xml} *file* *folder*

## Example

### Run.py

    python run.py http://www.osti.gov/scitech/scitechxml?searchFor=batter*+lepidocrocite *lepidocrocite*

### Individual files

1. `python download_xml_services.py --download http://www.osti.gov/scitech/scitechxml?searchFor=batter* batter`
2. `python extract_links_osti_xml.py --identifier_links batter`
3. `python download_osti_files.py --txt+xml identifier_links_all.txt batter_files`

## Author

Simon Engelke ([engelke.co](http://engelke.co))

## License

MIT

## Version

1.0

## Google Summer of Code 2014

This code was developed as part of [Google Summer of Code 2014](https://www.google-melange.com/gsoc/project/details/google/gsoc2014/sengelke/5668600916475904)

### Please reach out for questions, comments, improvements etc.
