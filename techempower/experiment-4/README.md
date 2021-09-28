## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the top 5 best configuration were run to reproduce the data and were be updated at [manuals](/manuals) dir

# Summary of data
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

- Fourth best configuration is considered as that configuration generated best response time along with lesser memory usage.
- Comparing the best configuration with the baseline (where no configuration is set), 
	- Throughput improved by ~18.96% 
	- Response time reduced by ~60%
	- Max response time increased by ~23%
	- CPU usage increased by ~89%
	- Memory usage increased by ~45%


Note: Best configuration from multiple trials is picked based on having least response time, no errors while running the load and ensuring the data has met the convergence criteria.
Each trial would have an individual configuartion based on the tunables.For information on the configuration of a particular trial, look into experiment-data.csv
