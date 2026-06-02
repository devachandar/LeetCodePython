class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ptr = 0
        result_list = [""] * numRows
        print(result_list)
        gng_down = False
        # gng_up = False

        for ch in s:
            if ptr == 0:
                gng_down = True
            
            if ptr == numRows-1:
                gng_down = False

            result_list[ptr]+= ch

            if gng_down:
                ptr+=1
            else:
                ptr-=1
            
        return "".join(result_list)



















        # if numRows == 1:
        #     return s 
        # rows = [""] * numRows
        # currRow = 0
        # goingDown= False

        # for letter in s:
        #     if currRow == 0:
        #         goingDown = True
            
        #     if currRow == numRows - 1:
        #         goingDown = False
            
            
        #     rows[currRow]+= letter
        #     print("dd", rows)

        #     if goingDown == True:
        #         currRow +=1
        #     else:
        #         currRow -=1
        
        # return "".join(rows)
