#Given the list motions=[1,1] which means the robot 
#moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves 
#right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]    #### Uniform distribution at the begining
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green'] ### Robot sense red then green
motions = [1,1]      ### Robot moves Right then Right again

pHit = 0.6    ## probabilities of Hit the color or Miss it 
pMiss = 0.2

pExact = 0.8      ### probabilities  of making Exact required posisition or missing it or overshooting it.
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])   ## set flag  to give 1 if input measurement is same as grid cell color and gives 0 otherwise
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s          ####  To normalize prob. values in q
    return q

def move(p, U):
    q = []
    for i in range(len(p)):                           
        s = pExact * p[(i-U) % len(p)]             #### probab. of robot moving to the exact place with no error with probab. of Doing that = 0.8 
        s = s + pOvershoot * p[(i-U-1) % len(p)]   #### probab. of robot moving to overshoot place with probab. of error= 0.1, (i-U-1) shift one cell right 
        s = s + pUndershoot * p[(i-U+1) % len(p)]  #### probab. of robot moving to Undershoot place with probab. of error= 0.1, (i-U-1) shift one cell Left 
        q.append(s)
    return q
#
for k in range(len(measurements)):   ### len(measurements) = 2 in this example.
    p=sense(p,measurements[k])       ### the arrangement between sense and move function is very important ,In this example the robot sense first then moves
    p=move(p,motions[k])           ### so function must be written in this way unless it will give wrong probabilities
#
print(p)         
