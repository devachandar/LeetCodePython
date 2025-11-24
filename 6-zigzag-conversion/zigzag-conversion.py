class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s 
        rows = [""] * numRows
        currRow = 0
        goingDown= False

        for letter in s:
            if currRow == 0:
                goingDown = True
            
            if currRow == numRows - 1:
                goingDown = False
            
            
            rows[currRow]+= letter

            if goingDown == True:
                currRow +=1
            else:
                currRow -=1
        
        return "".join(rows)
