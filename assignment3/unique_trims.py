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
    key = records[0]
    value = records[1]
    hashable = value.split()
    trim = hashable[0][:-10]
    mr.emit_intermediate(trim, key)

def reducer(trimmed_nucl, keys):
    # key: word
    # value: list of occurrence counts
    mr.emit(trimmed_nucl)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
