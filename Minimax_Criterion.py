## This script will perform the Minimax Criterion for a set of decisions:
# It prompts the user to input numbers and names and then prescribes action
# The minimax is a decision analysis criterion which is extremely conservative
# It assumes the worst is going to happen and tries to choose the action
# With the smallest maximum loss associated with it.
### IMPORT ###

import sys

### DATA TO BE USED ###

d = {'yes':1,'y':1,'YES':1,'Yes':1,'Y':1,'1':1,'n':0,'n':0,'N':0,"No":0,'NO':0,'0':0}


### FUNCTIONS ########


# This function prompts user to input the names of the states of nature

def THETA_name_Prompt():
    n = int(raw_input('How many states of nature? - '))
    THETA = n*['']
    for i in range(n):
        print('Name of state of nature '+str(i+1)+' - ')
        THETA[i] = sys.stdin.readline().strip()
    return THETA


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

def ACTION_MAX(L_A_THETA,ACTION_name):
    n = len(L_A_THETA)
    Max_Loss = n*[0]
    val = 10000000000000
    for i in range(n):
        Max_Loss[i] = max(L_A_THETA[i])
        if Max_Loss[i] < val:
            val = Max_Loss[i]
            p = i
    return Max_Loss,p

    
### MAIN BODY OF SCRIPT ###


print("This script performs Minimax decision procedure with user input\n")
a0 = True
while a0 == True:
    THETA = THETA_name_Prompt()
    print('Advance to Action naming?')
    a0 =  not d[sys.stdin.readline().strip()]        

a0 = True
while a0 == True:
    ACTION_name = ACTION_name_Prompt()
    print('Advance to Loss Table?')
    a0 =  not d[sys.stdin.readline().strip()]

a0 = True
while a0 == True:
    L_A_THETA = LOSS_TABLE(ACTION_name,THETA)
    print('Continue to Max loss of actions?')
    a0 =  not d[sys.stdin.readline().strip()]

print('Maximum loss of each action is: ')

Max_Loss,p = ACTION_MAX(L_A_THETA,ACTION_name)
for i in range(len(ACTION_name)):
    print('Action: '+ACTION_name[i]+'-------Maximum Loss: '+str(Max_Loss[i]))


print('Action which minimises the max loss is: '+ACTION_name[p]+' --> '+str(Max_Loss[p]))



## POSSIBLE IMPROVEMENTS:If two or more actions have equal max values that
# minimise the minimax then we should then only consider these and select from
# these the one which minimises the next maximum value.
