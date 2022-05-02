## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the best configuration were run to reproduce the data and were updated at [manuals](manuals) dir

# Goal of the experiment:
- Minimize transaction response time.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Container] 	      cpuRequest             [None, 1-8]             =    7.8
[Container]           memoryRequest          [None, 270M-4096M]      =  2598M
[Hotspot]             GCPolicy		     [ , ]		     =  ParallelGC

```
The above experiment is to find which GCPolicy is suitable for the available cpu and memory. Tunables used for this experiment are cpu, memory and GCPolicy. Requests and limits of cpu and memory resources is set to same.

- Trial 66 is considered as the best configuration in the experiment.
- ParallelGC is considered more suitable for the experiment.


From [experiment-data.csv](experiment-data.csv), below are the best configurations from each GCPolicy.
```
Trial	THROUGHPUT	RESPONSE_TIME	MAX_RESPONSE_TIME	RESPONSE_TIME_50p	RESPONSE_TIME_95p	RESPONSE_TIME_97p	CPU_REQ	MEM_REQ	GC_POLICY	total_trials_with_GC
29	37394.4		7.98641		1523.609537		3.33647			45.7232			51.4843			7.8	 1675M 	 UseG1GC 		6
66	40933.5		4.47496		1453.52874		1.48211			16.7181			28.6172			7.8	 2598M 	 UseParallelGC 		55
69	39149.2		9.23887		1222.022798		4.15719			35.3883			40.8779			8	 2429M 	 UseSerialGC 		8
40	33543.6		8.86025		4858.555167		3.69143			49.3371			56.0952			8	 2698M 	 UseShenandoahGC 	9
61	32114		9.6061		1522.434658		3.68283			56.908			63.0062			7.8	 2628M 	 UseZGC 		6

```

Below are the charts of Throughput and Response_time of GC Policy which has best configuration.

![Throughput Vs GCPolicy](https://user-images.githubusercontent.com/17760990/166127781-f989bdeb-1f72-4c43-b0c3-2fcad387df39.png)
![Response_time Vs GCPolicy](https://user-images.githubusercontent.com/17760990/166127788-f85d3fac-9c17-41dc-a02d-6fad903d2a3f.png)



### Configuration Details:
```
- JDK                   eclipse-temurin:17
- Quarkus               1.13.2.F
```
- Machine: 
```
  - Server:  openshift cluster v4.8.13
    Master nodes	3
    Worker nodes	3
    CPU per node	56
    Memory per node	512G

  - Client: RHEL 8.3
    CPU  		64
    Memory 		512G  
```
- Load: 
```
 	Users :		512
	Threads :	56
```


Note: Best configuration from multiple trials is picked based on having least response time with good throughput, no errors while running the load and ensuring the data has met the convergence criteria.
Each trial would have an individual configuartion based on the tunables.For information on the configuration of a particular trial, look into experiment-data.csv
