flights = {'Montreal': ['Toronto', 'Tampa Bay'], 'Toronto': ['Montreal', 'Tampa Bay'], 'Tampa Bay': ['Atlanta', 'Toronto'], 'Atlanta': ['Tampa Bay']}  # the dictionary of cities and their possible "hops"


def one_hop(flights, city1, city2):  # this function takes in the two given cites and loops through dictionary keys to see if the values line up
    index = (flights[city1])  # index is the two (or one for Atlanta) values that will be check to see if there is a hop
    for halfhop in index: # this loop runs through the indexes and the halfhop variable is the new key that will be looked at
        for x in range(len(flights[halfhop])):  # this loop looks through the values at the halfhop key
            if city2 in flights[halfhop]:  # if one of the values in the new key is city 2, a one hop is possible, and so the function ends
                print("There is a one-hop")
                return
    print("There is not a one-hop")


one_hop(flights, city1=input("city 1 "), city2=input("city 2 "))  # This takes the city inputs to be used for finding the one hops and calls the function
