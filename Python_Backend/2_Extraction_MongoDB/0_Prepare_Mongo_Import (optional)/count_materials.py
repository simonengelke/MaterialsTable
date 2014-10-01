from pymongo import Connection
import os, codecs, re, sys

con = Connection()
db = con.osti

twothousandallfiltered = db.twothousandallfiltered

results = twothousandallfiltered.aggregate([
    # Unwind the array
    { "$unwind": "$materials_experimental" },

    # Group the results and count
    { "$group": {
        "_id": "$materials_experimental",
        "count": { "$sum": 1 }
    }},

    { "$sort" : { "count" : -1}}
])

print results

"""Extracts material formulas from experimental part"""
textstring = str(results)
#print textstring
pat = re.compile(ur"""
u'_id': u'(.*?)'}
""", re.VERBOSE | re.UNICODE | re.DOTALL)

materials_tuple = re.findall(pat,textstring)
#print materials_tuple

if not materials_tuple:
  x = "nothing"
  #sys.stderr.write('Couldn\'t find the materials!\n')
else:
	save_file(filename, 'materials', str(list(set(materials_tuple))))
	#print list(set(materials_tuple))

filename = 'counted_materials.json'
dir_path = os.path.join('created_files')  # will return 'feed/address'
if not os.path.exists('created_files'):
    os.makedirs('created_files')
new_file = codecs.open(os.path.join(dir_path, filename), 'wb', 'utf-8')
print new_file
new_file.write(str(results))
new_file.close()

def save_file(filename, extension, content):
  #plain_pii_file = str(pii) + '.txt'
  #path_plain_pii_file = path_to_file + plain_pii_file
  print 'Filename: ' + filename
  new_filename = filename[:-4] + '_' + extension + filename[-4:]
  dir_path = os.path.join('created_files')  # will return 'feed/address'
  if not os.path.exists('created_files'):
      os.makedirs('created_files')
  new_file = codecs.open(os.path.join(dir_path, new_filename), 'wb', 'utf-8')
  print new_file
  new_file.write(content)
  new_file.close()
