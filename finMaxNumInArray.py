import heapq
class Solution:
  def findMaxNumInArray(nums):
    heap = []
    for num in nums:
      heapq.heappush(heap,-num)
    return -heap[0]

  if __name__== "__main__":
    s = findMaxNumInArray([73,74,75,69,77])
    print (s)
