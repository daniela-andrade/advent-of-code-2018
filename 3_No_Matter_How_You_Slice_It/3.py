import re

ids = []
count = 0

def removeFromIds(ID):
  if ID in ids:
    ids.remove(ID)

with open('input.txt','r') as file:

  fabric = dict([]) 
  lines = file.readlines()
  prog = re.compile(r"[#](\d*)\s\D\s(\d*)\D(\d*)\D\s(\d*)[x](\d*)")

  for line in lines:
    result = prog.search(line)
    if result:
      ID = int(result.group(1))
      x = int(result.group(2))
      y = int(result.group(3))
      w = int(result.group(4))
      h = int(result.group(5))

      ids.append(ID)

      for i in range(x,x+w):
        for j in range(y,y+h):
          if (i,j) in fabric:
            if len(fabric[(i,j)]) == 1:
              count += 1;
            fabric[(i,j)].append(ID)
            for id in fabric[(i,j)]:
              removeFromIds(id)
          else:
            fabric[(i,j)] = [ID]   

  print(count, ids)

def printMatrix(x, y, w, h):
  for i in range(x,x+w):
    row = ''
    for j in range(y,y+h):
      row += str(fabric[(i,j)])
    print(row)


