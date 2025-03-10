"""
Utility to generate benchmark summary data in a format suitable for CI/CD monitoring.
"""

import json
import statistics
import datetime
from typing import Dict, List, Any


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
                          output_path: str = "benchmark-results/benchmark_summary.json"):
    """
    Save benchmark summary to a JSON file.
    
    Args:
        benchmark_results: Dictionary with benchmark results
        benchmark_name: Name of the benchmark
        output_path: Path to save the JSON file
    """
    summary = generate_benchmark_summary(benchmark_results, benchmark_name)
    
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
