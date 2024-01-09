import sys

file_name = sys.argv[-1]

flags = {'F':'X', 'D':'X', 'E':'X', 'M':'X', 'W':'X'}

curr_stall = False
next_stall = False
codes = [[0, 0, 0, 0]]

with open(file_name, 'r') as f:
    lines = f.readlines()
    
if len(lines) == 0:
    sys.exit(0)
    
for line in lines:
    code, arg_1, arg_2, arg_3 = line.split(',')
    arg_1 = int(arg_1)
    arg_2 = int(arg_2)
    arg_3 = int(arg_3.split('\n')[0])
    
    codes.append([code, arg_1, arg_2, arg_3])

n_inst = len(codes)-1

executed_inst = 0
idx = 1
cycle = 0

output = [['00' for _ in range(5)] for __ in range(n_inst)]


def check_next_stall():
    global next_stall

    if executed_inst == 0:
        next_stall = False
    else:
        curr_inst = executed_inst
        prev_code, prev_1, prev_2, prev_3 = tuple(codes[curr_inst-1])
        curr_code, curr_1, curr_2, curr_3 = tuple(codes[curr_inst])
        
        if prev_code == 'L' or prev_code == 'S':
            if curr_code == 'R':
                next_stall = (curr_2 == prev_1 or curr_3 == prev_1)
            elif curr_code == 'I':
                next_stall = curr_3 == prev_1
            elif curr_code == 'L' or curr_code == 'S':
                next_stall = curr_3 == prev_1
    return 
        

def WB():
    flags['W'] = flags['M']
    
def Mem():
    flags['M'] = flags['E']
    
def Exec():
    if curr_stall:
        flags['E'] = 'X'
    else:
        flags['E'] = flags['D']

def Decode():
    if curr_stall:
        return
    
    check_next_stall()
    
    flags['D'] = flags['F']
        
def Fetch():
    global executed_inst, next_stall
    if curr_stall:
        next_stall = False
        return
    if executed_inst >= n_inst:
        flags['F'] = 'X'
    else:
        executed_inst += 1
        flags['F'] = executed_inst

def print_flags():
    output = [str(k) + str(v) for k, v in flags.items()]
    output.append(f"Idx = {executed_inst}")
    output = '|'.join(output)
    print(output)
    
def get_output():
    f, d, e, m, w = tuple(flags.values())
    if f != 'X':
        output[f-1][0] = cycle
    if d != 'X':
        output[d-1][1] = cycle
    if e != 'X':
        output[e-1][2] = cycle
    if m != 'X':
        output[m-1][3] = cycle
    if w != 'X':
        output[w-1][4] = cycle
        
def print_output():
    final = []
    for each in output:
        temp = []
        for num in each:
            if num < 10:
                temp.append('0' + str(num))
            else:
                temp.append(str(num))
        final.append(','.join(temp))
    final = '\n'.join(final)
    print(final)
                
        
    
def check_flags():
    if executed_inst == 0:
        return False
    for value in flags.values():
        if value != 'X':
            return False
    return True
    

while not check_flags():

    WB()
    Mem()
    Exec()
    Decode()
    Fetch()
    get_output()
    curr_stall = next_stall
    cycle += 1
    
print_output()



