from typing import List

## naive solution Time : O(n*n), Space : O(1)
class NaiveSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        while len(nums) > 1:
            if nums[0] in nums[1:]:
                return True
            nums.pop(0)
        return False


## better solution
class BetterSolution:
    def __init__(self):
        self.hashset = set()
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if num in self.hashset:
                return True
            self.hashset.add(num)
        return False


if __name__ == "__main__":
    nums = [1,2,3,4]
    assert False == NaiveSolution().containsDuplicate(nums)
    assert False == BetterSolution().containsDuplicate(nums)

    print()