try:
    with open("input_day_4.txt", "r") as f:
        data = f.read().splitlines()
except FileNotFoundError:
    print("you need to get input_day_4.txt in the same directory ")


#part 1
def xmax_count_part1(data,line_number,caracter_index): #when we find an x, we check if there is a xmas in the 8 directions
    direction = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]
    count = 0
    for (i, j) in direction:
        if  line_number + i*3 >=0 and caracter_index + j*3 >= 0 and line_number + i*3 < len(data) and caracter_index + j*3 < len(data[line_number]):
            word =''.join([data[line_number + i*k][caracter_index + j*k] for k in range(4)] )
            if word == 'XMAS' and line_number + i*3 >=0 and caracter_index + j*3 >= 0:
                count +=1
                #print(line_number,caracter_index," direction : ",i,j)
    return count

count_part1 = 0
for line_number in range(len(data)):
    for caracter_index in range(len(data[line_number])):
        if data[line_number][caracter_index] == 'X':
            count_part1 += xmax_count_part1(data,line_number,caracter_index)
print("number of xmas : ", count_part1)

#part2
def is_xmax(data,line_number,caracter_index): #when we find an A, we check if there is a xmas in the 8 directions
    direction = [(i, j) for i in [-1,1] for j in [-1,1] ]
    count = 0
    for (i, j) in direction:
        word = ''.join([data[line_number + i*k][caracter_index + j*k] for k in range(-1,2)] )
        if word == 'MAS' :
            count +=1
    if count <2:
        return False
    else:
        return True 
    
count_part2 = 0
for line_number in range(1,len(data) -1):
    for caracter_index in range(1,len(data[line_number] )-1):
        if data[line_number][caracter_index] == 'A':
            count_part2 += is_xmax(data,line_number,caracter_index)
print("number of x-mas : ", count_part2)
