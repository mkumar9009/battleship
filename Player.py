from Ship import *
from BattleField import *
from GameFunctions import converttonumber
class Player():
    _myships=[]
    _misiles_tgt_loc=[]
    _ship_locs={}
    def __init__(self,name,bndry_width,bndry_height):
        self.name=name
        self.BF = BattleField(bndry_width,bndry_height)
        self._misiles={}

    def add_ship(self,ship_width,ship_height,loc,ship_no,BF,ship_hit_points):
        if (BF.loc_availability(ship_width,ship_height,loc,ship_hit_points)):
            s= Ship(ship_width,ship_height,loc,ship_hit_points)
            return self._myships.append(s)
        else:
            AssertionError("Location is not available")

    def convert_tgtlocs(self,locs):
        tgtlocs=[]
        for loc in locs:
            coord = list(loc)
            coord[0]=converttonumber(coord[0])
            tgtlocs.append(coord[1]+coord[0])
        return tgtlocs

    
    @property
    def misiles(self):
        return self._misiles

    @misiles.setter
    def misiles(self,tgtlocs):
        tgtlocs = self.convert_tgtlocs(tgtlocs)
        self._misiles=tgtlocs
        print (self._misiles)

    def remaining_ships(self):
        return len(self._myships)
    
    def isShipLocated(self,tgtloc):
        print ("Tgt loc is ",tgtloc)
        print ("field locs",self.BF.field)
        if tgtloc in self.BF.field:
            print ("Target loc HIT")
            return 1 
        else:
            return 0

    def HitOrMiss(self,tgtloc):
        print ("check hit misss")
        if (self.isShipLocated(tgtloc)==1):
            print ("shiplocated and a hit")
            return 1
        else:
            print ("Miss it is")
            return 0
       
    def UpdateShipHealth(self,tgtloc):
        #reduce hit points of ship
        print ("ship health",self.BF.field[tgtloc])
        self.BF.field[tgtloc]=self.BF.field[tgtloc]-1
        print ("updated ship health",self.BF.field[tgtloc])
        return self.BF.field[tgtloc]
                
    def MisilesLeft(self):
        return len(self._misiles_tgt_loc)

    def isMisileLeft(self):
        if len(self._misiles) > 0:
            return 1
        else:
            return 0

    def isShipLeft(self):
        if len(self.BF.field)>0:
            return 1
        else:
            return 0 
    
    def gettargetloc(self):
        print ("Misiles", self._misiles)
        return self._misiles[0]

    def UpdateMisiles(self):
        print ("decreased misiles")
        self._misiles.pop(0)
        print ("Misiles",self._misiles)
        
