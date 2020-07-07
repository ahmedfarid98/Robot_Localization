#####################     MOVE AND SHIFT  FUNCTION   ######################
#Develop a function with inputs [ p (current probabilities) && U (number of moves) ] and return probabilities after that shifting (q)
p = [0,1,0,0,0]
def move(p,u):
	q=[]
	for i in range(len(p)):
		q.append(p[(i-u) % len(p)])
	return q
'''
####  Alternative Solution	isnside the same Move Function
	u=u % len(p)
	q=p[-u:]+p[:-u]
'''
print("1.  Exact move probabilities are :")
print(move(p,0))

#########################		Inexact Move Function   #######################

#########################    In Exact Move function where there is a probability of overshoot or undershoot the target 	 ##################
pExact=0.8
pOvershoot=0.1 
pUndershoot=0.1 
def in_exact_move(p, U):
    q = []
    for i in range(len(p)):
        S=pExact * p[(i-U) % len(p)]
        S=S +pOvershoot * p[(i-U-1) % len(p)]
        S=S +pUndershoot * p[(i-U+1) % len(p)]
        q.append(S)
    return q

print("2. In Exact move probabilities are :")
print(in_exact_move(p,1))

########################## If robot moves 1000 times and therse moves have error it will reach Max uncertainty state as following :
for k in range(1000):
	p=in_exact_move(p,k)


print("3. with moving 1000 times the robot reaches max. uncertainty \n  with probabilities equal at all cells as below :")
print(p)	