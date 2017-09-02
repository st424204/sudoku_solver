from tkinter import *
from tkinter import font
from soku import Solver
windows = Tk()
windows.wm_title("Sudoku Solver")
fonts = font.Font(family='Helvetica',size=20, weight='bold')
C = Canvas(windows, bg = '#FFFFFF', height =38*15, width = 38*15)

for i in range(3,13):
	C.create_line(38*i,3*38,38*i,12*38,fill = 'black',width=1 if (i+3)%3 else 2)
for i in range(3,13):
	C.create_line(3*38,38*i,12*38,38*i,fill = 'black',width=1 if (i+3)%3 else 2)


sol = Solver()
sol.get()
sol.solve()

c_data = []
for i in range(9):
	c_data.append([])
	for j in range(9):
		y = 3*38 + 17 + 38* i
		x = 3*38 + 17 + 38* j
		c_data[i].append(C.create_text( x,y,text=str(sol.data[i][j]),font=fonts))

C.pack()
windows.mainloop()