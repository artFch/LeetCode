class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if not stack:
                result[nums2[i]] = -1
            else:
                result[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        answer = []
        for num in nums1:
            answer.append(result.get(num, -1))
        return answer
