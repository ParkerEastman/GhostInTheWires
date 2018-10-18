hex_string=('0123456789abcdef')
hex_list=[]
hex_dict=dict()
i=0
n=0


while n<16:
	while i<16:
		hex_list.append(hex_string[n]+hex_string[i])
		i+=1
	i=0
	n+=1


i=0
while i<256:
	hex_dict[hex_list[i]]=chr(i)
	i+=1


#-------------------------------------------------------------------------------------------------
delimiter=' '

code='a4 99 35 bc 9f 8a e5 81 79 7c 5d ce 70 47 75 c2 1d 4b f4 34 14 8c 79 b7 d1 74 57 3b 11 de c3'
split_code=code.split(delimiter)


for item in split_code:
	if item in hex_dict:
		print(hex_dict[item], end='')

