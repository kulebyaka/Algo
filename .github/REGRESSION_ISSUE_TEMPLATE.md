---
title: 🚨 Performance Regression Detected
labels: performance, bug, high-priority
assignees: kulebyaka
---

## Performance Regression Alert

A significant performance regression has been detected in the algorithm repository.

### Details:

- **Repository:** {{ env.GITHUB_REPOSITORY }}
- **Commit:** [{{ env.GITHUB_SHA }}](https://github.com/{{ env.GITHUB_REPOSITORY }}/commit/{{ env.GITHUB_SHA }})
- **Workflow Run:** [GitHub Actions Run #{{ env.GITHUB_RUN_ID }}](https://github.com/{{ env.GITHUB_REPOSITORY }}/actions/runs/{{ env.GITHUB_RUN_ID }})
- **Detected On:** {{ date | date('YYYY-MM-DD HH:mm:ss') }}

### Affected Algorithms:

The performance regression was detected in one or more of the following algorithms:

- Three Sum
- LRU Cache
- Longest Substring Without Repeating Characters
- Number of Islands
- Search in Rotated Sorted Array

### Next Steps:

1. Check the benchmark results in the GitHub Actions artifacts
2. Compare current performance with previous runs
3. Identify the cause of the regression
4. Revert or fix the problematic changes

### Benchmark Visualization

The benchmark results are available as artifacts in the GitHub Actions run.

To view long-term performance trends, check the GitHub Pages site for this repository:
https://{{ env.GITHUB_REPOSITORY_OWNER }}.github.io/{{ env.GITHUB_REPOSITORY | split('/') | last }}/dev/bench/

---

This issue was automatically created by the GitHub Actions workflow.
