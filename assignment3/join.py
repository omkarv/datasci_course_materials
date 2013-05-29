import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(records):
    # key: document identifier
    # value: document contents
    key = records[1]
##    print key
    mr.emit_intermediate(key, records)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    order = []
    for v in list_of_values:
      if v[0] == 'order':
          order = v
          break
    for v in list_of_values:
      if v[0] == 'line_item':
##        print order
##        print v
##        print order + v
        mr.emit((order + v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
