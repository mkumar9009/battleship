class BattleField:
    
    _shiplocs = {}

    def __init__(self,bndry_width,bndry_height):
        
        self.width=bndry_width
        self.height=bndry_height
        self.field={}

    def setloc(self,xy,player_name):
        self.field[xy]=player_name

    def WithinBoundry(self,x,y):
        if (x>self.width or y > self.height):
            return 0
        else:
            return 1

#if 0 is returned then location is not available. Its already occupied.
#if 1 is returned then location is  
    def isLocAvailable(self,loc):
        if str(loc[1]+loc[0]) in self.field:
            return 0
        else:
            return 1

    def isSpaceAvailable(self,space_inright,space_inleft,space_up,space_down,ship_width,ship_height):
        if((space_inright >= ship_width) and (space_down >= ship_height)):
            xcntr=0
            ycntr=0
        elif((space_inright>= ship_width) and (space_up >= ship_height)):
            xcntr=0
            ycntr=-ship_height
        elif((space_inleft >= ship_width) and (space_down >= ship_height)):
            xcntr=-ship_width
            ycntr=0
        elif((space_inleft >= ship_width) and (space_up >= ship_height)):
            xcntr=-ship_width
            ycntr=-ship_height
        else:
            AssertionError( "Space NOt available. Ship cannot be added")
            return 0,0,0  
        return xcntr,ycntr,1 

    def PlaceShip(self,loc,xcntr,ycntr,w,h,ship_hit_points):
        for x in range(w):
            for y in range(h):
                self.field[str(int(loc[1])+xcntr+x)+str(int(loc[0])+ycntr+y)]=ship_hit_points

    def check_ship_placement(self,loc,ship_width,ship_height,ship_hit_points):
        space_inright = self.width - int(loc[1]) +1
        space_inleft  = int(loc[1])

        space_down      = self.height - int(loc[0])+1
        space_up        = int(loc[0])

        xcntr,ycntr,space_found=self.isSpaceAvailable(space_inright,space_inleft,space_up,space_down,ship_width,ship_height)
        if(space_found):
            self.PlaceShip(loc,xcntr,ycntr,ship_width,ship_height,ship_hit_points)
        else:
            return 0

        return 1
 
#w = width of ship
#h = height of ship
#loc contains the input location
    def loc_availability(self,w,h,loc,ship_hit_points):
        if (self.WithinBoundry(int(loc[1]),int(loc[0]))):
            if (self.isLocAvailable(loc)==1):
                return self.check_ship_placement(loc,int(w),int(h),ship_hit_points)
        else:
            raise AssertionError("NOt in boundry can't place it")

    def UpdateBattleField(self,tgtloc):
        if(self.field[tgtloc]==0):
            self.field.pop(tgtloc,None)
        return 1
