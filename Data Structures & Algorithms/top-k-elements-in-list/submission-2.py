class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        l = []
        for i in nums:
            if i in output:
                output[i] += 1

            else:
                output[i] = 1

        sorted_keys = sorted(output, key=output.get, reverse=True)

        return sorted_keys[:k]