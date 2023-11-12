# Use most_common(), zip and unpacking(*)
# Time: O(n) 79.44%
class Solution(object):
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k))[0])

# Use heap
# Time: O(n) 83.15%
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = collections.Counter(nums)
        freq_heap = []
        for key in freq_dict:
            heapq.heappush(freq_heap, (-freq_dict[key], key)) # Max heap
        output = []
        for _ in range(k):
            output.append(heapq.heappop(freq_heap)[1])
        return output