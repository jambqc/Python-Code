#!/usr/bin/env python

def swap(arr):
    '''
    Determines if the array can be sorted by swapping any 
    two elements in the array

    INPUT:
    arr- an array
    
    OUTPUT:
    Yes, if it can be sorted by this operation along with the
    positions of the two elements to swap, else it returns False
    '''
    count = 0
    positions = []
    
    temparr = arr[:]
    for i in range(len(arr)-1):
        #print(temparr[i])
        if (temparr[i] > temparr[i+1]):
            count += 1
            # keeping track of the positions that the condition occurs
            # Note that if there is two positions that this occurs, then
            # the we are actually concerned with the smaller value (i+1)
            positions.append(i)
        if count >= 3:
            break
    #print(temparr[positions[0]], temparr[positions[1]])
    # after the for loop, see how many times the occurence arr[i]>arr[i+1] ocurred
    if count == 0:  # if 0 then the list is sorted
        return 'yes'
    
    # if it occured just one time, swap the arr[i] with arr[i+1]
    # then see if that sorted the list
    elif count == 1: 
        if len(temparr) == 2:
            return (positions[0]+1, positions[0]+2)
        
        temparr[positions[0]], temparr[positions[0]+1] = \
        temparr[positions[0]+1], temparr[positions[0]]
        yesOrNo = all(temparr[i] < temparr[i+1] for i in range(len(temparr)-1))
        
        
        # if the list is sorted, then return the postions that were swapped
        if yesOrNo:
            return (positions[0]+1, positions[0]+2)
        
        else:  # else False and then we'll try reverse function
            return False
        
    elif count == 2:
        if (temparr[positions[0]] > temparr[positions[1]]) \
        and (temparr[positions[0]] < temparr[positions[1]+2]) \
        and (temparr[positions[1]+1] < temparr[positions[0]+1]) \
        and ((temparr[positions[0]] > temparr[positions[1]])):
            return (positions[0]+1, positions[1]+2) 
        else:
            return False
    else:
        return False
    
def reverseSeq(arr):
    '''
    Determines if an array can be sorted by reversing on sub-segment of
    the array.

    INPUT:
    arr- an array

    OUTPUT:
    If yes, then the positions of the first and last element in the sub-segment

    '''
    temparr = arr[:]
    start = None
    finish = None
    for i in range(len(temparr)-1):
        if (arr[i] > arr[i+1]):
            start = i
            for j in range(i, len(temparr)-1):
                if (temparr[j] <  temparr[j+1]):
                    finish = j
                    break
            break
    if finish == None:
        finish = j+1
        
    if (start == 0 and finish == len(temparr)-1):
        return  start+1, finish+1
    for k in range(j+1, len(temparr)-1):
        if (temparr[k] > temparr[k+1]):
            return 'no'
        
    if (start == 0 and temparr[start] < temparr[finish+1]):
        return  start+1, finish+1
    elif (finish ==len(temparr)-1 and temparr[finish] > temparr[start-1]):
        return  start+1, finish+1
    elif (temparr[start] < temparr[finish+1] and
         temparr[finish] > temparr[start-1]):
        return  start+1, finish+1
    else:
        return 'no'    
#--------------------------------------------------------------------------------
if __name__ == '__main__':

    arr = [int(x) for x in input('Enter and array: ').strip().split(' ')]

    if swap(arr) != False:
        if swap(arr) == 'yes':
            print(swap(arr), sep='')
        else:
            print('yes\nswap ', swap(arr)[0], ' ', swap(arr)[1], sep='')
            
    else:
        if reverseSeq(arr) == 'no':
            print('no')
        else:
            print('yes\nreverse ', reverseSeq(arr)[0], ' ', reverseSeq(arr)[1], sep='')
