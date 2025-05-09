try:
    with open("input_day_2.txt", "r") as f:
        data = f.read().splitlines()
except FileNotFoundError:
    print("you need to get input_day_2.txt in the same directory ")


reports = [[int(number) for number in report.split(' ')] for report in data]
safe_number = 0 #count the number of safe reports

def is_safe_part1(line):
    if abs(line[0] - line[1]) > 3:
        return False
    for i in range(1, len(line)-1): 
        if not (abs(line[i] - line[i+1]) <= 3 and (line[i-1] - line[i]) * (line[i] - line[i+1]) > 0):
            return False
    return True
        

for line in reports:
    safe_number += is_safe_part1(line) 
        
print("number of safe reports : ", safe_number)


#part 2 
def is_safe_part2(line): #not optimal but the code is simple
    for i in range(0, len(line)): 
        cut_line = line[0:i] + line[i+1:]
        if is_safe_part1(cut_line):
            return True
    return False

safe_numper_part2 = 0
for line in reports: 
    safe_numper_part2 += is_safe_part2(line)
print("number of safe reports with new rules : ", safe_numper_part2)