"""
Utility to generate benchmark summary data in a format suitable for CI/CD monitoring.
"""

import json
import statistics
import datetime
import os
from typing import Dict, List, Any
from pathlib import Path


def generate_benchmark_summary(benchmark_results: Dict[str, Dict[int, List[float]]],
                              benchmark_name: str) -> Dict[str, Any]:
    """
    Generate a benchmark summary in a format suitable for tracking in CI/CD.
    
    Args:
        benchmark_results: Dictionary with benchmark results
        benchmark_name: Name of the benchmark
        
    Returns:
        Dictionary with formatted benchmark summary
    """
    summary = {
        "name": benchmark_name,
        "date": datetime.datetime.now().isoformat(),
        "implementations": {}
    }
    
    for impl_name, size_results in benchmark_results.items():
        impl_summary = {
            "name": impl_name,
            "metrics": {}
        }
        
        # Get the largest input size for comparison
        largest_size = max(size_results.keys())
        
        # Calculate average for largest size
        avg_time = statistics.mean(size_results[largest_size])
        
        # Add to metrics
        impl_summary["metrics"] = {
            "avg_time_ms": avg_time * 1000,  # Convert to milliseconds
            "input_size": largest_size
        }
        
        summary["implementations"][impl_name] = impl_summary
    
    return summary


def save_benchmark_summary(benchmark_results: Dict[str, Dict[int, List[float]]],
                          benchmark_name: str,
                          output_path: str = "../benchmark-results/benchmark_summary.json"):
    """
    Save benchmark summary to a JSON file.
    
    Args:
        benchmark_results: Dictionary with benchmark results
        benchmark_name: Name of the benchmark
        output_path: Path to save the JSON file
    """
    summary = generate_benchmark_summary(benchmark_results, benchmark_name)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Read existing file if it exists
    try:
        with open(output_path, 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {"benchmarks": []}
    
    # Add new benchmark data
    existing_data["benchmarks"].append(summary)
    
    # Write updated data
    with open(output_path, 'w') as f:
        json.dump(existing_data, f, indent=2)
    
    # Also save the GitHub Action Benchmark formatted output
    github_action_path = os.path.join(os.path.dirname(output_path), "github_action_benchmark.json")
    save_github_action_output(benchmark_results, benchmark_name, github_action_path)
    
    print(f"Benchmark summary saved to {output_path}")
    
    # Check if this run shows a performance regression
    if check_for_regression(summary):
        regression_path = os.path.join(os.path.dirname(output_path), "regression_detected.txt")
        with open(regression_path, 'w') as f:
            f.write(f"Performance regression detected in {benchmark_name} at {datetime.datetime.now().isoformat()}")
        print(f"⚠️ Performance regression detected! See {regression_path} for details.")


def generate_github_action_output(benchmark_results: Dict[str, Dict[int, List[float]]],
                                 benchmark_name: str) -> List[Dict[str, Any]]:
    """
    Generate output in the format expected by the GitHub Action Benchmark.
    
    Args:
        benchmark_results: Dictionary with benchmark results
        benchmark_name: Name of the benchmark
        
    Returns:
        List of benchmark entries for GitHub Action Benchmark
    """
    action_data = []
    
    for impl_name, size_results in benchmark_results.items():
        # Get the largest input size for comparison
        largest_size = max(size_results.keys())
        
        # Calculate average for largest size
        avg_time = statistics.mean(size_results[largest_size])
        
        # Create benchmark entry
        entry = {
            "name": f"{benchmark_name} - {impl_name} (size {largest_size})",
            "unit": "ms",
            "value": avg_time * 1000  # Convert to milliseconds
        }
        
        action_data.append(entry)
    
    return action_data


def save_github_action_output(benchmark_results: Dict[str, Dict[int, List[float]]],
                             benchmark_name: str,
                             output_path: str = "../benchmark-results/github_action_output.json"):
    """
    Save benchmark data in the format expected by GitHub Action Benchmark.
    
    Args:
        benchmark_results: Dictionary with benchmark results
        benchmark_name: Name of the benchmark
        output_path: Path to save the JSON file
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Generate GitHub Action output
    action_data = generate_github_action_output(benchmark_results, benchmark_name)
    
    # Write to file
    with open(output_path, 'w') as f:
        json.dump(action_data, f, indent=2)
    
    print(f"GitHub Action output saved to {output_path}")


def check_for_regression(summary: Dict[str, Any]) -> bool:
    """
    Check if the current benchmark results show a performance regression.
    This is a simple implementation that could be expanded as needed.
    
    Args:
        summary: Dictionary with benchmark summary
        
    Returns:
        True if a regression is detected, False otherwise
    """
    # This is a placeholder. In a real implementation, you would compare
    # with previous benchmark results to detect regressions.
    # For now, always return False to avoid false positives.
    return False
