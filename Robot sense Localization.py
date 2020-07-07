###############################   Robot Localization    #########################
#################   Example 1   ####################

#Modify the code below so that the function sense, which takes p and Z as inputs, will output the NON-normalized probability distribution, q, 
#after multiplying the entries in p by pHit or pMiss according to the color in the corresponding cell in world.
#### Then Normalize the values in q and get the final posterior Probability.

p=[0.2, 0.2, 0.2, 0.2, 0.2]   ### prior probab. are equal at the begining before any sense or measurement
world=['green', 'red', 'red', 'green', 'green']
Z='red'

pHit = 0.6   ## if robot sense red multiply it's probab. by 0.6
pMiss = 0.2  ## if robot sense green multiply it's probab. by 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])  ### flag set to be used in the next line 
                                    #   this flag = 1 if color is red   & flag=0  if color is green
        q.append(p[i]*(hit*pHit + (1-hit)*pMiss))  ## Nice Logic code  to give us the posterior probability
    
#	To normalize probabilities
    s=sum(q)
    for i in range(len(p)):
        q[i]=q[i]/s
    return q
print(sense(p,Z))
############################

##############  Example 2   ####################
''' For Multiple Measurement   
#measurements = ['red' , 'green']
for k in range(len(measurements)):
	p=sense(p,measurements[k])
print(p)	
'''
#####################################################################

