import argparse
import json
import csv
import os

parser = argparse.ArgumentParser(description="Convert JSON to CSV")
parser.add_argument('dir', help='The directory holding the JSON files.')
parser.add_argument('outfile', help='The file to write to.')
args = parser.parse_args()

attributes = ['username','age','gender','ethnicity','occupation',
              'status', 'religion', 'location',
              'year_reported','month_reported','last_activity', 'scam']

# 'location','country','longitude','latitude',

outhandle = csv.writer(open(args.outfile, 'w', newline = '', encoding='utf-8'))
outhandle.writerow(attributes)

for jsonfile in os.listdir(args.dir):
  profile = json.load(open(args.dir+os.sep+jsonfile,'r'))
  # number = int(jsonfile[:jsonfile.rindex('.')])
  values = []
  for k in attributes:
    if k in profile:
      values.append(profile[k])
# =============================================================================
#     elif k == 'number':
#       values.append(number)
# =============================================================================
    elif k == 'fold':
      values.append(0)
    else:
      values.append(None)
  outhandle.writerow(values)
