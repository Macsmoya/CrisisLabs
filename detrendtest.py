start = 1
lst = [1,2,3,4,5,5,2,12,3,4,1]

def detrend(start, lst):
    if len(lst) == 0:
        return lst
    else:
        return [lst[0] - start] + detrend(lst[0], lst[1:])
print(detrend(start,lst))
