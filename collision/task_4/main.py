def intersectionAreaRect(rect1, rect2):
    (x1, y1), (x2, y2) = rect1
    (x3, y3), (x4, y4) = rect2
    left = x1 if x1 > x3 else x3  
    right = x2 if x2 < x4 else x4  
    bottom = y1 if y1 > y3 else y3  
    top = y2 if y2 < y4 else y4  
    if left < right and bottom < top:
        width = right - left
        height = top - bottom
        return width * height
    
    return 0
print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))
