## All the experiments in this folder were run on dedicated infrastructure. 

# Goal of the experiment:
- Minimize transaction response time.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Container] cpuRequest				[None, 1-2]		=   1.88
[Container] memoryRequest			[None, 270M-4096M]	=  2074M
[Quarkus]   quarkus.thread-pool.core-threads	[1, 0-32]		=      9
[Quarkus]   quarkus.thread-pool.queue-size	[unbounded, 0-10000]	=   5620
[Quarkus]   quarkus.datasource.jdbc.min-size	[0, 1-12]		=      2
[Quarkus]   quarkus.datasource.jdbc.max-size	[12, 12-90]		=     37
[Hotspot]   FreqInlineSize			[325, 325-500]		=    451
[Hotspot]   MaxInlineLevel			[9, 9-50]		=     26
[Hotspot]   MinInliningThreshold		[250, 0-200]		=     81
[Hotspot]   CompileThreshold			[1500, 1000-10000]	=   2982
[Hotspot]   CompileThresholdScaling		[1, 1-15]		=   4.77
[Hotspot]   ConcGCThreads			[0, 0-8]		=      2
[Hotspot]   InlineSmallCode			[1000, 500-5000]	=   1522
[Hotspot]   LoopUnrollLimit			[50, 20-250]		=    196
[Hotspot]   LoopUnrollMin			[4, 0-20]		=     14
[Hotspot]   MinSurvivorRatio			[3, 3-48]		=     21
[Hotspot]   NewRatio				[2, 1-10]		=      1
[Hotspot]   TieredStopAtLevel			[4, 0-4]		=      2
[Hotspot]   TieredCompilation			[false, ]		=  false
[Hotspot]   AllowParallelDefineClass		[false, ]		=   true
[Hotspot]   AllowVectorizeOnDemand		[true, ]		=   true
[Hotspot]   AlwaysCompileLoopMethods		[false, ]		=  false
[Hotspot]   AlwaysPreTouch			[false, ]		=   true
[Hotspot]   AlwaysTenure			[false, ]		=  false
[Hotspot]   BackgroundCompilation		[true, ]		=   true
[Hotspot]   DoEscapeAnalysis			[true, ]		=   true
[Hotspot]   UseInlineCaches			[true, ]		=  false
[Hotspot]   UseLoopPredicate			[true, ]		=   true
[Hotspot]   UseStringDeduplication		[false, ]		=   true
[Hotspot]   UseSuperWord			[true, ]		=  false
[Hotspot]   UseTypeSpeculation			[true, ]		=   true

```
Along with the above tunables, other JVM options hardcoded are "-server -XX:MAXRamPercentage=70 -XX:+UseG1GC"
Quarkus tunable quarkus.datasource.jdbc.initial-size is set same as quarkus.datasource.jdbc.min-size to avoid min-size being picked with default when min-size is set higher than initial-size.
Hotspot tunable ParallelGCThreads set same as ConcGCThreads to avoid JVM exit when ParallelGCThreads are less than ConcGCThreads.

Baseline / Default configuration used is cpu request and limits set to 2 ; memory requests and limits set to 4096M ; JAVA_OPTIONS= "-server -XX:+UseG1GC"

- Trial 113 is considered as the best configuration in the experiment.
- Comparing the best configuration from autotune with the baseline, 
	- Response time reduced by ~71.14%

![Throughput](https://user-images.githubusercontent.com/17760990/151572385-c7fdae9b-5f4a-4bb7-8104-69721a15dcaa.png)
![Response_time](https://user-images.githubusercontent.com/17760990/151572440-70f5fa55-e6fe-41e1-9322-d185faab2fbe.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/151572454-4f17e392-7970-456f-9296-7fd70ea8cfdc.png)
![Cpu_usage](https://user-images.githubusercontent.com/17760990/151572464-2307ca94-7a0b-4474-8616-39dc34653744.png)
![Memory_usage](https://user-images.githubusercontent.com/17760990/151572481-ddc3c0f6-d9fc-47cd-b3ba-bb605fc99703.png)

![Response_time VS Trials](https://user-images.githubusercontent.com/17760990/151572600-55932a0b-584a-48fa-9b61-0f7e07ad1700.png)
![Max_Response_time VS Trials](https://user-images.githubusercontent.com/17760990/151572618-e2cfde41-9b0a-4aba-9d0a-840f313e03b2.png)

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
