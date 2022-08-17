#Returns all the dictionaries that contain the lod with k:v pairs
def copy_matching(lod, k, v):
  accumulator = []
  for dicts in lod:
    if dicts.get(k,None) == v:
      accumulator.append(dicts)
  return accumulator


def sorting(lst):
  return lst[0]

#Sorts each list from farthest time to closest time  
def sorter(lol):
  lol.sort(key=sorting)