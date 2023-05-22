## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the top 5 best configuration were run to reproduce the data and were updated at [manuals](manuals) dir

# Goal of the experiment:
- Minimize transaction response time.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data:
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Container] cpuRequest				[None, 1-32]		=  27.14
[Container] memoryRequest			[None, 270M-8192M]	=  7654M
[Quarkus]   quarkus.thread-pool.core-threads	[1, 3-256]		=    158
[Quarkus]   quarkus.thread-pool.queue-size	[unbounded, 0-10000]	=   5572
[Quarkus]   quarkus.datasource.jdbc.min-size	[0, 2-31]		=     23
[Quarkus]   quarkus.datasource.jdbc.max-size	[20, 32-100]		=     87
[Hotspot]   FreqInlineSize			[325, 325-1000]		=    404
[Hotspot]   MaxInlineLevel			[9, 9-50]		=     26
[Hotspot]   MinInliningThreshold		[250, 0-500]		=     82
[Hotspot]   CompileThreshold			[1500, 1000-20000]	=   8942
[Hotspot]   CompileThresholdScaling		[1, 1-20]		=   8.81
[Hotspot]   ConcGCThreads			[0, 0-32]		=     27
[Hotspot]   InlineSmallCode			[1000, 500-5000]	=   4095
[Hotspot]   LoopUnrollLimit			[50, 20-250]		=    237
[Hotspot]   LoopUnrollMin			[4, 0-20]		=      3
[Hotspot]   MinSurvivorRatio			[3, 3-48]		=     22
[Hotspot]   NewRatio				[2, 1-20]		=      1
[Hotspot]   TieredStopAtLevel			[4, 0-4]		=      4
[Hotspot]   TieredCompilation			[false, ]		=   true
[Hotspot]   AllowParallelDefineClass		[false, ]		=  false
[Hotspot]   AllowVectorizeOnDemand		[true, ]		=  false
[Hotspot]   AlwaysCompileLoopMethods		[false, ]		=  false
[Hotspot]   AlwaysPreTouch			[false, ]		=  false
[Hotspot]   AlwaysTenure			[false, ]		=  false
[Hotspot]   BackgroundCompilation		[true, ]		=   true
[Hotspot]   DoEscapeAnalysis			[true, ]		=  false
[Hotspot]   UseInlineCaches			[true, ]		=  false
[Hotspot]   UseLoopPredicate			[true, ]		=  false
[Hotspot]   UseStringDeduplication		[false, ]		=  false
[Hotspot]   UseSuperWord			[true, ]		=  false
[Hotspot]   UseTypeSpeculation			[true, ]		=   true

```
Along with the above tunables, other JVM options hardcoded are "-server -XX:MAXRamPercentage=70 -XX:+UseG1GC"
Quarkus tunable quarkus.datasource.jdbc.initial-size is set same as quarkus.datasource.jdbc.min-size to avoid min-size being picked with default when min-size is set higher than initial-size.
Hotspot tunable ParallelGCThreads set same as ConcGCThreads to avoid JVM exit when ParallelGCThreads are less than ConcGCThreads.

- Trial 59 is considered as the best configuration from the experiment.
- Comparing the best configuration with the baseline (where no configuration is set), 
	- Throughput improved by ~18.96% 
	- Response time reduced by ~60%
	- Max response time increased by ~23%
	- CPU usage increased by ~89%
	- Memory usage increased by ~45%

![Throughput](https://user-images.githubusercontent.com/17760990/135136932-4fd12d4e-1660-4bf2-a7fb-ccf1210af1bb.png)
![Response_time](https://user-images.githubusercontent.com/17760990/135136951-d8b1ee87-999f-447b-babf-d0c0ff747695.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/135136959-d5d2db56-8943-40f5-9a2c-187505212109.png)
![cpu_usage](https://user-images.githubusercontent.com/17760990/135136975-525ea091-bf0a-4aa8-95f1-ca3d56dd5d0d.png)
![memory_usage](https://user-images.githubusercontent.com/17760990/135136986-67981ac5-4ea9-49d9-a3dd-746dd0e08488.png)

![Response_time VS Trials](https://user-images.githubusercontent.com/17760990/139199809-55079879-d371-4d6e-968d-b57fa3ab2e46.png)
![Max_Response_time VS Trials](https://user-images.githubusercontent.com/17760990/139200287-6ba90a8f-9400-4ff5-9396-5912998778e1.png)

In the above graphs, trial 0 is the data of default configuration which is considered as baseline.

### Configuration Details:

```
- JVM			openjdk:11.0.6
- Quarkus		1.13.2.F
```
- Machine: 
```
  - Server:  openshift cluster v4.7.19
    Master nodes	3
    Worker nodes	6
    CPU per node	32
    Memory per node	64G

  - Client: RHEL 8.3
    CPU  		64
    Memory 		64G  
```
- Load: 
```
 	Users :		512
	Threads :	56
```

Note: Best configuration from multiple trials is picked based on having least response time, no errors while running the load and ensuring the data has met the convergence criteria.
Each trial would have an individual configuartion based on the tunables.For information on the configuration of a particular trial, look into experiment-data.csv
