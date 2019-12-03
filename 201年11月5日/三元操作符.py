x,y = 4,5
if x < y:
    small = x
else:
    small = y
'可以改进为'
small = x if x < y else y
