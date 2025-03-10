# GitHub Actions Workflows

This directory contains GitHub Actions workflows for CI/CD automation.

## Benchmark Workflow

The `benchmark.yml` workflow automatically runs performance benchmarks for algorithm implementations.

### When It Runs

- On every push to master/main branch
- On pull requests to master/main branch
- Weekly (Sunday at midnight)
- Manually via workflow_dispatch

### What It Does

1. Runs all algorithm benchmarks
2. Uploads benchmark results as artifacts
3. Stores performance data for historical comparison
4. Checks for performance regressions
5. Sends notifications when performance regressions are detected

### Notifications

When a performance regression is detected, the workflow:

1. Creates a GitHub issue with details about the regression
2. Sends an email notification (if configured)
3. Sends a Slack notification (if configured)

### Configuration

To enable email notifications, you need to add the following secrets to your repository:

- `MAIL_SERVER`: SMTP server address
- `MAIL_PORT`: SMTP server port
- `MAIL_USERNAME`: SMTP username
- `MAIL_PASSWORD`: SMTP password
- `NOTIFICATION_EMAIL`: Email address to send notifications to

To enable Slack notifications, you need to add:

- `SLACK_WEBHOOK`: Slack webhook URL

### Performance Visualization

The benchmark results are visualized and stored on GitHub Pages. To view them, go to:

```
https://[username].github.io/[repository]/dev/bench/
```

### Customization

You can customize the workflow by:

- Adjusting the alert threshold in the workflow file
- Modifying the notification settings
- Changing the frequency of scheduled runs
