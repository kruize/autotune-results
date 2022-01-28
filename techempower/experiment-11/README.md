## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the best configuration were run to reproduce the data and were updated at [manuals](manuals) dir

# Goal of the experiment:
- Minimize transaction response time.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Container] cpuRequest				[None, 1-4]		=   3.75
[Container] memoryRequest			[None, 270M-4096M]	=  3474M
[Quarkus]   quarkus.thread-pool.core-threads	[1, 0-32]		=     12
[Quarkus]   quarkus.thread-pool.queue-size	[unbounded, 0-10000]	=   2140
[Quarkus]   quarkus.datasource.jdbc.min-size	[0, 1-12]		=      1
[Quarkus]   quarkus.datasource.jdbc.max-size	[12, 12-90]		=     45
[Hotspot]   FreqInlineSize			[325, 325-500]		=    416
[Hotspot]   MaxInlineLevel			[9, 9-50]		=     42
[Hotspot]   MinInliningThreshold		[250, 0-200]		=      6
[Hotspot]   CompileThreshold			[1500, 1000-10000]	=   7080
[Hotspot]   CompileThresholdScaling		[1, 1-15]		=    3.6
[Hotspot]   ConcGCThreads			[0, 0-8]		=      6
[Hotspot]   InlineSmallCode			[1000, 500-5000]	=   1891
[Hotspot]   LoopUnrollLimit			[50, 20-250]		=    146
[Hotspot]   LoopUnrollMin			[4, 0-20]		=     13
[Hotspot]   MinSurvivorRatio			[3, 3-48]		=      7
[Hotspot]   NewRatio				[2, 1-10]		=      5
[Hotspot]   TieredStopAtLevel			[4, 0-4]		=      3
[Hotspot]   TieredCompilation			[false, ]		=  false
[Hotspot]   AllowParallelDefineClass		[false, ]		=   true
[Hotspot]   AllowVectorizeOnDemand		[true, ]		=  false
[Hotspot]   AlwaysCompileLoopMethods		[false, ]		=  false
[Hotspot]   AlwaysPreTouch			[false, ]		=  false
[Hotspot]   AlwaysTenure			[false, ]		=   true
[Hotspot]   BackgroundCompilation		[true, ]		=   true
[Hotspot]   DoEscapeAnalysis			[true, ]		=   true
[Hotspot]   UseInlineCaches			[true, ]		=   true
[Hotspot]   UseLoopPredicate			[true, ]		=   true
[Hotspot]   UseStringDeduplication		[false, ]		=   true
[Hotspot]   UseSuperWord			[true, ]		=  false
[Hotspot]   UseTypeSpeculation			[true, ]		=   true

```
Along with the above tunables, other JVM options hardcoded are "-server -XX:MAXRamPercentage=70 -XX:+UseG1GC"
Quarkus tunable quarkus.datasource.jdbc.initial-size is set same as quarkus.datasource.jdbc.min-size to avoid min-size being picked with default when min-size is set higher than initial-size.
Hotspot tunable ParallelGCThreads set same as ConcGCThreads to avoid JVM exit when ParallelGCThreads are less than ConcGCThreads.

Baseline / Default configuration used is cpu request and limits set to 4 ; memory requests and limits set to 4096M ; JAVA_OPTIONS= "-server -XX:+UseG1GC"

- Trial 100 is considered as the best configuration in the experiment.
- Comparing the best configuration from autotune with the baseline, 
	- Response time reduced by ~80.79%
	- Max response time reduced by ~12%

![Throughput](https://user-images.githubusercontent.com/17760990/139646364-355b352d-24ab-44d6-92a6-b4a8d349817d.png)
![Response_time](https://user-images.githubusercontent.com/17760990/139646372-2cffc205-d0b4-4947-8f03-f3cdfb35d126.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/139646381-85c6e4ed-e0c7-4319-9f60-51e8b18f0008.png)
![Cpu_usage](https://user-images.githubusercontent.com/17760990/139646400-b742f9a0-a11f-4916-b5ae-afb6184272fb.png)
![Memory_usage](https://user-images.githubusercontent.com/17760990/139646413-5bc8b68a-e5b4-4b42-a415-f7846dfca3ef.png)

![Response_time VS Trials](https://user-images.githubusercontent.com/17760990/139646277-ffaa05a5-3f69-42a0-aa7c-2f558b539a7d.png)
![Max_Response_time VS Trials](https://user-images.githubusercontent.com/17760990/139646283-9d561fe4-3833-450e-8dea-c0908db47c76.png)

In the above graphs, trial 0 is the data of default configuration which is considered as baseline.

### Configuration Details:
```
- JVM                   openjdk:11.0.6
- Quarkus               1.13.2.F
```
- Machine: 
```
  - Server:  openshift cluster v4.8.13
    Master nodes	3
    Worker nodes	3
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
