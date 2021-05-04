# Summary of data
- 19.2% reduced response time with optuna optimization tunables.
- Min response time is observed with following configuration
cpurequest=1.38 (container layer)
memrequest=957M (container layer)
maxinlinelevel=12 (hotspot layer)
quarkus.thread-pool.core.threads=2 (quarkus layer)
quarkus.thread-pool.queue.size=58 (quarkus layer)
quarkus.datasource.jdbc.min.size=5 (quarkus layer)
quarkus.datasource.jdbc.max.size=28 (quarkus layer)


## Tunables:
- cpuRequest 				Range : 1 - 3.2
- memoryRequest 			Range: 270MB - 1024MB
- maxinlinelevel			Range : 9 - 50
- quarkus.thread-pool.core.threads	Range: 3 - 24
- quarkus.thread-pool.queue.size	Range: 0 - 1000
- quarkus.datasource.jdbc.min.size	Range: 2 - 10
- quarkus.datasource.jdbc.max.size	Range: 20 - 48


![Responsetime](responsetimes.png)

![Responsetime Vs Trials](responsetimeVStrials.png)

![MaxResponsetime Vs Trials](maxresponsetimeVStrials.png)

![99.9 percentile latency Vs Trials](latency999pVStrials.png)

![99 percentile latency Vs Trials](latency99pVStrials.png)

![98 percentile latency Vs Trials](latency98pVStrials.png)

![50 nad 95 percentile latency Vs Trials](latency50p95pVStrials.png)

