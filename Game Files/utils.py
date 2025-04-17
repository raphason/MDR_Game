

def check_adjacency(position_one, position_two, cols_in_grid):
    return abs(position_one - position_two) == 1 or abs(position_one - position_two) == cols_in_grid


"""
Group is valid if every member in the group is touching at least one other member of the group, for example:

Group (a, b, c, d) position values -> return True or False
-> a needs to be touching one or more of b, c, or d
-> b needs to be touching one or more of a, c, or d
-> c needs to be touching one or more of b, a, or d
-> d needs to be touching one or more of b, c, or a

save time/memory below by eliminating checked node when true and also other adjacent nodes

check valid group (group)
    tocheck = group
    while tocheck not empty
        current = tocheck[0]
        others = group.pop(index of current in group)
        adjacent = False
        for other in others:
            if check adjacency (current, other) true
                adjacent = true
                tocheck = tocheck.pop(index of other)
        if adjacent = false
            return False
            break
        else
            tocheck.pop(index of current)
"""
