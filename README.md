# Algorithm Problems Collection

This repository contains solutions to various algorithm problems from LeetCode and other sources.

## Project Structure

```
algo-problems/
├── py/                      # Python algorithm implementations
│   ├── benchmarks/          # Performance benchmarking tools
│   ├── tests/               # Test directory
│   └── _*.py                # Individual algorithm solutions
├── .github/                 # GitHub Actions workflows
│   └── workflows/           # CI/CD configuration
├── requirements.txt         # Project dependencies
```

## Running Tests

To run all tests:

```bash
cd py
pytest tests/
```

To run a specific test file:

```bash
cd py
pytest tests/test_lru_cache.py
```

To run with coverage report:

```bash
cd py
pytest --cov=. tests/
```

## Benchmarking

The repository includes tools for benchmarking algorithm performance.

To run all benchmarks:

```bash
cd py
python -m benchmarks.benchmark_algorithms all
```

To benchmark a specific algorithm:

```bash
cd py
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

[![Algorithm Performance Benchmarks](https://github.com/kulebyaka/Algo/actions/workflows/benchmark.yml/badge.svg)](https://github.com/kulebyaka/Algo/actions/workflows/benchmark.yml)

### Notifications

When performance regressions are detected, the system:

1. **Creates a GitHub Issue** with detailed information about the regression
2. **Sends a webhook notification** to a Make.com integration
3. **Comments on the PR** if the regression was introduced in a pull request

The webhook sends the following data to Make.com:
```json
{
  "type": "performance_regression",
  "repository": "username/repo",
  "commit": "commit-sha",
  "workflow_run_id": "run-id",
  "workflow_run_url": "url-to-github-action",
  "detected_at": "timestamp",
  "branch": "branch-name",
  "action_url": "url-to-action"
}
```

You can use this webhook data in Make.com to trigger various automations like sending emails, Slack messages, creating tickets in project management tools, etc.

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
