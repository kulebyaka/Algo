"""
Runner for auto-discovery benchmark system.

This module provides an entry point for running benchmarks using the auto-discovery system.
"""

from py.benchmarks.auto_discovery.benchmark_metadata import AutoBenchmark


def main():
    """Run the automated benchmarking system."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Benchmark algorithm implementations")
    parser.add_argument("problem", nargs="?", default="all", 
                      help="Problem to benchmark (e.g., '15. three sum') or 'all'")
    args = parser.parse_args()
    
    auto_benchmark = AutoBenchmark()
    auto_benchmark.discover_solutions()
    
    if args.problem.lower() == "all":
        auto_benchmark.run_all_benchmarks()
    else:
        # Find matching problem
        matching_problems = [p for p in auto_benchmark.solutions if args.problem.lower() in p.lower()]
        
        if matching_problems:
            for problem in matching_problems:
                print(f"\n=== Running {problem} Benchmark ===")
                auto_benchmark.run_benchmark(problem)
        else:
            print(f"No matching problems found for '{args.problem}'")
            print("Available problems:")
            for problem in sorted(auto_benchmark.solutions.keys()):
                print(f"  - {problem}")


if __name__ == "__main__":
    main()
