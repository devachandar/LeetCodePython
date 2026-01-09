class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = defaultdict(list)
        for word in strs:
            print(word)
            key = "".join(sorted(word))
            output_dict[key].append(word)

        return list(output_dict.values())       

        # output_list = []
        # for s_str in strs:
        #     for output in output_list:
        #         if Counter(output[0]) == Counter(s_str):
        #             output.append(s_str)
        #             break
        #     else:
        #         output_list.append([s_str])

        # return output_list