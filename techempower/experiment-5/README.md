## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the top 5 best configuration were run to reproduce the data and were be updated at [manuals](/manuals) dir

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

- Fourth best configuration is considered as that configuration generated best response time along with lesser memory usage.
- Comparing the best configuration with the baseline (where no configuration is set), 
	- Throughput improved by ~6.66% 
	- Response time reduced by ~132.9%
	- Max response time increased by ~38.4%
	- Memory usage increased by ~32%

![Throughput](https://user-images.githubusercontent.com/17760990/135136932-4fd12d4e-1660-4bf2-a7fb-ccf1210af1bb.png)
![Response_time](https://user-images.githubusercontent.com/17760990/135136951-d8b1ee87-999f-447b-babf-d0c0ff747695.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/135136959-d5d2db56-8943-40f5-9a2c-187505212109.png)
![cpu_usage](https://user-images.githubusercontent.com/17760990/135136975-525ea091-bf0a-4aa8-95f1-ca3d56dd5d0d.png)
![memory_usage](https://user-images.githubusercontent.com/17760990/135136986-67981ac5-4ea9-49d9-a3dd-746dd0e08488.png)

Note: Best configuration from multiple trials is picked based on having least response time, no errors while running the load and ensuring the data has met the convergence criteria.
Each trial would have an individual configuartion based on the tunables.For information on the configuration of a particular trial, look into experiment-data.csv
