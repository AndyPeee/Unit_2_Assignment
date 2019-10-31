lengthofargs = int(input(("length ")))  # asks for the length of the list that will be used
argslist = [] # makes a list to have the arguments in to loop through
args = (argslist) # makes a tuple out of the list, so that the final list won't get altered
x = 0
for appendtoargs in range(lengthofargs):  # this loop makes the list the length given
    argslist.append(x)
    x += 1  # the reason I chose to use x rather than appendtoargs is so the first value is 1 rather than 0
def extremetuple(args):  # this function is used to sort the list and determine the max and min
    if len(args) == 0: # if the list length is 0, it ends the function
        return False
    args.sort()  # sorts the list from lowest to highest
    mi = (args[0])  # because it is sorted, the first index will be the lowest number
    ma = (args[-1])  # because it is sorted, the last index will be the highest number
    mi = tuple(str(mi))
    ma = tuple(str(ma))
    print(mi)
    print(ma)
    return True
if not extremetuple(args):  # calls the function, if the length = 0, it will print that it is 0, otherwise will run the function as normal
    print("its 0")
