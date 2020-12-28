''' PyMath Alpha-1, use freely. Use the GetIndex() function to see what a function does. You use it as i.e: print(GetIndex('PMV'))'''


def Round(k,b):
  if b < 2:
    return round(k)
  return (k+b)-(k%b)
def Base(k,b):
  base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ret = ""
  while k:
    ret += base[k%b]
    k //= b
  return ret[::-1] or "0"
def Dist(c1,c2):
  return (c2[0]-c1[0])**2+(c2[1]-c1[1])**2 
def Perm(k,b):
  return k**b
def Fact(k):
  f = 1
  for i in range(1,k+1):
    f *= i
  return f
def Comb(n,r):
  return Fact(n)/Fact(r*Fact(n-r))
def Mod(k,b):
  return k%b
def Quo(k,b):
  return k // b
def Add(k,b):
  return k+b
def Sub(k,b):
  return k-b
def Div(k,b):
  return k/b
def IrrPi(k):
  pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989'
  if k > len(pi):
    return None
  elif k == 0:
    return 3
  else:
    return float(pi[:k+2])
def IrrFib(k,b):
  ret = [k[0],k[1]]
  for i in range(b):
    ret.append(ret[-1]+ret[-2])
  return ret
def Sqrt(k):
  return k**0.5
def Ceil(k,b):
  return b-k%b+k
def Floor(k,b):
  return b-k%b+k-b
def AbsPos(k):
  if k < 0:
    return -k
  else:
    return k
def AbsNeg(k):
  if k > 0:
    return -k
  else:
    return k
def AbsOpp(k):
  return -k
def Term(k):
  return (k**2+k)/2
def BC_AD(bc,ad):
  bc = AbsNeg(bc)
  return ad-bc
def Lineq(k,b,n):
  if k < b and n == True:
    return True
  elif k == b:
    return True
  elif k > b and n == False:
    return True
  else:
    return False
def Circ(d):
  return IrrPi(3)*d
def Care(d):
  return IrrPi(3)*(d/2)**2
def Diam(r):
  return r * 2
def GetIndex(k):
  index = {
    'Round': 'Rounds to ~arg1~ to nearest ~arg2~',
    'Base': 'Converts base 10 number ~arg1~ to base ~arg2~',
    'Dist': 'Uses pythagorean theorem to find distance between ~arg1: [x,y]~ and ~arg2: [x,y]~.',
    'Perm': 'Finds permutations of value: ~arg1~, and sample: ~arg2~',
    'Fact': 'Gets the factorial value of ~arg1~',
    'Comb': 'Finds combinations of value: ~arg1, and sample: ~arg2~',
    'Mod': 'Modulo',
    'Quo': 'Quotient',
    'Add': 'Addition',
    'Sub': 'Subtration',
    'Div': 'Division',
    'IrrPi': 'Gets pi to the ~arg1~th digit.',
    'IrrFib': 'Gets fib to the ~arg2~th digit when the first two numbers are ~arg1: [num1,num2]~.',
    'Sqrt': 'Square root',
    'Ceil': 'Ceilings ~arg1~ to ~arg2~',
    'Floor': 'Floors ~arg1~ to ~arg2~',
    'AbsPos': 'Absolute value',
    'AbsNeg': 'Returns negative value',
    'AbsOpp': 'If positive, returns negitave, if negative, returns positive',
    'Term': 'Finds terminal (addition factorial)',
    'BC_AD': 'Finds time between bc ~arg1~ and ad ~arg2~',
    'Lineq': 'Finds if ~arg3~ True, if ~arg1~ <= ~arg2~, otherwise finds if ~arg1~ >= ~arg2~.',
    'Circ': 'Finds circumference from ~arg1~ (diameter)',
    'Care': 'Finds area of circle from ~arg1~ (diameter)',
    'Diam': 'Finds diameter from ~arg1~ (radius)',
    'GetIndex': 'Gets purpose of ~arg1; i.e GetIndex(\'Diam\')~ function.',
    'PMV': 'Gets version of PyMath (PM)'
      }
  return index[k]
def PMV():
  return 'Stage Alpha 1: Please suggest your ideas on github.com/nprghu/PyMath/discussions/1 (GitHub)'
  
