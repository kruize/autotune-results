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
- quarkus.thread-pool.core.threads	Range: 1 - 3
- quarkus.thread-pool.queue.size	Range: 1 - 100
- quarkus.datasource.jdbc.min.size	Range: 0 - 10
- quarkus.datasource.jdbc.max.size	Range: 20 - 50

![Responsetime](responsetime.png)

![Responsetime Vs Trials](maxresponsetimeVStrials.png)

![MaxResponsetime Vs Trials](responsetimeVStrials.png)

