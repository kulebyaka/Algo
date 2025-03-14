"""
Benchmark utility for measuring algorithm performance.

This module provides tools to benchmark different algorithm implementations,
measure execution time, and compare performance across different input sizes.
"""

import time
import random
import statistics
import matplotlib.pyplot as plt
from typing import List, Callable, Dict, Any, Tuple, Union
import numpy as np
import os
import sys
import json
from pathlib import Path
import copy

# Import summary generator - using relative import
from benchmarks.summary_generator import (save_benchmark_summary, 
                                         save_github_action_output)

# Add the py directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import original implementations - using direct imports without the py. prefix
from py._15_three_sum import Solution as OriginalThreeSum, Solution2 as OriginalThreeSumTwo
from py._146_LRU_cache import LRUCache as OriginalLRUCache
from py._3_longest_substr_no_repeating_characters import Solution1 as OriginalLongestSubstr1
from py._3_longest_substr_no_repeating_characters import Solution2 as OriginalLongestSubstr2
from py._200_islands_number import Solution as OriginalIslands
from py._33_search_in_rotated_sorted_array import Solution as OriginalRotatedSearch


class AlgorithmBenchmark:
    """Utility class for benchmarking algorithm performance."""
    
    def __init__(self, name: str):
        """
        Initialize a benchmark instance.
        
        Args:
            name: The name of the benchmark
        """
        self.name = name
        self.results = {}
    
    def time_execution(self, func: Callable, *args, **kwargs) -> float:
        """
        Measure execution time of a function.
        
        Args:
            func: The function to benchmark
            *args: Positional arguments to pass to the function
            **kwargs: Keyword arguments to pass to the function
            
        Returns:
            Execution time in seconds
        """
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time
    
    def run_benchmark(self, 
                     implementations: Dict[str, Callable], 
                     input_generator: Callable[[int], Any], 
                     input_sizes: List[int],
                     num_runs: int = 5) -> Dict[str, Dict[int, List[float]]]:
        """
        Run benchmark comparison between different implementations.
        
        Args:
            implementations: Dictionary mapping names to implementation functions
            input_generator: Function to generate inputs of different sizes
            input_sizes: List of input sizes to test
            num_runs: Number of times to run each test for statistical significance
            
        Returns:
            Dictionary with results
        """
        results = {name: {size: [] for size in input_sizes} for name in implementations}
        
        for size in input_sizes:
            print(f"Benchmarking input size: {size}")
            
            # Generate input once for this size
            input_data = input_generator(size)
            
            for name, implementation in implementations.items():
                print(f"  Running {name}...")
                
                # Run multiple times for statistical significance
                for _ in range(num_runs):
                    # Create a deep copy of input data if it's mutable
                    input_copy = copy.deepcopy(input_data)
                    
                    # Time the execution
                    execution_time = self.time_execution(implementation, input_copy)
                    results[name][size].append(execution_time)
                
                # Calculate and print statistics
                times = results[name][size]
                avg_time = statistics.mean(times)
                print(f"    Average time: {avg_time:.6f}s")
                
        self.results = results
        
        # Save benchmark summary
        benchmark_dir = Path("../benchmark-results")
        benchmark_dir.mkdir(exist_ok=True)
        save_benchmark_summary(results, self.name, str(benchmark_dir / "benchmark_summary.json"))
        save_github_action_output(results, self.name, str(benchmark_dir / "github_action_output.json"))
        
        return results
    
    def plot_results(self, title: str = None, log_scale: bool = False, save_path: str = None):
        """
        Plot benchmark results.
        
        Args:
            title: Plot title (defaults to benchmark name)
            log_scale: Whether to use logarithmic scale for y-axis
            save_path: Path to save the plot image (if None, shows plot)
        """
        if not self.results:
            print("No benchmark results to plot")
            return
        
        plt.figure(figsize=(10, 6))
        
        # Determine input sizes and implementations
        implementations = list(self.results.keys())
        input_sizes = list(self.results[implementations[0]].keys())
        
        # Plot each implementation
        for name in implementations:
            # Calculate average times for each input size
            avg_times = [statistics.mean(self.results[name][size]) for size in input_sizes]
            plt.plot(input_sizes, avg_times, marker='o', label=name)
        
        # Set plot properties
        if log_scale:
            plt.yscale('log')
        
        plt.xlabel('Input Size')
        plt.ylabel('Execution Time (seconds)')
        plt.title(title or self.name)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Save or show plot
        if save_path:
            benchmark_dir = Path("../benchmark-results")
            benchmark_dir.mkdir(exist_ok=True)
            full_path = str(benchmark_dir / save_path)
            plt.savefig(full_path)
            print(f"Plot saved to {full_path}")
        else:
            plt.show()


# Input generators for different algorithm types
def generate_three_sum_input(size: int) -> List[int]:
    """Generate random array for Three Sum algorithm."""
    return random.choices(range(-size, size), k=size)

def generate_lru_cache_operations(capacity: int) -> List[Tuple[str, Union[int, Tuple[int, int]]]]:
    """Generate sequence of LRU Cache operations."""
    operations = []
    max_key = capacity * 2  # Use a range of keys larger than capacity
    
    # Generate a mix of get and put operations
    for _ in range(capacity * 10):  # Number of operations scales with capacity
        if random.random() < 0.7:  # 70% put operations
            operations.append(("put", (random.randint(0, max_key), random.randint(0, 1000))))
        else:  # 30% get operations
            operations.append(("get", random.randint(0, max_key)))
            
    return operations

def generate_string_for_longest_substring(size: int) -> str:
    """Generate random string for Longest Substring Without Repeating Characters."""
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=size))

def generate_islands_grid(size: int) -> List[List[str]]:
    """Generate random grid for Number of Islands."""
    # Create a grid with approximately 30% land
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            # 30% chance of land
            cell = "1" if random.random() < 0.3 else "0"
            row.append(cell)
        grid.append(row)
    return grid

def generate_rotated_array(size: int) -> Tuple[List[int], int]:
    """Generate rotated sorted array and target for Search in Rotated Sorted Array."""
    # Create sorted array
    array = list(range(size))
    
    # Rotate array
    rotation_point = random.randint(0, size - 1)
    rotated_array = array[rotation_point:] + array[:rotation_point]
    
    # Select random target (50% chance of being in the array)
    if random.random() < 0.5:
        target = random.choice(rotated_array)
    else:
        target = size + random.randint(1, 10)  # Target not in array
        
    return (rotated_array, target)


# Example benchmark runners
def benchmark_three_sum():
    """Benchmark Three Sum implementations."""
    benchmark = AlgorithmBenchmark("Three Sum Algorithms")
    
    # Define implementations to compare
    implementations = {
        "Original Brute Force": lambda nums: OriginalThreeSum().threeSum(nums),
        "Original Two Sum": lambda nums: OriginalThreeSumTwo().threeSum(nums)
    }
    
    # Input sizes to test
    input_sizes = [10, 50, 100, 200, 300]
    
    # Run benchmark
    benchmark.run_benchmark(implementations, generate_three_sum_input, input_sizes, num_runs=3)
    
    # Plot results
    benchmark.plot_results(log_scale=True, save_path="three_sum_benchmark.png")


def benchmark_lru_cache():
    """Benchmark LRU Cache implementations."""
    benchmark = AlgorithmBenchmark("LRU Cache Operations")
    
    def run_original_lru_cache(operations):
        cache = OriginalLRUCache(len(operations) // 10)  # Capacity based on operation count
        for op, args in operations:
            if op == "get":
                cache.get(args)
            else:  # put
                key, value = args
                cache.put(key, value)

    
    # Define implementations to compare
    implementations = {
        "Original LRU Cache": run_original_lru_cache,
    }
    
    # Input sizes (number of operations)
    input_sizes = [100, 500, 1000, 2000, 5000]
    
    # Run benchmark
    benchmark.run_benchmark(implementations, generate_lru_cache_operations, input_sizes, num_runs=3)
    
    # Plot results
    benchmark.plot_results(save_path="lru_cache_benchmark.png")


def benchmark_longest_substring():
    """Benchmark Longest Substring Without Repeating Characters implementations."""
    benchmark = AlgorithmBenchmark("Longest Substring Without Repeating Characters")
    
    # Define implementations to compare
    implementations = {
        "Original Approach 1": lambda s: OriginalLongestSubstr1().lengthOfLongestSubstring(s),
        "Original Approach 2": lambda s: OriginalLongestSubstr2().lengthOfLongestSubstring(s),
    }
    
    # Input sizes to test
    input_sizes = [10, 100, 1000] #, 5000, 10000]
    
    # Run benchmark
    benchmark.run_benchmark(implementations, generate_string_for_longest_substring, input_sizes, num_runs=3)
    
    # Plot results
    benchmark.plot_results(log_scale=True, save_path="longest_substring_benchmark.png")


def benchmark_islands():
    """Benchmark Number of Islands implementations."""
    benchmark = AlgorithmBenchmark("Number of Islands")
    
    # Define implementations to compare
    implementations = {
        "Original Implementation": lambda grid: OriginalIslands().numIslands(grid),
    }
    
    # Input sizes to test (grid dimensions)
    input_sizes = [10, 20, 50, 75, 100]
    
    # Run benchmark
    benchmark.run_benchmark(implementations, generate_islands_grid, input_sizes, num_runs=3)
    
    # Plot results
    benchmark.plot_results(save_path="islands_benchmark.png")


def benchmark_rotated_search():
    """Benchmark Search in Rotated Sorted Array implementations."""
    benchmark = AlgorithmBenchmark("Search in Rotated Sorted Array")
    
    def run_original_rotated_search(data):
        array, target = data
        return OriginalRotatedSearch().search(array, target)

    
    # Define implementations to compare
    implementations = {
        "Original Implementation": run_original_rotated_search,
    }
    
    # Input sizes to test
    input_sizes = [10, 100, 1000] # ,  10000, 100000]
    
    # Run benchmark
    benchmark.run_benchmark(implementations, generate_rotated_array, input_sizes, num_runs=3)
    
    # Plot results
    benchmark.plot_results(save_path="rotated_search_benchmark.png")


def run_all_benchmarks():
    """Run all benchmarks."""
    print("=== Running Three Sum Benchmark ===")
    benchmark_three_sum()
    
    print("\n=== Running LRU Cache Benchmark ===")
    benchmark_lru_cache()
    
    print("\n=== Running Longest Substring Benchmark ===")
    benchmark_longest_substring()
    
    print("\n=== Running Number of Islands Benchmark ===")
    benchmark_islands()
    
    print("\n=== Running Rotated Search Benchmark ===")
    benchmark_rotated_search()
    
    print("\nAll benchmarks completed!")
    
    # Combine all GitHub Action outputs into one file
    combine_github_action_outputs()


def combine_github_action_outputs():
    """Combine all GitHub Action outputs into a single file."""
    benchmark_dir = Path("../benchmark-results")
    output_file = benchmark_dir / "benchmark_summary.json"
    combined_file = benchmark_dir / "combined_output.json"
    
    if output_file.exists():
        try:
            with open(output_file, 'r') as f:
                data = json.load(f)
                
            # Write combined data
            with open(combined_file, 'w') as f:
                json.dump(data, f, indent=2)
                
            print(f"Combined benchmark data saved to {combined_file}")
        except Exception as e:
            print(f"Error combining benchmark outputs: {e}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Benchmark algorithm implementations")
    parser.add_argument("algorithm", nargs="?", choices=["three_sum", "lru_cache", 
                                                       "longest_substring", "islands", 
                                                       "rotated_search", "all"],
                       default="all", help="Algorithm to benchmark")
    args = parser.parse_args()
    
    if args.algorithm == "all":
        run_all_benchmarks()
    elif args.algorithm == "three_sum":
        benchmark_three_sum()
    elif args.algorithm == "lru_cache":
        benchmark_lru_cache()
    elif args.algorithm == "longest_substring":
        benchmark_longest_substring()
    elif args.algorithm == "islands":
        benchmark_islands()
    elif args.algorithm == "rotated_search":
        benchmark_rotated_search()
