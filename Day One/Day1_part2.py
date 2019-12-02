import math

path_name = 'Day One/AoC_day1.txt'


def launch_module(mass):
    fuel_rec = math.floor((mass / 3) - 2)
    return fuel_rec


# Slightly modified version of the first one
# Sums fuel requirements for all modules AND the required fuel
def tot_fuel_required(lst):
    all_fuel_rec = 0
    for a in lst:
        fuel_needs_fuel(a, 0)
        all_fuel_rec = all_fuel_rec + fuel_needs_fuel(a, 0)
    return all_fuel_rec


def read_file(path):
    f = open(path, 'r')
    l = f.readlines()
    lst = []
    for i in l:
        lst.append(int(i.rstrip()))
    # for the visuals
    print(tot_fuel_required(lst))
    return tot_fuel_required(lst)


# Fuel needs fuel to power the fuel (and also the modules).
# Can't add stuff during recursion, so sending it as a param.
def fuel_needs_fuel(fuel_mass, sum_all_fuel):
    if launch_module(fuel_mass) <= 0:
        return sum_all_fuel
    else:
        calc_module_only = (launch_module(fuel_mass))
        sum_all_fuel = sum_all_fuel + calc_module_only
        return fuel_needs_fuel(calc_module_only, sum_all_fuel)


read_file(path_name)
#answer is: 4898972