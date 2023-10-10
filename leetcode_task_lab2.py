class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        def bubble_sort(my_list):

            n = len(my_list)

            for i in range(n - 1):
                for j in range(n - 1 - i):
                    if my_list[j] > my_list[j + 1]:
                        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

            return my_list


        allst = []
        evst = bubble_sort([nums[i] for i in range(len(nums)) if i % 2 == 0])
        oddst = bubble_sort([nums[i] for i in range(len(nums)) if i % 2 == 1])[::-1]

        for i in range(len(evst) + len(oddst)):
            allst.append(evst[i // 2] if i % 2 == 0 else oddst[i // 2])

        return allst

            
