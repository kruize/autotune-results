## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the best configurations are run to reproduce the data and will be updated at [manuals](manuals) dir

# Goal of the experiment:
- Minimize transaction response time.
- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Container] cpuRequest				[None, 1-4]		=      4
[Container] memoryRequest			[None, 270M-4096M]	=  3319M
[Quarkus]   quarkus.thread-pool.core-threads	[1, 0-32]		=     19
[Quarkus]   quarkus.thread-pool.queue-size	[unbounded, 0-10000]	=   3700
[Quarkus]   quarkus.datasource.jdbc.min-size	[0, 1-12]		=     10
[Quarkus]   quarkus.datasource.jdbc.max-size	[12, 12-90]		=     86
[Hotspot]   FreqInlineSize			[325, 325-500]		=    340
[Hotspot]   MaxInlineLevel			[9, 9-50]		=     50
[Hotspot]   MinInliningThreshold		[250, 0-200]		=     55
[Hotspot]   CompileThreshold			[1500, 1000-10000]	=   6930
[Hotspot]   CompileThresholdScaling		[1, 1-15]		=    8.3
[Hotspot]   ConcGCThreads			[0, 0-8]		=      6
[Hotspot]   InlineSmallCode			[1000, 500-5000]	=   1416
[Hotspot]   LoopUnrollLimit			[50, 20-250]		=    128
[Hotspot]   LoopUnrollMin			[4, 0-20]		=     13
[Hotspot]   MinSurvivorRatio			[3, 3-48]		=     12
[Hotspot]   NewRatio				[2, 1-10]		=      9
[Hotspot]   TieredStopAtLevel			[4, 0-4]		=      4
[Hotspot]   TieredCompilation			[false, ]		=   true
[Hotspot]   AllowParallelDefineClass		[false, ]		=  false
[Hotspot]   AllowVectorizeOnDemand		[true, ]		=   true
[Hotspot]   AlwaysCompileLoopMethods		[false, ]		=  false
[Hotspot]   AlwaysPreTouch			[false, ]		=  false
[Hotspot]   AlwaysTenure			[false, ]		=   true
[Hotspot]   BackgroundCompilation		[true, ]		=   true
[Hotspot]   DoEscapeAnalysis			[true, ]		=   true
[Hotspot]   UseInlineCaches			[true, ]		=  false
[Hotspot]   UseLoopPredicate			[true, ]		=  false
[Hotspot]   UseStringDeduplication		[false, ]		=  false
[Hotspot]   UseSuperWord			[true, ]		=   true
[Hotspot]   UseTypeSpeculation			[true, ]		=   true

```
Along with the above tunables, other JVM options hardcoded are "-server -XX:MAXRamPercentage=70 -XX:+UseG1GC"
Quarkus tunable quarkus.datasource.jdbc.initial-size is set same as quarkus.datasource.jdbc.min-size to avoid min-size being picked with default when min-size is set higher than initial-size.
Hotspot tunable ParallelGCThreads set same as ConcGCThreads to avoid JVM exit when ParallelGCThreads are less than ConcGCThreads.

Baseline / Default configuration used is cpu request and limits set to 4 ; memory requests and limits set to 4096M ; JAVA_OPTIONS= "-server -XX:+UseG1GC"

- Trial 38 is considered as the best configuration in the experiment.
- Comparing the best configuration from autotune with the baseline, 
	- Throughput improved by ~6.85% 
	- Response time reduced by ~61.97%
	- Max response time increased by ~57.67%
	- Memory usage increased by ~164.9%

![Throughput](https://user-images.githubusercontent.com/17760990/137851168-a6ad67a9-addd-46d6-9eac-428c1347ee1e.png)
![Response_time](https://user-images.githubusercontent.com/17760990/137851181-c21263b7-edb4-443d-a81b-db29f520b271.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/137851192-00352d5b-2a4c-4fbe-815a-3fd66138cbb2.png)
![Cpu_usage](https://user-images.githubusercontent.com/17760990/137851222-f367d291-3331-4419-ad1a-0d773d8b1028.png)
![Memory_usage](https://user-images.githubusercontent.com/17760990/137851236-4bba5a08-b87e-4de6-a4ad-3d19f4a8797b.png)

![Response_time VS Trials](https://user-images.githubusercontent.com/17760990/139204216-1d799875-dfcd-44a3-b5c6-0cf35b206da7.png)
![Max_Response_time VS Trials](https://user-images.githubusercontent.com/17760990/139204283-f9428803-8c3d-4dfe-acd1-9f6ae9edbbde.png)
In the above graphs, trial 0 is the data of default configuration which is considered as baseline.

### Configuration Details:
- JVM                   openjdk:11.0.6
- Quarkus               1.13.2.F
- Machine: 
```
  - Server:  openshift cluster v4.8.13
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


Note: Best configuration from multiple trials is picked based on having least response time with good throughput, no errors while running the load and ensuring the data has met the convergence criteria.
Each trial would have an individual configuartion based on the tunables.For information on the configuration of a particular trial, look into experiment-data.csv
