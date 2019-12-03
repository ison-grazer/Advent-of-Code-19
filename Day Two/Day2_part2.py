def make_lst(*numbers):
    op_lst = []
    for i in numbers:
        op_lst.append(i)
    #print(op_lst)
    return op_lst


# This is messy as shit, I'm so sorry
def process_by_index(lst, instruction_pointer,wanted_num):
    # the opcodes
    if lst[instruction_pointer] == 1:
        #lst[instruction_pointer] = 0
        # parameters
        noun = lst[instruction_pointer+1] % len(lst)
        verb = lst[instruction_pointer+2] % len(lst)
        
        destination = lst[instruction_pointer+3]
        lst[destination] = (lst[noun] + lst[verb])
        print(lst[noun] + lst[verb])
        if (100 * lst[noun] + lst[verb]) == wanted_num:
            print("Found it!", noun, "+", verb)
        else:
            process_by_index(lst, instruction_pointer+4, wanted_num)

    elif lst[instruction_pointer] == 2:
        #lst[instruction_pointer] = 0
        noun = lst[instruction_pointer+1] % len(lst)
        verb = lst[instruction_pointer+2] % len(lst)
        destination = lst[instruction_pointer + 3]


        lst[destination] = (lst[noun] * lst[verb])
        print(lst[noun] * lst[verb])
        if (100 * lst[noun] * lst[verb]) == wanted_num:
            print("Found it!", noun, "*", verb)
        else:
            process_by_index(lst, instruction_pointer + 4, wanted_num)

    elif lst[instruction_pointer] == 99:
        print("Reached end of OpCode., terminating .. ", lst)
        return lst

    print(lst)
    return lst


def restore_program(lst):
    lst[1] = 12
    lst[2] = 2
    #print(lst, "list has been properly swapped")
    return lst


big_bad_list = make_lst(1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0)
is_restored = restore_program(big_bad_list)
process_by_index(is_restored, 0, 19690720) #wanted_num


# Determine what pair of inputs produces the output 19690720
