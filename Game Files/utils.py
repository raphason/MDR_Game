from constants import COLS

def check_adjacency(position_one, position_two, cols_in_grid=COLS): #(int), (int), (int) -> Bool
    return abs(position_one - position_two) == 1 or abs(position_one - position_two) == cols_in_grid

def check_valid_grouping(grouping): #grouping (List of position values (int)) -> Bool
    """ 
    Loop through copy of given grouping, removing entries which do have an adjacency, as well as all of their adjacencies. If an entry 
    does not have an adjacency, return False. Once grouping empty, we know all entries had an adjacency, return True. 
    """
    to_check = [x for x in grouping]
    while to_check:
        current = to_check[0]
        others = [x for x in grouping if x != current]

        adjacent = False
        for other in others:
            if check_adjacency(current, other):
                adjacent = True
                if current in to_check:
                    to_check.pop(to_check.index(current))
                if other in to_check:
                    to_check.pop(to_check.index(other))
        if not adjacent:
            return False
    return True
