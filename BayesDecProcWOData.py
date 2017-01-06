## This script will perform Bayes Decision Procedure without Data:
# It prompts the user to input numbers and names and then prescribes action

### IMPORT ###

import sys

### DATA TO BE USED ###

d = {'yes':1,'y':1,'YES':1,'Yes':1,'Y':1,'1':1,'n':0,'n':0,'N':0,"No":0,'NO':0,'0':0}


### FUNCTIONS ########


# find the dot product of two vectors represented by lists

def dot_prod(V1,V2):
    dotprod = 0
    for i in range(len(V1)):
        dotprod = dotprod + V1[i]*V2[i]
    return dotprod

# This function prompts user to input the names of the states of nature

def THETA_name_Prompt():
    n = int(raw_input('How many states of nature? - '))
    THETA = n*['']
    for i in range(n):
        print('Name of state of nature '+str(i+1)+' - ')
        THETA[i] = sys.stdin.readline().strip()
    return THETA
# This function prompts the user to input the prior distribution of the states of nature
def PriDist(THETA):
    n = len(THETA)
    P_THETA = n*[0]
    for i in range(len(THETA)):
        print('Prior Probability of '+ THETA[i] +' - ')
        P_THETA[i] = float(sys.stdin.readline().strip())
    return P_THETA

# This function prompts user to input the names of the actions available

def ACTION_name_Prompt():
    n = int(raw_input('How many actions available? - '))
    ACTION_name = n*['']
    for i in range(n):
        print('Name action '+str(i+1)+' - ')
        ACTION_name[i] = sys.stdin.readline().strip()
    return ACTION_name

# This function prompts the user to give the loss table:

def LOSS_TABLE(ACTION_name,THETA):
    n = len(ACTION_name)
    m = len(THETA)
    L_A_THETA = n*[0]
    print('Now we determine the LOSS table by inputing loss function values \n')
    for i in range(len(ACTION_name)):
        L_A_THETA[i] = []
        for j in range(len(THETA)):
            print('L('+ACTION_name[i]+','+THETA[j]+') = ')
            v = float(sys.stdin.readline().strip())
            L_A_THETA[i].append(v)
    return L_A_THETA

    
# This function calculates the expected value of loss for each action

def Expected_Loss(L_A_THETA,P_THETA):
    n = len(L_A_THETA)
    Exp_Loss = n*[0]
    for i in range(n):
        Exp_Loss[i] = dot_prod(L_A_THETA[i],P_THETA)
    return Exp_Loss

    
### MAIN BODY OF SCRIPT ###


print("This script performs Bayes Decision Procedure without Data with user input\n")
a0 = True
while a0 == True:
    THETA = THETA_name_Prompt()
    print('Advance to Prior Distribution?')
    a0 =  not d[sys.stdin.readline().strip()]
        
a0 = True
while a0 == True:
    P_THETA = PriDist(THETA)
    print('Advance to naming Actions?' )
    a0 =  not d[sys.stdin.readline().strip()]

a0 = True
while a0 == True:
    ACTION_name = ACTION_name_Prompt()
    print('Advance to Loss Table?')
    a0 =  not d[sys.stdin.readline().strip()]

a0 = True
while a0 == True:
    L_A_THETA = LOSS_TABLE(ACTION_name,THETA)
    print('Continue to Expected Loss Result?')
    a0 =  not d[sys.stdin.readline().strip()]

print('Expected loss of each action is: ')

Exp_Loss = Expected_Loss(L_A_THETA,P_THETA)
for i in range(len(ACTION_name)):
    print('Action: '+ACTION_name[i]+'-------Expected Loss: '+str(Exp_Loss[i]))
