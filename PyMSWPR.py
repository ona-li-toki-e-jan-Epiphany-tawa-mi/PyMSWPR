import casioplot as csp
rows=6; columns=21; cell_count=rows*columns
def get_cell2d(cell):
  row=cell//columns
  return (cell-row*columns,row)
get2d_cell=lambda x,y: columns*y+x
shown_board=0; flag_board=0; bomb_board=-1
get_cell=lambda board,cell: (board>>cell)&1
def set_shown(cell,bit):
  global shown_board
  if bit!=get_cell(shown_board,cell): shown_board=shown_board^(1<<cell)
def toggle_flag(cell):
  global flag_board; flag_board=flag_board^(1<<cell)
def set_bomb(cell,bit):
  global bomb_board
  if bit!=get_cell(bomb_board,cell): bomb_board=bomb_board^(1<<cell)
seed=0; bitmask=(1<<64)-1
def random_number():  
  global seed
  seed=(seed^(seed<<13))&bitmask
  seed=(seed^(seed>>7))&bitmask
  seed=(seed^(seed<<17))&bitmask
  return seed
def mutate_seed(random_input): 
  global seed; seed=(random_input+seed+random_number())&bitmask
current_cell=cell_count//2+columns//2
def count_nearby(cell):
  x,y=get_cell2d(cell); count=0
  for dx in range(-1,2):
    for dy in range(-1,2):
      x1=x+dx; y1=y+dy
      if not(x1==0 and y1==0) and x1>=0 and x1<columns and y1>=0 and y1<rows:
        cell=get2d_cell(x1,y1)
        if get_cell(bomb_board,cell)==1:
          count=count+1
  return count
def show_board():
  csp.clear_screen()
  for i in range(0,rows):
    for k in range(0,columns):
      cell=i*columns+k
      if get_cell(flag_board,cell)==1:
        if current_cell==cell: print("F",end="")
        else: print("?",end="")
      elif get_cell(shown_board,cell)!=1:
        if current_cell==cell: print("U",end="")
        else: print(".",end="")
      elif get_cell(bomb_board,cell):
        if current_cell==cell: print("B",end="")
        else: print("@",end="")
      else:
        nearby=count_nearby(cell)
        if current_cell==cell: 
          if nearby==0: print("E",end="")
          else: print("#",end="")
        else: 
          if nearby==0: print(" ",end="")
          else: print(nearby,end="")
    print()
last_input="9"
def get_input():
  command=input()
  global last_input
  if len(command)==0:
    command=last_input
  else:
    last_input=command
  return command
def has_won():
  for cell in range(0,cell_count):
    if get_cell(bomb_board,cell)!=1:
      if get_cell(flag_board,cell)==1 or get_cell(shown_board,cell)!=1:
        return False
  return True
def try_move(command):
  global current_cell
  if command=="8":
    next_cell=current_cell-columns
    if next_cell>=0: current_cell=next_cell
    else: current_cell=cell_count+next_cell
  elif command=="4":
    current_cell=current_cell-1
    if current_cell<0:
      current_cell=0
  elif command=="6":
    current_cell=current_cell+1
    if current_cell>=cell_count: 
      current_cell=cell_count-1
  elif command=="2":
    next_cell=current_cell+columns
    if next_cell<cell_count: current_cell=next_cell
    else: current_cell=next_cell-cell_count
def try_autosweep(x,y):
  if x>=0 and x<columns and y>=0 and y<rows:
    cell=get2d_cell(x,y)
    if get_cell(shown_board,cell)!=1 and get_cell(bomb_board,cell)!=1 and get_cell(flag_board,cell)!=1:
      set_shown(cell,1)
      return True
  return False
def autosweep():
  while True:
    count=0
    for cell in range(0,cell_count):
      if get_cell(shown_board,cell)==1:
        x,y=get_cell2d(cell)
        if try_autosweep(x,y+1): count=count+1
        if try_autosweep(x-1,y): count=count+1
        if try_autosweep(x+1,y): count=count+1
        if try_autosweep(x,y-1): count=count+1
    if count==0: break
def try_sweep():
  if get_cell(shown_board,current_cell)!=1 and get_cell(flag_board,current_cell)!=1:
    if get_cell(bomb_board,current_cell)==1:
      return False
    else:
      set_shown(current_cell,1)
      autosweep() 
  return True
while True:
  win=None
  while True:
    show_board()
    for command in get_input():
      mutate_seed(ord(command))
      if command=="7":
        if get_cell(shown_board,current_cell)!=1:
          toggle_flag(current_cell)
      elif command=="9":
        if bomb_board==-1:
          bomb_board=((random_number()<<64)+random_number())&((1<<cell_count)-1)
          set_bomb(current_cell,0)
        if not try_sweep():
          win=False; break
        if has_won():
          win=True; break
      else:
        try_move(command)
    if win!=None:
      break
  shown_board=~0; flag_board=0; show_board()
  if win: print("You win!",end="")
  else: print("BOOM!",end="")
  input() 
  shown_board=0; flag_board=0; bomb_board=-1     