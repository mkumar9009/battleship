from BattleField import *
class inttype:

    def __init__(self,default):
        self.a=default

    def __get__(self):
        return self.a

    def __set__(self,val):
        self.a=val

    def __delete__(self, instance):
        del self.a

class Ship:


#    field = BattleField()

    def __init__(self,width,height,loc,ship_hit_points):
        self._width=width
        self._height=height
        self._ship_hit_points=ship_hit_points

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,swidth):
        self._width=swidth

    @property
    def hitpoints(self):
        return self._ship_hit_points

    @hitpoints.setter
    def hitpoints(self,ship_hit_points):
        self._ship_hit_points=ship_hit_points

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,sheight):
        self._height=sheight

    @property
    def loc(self):
        return self._sloc
    
    @loc.setter
    def loc(self,sloc):
        self._loc=sloc



