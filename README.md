# autotune-results
Recommendations and Results from Autotune

# Methodology to generate the autotune-results
Below are the factors considered while running the benchmark in an autotune experiment.
- Repetability
- Convergence
- Reproducibility

Above factors are measured using the below process:
1. Each Autotune experiment is usually composed of 100 trials.
2. Each Trial tests a specific config from HPO.
3. Each trial runs the benchmark with multiple iterations. The benchmark container gets re-deployed at the start of each iteration.
4. Each iteration in a trial includes warmup and measurement cycles. Duration of warmup cycles is based on pre-run data from the benchmark.
5. For each trial, measure convergence in the benchmark data by calculating the confidence interval by using T-distribution for each metric.
6. Calculates the min, max, mean and percentile info for the metrics.
