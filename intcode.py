def get_digit(number, n):
    return number // 10**n % 10

def expand_list(l, idx):
    #if len(l)<=idx:
    #    l.extend([0] * (idx-len(l)+3))
    if idx not in l:
        l[idx] = 0
    return l

def mode(l, idx, m, relative_base):
    if m == 0:
        l = expand_list(l, max(l[idx], idx))
        return l[l[idx]]
    elif m == 1:
        l = expand_list(l, idx)
        return l[idx]
    else:
        l = expand_list(l, l[idx]+relative_base)
        return l[l[idx]+relative_base]
    
def l_update(l, idx, relative_base, mode, value):
    m = max(l[idx], l[idx]+relative_base)
    l = expand_list(l, m)
    if mode == 0:
        l[l[idx]] = value
    elif mode == 1:
        l[idx] = value
    else:
        l[l[idx]+relative_base] = value
    return l

def TEST2(l, test_input, starting_point, relative_base):
    i=starting_point
    result = []
    relative_base = relative_base
    while (get_digit(l[i],0)+get_digit(l[i],1)*10)!=99:
        opcode = (get_digit(l[i],0)+get_digit(l[i],1)*10)
        mode1 = get_digit(l[i],2)
        mode2 = get_digit(l[i],3)
        mode3 = get_digit(l[i],4)
        n1 = mode(l, i+1, mode1, relative_base)
        n2 = mode(l, i+2, mode2, relative_base)
        if opcode == 1:
            l = l_update(l, i+3, relative_base, mode3, n1+n2)
            i = i+4
        elif opcode == 2:
            l = l_update(l, i+3, relative_base, mode3, n1*n2)
            i = i+4
        elif opcode == 3:
            l = l_update(l, i+1, relative_base, mode1, test_input)
            i = i+2
        elif opcode == 4:
            print(n1, i)
            result.append(n1)
            i = i+2
            #if len(result)==2:
            #   return result, l, i, relative_base
        elif opcode == 5:
            if n1 != 0:
                i = n2
            else:
                i = i+3
        elif opcode == 6:
            if n1 == 0:
                i = n2
            else:
                i = i+3
        elif opcode == 7:
            if n1<n2:
                l = l_update(l, i+3, relative_base, mode3, 1)
            else:
                l = l_update(l, i+3, relative_base, mode3, 0)
            i = i+4
        elif opcode == 8:
            if n1==n2:
                l = l_update(l, i+3, relative_base, mode3, 1)
            else:
                l = l_update(l, i+3, relative_base, mode3, 0)
            i = i+4
        elif opcode == 9:
            relative_base = relative_base+n1
            i = i+2  
    return result

def TEST3(l, test_input, starting_point, relative_base):
    i=starting_point
    result = []
    relative_base = relative_base
    while (get_digit(l[i],0)+get_digit(l[i],1)*10)!=99:
        opcode = (get_digit(l[i],0)+get_digit(l[i],1)*10)
        mode1 = get_digit(l[i],2)
        mode2 = get_digit(l[i],3)
        mode3 = get_digit(l[i],4)
        n1 = mode(l, i+1, mode1, relative_base)
        n2 = mode(l, i+2, mode2, relative_base)
        if opcode == 1:
            l = l_update(l, i+3, relative_base, mode3, n1+n2)
            i = i+4
        elif opcode == 2:
            l = l_update(l, i+3, relative_base, mode3, n1*n2)
            i = i+4
        elif opcode == 3:
            l = l_update(l, i+1, relative_base, mode1, test_input)
            i = i+2
        elif opcode == 4:
            #print(n1, i)
            result.append(n1)
            i = i+2
            if len(result)==1:
                return result, l, i, relative_base
        elif opcode == 5:
            if n1 != 0:
                i = n2
            else:
                i = i+3
        elif opcode == 6:
            if n1 == 0:
                i = n2
            else:
                i = i+3
        elif opcode == 7:
            if n1<n2:
                l = l_update(l, i+3, relative_base, mode3, 1)
            else:
                l = l_update(l, i+3, relative_base, mode3, 0)
            i = i+4
        elif opcode == 8:
            if n1==n2:
                l = l_update(l, i+3, relative_base, mode3, 1)
            else:
                l = l_update(l, i+3, relative_base, mode3, 0)
            i = i+4
        elif opcode == 9:
            relative_base = relative_base+n1
            i = i+2  
    return 
