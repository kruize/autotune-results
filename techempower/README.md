## Tunables used for these experiments:
```
[Container Layer] cpuRequest [None]				- CPU request for a pod.
[Container Layer] memoryRequest [None]				- Memory request for a pod.
[Quarkus Layer]   quarkus.thread-pool.core-threads [1] 		- The core thread pool size. This number of threads will always be kept alive.
[Quarkus Layer]   quarkus.thread-pool.queue-size [unbounded]	- The queue size.
[Quarkus Layer]   quarkus.datasource.jdbc.min-size [0]		- The datasource pool minimum size.
[Quarkus Layer]   quarkus.datasource.jdbc.max-size [20]		- The datasource pool maximum size.
[Hotspot Layer]   FreqInlineSize [325]				- The maximum bytecode size of a frequent method to be inlined.
[Hotspot Layer]   MaxInlineLevel [9] 				- The maximum number of nested calls that are inlined.
[Hotspot Layer]   MinInliningThreshold [250]  			- The minimum invocation count a method needs to have to be inlined. 
[Hotspot Layer]   CompileThreshold [1500] 			- The number of interpreted method invocations before (re-)compiling.
[Hotspot Layer]   CompileThresholdScaling [1]			- Factor to control when first compilation happens.
[Hotspot Layer]   ConcGCThreads [0]   				- Number of threads concurrent gc will use.
[Hotspot Layer]   InlineSmallCode [1000] 			- Only inline already compiled methods if their code size is less than this.
[Hotspot Layer]   LoopUnrollLimit [50] 				- Unroll loop bodies with node count less than this.
[Hotspot Layer]   LoopUnrollMin [4]    				- Minimum number of unroll loop bodies before checking progress of rounds of unroll,optimize,..
[Hotspot Layer]   MinSurvivorRatio [3] 				- Minimum ratio of young generation/survivor space size.
[Hotspot Layer]   NewRatio [2]  				- Ratio of old/new generation sizes.
[Hotspot Layer]   TieredStopAtLevel [4]  			- Stop at given compilation level.
[Hotspot Layer]   TieredCompilation [false]  			- Enable tiered compilation.
[Hotspot Layer]   AllowParallelDefineClass [false]   		- Allow parallel defineClass requests for class loaders registering as parallel capable.
[Hotspot Layer]   AllowVectorizeOnDemand [true]  		- Globally supress vectorization set in VectorizeMethod.
[Hotspot Layer]   AlwaysCompileLoopMethods [false] 		- When using recompilation, never interpret methods containing loops.
[Hotspot Layer]   AlwaysPreTouch [false]			- Force all freshly committed pages to be pre-touched.
[Hotspot Layer]   AlwaysTenure [false]       			- Always tenure objects in eden (ParallelGC only).
[Hotspot Layer]   BackgroundCompilation [true]  		- A thread requesting compilation is not blocked during compilation.
[Hotspot Layer]   DoEscapeAnalysis [true]   			- Perform escape analysis.
[Hotspot Layer]   UseInlineCaches [true]   			- Use Inline Caches for virtual calls.
[Hotspot Layer]   UseLoopPredicate [true]   			- Generate a predicate to select fast/slow loop versions.
[Hotspot Layer]   UseStringDeduplication [false]  		- Use string deduplication.
[Hotspot Layer]   UseSuperWord [true]    			- Transform scalar operations into superword operations.
[Hotspot Layer]   UseTypeSpeculation [true]    			- Speculatively propagate types from profiles.

```

## Summary of Experiments
- will be updated soon 

## List of Experiments:

```
experiment-1	Minimize `transaction_response_time` on shared hardware with 7 tunables.
experiment-2	Minimize `transaction_response_time` on shared hardware with 7 tunables.
experiment-3	Minimize `transaction_response_time` on shared hardware with 7 tunables.
experiment-4	Minimize `transaction_response_time` on dedicated hardware and 32c-8GB MW cluster with 31 tunables.
experiment-5	Minimize `transaction_response_time` on dedicated hardware and 2c-4GB MW cluster with 31 tunables.
experiment-6	Minimize `transaction_response_time` on dedicated hardware and 4c-4GB MW cluster with 31 tunables.
experiment-7	Maximize `(1.25 * throughput) - (1.5 * transaction_response_time) - (0.25 * max_response_time)` on dedicated hardware and 4c-4GB MW cluster with 31 tunables.
experiment-8	Maximize `(( throughput / transaction_response_time) /  max_response_time) * 100` on dedicated hardware and 4c-4GB MW cluster with 31 tunables.
experiment-9	Minimize `transaction_response_time` on dedicated hardware and 2c-4GB SLP cluster with 31 tunables.
experiment-10   Maximize `( 125 * throughput ) / ( 150 * transaction_response_time ) / ( (25 * max_response_time )/100 )` on dedicated hardware and 4c-4GB SLP cluster with 31 tunables.
experiment-11	Maximize `( 125 * throughput ) / ( 150 * transaction_response_time ) / ( (25 * max_response_time )/100 ) / ( 1 + ( thrpt_ci * rsp_ci ))` on dedicated 4c-4GB SLP cluster with 31 tunables.
experiment-12	Maximize `( 125 * throughput ) / ( 150 * transaction_response_time ) / ( (25 * max_response_time )/100 )` with constant container tunables on dedicated 4c-4GB SLP cluster with 29 tunables.
```
