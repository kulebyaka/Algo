# Auto-Discovery Benchmark System

This system automatically discovers and benchmarks LeetCode solutions without requiring manual updates to `benchmark_algorithms.py`.

## Features

- **Automatic Solution Discovery**: Finds all LeetCode solution files using naming pattern `_NUMBER_name.py`
- **Smart Input Generation**: Automatically selects appropriate input generators for different problem types
- **Custom Benchmarking**: Allows custom benchmark configurations to be defined in solution files
- **Backward Compatibility**: Works with existing benchmark infrastructure

## Usage

### Basic Usage

Run all benchmarks:
```bash
python -m py.benchmarks.auto_discovery.runner
```

Run benchmark for a specific problem:
```bash
python -m py.benchmarks.auto_discovery.runner "three sum"
```

### Adding Custom Benchmark Info

You can add custom benchmark information to any LeetCode solution file:

```python
from py.benchmarks.auto_discovery.benchmark_metadata import BenchmarkInfo

# Solution class(es) here...

# Define custom benchmark info (optional)
BENCHMARK_INFO = BenchmarkInfo(
    input_generator=my_custom_generator,
    input_sizes=[10, 100, 1000],
    num_runs=5,
    name="Custom Benchmark Name"
)

def my_custom_generator(size):
    # Generate custom input data
    return data
```

If `BENCHMARK_INFO` is defined in a module, it will be used instead of the auto-inferred configuration.

## How It Works

1. The system scans the `py` directory for files matching the pattern `_NUMBER_name.py`
2. For each file, it imports the module and finds solution classes
3. It analyzes the filename to infer the problem type
4. Based on the problem type, it selects an appropriate input generator
5. When benchmarking is requested, it creates wrapper functions to call the solution methods
6. It uses the existing `AlgorithmBenchmark` class to run benchmarks and generate plots

## Extending

You can extend the system by:

1. Adding more input generators for new problem types in `_create_input_generators()`
2. Enhancing the inference logic in `infer_benchmark_info()`
3. Adding more wrapper functions for special problem types
