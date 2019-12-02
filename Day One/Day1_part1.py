import math

path_name = 'Day One/AoC_day1.txt'


def launch_module(mass):
    fuel_rec = math.floor((mass / 3) - 2)
    return fuel_rec


# Sums all separate fuel requirements in the list
def tot_fuel_required(lst):
    all_fuel_rec = 0
    for a in lst:
        all_fuel_rec = all_fuel_rec + launch_module(a)
    return all_fuel_rec


# Reads from file, default is String so cast to int.
def read_file(path):
    f = open(path, 'r')
    l = f.readlines()
    lst = []
    for i in l:
        lst.append(int(i.rstrip()))
    #for the visuals
    print(tot_fuel_required(lst))
    return tot_fuel_required(lst)


read_file(path_name)
# right answer is: 3267890
