# https://leetcode.com/problems/flipping-an-image/

# Time O(N ^ 2) | Space O(1)
def flipandInvertImage(image):
    for row in image:
        i, j = 0, len(row) - 1
        while i <= j:
            row[i], row[j] = row[j]^1, row[i]^1 # just filp and complement the numbers
            i += 1 
            j -= 1
                
    return image