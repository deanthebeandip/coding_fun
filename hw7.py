#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:01:49 2019

@author: Juan Carbajal
@content: function knights_tour(n) creates an nxn grid for
user to attempt to click through a knights tour
"""
#create class and function knights tour(n) that together launch an n × n knight’s tour game
import Tkinter as Tk
#import numpy as np
class Ktour(object):
    def __init__(self,root,n):
        cubeSize = 100 # store size of each cube
        game_board = [] # list composed of 2-element lists as its elements
        self.cubes = []
        self.current = (0,0)
        for i in range(n+1):
            for j in range(n+1):
                game_board.append([i,j])
        #self.color_s_list = [[0]*(n+1)]*(n+1) # 2d list to store square positions
        # Canvas object where grid will be printed on
        self.w = Tk.Canvas(root, width = n*100, height = n*100)
        self.w.pack()
        # create lines
        for i in range(n-1):
            d = (i+1)*cubeSize
            self.w.create_line(d,0,d,n*100,)
            self.w.create_line(0,d,n*100,d)
        # create rectangles that overlap on canvas object and append to 1D cubes array
        for i in range(n):
            for j in range(n):
                self.cubes.append(self.w.create_rectangle(cubeSize*game_board[j][1],cubeSize*game_board[i][1],cubeSize*game_board[j][1]+cubeSize,cubeSize*game_board[i][1]+cubeSize))
        # set first square (top-left) to be orange
        self.w.itemconfigure(self.cubes[0], fill = 'orange')
        #paint every other square orange
        #for i in range(0,n*n+1,2):
            #self.w.itemconfigure(cubes[i], fill = 'orange')
        self.w.bind('<Button-1>',self.squareclick)
        self.w.pack()
    def squareclick(self,event):
        # should get the position of the click and compare it with
        # self.current coordinate-wise to determine if valid move
        floor_row = (event.y / 100)
        floor_column = (event.x / 100)
        item = self.w.find_closest(event.x,event.y)
        # take abs value of each x and y and this will account for all 8 combinations 
        # if abs difference x = 1 and y = 2 OR x = 2 and y = 1
        if self.w.type(item) == 'rectangle':
            if (abs(floor_row-self.current[0]) == 2 and abs(floor_column-self.current[1]) == 1) or (abs(floor_row-self.current[0]) == 1 and abs(floor_column-self.current[1]) == 2):
                # update colors 
                self.w.itemconfig(self.cubes[self.current[1] + 5*self.current[0]], fill = 'blue')
                self.w.itemconfig(self.cubes[floor_column + 5*floor_row], fill = 'orange')
                # update curreny position
                self.current = (floor_row,floor_column)
            else:
                pass
        else:
            pass
def knights_tour(n):
    root = Tk.Tk() # root
    game = Ktour(root,n)
    root.mainloop()
if __name__=='__main__':
    knights_tour(5)   