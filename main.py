#! /usr/bin/env python
#this is the main file which runs the battleship game after getting the input file 
#   Prerequisties: 
#           Input file has to be placed in the same location as that of main.py
#
#
#
# function to convert the boundry width to a number
import sys
from Player import *
from GameFunctions import *

if __name__ == '__main__':

    #read the input
    try:
        f = open(sys.argv[1], 'r')
        rawinput = f.readlines()

        #get battlefield dimensions
        bndry_width = int(rawinput[0].split()[3])
        bndry_height = int(ConvertToNumber(rawinput[0].split()[4]))

        #battleship type
        ship_type1 = rawinput[1].split()[4]
        ship_type2 = rawinput[5].split()[4]

        ship_hit_points1 = ShipHitPoints(ship_type1)
        ship_hit_points2 = ShipHitPoints(ship_type2)

        #dimension of battleship
        ship1_width=rawinput[2].split()[4]
        ship1_height=rawinput[2].split()[5]
        ship2_width=rawinput[6].split()[4]
        ship2_height=rawinput[6].split()[5]
        
        #location of battleship
        loc1A=list(rawinput[3].split()[7])
        loc1A[0]=ConvertToNumber(loc1A[0])
        loc1B=list(rawinput[4].split()[7])
        loc1B[0]=ConvertToNumber(loc1B[0])

        loc2A=list(rawinput[7].split()[7])
        loc2A[0]=ConvertToNumber(loc2A[0])
        loc2B=list(rawinput[8].split()[7])
        loc2B[0]=ConvertToNumber(loc2B[0])

        misiles_of_A = rawinput[9].split()[5:]
        misiles_of_B = rawinput[10].split()[5:]
#        print ship_type1,ship_type2,ship1_width,ship1_height,ship2_width,ship1_height,loc1A,loc1B,loc2A,loc2B,misiles_of_A,misiles_of_B

        player1 = Player("Player-1",bndry_width,bndry_height)
        player2 = Player("Player-2",bndry_width,bndry_height) 

        player1.add_ship(ship1_width,ship1_height,loc1A,1,player1.BF,ship_hit_points1)
        player1.add_ship(ship2_width,ship2_height,loc2A,2,player1.BF,ship_hit_points2)
 
        player2.add_ship(ship1_width,ship1_height,loc1B,1,player2.BF,ship_hit_points1)
        player2.add_ship(ship2_width,ship2_height,loc2B,2,player2.BF,ship_hit_points2)

        player1.misiles=misiles_of_A
        player2.misiles=misiles_of_B
    
        #call the battleship game
        StartGame(player1,player2)
        # do stuff with f
    finally:
        if f is not None:
            f.close()

