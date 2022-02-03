## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the best configuration were run to reproduce the data and were updated at [manuals](manuals) dir

# Goal of the experiment:
- Minimize transaction response time.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Quarkus]   quarkus.thread-pool.core-threads	[1, 0-32]		=      4
[Quarkus]   quarkus.thread-pool.queue-size	[unbounded, 0-10000]	=   1820
[Quarkus]   quarkus.datasource.jdbc.min-size	[0, 1-12]		=     11
[Quarkus]   quarkus.datasource.jdbc.max-size	[12, 12-90]		=     39
[Hotspot]   FreqInlineSize			[325, 325-500]		=    364
[Hotspot]   MaxInlineLevel			[9, 9-50]		=     35
[Hotspot]   MinInliningThreshold		[250, 0-200]		=     95
[Hotspot]   CompileThreshold			[1500, 1000-10000]	=   3180
[Hotspot]   CompileThresholdScaling		[1, 1-15]		=    6.3
[Hotspot]   ConcGCThreads			[0, 0-8]		=      8
[Hotspot]   InlineSmallCode			[1000, 500-5000]	=   1840
[Hotspot]   LoopUnrollLimit			[50, 20-250]		=    138
[Hotspot]   LoopUnrollMin			[4, 0-20]		=      7
[Hotspot]   MinSurvivorRatio			[3, 3-48]		=     18
[Hotspot]   NewRatio				[2, 1-10]		=      2
[Hotspot]   TieredStopAtLevel			[4, 0-4]		=      2
[Hotspot]   TieredCompilation			[false, ]		=  false
[Hotspot]   AllowParallelDefineClass		[false, ]		=  false
[Hotspot]   AllowVectorizeOnDemand		[true, ]		=  false
[Hotspot]   AlwaysCompileLoopMethods		[false, ]		=  false
[Hotspot]   AlwaysPreTouch			[false, ]		=  false
[Hotspot]   AlwaysTenure			[false, ]		=  false
[Hotspot]   BackgroundCompilation		[true, ]		=   true
[Hotspot]   DoEscapeAnalysis			[true, ]		=  false
[Hotspot]   UseInlineCaches			[true, ]		=   true
[Hotspot]   UseLoopPredicate			[true, ]		=   true
[Hotspot]   UseStringDeduplication		[false, ]		=  false
[Hotspot]   UseSuperWord			[true, ]		=  false
[Hotspot]   UseTypeSpeculation			[true, ]		=  false

```
The above experiment uses constant container tunables. The configuration used is cpu request and limit set to 4 ; memory request and limit set to 4096M.
Along with the above tunables, other JVM options hardcoded are "-server -XX:MAXRamPercentage=70 -XX:+UseG1GC"
Quarkus tunable quarkus.datasource.jdbc.initial-size is set same as quarkus.datasource.jdbc.min-size to avoid min-size being picked with default when min-size is set higher than initial-size.
Hotspot tunable ParallelGCThreads set same as ConcGCThreads to avoid JVM exit when ParallelGCThreads are less than ConcGCThreads.

Baseline / Default configuration used is cpu request and limit set to 4 ; memory request and limit set to 4096M ; JAVA_OPTIONS= "-server -XX:+UseG1GC"

- Trial 136 is considered as the best configuration in the experiment.
- Comparing the best configuration from autotune with the baseline, 
	- Response time reduced by ~81.9%
	- 78% of the requests took < 1ms with Autotune Config; where as only 5% of requests took < 1ms with default config(represented in graph "% Requests Served") 

![Throughput](https://user-images.githubusercontent.com/17760990/151574878-4857838d-66ce-464c-94c4-3bffe6ee0cb4.png)
![Response_time](https://user-images.githubusercontent.com/17760990/151574891-76e04cf0-5eeb-44a9-9723-b1abb819d5ec.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/151574896-09e85502-ac1d-4ca7-ab03-66d92d7ac325.png)
![Cpu_usage](https://user-images.githubusercontent.com/17760990/151574699-f9c8c74e-72ab-4b9e-8af2-854b196208f7.png)
![Memory_usage](https://user-images.githubusercontent.com/17760990/151574715-ac997e4e-882b-4554-bf98-c87aa803e1e4.png)

![Percentile_Response_time](https://user-images.githubusercontent.com/17760990/152111671-6c4d5feb-960c-4119-abb9-8c2a2a58da6f.png)
![Percentage Requests Served(within responsetime bucket)](https://user-images.githubusercontent.com/17760990/152286076-87605eac-8504-44a4-9ded-249955649e0a.png)

The above percentile data and Requests Served graphs are based on [manuals](manuals)/set-2 experiments.


![Response_time VS Trials](https://user-images.githubusercontent.com/17760990/151575084-ef6e2d39-a6a1-4d9b-a0f3-8d003eaf5160.png)
![Max_Response_time VS Trials](https://user-images.githubusercontent.com/17760990/151575096-4836455a-2bd4-4c4b-a753-365310558bc8.png)

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
