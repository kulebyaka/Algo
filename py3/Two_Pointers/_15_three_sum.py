"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
from typing import List, Tuple
import random

# Import BenchmarkInfo for custom benchmarking
from py3.benchmarks.auto_discovery.benchmark_metadata import BenchmarkInfo


# brute force
def filter_out_by_indexes(lst, index_list:List[int]):
    return [element for i, element in enumerate(lst) if i not in index_list]

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        all_sums = list(map(lambda x: -x, nums))
        for i, num in enumerate(nums):
                for j in range(i+1, len(nums)):
                    filtered_list = filter_out_by_indexes(all_sums, [i, j])
                    if nums[i]+nums[j] in filtered_list:
                        res.add(tuple(sorted([nums[i], nums[j], -(nums[i]+nums[j])])))
        return list(res)

# two sum approach

def two_sum(array: List[int], target_sum: int) -> Tuple[List[int], bool]:
    left = 0
    right = len(array) - 1

    while left < right:
        s = array[left] + array[right]

        if s == target_sum:
            return [array[left], array[right]], True
        elif s < target_sum:
            left += 1
        else:
            right -= 1

    return [], False


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i, target in enumerate(nums):
            filtered_list = filter_out_by_indexes(nums, [i])
            two_sum_res = two_sum(filtered_list, -target)
            if not two_sum_res[1]:
                continue
            pair = two_sum_res[0]
            pair.append(target)
            res.add(tuple(sorted(pair)))

        return list(res)


def main():
    # print(Solution().threeSum([-1,0,1,2,-1,-4]))
    print(Solution2().threeSum([-1,0,1,2,-1,-4]))

if __name__ == "__main__":
    main()


# Custom input generator for Three Sum
def generate_three_sum_input(size: int) -> List[int]:
    """Generate random array for Three Sum algorithm with some zeros and negative numbers."""
    # Ensure a mix of negative, zero, and positive values for interesting three sum cases
    result = []
    # Add some zeros (about 5%)
    zeros_count = max(1, size // 20)
    result.extend([0] * zeros_count)
    
    # Add negative and positive numbers
    remaining = size - zeros_count
    neg_count = remaining // 2
    pos_count = remaining - neg_count
    
    # Add negative numbers
    result.extend(random.choices(range(-size, 0), k=neg_count))
    
    # Add positive numbers
    result.extend(random.choices(range(1, size), k=pos_count))
    
    # Shuffle the result
    random.shuffle(result)
    return result

# Define custom benchmark info
BENCHMARK_INFO = BenchmarkInfo(
    input_generator=generate_three_sum_input,
    input_sizes=[10, 50, 100, 200, 300],
    num_runs=3,
    name="Three Sum Optimization"
)
