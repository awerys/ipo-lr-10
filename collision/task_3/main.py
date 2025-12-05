def isCorrectRect(points):
    if len(points) != 2:
        return False
    left_bottom = points[0]
    right_top = points[1]
    if left_bottom[0] < right_top[0] and left_bottom[1] < right_top[1]:
        return True
    else:
        return False
print(isCorrectRect([(-3.4, 1), (9.2, 10)])) 
print(isCorrectRect([(-7, 9), (3, 6)])) 
print(isCorrectRect([(0, 0), (5, 5)]))       
print(isCorrectRect([(5, 5), (0, 0)]))      
print(isCorrectRect([(0, 0), (0, 5)]))      
print(isCorrectRect([(0, 0), (5, 0)])) 
