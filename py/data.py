import csv
from hashlib import new
import json
from lib2to3.pgen2.token import NEWLINE
import urllib.request

#Return 1st par as a key and 2nd par as a value
def dic_list_gen(list_strings, list_lists):
  retlist = []
  for lists in list_lists:
    dicts = {}
    for i in range(0,len(list_strings)):
      value = lists[i]
      key = list_strings[i]
      dicts[key] = value
    retlist.append(dicts)
  return retlist

#Return each line of a file as a list in a list
def read_values(filename):
  retval = []
  with open(filename) as f:
    reader = csv.reader(f)
    next(reader)
    for lines in reader:
      retval.append(lines)
  return retval

#Make lists of the 1st par value paired with the 2nd par value
def make_lists(dict_keys, list_dicts):
  retlist = []
  for dicts in list_dicts:
    list_for_dict = []
    for keys in dict_keys:
      value = dicts[keys]
      list_for_dict.append(value)
    retlist.append(list_for_dict)
  return retlist



#Converts json blob into python data
def json_loader(url):
  request = urllib.request.urlopen(url, data=None, cafile=None, capath=None, cadefault=False,context=None)
  j_content = request.read().decode()
  content = json.loads(j_content)
  return content

#Makes values of keys in the 1st param into floats
def make_values_numeric(keys,d):
  for key in d:
    if key in keys:
      d[key] = float(d[key])
  return d

#Write the values of the keys into the given file
def write_values_h(filename, list_lists, head):
  with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(head)
    for lists in list_lists:
      writer.writerow(lists)

def save_data(l_s,l_d,filename):
  lists= make_lists(l_s, l_d)
  write_values_h(filename, lists, l_s)

#Make the header columns into keys and the corresponding info on each row into values
def load_data(filename):
  with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
  lists = read_values(filename)
  retval = dic_list_gen(header,lists)
  return retval

#Compares data between 2 files and adds more onto file1 if some is missing
def compare_data(filename1,filename2):
  r1 = read_values(filename1)
  r2 = read_values(filename2)
  with open(filename1, 'a', newline='') as f:
    writer = csv.writer(f)
    for lists in r2:
      if lists not in r1:
        writer.writerow(lists)
