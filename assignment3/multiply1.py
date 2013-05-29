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
    matrix = records[0]
    key = records[1:3]
    value = records[3]
    if matrix == 'a':
        k=0
        while k<5:
            mr.emit_intermediate((key[0],k), records)
            k += 1
    if matrix == 'b':
        i = 0
        while i<5:
            mr.emit_intermediate((i,key[1]), records)
            i += 1

def reducer(keys, subelements_list):
    # key: word
    # value: list of occurrence counts

    amatrix = []
    bmatrix = []
    value = 0
    for sub in subelements_list:
        if sub[0] == 'a':
            amatrix += [sub[1:]]
        if sub[0] == 'b':
            bmatrix += [sub[1:]]
    for aelems in amatrix:
        for belems in bmatrix:
            if aelems[1] == belems[0]:
        #get all records with the same k...
                    value += aelems[2]*belems[2]
    output = list(keys)
    output.insert(2, value)
    output = tuple(output)
    mr.emit(output)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  

