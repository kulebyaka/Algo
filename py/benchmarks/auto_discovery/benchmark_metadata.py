"""
Auto-discovery benchmark system for LeetCode solutions.

This module provides tools to automatically discover and benchmark LeetCode solutions
without requiring manual updates to benchmark_algorithms.py.
"""

import inspect
import random
import time
import statistics
import os
import sys
import copy
import importlib
import re
from typing import List, Callable, Dict, Any, Tuple, Type, Optional, Union


class BenchmarkInfo:
    """Metadata class for benchmarking information."""
    
    def __init__(
        self,
        input_generator: Callable[[int], Any],
        input_sizes: List[int] = None,
        num_runs: int = 3,
        target_method: str = None,
        name: str = None,
        wrapper: Callable = None
    ):
        """
        Initialize benchmark metadata.
        
        Args:
            input_generator: Function to generate inputs of different sizes
            input_sizes: List of input sizes to test (default: [10, 50, 100, 200])
            num_runs: Number of runs for each test (default: 3)
            target_method: Method to benchmark (default: main solution method)
            name: Custom name for the benchmark
            wrapper: Optional wrapper function to call the target method correctly
        """
        self.input_generator = input_generator
        self.input_sizes = input_sizes or [10, 50, 100, 200]
        self.num_runs = num_runs
        self.target_method = target_method
        self.name = name
        self.wrapper = wrapper


class AutoBenchmark:
    """Automated benchmarking system for LeetCode solutions."""
    
    def __init__(self, base_dir: str = None):
        """
        Initialize the auto-benchmark system.
        
        Args:
            base_dir: Base directory containing LeetCode solutions (default: py directory)
        """
        # Ensure py directory is in the path
        if base_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        self.base_dir = base_dir
        if base_dir not in sys.path:
            sys.path.append(base_dir)
        
        # Registry to store discovered solutions
        self.solutions = {}
        
        # Pre-defined input generators
        self.input_generators = self._create_input_generators()
    
    def discover_solutions(self):
        """Discover all solution classes in LeetCode problem files."""
        py_dir = self.base_dir
        pattern = re.compile(r'^_(\d+)_(.+)\.py$')
        
        for filename in os.listdir(py_dir):
            match = pattern.match(filename)
            if match and not filename.startswith('__'):
                problem_number = match.group(1)
                problem_name = match.group(2).replace('_', ' ')
                full_name = f"{problem_number}. {problem_name}"
                module_name = filename[:-3]  # Remove .py extension
                
                # Import the module
                try:
                    # Use absolute import based on sys.path
                    module = importlib.import_module(f"py.{module_name}")
                    
                    # Find solution classes in the module
                    solution_classes = []
                    for name, obj in inspect.getmembers(module):
                        if (inspect.isclass(obj) and 
                            name.startswith("Solution") and 
                            obj.__module__ == module.__name__):
                            solution_classes.append(obj)
                    
                    if solution_classes:
                        self.solutions[full_name] = {
                            'module': module,
                            'classes': solution_classes,
                            'file': filename
                        }
                        
                except (ImportError, AttributeError) as e:
                    print(f"Error importing {module_name}: {e}")
        
        return self.solutions
    
    def _create_input_generators(self) -> Dict[str, Callable[[int], Any]]:
        """Create a dictionary of input generators for different problem types."""
        generators = {}
        
        # Integer array input (e.g., Three Sum)
        generators['array'] = lambda size: random.choices(range(-size, size), k=size)
        
        # String input (e.g., Longest Substring)
        generators['string'] = lambda size: ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=size))
        
        # Matrix/grid input (e.g., Number of Islands)
        generators['grid'] = lambda size: [
            [random.choice(['0', '1']) for _ in range(size)] for _ in range(size)
        ]
        
        # LRU Cache operations
        generators['lru_cache'] = lambda capacity: [
            ("put" if random.random() < 0.7 else "get", 
             (random.randint(0, capacity * 2), random.randint(0, 1000)) if random.random() < 0.7 else random.randint(0, capacity * 2))
            for _ in range(capacity * 10)
        ]
        
        # Rotated sorted array and target
        generators['rotated_array'] = lambda size: (
            sorted(random.sample(range(size * 3), size))[random.randint(0, size//2):] + 
            sorted(random.sample(range(size * 3), size))[:random.randint(0, size//2)],
            random.randint(0, size * 3)
        )
        
        # Stock prices (for buy/sell stock problems)
        generators['stock_prices'] = lambda size: [
            random.randint(1, size * 10) for _ in range(size)
        ]
        
        return generators
    
    def infer_benchmark_info(self, problem_name: str) -> Optional[BenchmarkInfo]:
        """
        Infer benchmarking information for a problem based on its name and structure.
        
        Args:
            problem_name: Name of the problem to analyze
            
        Returns:
            BenchmarkInfo object or None if inference fails
        """
        if problem_name not in self.solutions:
            return None
        
        problem_data = self.solutions[problem_name]
        filename = problem_data['file'].lower()
        module = problem_data['module']
        
        # First check if the module has explicit BENCHMARK_INFO
        if hasattr(module, 'BENCHMARK_INFO'):
            return module.BENCHMARK_INFO
        
        # Try to infer problem type from filename
        if '3_sum' in filename or 'three_sum' in filename:
            return BenchmarkInfo(
                input_generator=self.input_generators['array'],
                input_sizes=[10, 50, 100, 200, 300],
                target_method='threeSum'
            )
        
        elif 'longest_substr' in filename:
            return BenchmarkInfo(
                input_generator=self.input_generators['string'],
                input_sizes=[10, 100, 1000, 5000],
                target_method='lengthOfLongestSubstring'
            )
        
        elif 'islands' in filename:
            return BenchmarkInfo(
                input_generator=self.input_generators['grid'],
                input_sizes=[10, 20, 50, 75, 100],
                target_method='numIslands'
            )
        
        elif 'lru_cache' in filename:
            # Special case for LRU Cache
            def lru_wrapper(operations):
                first_cls = problem_data['classes'][0]
                cache = first_cls(len(operations) // 10)  # Capacity based on operation count
                for op, args in operations:
                    if op == "get":
                        cache.get(args)
                    else:  # put
                        key, value = args
                        cache.put(key, value)
            
            return BenchmarkInfo(
                input_generator=self.input_generators['lru_cache'],
                input_sizes=[100, 500, 1000, 2000],
                wrapper=lru_wrapper
            )
        
        elif 'rotated' in filename and 'search' in filename:
            def rotated_wrapper(data):
                array, target = data
                first_cls = problem_data['classes'][0]()
                return first_cls.search(array, target)
                
            return BenchmarkInfo(
                input_generator=self.input_generators['rotated_array'],
                input_sizes=[10, 100, 1000, 10000],
                wrapper=rotated_wrapper
            )
        
        elif 'stock' in filename or 'buy' in filename and 'sell' in filename:
            return BenchmarkInfo(
                input_generator=self.input_generators['stock_prices'],
                input_sizes=[10, 100, 1000, 10000],
                target_method='maxProfit'
            )
        
        # Default fallback - try to find a common method name
        for cls in problem_data['classes']:
            for method_name, method in inspect.getmembers(cls, inspect.isfunction):
                if method_name not in ('__init__', '__new__') and not method_name.startswith('_'):
                    # Found a potential method to benchmark
                    return BenchmarkInfo(
                        input_generator=self.input_generators['array'],  # Default
                        target_method=method_name
                    )
        
        return None
    
    def run_benchmark(self, problem_name: str, benchmark_info: BenchmarkInfo = None):
        """
        Run benchmarks for a specific problem.
        
        Args:
            problem_name: Name of the problem to benchmark
            benchmark_info: Optional BenchmarkInfo object (will be inferred if not provided)
            
        Returns:
            Dictionary with benchmark results
        """
        if problem_name not in self.solutions:
            print(f"Problem {problem_name} not found in solutions")
            return None
        
        problem_data = self.solutions[problem_name]
        
        # Use provided benchmark info or infer it
        if benchmark_info is None:
            benchmark_info = self.infer_benchmark_info(problem_name)
            if benchmark_info is None:
                print(f"Could not infer benchmark info for {problem_name}")
                return None
        
        # Create implementations dictionary
        implementations = {}
        
        if benchmark_info.wrapper:
            # Special case: use wrapper function directly
            implementations[f"{problem_name}"] = benchmark_info.wrapper
        else:
            # Standard case: benchmark each solution class
            for cls in problem_data['classes']:
                cls_name = cls.__name__
                
                # Create instance of the class
                instance = cls()
                
                # Get the target method
                target_method = benchmark_info.target_method
                if target_method is None:
                    # Try to find an appropriate method
                    for method_name, method in inspect.getmembers(instance, inspect.ismethod):
                        if method_name not in ('__init__', '__new__') and not method_name.startswith('_'):
                            target_method = method_name
                            break
                
                if target_method and hasattr(instance, target_method):
                    method = getattr(instance, target_method)
                    implementations[f"{cls_name}"] = lambda x, m=method: m(x)
        
        if not implementations:
            print(f"No implementations found for {problem_name}")
            return None
        
        # Create AlgorithmBenchmark from existing benchmark code
        # Assuming AlgorithmBenchmark is imported from benchmark_algorithms.py
        from py.benchmarks.benchmark_algorithms import AlgorithmBenchmark
        
        benchmark = AlgorithmBenchmark(problem_name)
        
        # Run benchmark
        results = benchmark.run_benchmark(
            implementations,
            benchmark_info.input_generator,
            benchmark_info.input_sizes,
            benchmark_info.num_runs
        )
        
        # Plot results
        benchmark.plot_results(log_scale=True, save_path=f"{problem_name.replace(' ', '_')}_benchmark.png")
        
        return results
    
    def run_all_benchmarks(self):
        """Discover and run benchmarks for all solutions."""
        self.discover_solutions()
        
        for problem_name in self.solutions:
            print(f"\n=== Running {problem_name} Benchmark ===")
            self.run_benchmark(problem_name)
