class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for outer_row in range(len(board)):
        #     for outer_column in range(len(board)):
        #         target = board[outer_row][outer_column]
        #         if target != ".":
        #             for inner_row in range(outer_row+1,len(board)):
        #                 if target == board[inner_row][outer_column]:
        #                     return False
        #             for inner_column in range(outer_column+1,len(board)):
        #                 if (target == board[outer_row][inner_column]):
        #                     return False

        # return True

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        print(rows,"rows")
        print("cols", cols)
        print("boxex",boxes)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)
                # print("box_index",box_index)

                # Check if value already exists in row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False

                # Add value to row, column, and box sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        print("rows",rows)
        print("cols",cols)
        # print("boxes",boxes)
        return True

        