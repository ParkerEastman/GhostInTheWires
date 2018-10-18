code='164'
delimiter=' '
solved=[]
code_list=code.split(delimiter)
for item in code_list:
	solved.append(chr(int(item)))

for element in solved:
	print(element, end='')

