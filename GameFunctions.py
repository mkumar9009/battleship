
def converttonumber(a):
    return str(ord(a)-ord('A')+1)

# 1 - it was a hit
# 0 - it was a miss

def firemisile(attacker,opponent,tgtloc):
    return opponent.HitOrMiss(tgtloc)

def ShipHitPoints(ship_type):
    if(ship_type=='P'):
        return 1
    elif(ship_type=='Q'):
        return 2
        
def isAttackerWinner(attacker,opponent):
    if(opponent.isShipLeft()==0):
        print (attacker.name + " won the battle")
        return 1
    else:
        return 0

def ChangeTurn(attacker,opponent,misilehit):
    if(opponent.isMisileLeft()==1 and misilehit==0):
        temp=attacker
        attacker=opponent
        opponent=temp
        return attacker,opponent
    elif(opponent.isMisileLeft()==0 and misilehit==0):
        print (opponent.name, "has no more misiles left")
        return attacker,opponent
    else:
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
        attacker.UpdateMisiles()
        if(misilehit==1):
            print (attacker.name, "fires a misile with target" , tgtloc, "which hit")
            opponent.UpdateShipHealth(tgtloc)
            opponent.BF.UpdateBattleField(tgtloc)
            if(isAttackerWinner(attacker,opponent)):
                break;
        else:
            print (attacker.name, "fires a misile with target" , tgtloc, "which missed")
            
        if(DeclarePeace(attacker,opponent)==1):
            break;
            
        attacker,opponent=ChangeTurn(attacker,opponent,misilehit)
                 
    return 1
