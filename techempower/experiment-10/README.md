## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the best configuration were run to reproduce the data and were updated at [manuals](manuals) dir

# Goal of the experiment:
- Minimize transaction response time.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Container] cpuRequest				[None, 1-4]		=   3.88
[Container] memoryRequest			[None, 270M-4096M]	=  3016M
[Quarkus]   quarkus.thread-pool.core-threads	[1, 0-32]		=     25
[Quarkus]   quarkus.thread-pool.queue-size	[unbounded, 0-10000]	=   2550
[Quarkus]   quarkus.datasource.jdbc.min-size	[0, 1-12]		=      4
[Quarkus]   quarkus.datasource.jdbc.max-size	[12, 12-90]		=     53
[Hotspot]   FreqInlineSize			[325, 325-500]		=    479
[Hotspot]   MaxInlineLevel			[9, 9-50]		=     29
[Hotspot]   MinInliningThreshold		[250, 0-200]		=     24
[Hotspot]   CompileThreshold			[1500, 1000-10000]	=   1850
[Hotspot]   CompileThresholdScaling		[1, 1-15]		=    3.3
[Hotspot]   ConcGCThreads			[0, 0-8]		=      7
[Hotspot]   InlineSmallCode			[1000, 500-5000]	=   3376
[Hotspot]   LoopUnrollLimit			[50, 20-250]		=    140
[Hotspot]   LoopUnrollMin			[4, 0-20]		=      6
[Hotspot]   MinSurvivorRatio			[3, 3-48]		=     42
[Hotspot]   NewRatio				[2, 1-10]		=     10
[Hotspot]   TieredStopAtLevel			[4, 0-4]		=      4
[Hotspot]   TieredCompilation			[false, ]		=   true
[Hotspot]   AllowParallelDefineClass		[false, ]		=   true
[Hotspot]   AllowVectorizeOnDemand		[true, ]		=  false
[Hotspot]   AlwaysCompileLoopMethods		[false, ]		=   true
[Hotspot]   AlwaysPreTouch			[false, ]		=   true
[Hotspot]   AlwaysTenure			[false, ]		=  false
[Hotspot]   BackgroundCompilation		[true, ]		=   true
[Hotspot]   DoEscapeAnalysis			[true, ]		=   true
[Hotspot]   UseInlineCaches			[true, ]		=  false
[Hotspot]   UseLoopPredicate			[true, ]		=   true
[Hotspot]   UseStringDeduplication		[false, ]		=  false
[Hotspot]   UseSuperWord			[true, ]		=  false
[Hotspot]   UseTypeSpeculation			[true, ]		=  false

```
Along with the above tunables, other JVM options hardcoded are "-server -XX:MAXRamPercentage=70 -XX:+UseG1GC"
Quarkus tunable quarkus.datasource.jdbc.initial-size is set same as quarkus.datasource.jdbc.min-size to avoid min-size being picked with default when min-size is set higher than initial-size.
Hotspot tunable ParallelGCThreads set same as ConcGCThreads to avoid JVM exit when ParallelGCThreads are less than ConcGCThreads.

Baseline / Default configuration used is cpu request and limits set to 4 ; memory requests and limits set to 4096M ; JAVA_OPTIONS= "-server -XX:+UseG1GC"

- Trial 187 is considered as the best configuration in the experiment.
- Under 100 trials, trial 97 is considered as the best configuration in the experiment.
- Comparing the best configuration from autotune with the baseline, 
	- Response time reduced by ~80.12%

![Throughput](https://user-images.githubusercontent.com/17760990/151572920-231dc300-aac6-47be-9da1-7793fe03dc59.png)
![Response_time](https://user-images.githubusercontent.com/17760990/151572933-3ee5350c-0306-43ab-b6af-6b610b52db63.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/151572949-12bce231-d66b-4498-b542-3b660a473509.png)
![Cpu_usage](https://user-images.githubusercontent.com/17760990/151572964-707d781e-64e7-44c6-b66f-54ae0ed6b230.png)
![Memory_usage](https://user-images.githubusercontent.com/17760990/151572978-c8d41226-3d6c-48d3-9b4b-91e97cb4fda4.png)

![Response_time VS Trials](https://user-images.githubusercontent.com/17760990/151573077-32e3cf21-dee1-4f65-b8ee-c5bf5af13d2e.png)
![Max_Response_time VS Trials](https://user-images.githubusercontent.com/17760990/151573089-834c14cc-a2e8-41b1-901b-41e8962d4ab9.png)

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
