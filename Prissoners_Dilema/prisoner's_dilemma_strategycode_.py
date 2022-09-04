from numpy import random

akh_srj_d_cnt = 0
akh_srj_c_cnt = 0

def akhilesh_suraj(oppIn = None):
    global akh_srj_d_cnt
    global akh_srj_c_cnt
    
    if (oppIn == None):
        akh_srj_d_cnt = 0
        akh_srj_c_cnt = 0

    if (akh_srj_d_cnt < 4):
        akh_srj_d_cnt += 1
        return "D"

    akh_srj_c_cnt += 1

    if (akh_srj_c_cnt % 2 == 0):
        akh_srj_d_cnt = 0

    return "C"

def allC(oppIn = None):
    return "C"

def allD(oppIn = None):
    return "D"

def tft(oppIn = None):
  if(oppIn == "C"):
    return "D"
  else:
    return "C"

def tft1(oppIn = None):
  if(oppIn == "D"):
    return "C"
  else:
    return "D"

def random1(oppIn = None):
  return random.choice(["C", "D"])

############ Main
i = 1
n = 15 #round
out1 = akhilesh_suraj()
out2 = tft()
p1 = 0
p2 = 0
print("Player 1 - Player 2")
while(i!=n):
	if(out1 == out2 and out1 == "C"):
		print("20 Points - 20 Points")
		p1 = p1 + 20
		p2 = p2 + 20
	elif(out1 == out2 and out1 == "D"):
		print("10 Points - 10 Points")
		p1 = p1 + 10
		p2 = p2 + 10
	elif(out1 != out2 and out1 == "D"):
		print("30 Points - 0 Points")
		p1 = p1 + 30
	else:
		print("0 Points - 30 Points")
		p2 = p2 + 30
        
	out1T = akhilesh_suraj(out2)
	print(out1, " - ", out2)
	out2 = tft(out1)
	out1 = out1T
	i+=1
print("___________________________________")
print("P1 =", p1, " - P2 =", p2)
