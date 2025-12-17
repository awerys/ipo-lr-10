class RectCorrectError(Exception):
    pass
def intersectionAreaMultiRect(rectangles):
    if len(rectangles) < 2:
        return 0
    for rect in rectangles:
        (x1, y1), (x2, y2) = rect
    if len(rectangles) == 2:
        (x1, y1), (x2, y2) = rectangles[0]
        (x3, y3), (x4, y4) = rectangles[1]
        area1 = (x2 - x1) * (y2 - y1)
      
        area2 = (x4 - x3) * (y4 - y3)
        left = max(x1, x3)
        right = min(x2, x4)
        bottom = max(y1, y3)
        top = min(y2, y4)
        if left < right and bottom < top:
            intersection = (right - left) * (top - bottom)
        else:
            intersection = 0
        return area1 + area2 - intersection
    total_area = 0
    for rect in rectangles:
        (x1, y1), (x2, y2) = rect
        total_area += (x2 - x1) * (y2 - y1)
    return total_area
rectangles = [
    [(0, 0), (2, 2)], 
    [(1, 1), (3, 3)],  
]
print(f"Результат: {intersectionAreaMultiRect(rectangles)}")  
