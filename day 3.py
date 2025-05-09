try:
    with open("input_day_3.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("you need to get input_day_3.txt in the same directory ")


number = ['0','1','2','3','4','5','6','7','8','9']
sum = 0
i = 0
while i + 7 < len(data):
    if data[i:i+4] == 'mul(':
        is_first_number_valid = True
        is_coma_valid = True
        is_parenthesis_valid = True
        is_second_number_valid = True
        p,q =0,0
        while data[i+4+p] in number and is_first_number_valid: #read first number
            p = p+1
            if p>3:
                is_first_number_valid = False 
        if p ==0: 
            is_first_number_valid = False

        if data[i+4+p] != ',':
            is_valid = False
        while data[i+4+p+1+q] in number and is_second_number_valid: #read second number
            q = q+1
            if q>3:
                is_second_number_valid = False
        if q ==0:
            is_second_number_valid = False

        if data[i+4+p+1+q] != ')' or q == 0:
            is_parenthesis_valid = False

        is_valid = is_first_number_valid and is_coma_valid and is_parenthesis_valid and is_second_number_valid
        if is_valid:
            a = int(data[i+4:i+4+p])
            b = int(data[i+4+p+1:i+4+p+1+q])
            sum += a*b
    i = i + 1
                    
print("sum : ", sum)

#part 2 : code is a bit less readable but a bit more compact, those a two proposals
sum_part2 = 0
enable = True
i= 0
while i + 7 < len(data):
    if data[i:i+4] == 'mul(' and enable == True:
        is_valid = True
        p,q =0,0
        while data[i+4+p] in number and p < 3: #read first number
            p = p+1
        if data[i+4+p] != ',' or p == 0:
            is_valid = False
        while is_valid and data[i+4+p+1+q] in number and q < 3: #read second number
            q = q+1
        if data[i+4+p+1+q] != ')' or q == 0:
            is_valid = False

        if is_valid:
            a = int(data[i+4:i+4+p])
            b = int(data[i+4+p+1:i+4+p+1+q])
            sum_part2 += a*b
        i+= 4 + p + q


    elif data[i:i+4] == 'do()':
        enable = True
        i += 4
    elif data[i:i+7] == "don't()":
        enable = False
        i+=7
    else:
        i+=1
                
print("sum with new rules : ", sum_part2)


        
        