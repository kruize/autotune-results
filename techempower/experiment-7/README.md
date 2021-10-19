## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the best configurations were run to reproduce the data and were be updated at [manuals](/manuals) dir

# Summary of data
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Container] cpuRequest				[None, 1-4]		=      4
[Container] memoryRequest			[None, 270M-4096M]	=  3319M
[Quarkus]   quarkus.thread-pool.core-threads	[1, 0-16]		=     19
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

- Fourth best configuration is considered as that configuration generated best response time along with lesser memory usage.
- Comparing the best configuration from autotune with the baseline, 
	- Throughput improved by ~6.85% 
	- Response time reduced by ~61.97%
	- Max response time increased by ~57.67%
	- Memory usage increased by ~164.9%

![Throughput](https://user-images.githubusercontent.com/17760990/137093662-bdc4658b-5990-4c43-aa56-73f71b64c98f.png)
![Response_time](https://user-images.githubusercontent.com/17760990/137093677-08e8d604-06c3-4cad-9f8b-2903f6a6814d.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/137093683-6c2124e7-0c27-40a8-9621-6b31fdcac6b5.png)
![Cpu_usage](https://user-images.githubusercontent.com/17760990/137093692-4a95c061-773a-4d80-898b-01e59627ad41.png)
![Memory_usage](https://user-images.githubusercontent.com/17760990/137093699-d32d6253-442e-46bb-aeda-03613386071a.png)

Note: Best configuration from multiple trials is picked based on having least response time with good throughput, no errors while running the load and ensuring the data has met the convergence criteria.
Each trial would have an individual configuartion based on the tunables.For information on the configuration of a particular trial, look into experiment-data.csv
