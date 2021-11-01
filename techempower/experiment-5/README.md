## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the top 5 best configuration were run to reproduce the data and were be updated at [manuals](manuals) dir

# Goal of the experiment:
- Minimize transaction response time.
- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Container] cpuRequest				[None, 1-2]		=   1.99
[Container] memoryRequest			[None, 270M-4096M]	=  2996M
[Quarkus]   quarkus.thread-pool.core-threads	[1, 0-16]		=     10
[Quarkus]   quarkus.thread-pool.queue-size	[unbounded, 0-10000]	=   2850
[Quarkus]   quarkus.datasource.jdbc.min-size	[0, 1-6]		=      6
[Quarkus]   quarkus.datasource.jdbc.max-size	[20, 6-40]		=     40
[Hotspot]   FreqInlineSize			[325, 325-500]		=    371
[Hotspot]   MaxInlineLevel			[9, 9-50]		=     12
[Hotspot]   MinInliningThreshold		[250, 0-200]		=    111
[Hotspot]   CompileThreshold			[1500, 1000-10000]	=   7001
[Hotspot]   CompileThresholdScaling		[1, 1-15]		=  13.35
[Hotspot]   ConcGCThreads			[0, 0-4]		=      2
[Hotspot]   InlineSmallCode			[1000, 500-5000]	=    646
[Hotspot]   LoopUnrollLimit			[50, 20-250]		=     95
[Hotspot]   LoopUnrollMin			[4, 0-20]		=     10
[Hotspot]   MinSurvivorRatio			[3, 3-48]		=     38
[Hotspot]   NewRatio				[2, 1-10]		=      3
[Hotspot]   TieredStopAtLevel			[4, 0-4]		=      4
[Hotspot]   TieredCompilation			[false, ]		=   true
[Hotspot]   AllowParallelDefineClass		[false, ]		=  false
[Hotspot]   AllowVectorizeOnDemand		[true, ]		=   true
[Hotspot]   AlwaysCompileLoopMethods		[false, ]		=  false
[Hotspot]   AlwaysPreTouch			[false, ]		=   true
[Hotspot]   AlwaysTenure			[false, ]		=  false
[Hotspot]   BackgroundCompilation		[true, ]		=   true
[Hotspot]   DoEscapeAnalysis			[true, ]		=   true
[Hotspot]   UseInlineCaches			[true, ]		=   true
[Hotspot]   UseLoopPredicate			[true, ]		=   true
[Hotspot]   UseStringDeduplication		[false, ]		=   true
[Hotspot]   UseSuperWord			[true, ]		=   true
[Hotspot]   UseTypeSpeculation			[true, ]		=   true

```
Along with the above tunables, other JVM options hardcoded are "-server -XX:MAXRamPercentage=70 -XX:+UseG1GC"
Quarkus tunable quarkus.datasource.jdbc.initial-size is set same as quarkus.datasource.jdbc.min-size to avoid min-size being picked with default when min-size is set higher than initial-size.
Hotspot tunable ParallelGCThreads set same as ConcGCThreads to avoid JVM exit when ParallelGCThreads are less than ConcGCThreads.

Baseline / Default configuration used is cpu request and limits set to 2 ; memory requests and limits set to 4096M ; JAVA_OPTIONS= "-server -XX:+UseG1GC"

- Trial 99 is considered as the best configuration from the experiment.
- Comparing the best configuration from autotune with the baseline, 
	- Throughput improved by ~9.19% 
	- Response time reduced by ~56.37%
	- Max response time increased by ~19.15%
	- Memory usage increased by ~58.33%

![Throughput](https://user-images.githubusercontent.com/17760990/136068973-02a00b0a-2f77-4852-8db7-36233ad0b048.png)
![Response_time](https://user-images.githubusercontent.com/17760990/136068987-45242d37-28c3-414b-9687-95a8dcbe8284.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/139278129-b1ca4be8-9dd9-4c19-bd38-f82158fa325d.png)
![Cpu_usage](https://user-images.githubusercontent.com/17760990/136069011-182dc00e-3ed9-49ce-994f-d49650dd25c9.png)
![Memory_usage](https://user-images.githubusercontent.com/17760990/136069022-aca0da8a-ff7d-4660-92ff-e1cad22ddd0f.png)

![Response_time VS Trials](https://user-images.githubusercontent.com/17760990/139203111-86b3ef92-b63f-44aa-93d4-51272315c5d6.png)
![Max_Response_time VS Trials](https://user-images.githubusercontent.com/17760990/139203143-ecc942ac-d723-4ea1-8678-100403e182ac.png)
In the above graphs, trial 0 is the data of default configuration which is considered as baseline.

### Configuration Details:
- JVM                   openjdk:11.0.6
- Quarkus               1.13.2.F
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
