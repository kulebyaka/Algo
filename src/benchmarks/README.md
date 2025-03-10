# Algorithm Benchmarking Tools

This directory contains tools for benchmarking algorithm performance and comparing different implementations.

## Overview

The benchmarking tools allow you to:
- Measure execution time of different algorithm implementations
- Compare performance across varying input sizes
- Generate visualizations of performance characteristics
- Analyze algorithm efficiency empirically

## Usage

### Running All Benchmarks

To run all available benchmarks:

```bash
python -m benchmarks.benchmark_algorithms all
```

### Running Specific Benchmarks

To benchmark a specific algorithm:

```bash
python -m benchmarks.benchmark_algorithms three_sum
```

Available options:
- `three_sum`: Three Sum algorithm
- `lru_cache`: LRU Cache operations
- `longest_substring`: Longest Substring Without Repeating Characters
- `islands`: Number of Islands
- `rotated_search`: Search in Rotated Sorted Array

### Benchmark Results

Benchmark results will be displayed in the console and saved as PNG visualizations in the current directory.

## Adding New Benchmarks

To add a new algorithm benchmark:

1. Create an input generator function that produces test data for different sizes
2. Define a benchmark function that compares different implementations
3. Add the new benchmark to the available options in the command-line interface

Example:

```python
def generate_new_algorithm_input(size: int) -> Any:
    # Generate test data of specified size
    return data

def benchmark_new_algorithm():
    benchmark = AlgorithmBenchmark("New Algorithm")
    
    implementations = {
        "Original Implementation": original_implementation,
        "Improved Implementation": improved_implementation
    }
    
    input_sizes = [10, 100, 1000]
    benchmark.run_benchmark(implementations, generate_new_algorithm_input, input_sizes)
    benchmark.plot_results(save_path="new_algorithm_benchmark.png")
```

## Interpreting Results

The benchmark plots show:
- X-axis: Input size
- Y-axis: Execution time in seconds
- Each line represents a different implementation

Logarithmic scales are used for algorithms with exponential time complexity to better visualize differences.

## Requirements

The benchmarking tools require:
- matplotlib
- numpy
- statistics (part of Python standard library)
