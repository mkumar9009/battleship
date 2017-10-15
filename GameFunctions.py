
def converttonumber(a):
    return str(ord(a)-ord('A')+1)

# 1 - it was a hit
# 0 - it was a miss

def firemisile(attacker,opponent,tgtloc):
    print ("fired")
    return opponent.HitOrMiss(tgtloc)

def ShipHitPoints(ship_type):
    if(ship_type=='P'):
        return 1
    elif(ship_type=='Q'):
        return 2
        
def isAttackerWinner(attacker,opponent):
    if(opponent.isShipLeft()==0):
        print (attacker.name + " is winner")
        print ("Game Ends Here")
        return 1
    else:
        return 0

def ChangeTurn(attacker,opponent,misilehit):
    if(opponent.isMisileLeft()==1 and misilehit==0):
        print ("##################################################################################################Opponent Turn")
        temp=attacker
        attacker=opponent
        opponent=temp
        return attacker,opponent
#    if(attacker.isMisileLeft()==1 and misilehit==1):
#        print("Its a hit . next chance to attacker")
#        return attacker,opponent
    else:
        print ("continue Same turn")
        return attacker,opponent

def DeclarePeace(attacker,opponent):
    if(attacker.isMisileLeft()==0 and opponent.isMisileLeft()==0):
        print ("There is no winner!, Declare peace")
        return 1
    else:
        return 0

def StartGame(attacker,opponent):
    while(1):
        tgtloc = attacker.gettargetloc()
        misilehit = firemisile(attacker,opponent,tgtloc)
        print ("misilehit", misilehit)
        attacker.UpdateMisiles()
        if(misilehit==1):
            opponent.UpdateShipHealth(tgtloc)
            opponent.BF.UpdateBattleField(tgtloc)
            if(isAttackerWinner(attacker,opponent)):
                break;
        if(DeclarePeace(attacker,opponent)==1):
            break;
            
        attacker,opponent=ChangeTurn(attacker,opponent,misilehit)
                 
    return 1
