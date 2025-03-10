# Algorithm Problems Collection

This repository contains solutions to various algorithm problems from LeetCode and other sources.

## Project Structure

```
algo-problems/
├── src/                     # Algorithm implementations
├── tests/                   # Test directory
│   ├── test_algorithms.py   # Main test suite
│   ├── test_lru_cache.py    # LRU Cache specific tests
│   └── ...                  # Other specific tests
├── benchmarks/              # Performance benchmarking tools
│   └── benchmark_algorithms.py  # Benchmarking utilities
├── .github/                 # GitHub Actions workflows
│   └── workflows/           # CI/CD configuration
├── requirements.txt         # Project dependencies
└── setup.py                 # Package setup
```

## Running Tests

To run all tests:

```bash
pytest tests/
```

To run a specific test file:

```bash
pytest tests/test_lru_cache.py
```

To run with coverage report:

```bash
pytest --cov=py tests/
```

## Benchmarking

The repository includes tools for benchmarking algorithm performance.

To run all benchmarks:

```bash
python -m benchmarks.benchmark_algorithms all
```

To benchmark a specific algorithm:

```bash
python -m benchmarks.benchmark_algorithms three_sum
```

Available benchmark options:
- `three_sum`: Three Sum algorithm
- `lru_cache`: LRU Cache operations
- `longest_substring`: Longest Substring Without Repeating Characters
- `islands`: Number of Islands
- `rotated_search`: Search in Rotated Sorted Array

Benchmark results will be displayed in the console and saved as PNG visualizations in the benchmark-results directory.

## Continuous Integration

This repository uses GitHub Actions for continuous integration:

- **Automated Testing**: Tests are run on every push and pull request
- **Performance Benchmarking**: Algorithm performance is tracked over time
- **Regression Detection**: Alerts are triggered when performance degrades

### Performance Monitoring

Performance of algorithm implementations is monitored automatically:

1. Benchmarks run after every push to master/main
2. Performance data is stored for historical comparison
3. Visualizations are generated to track trends
4. Notifications are sent when performance regressions occur

To view performance trends, check the GitHub Pages site after setup:
```
https://[username].github.io/[repository]/dev/bench/
```

## Algorithms Implemented

- LRU Cache (146)
- Reverse Words in a String (151)
- Three Sum (15)
- Letter Combinations of a Phone Number (17)
- Sign of the Product of an Array (1822)
- Number of Islands (200)
- Search in Rotated Sorted Array (33)
- Longest Substring Without Repeating Characters (3)
- Group Anagrams (49)
- Spiral Matrix (54)
- Longest Palindromic Substring (5)

## Installation

```bash
pip install -e .
```

This will install the package in development mode.
