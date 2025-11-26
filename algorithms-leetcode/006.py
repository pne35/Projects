#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        x,y = 1,0
        count = 0
        n = len(s)
        def increase(y,x,n,count):
            while y < numRows:
                count += 1
                y += 1
                print(f"({x},{y})")
            while count < n and y > 1:
                count += 1
                x += 1
                y -= 1
                print(f"({x},{y})")
            if count < n:
                increase(y,x,n,count)
        increase(y,x,n,count)

convert("helhfgfghh",3)
# not completed code, just showing my thinking, first I created this code which creates the zigzag pattern using recursion and plotting the coordinates. I plan to add the letters to each coordinate. 
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        cords = []
        word = ""
        x,y = 1,0
        count = 0
        n = len(s)

        #Functions
        def increase(y,x,n,count,cords):
            while y < numRows and count < n:
                count += 1
                y += 1
                # print(f"({x},{y})")
                cords.append([x,y])
            while count < n and y > 1:
                count += 1
                x += 1
                y -= 1
                # print(f"({x},{y})")
                cords.append([x,y])
            if count < n:
                cords = increase(y,x,n,count,cords)
            return cords
            
        def find_value(a, b, data):
            for x, y, value in data:
                if x == a and y == b:
                    return value
            return None
        

        cords = increase(y,x,n,count,cords)
        # print(cords)
        for cord in range(len(cords)):    
            cords[cord].append(s[cord])
        print(cords)
        for yCord in range(1,numRows+1):
            for xCord in range(1,cords[-1][0]+1):
                val = find_value(xCord, yCord, cords) 
                if val != None:
                    word = word + val
        # print(cords[-1][0])
        # print(word)
        return word
#final code, definatly not the most optimal however I made it challenging by adding coordinates and recursion
