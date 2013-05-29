import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
global   matrixdict
matrixdict={}
# =============================
# Do not modify above this line

def mapper(records):
    # key: document identifier
    # value: document contents
    matrix = records[0]
    key = records[1:3]
    value = records[3]
    if matrix == 'a':
        mr.emit_intermediate((key[1]), records)
    if matrix == 'b':
        mr.emit_intermediate((key[0]), records)

def reducer(keys, subelements_list):
    # key: word
    # value: list of occurrence counts
    #get all records with the same k...
    amatrix = []
    bmatrix = []
    for sub in subelements_list:
        if sub[0] == 'a':
            amatrix += [sub[1:]]
        if sub[0] == 'b':
            bmatrix += [sub[1:]]
##    print amatrix, bmatrix
    for aelems in amatrix:
        for belems in bmatrix:
            value = aelems[2]*belems[2]
            if (aelems[0],belems[1]) not in matrixdict:
                matrixdict[(aelems[0],belems[1])] = value
            else:
                matrixdict[(aelems[0],belems[1])] += value
    
## 
##            print output
          

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  matrixdict.sort()
  for elements in matrixdict:
      elelist = list(elements)
      elelist.insert(2,matrixdict[elements])
      elements = tuple(elelist)
      print elelist
