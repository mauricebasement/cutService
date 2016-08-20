import math
import sys
pi = math.pi

#Open File
dxf = open(sys.argv[1], "r")
lines = dxf.readlines()
lines = [w.replace('\n', '') for w in lines]
lines = [w.replace('\r', '') for w in lines]

lineNr = 0

def readline():
  global lineNr
  lineNr+=1
  return lines[lineNr-1]

print lines

counter = 0

distance = 0

x1=0
x2=0
y1=0
y2=0

def linecheck(line):
  if line == "EOF": #or line == "":
    return False
  else:
    return True
  

def LINE():
  while True:
    line = readline()
    if line == " 10":
	x1=float(readline())
    if line == " 11":
	x2=float(readline())
    if line == " 20":
	y1=float(readline())
    if line == " 21":
	y2=float(readline())
    if line == "  0":
      x = x2-x1
      y = y2-y1
      dist = math.sqrt(math.pow(x,2)+math.pow(y,2))
      print dist
      return dist
    if line == "EOF" or line == "":
      dist = -1
      return dist

def CIRCLE():
  while True:
    line = readline()
    if line == " 40":
      r=float(readline())
    if line == "  0":
      dist = 2 * math.pi * r
      print dist
      return dist
    if linecheck(line) == False:
      dist = -1
      return dist

def ARC():
  while True:
    line = readline()
    if line == " 40":
      r=float(readline())
    if line == " 50":
      a=float(readline())
    if line == " 51":
      b=float(readline())
    if line == "  0":
      dist = math.pi * math.pow(r,2) * math.fabs(a-b)/360;
      print dist
      return dist
    if linecheck(line) == False:
      dist = -1
      return dist

def error():
	print "ERROR in dxf file!"

while counter == 0:
  line = readline()
  #print line
  if line == "LINE":
    print "found line"
    dist = LINE()    
    if dist == -1:
      error()
    else:
      distance += dist

  if line == "CIRCLE":
    print "found circle"
    dist = CIRCLE()    
    if dist == -1:
      error()
    else:
      distance += dist

  if line == "ARC":
    print "found arc"
    dist = ARC()    
    if dist == -1:
      error()
    else:
      distance += dist

  if linecheck(line) == False:
    print distance
    counter = 1



exit()
