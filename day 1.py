#creation of two separated lists from the file list_day_1.txt
try:
    with open("input_day_1.txt", "r") as f:
        data = f.read().splitlines()
except FileNotFoundError:
    print("you need to get input_day_1.txt in the same directory ")

left_list = []
right_list = []
for line in data:
    numbers = line.split("   ")
    left_list.append(numbers[0])
    right_list.append(numbers[1])

#we need to sort those those list, we'll just use an already existent function because it's easier and it works with strings

left_list.sort()
right_list.sort()

#we calculate the distance between the two lists
distance =0
for i in range(len(left_list)):
    distance += abs(int(left_list[i]) - int(right_list[i]))

print("distance : ", distance)


#part 2 

count = {} #count the number of times a number appears in the right list
similarity = 0
for number in right_list:
    count[number] = count.get(number, 0) +1
for number in left_list: #calculate the similarity between the two lists
    similarity += count.get(number, 0)*int(number) 
print("similarity : ", similarity)



    
    