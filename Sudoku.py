from tkinter import *
from tkinter import font
from soku import Solver
import pandas as pd
import os

def next():
	global c_data,df,C,pro_id
	pro_id+=1
	if pro_id == df.shape[0]:
		pro_id-=1
	d = df[df.columns[0]].values[pro_id]
	sol = Solver()
	sol.get_string(d)
	sol.solve()
	for i in range(9):
		for j in range(9):
			C.itemconfig(c_data[i][j],text=str(sol.data[i][j]))

def previous():
	global c_data,df,C,pro_id
	pro_id-=1
	if pro_id == -1:
		pro_id+=1
	d = df[df.columns[0]].values[pro_id]
	sol = Solver()
	sol.get_string(d)
	sol.solve()
	for i in range(9):
		for j in range(9):
			C.itemconfig(c_data[i][j],text=str(sol.data[i][j]))
			
windows = Tk()
windows.wm_title("Sudoku Solver")
fonts = font.Font(family='Helvetica',size=20, weight='bold')
global c_data,df,C,pro_id

pro_id = 0
df = pd.read_csv("sudoku.csv")
C = Canvas(windows, bg = '#FFFFFF', height =38*15, width = 38*15)



for i in range(3,13):
	C.create_line(38*i,3*38,38*i,12*38,fill = 'black',width=1 if (i+3)%3 else 2)
for i in range(3,13):
	C.create_line(3*38,38*i,12*38,38*i,fill = 'black',width=1 if (i+3)%3 else 2)

C.create_window( 38*6,38*13,height =38*1, width = 38*2,window=Button(text="Previous",command=previous))
C.create_window( 38*9,38*13,height =38*1, width = 38*2,window=Button(text="Next",command=next))
c_data = []
for i in range(9):
	c_data.append([])
	for j in range(9):
		y = 3*38 + 17 + 38* i
		x = 3*38 + 17 + 38* j
		c_data[i].append(C.create_text( x,y,text=str(""),font=fonts))

C.pack()
windows.mainloop()