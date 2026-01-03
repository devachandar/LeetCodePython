class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1 = strs[0]
        for i in range(len(str1),-1,-1):
            sub_string = str1[:i]
            # print(sub_string)
            for j in strs:
                if not j.startswith(sub_string):
                    break
            else:
                return sub_string
        
        return sub_string

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         sub_string = strs[0]
        
#         for str in strs[1:]:
#             while not str.startswith(sub_string):
#                 sub_string = sub_string[:-1]

#                 if not sub_string:
#                     return ""

        
#         return sub_string


        