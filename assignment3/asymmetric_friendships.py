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
    records.sort()
    key = records[0]
    value = records[1]
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    friends = {}
    for v in list_of_values:
        if v not in friends:
            friends[v] = 1
        else:
            friends[v] += 1
    for f in friends:
        if friends[f] == 1:
               mr.emit((key,f))
               mr.emit((f, key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
