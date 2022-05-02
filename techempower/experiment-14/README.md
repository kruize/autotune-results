## All the experiments in this folder were run on dedicated infrastructure. Manual runs for the best configuration were run to reproduce the data and were updated at [manuals](manuals) dir

# Goal of the experiment:
- Minimize transaction response time.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data
- Min response time is observed with following configuration
```
[Layer]        [Tunable]                [Default, Range]      Best Config
[Hotspot]	GCPolicy		[ , ]		      =  ParallelGC

```
This experiment is to find the suitable GC policy for a specific cpu and memory resources. Requests and limits of cpu and memory resources is set to same.
All the experiments use "-server -XX:MaxRAMPercentage=70"

Multiple small experiments with 10 trials were done as part of this experiment with following cpu and memory resources.
- 4 cores - 3072 M. Data for this configuration is at [experiment-data-4c-3G.csv](experiment-data-4c-3G.csv)
- 1 core  - 3072 M. Data for this configuration is at [experiment-data-1c-3G.csv](experiment-data-1c-3G.csv)
- 4 cores - 8192 M. Data for this configuration is at [experiment-data-4c-8G.csv](experiment-data-4c-8G.csv)
- 1 core  - 8192 M. Data for this configuration is at [experiment-data-1c-8G.csv](experiment-data-1c-8G.csv)

With all the above configurations, ParallelGC showed good Throughput and Response time.
Below are the charts of Throughput, Response_time Vs GCPolicy for different cpu-memory configurations.
![Throughput Vs GCPolicy](https://user-images.githubusercontent.com/17760990/166085514-3a27e5a0-175c-4e1c-80d3-bc0d9f2d70bc.png)
![Response_time Vs GCPolicy](https://user-images.githubusercontent.com/17760990/166085519-81d2720b-c75b-4422-a1b5-62d9d193c143.png)

Below is the data for each GCPolicy with 4c-3G configuration.
```
Trial	THROUGHPUT	RESPONSE_TIME	MAX_RESPONSE_TIME    RESPONSE_TIME_50p	RESPONSE_TIME_95p	RESPONSE_TIME_97p    CPU_REQ	MEM_REQ GC_POLICY
6	20855.2		12.123		1809.035562		3.04707		79.6204			84.4543			4	 3072M 	 UseG1GC 
9	22787.4		9.8592		1905.754714		2.60115		74.2921			80.9008			4	 3072M 	 UseParallelGC 
7	20348		17.4423		1894.450675		4.43591		80.6273			85.2399			4	 3072M 	 UseSerialGC 
1	18628.4		16.348		2002.802079		3.84892		85.2428			89.1064			4	 3072M 	 UseShenandoahGC 
3	19380.9		15.6317		1966.780059		3.73461		83.7862			87.3885			4	 3072M 	 UseZGC 
```
Below is the data for each GCPolicy with 1c-3G configuration.
```
Trial	THROUGHPUT	RESPONSE_TIME	MAX_RESPONSE_TIME    RESPONSE_TIME_50p	RESPONSE_TIME_95p	RESPONSE_TIME_97p    CPU_REQ	MEM_REQ	GC_POLICY
1	5630.98		24.9629		4800.089152		0.796642	126.945			184.508			1	 3072M 	 UseG1GC 
2	6243.38		17.0966		3996.111767		0.806451	107.855			134.698			1	 3072M 	 UseParallelGC 
9	5581.72		22.6722		4242.027281		0.894095	140.995			191.508			1	 3072M 	 UseSerialGC 
10	5057.51		23.9023		4307.152263		0.817002	152.38			190.929			1	 3072M 	 UseShenandoahGC 
6	5355.62		23.8701		4918.530671		0.809669	109.248			181.624			1	 3072M 	 UseZGC 
```

Below is the data for each GCPolicy with 4c-8G configuration. In 10 trials, it didn't pick G1GC.
```
Trial   THROUGHPUT      RESPONSE_TIME   MAX_RESPONSE_TIME    RESPONSE_TIME_50p  RESPONSE_TIME_95p       RESPONSE_TIME_97p    CPU_REQ    MEM_REQ GC_POLICY
5	22387.5		7.95889		1802.014751		2.14989		68.2646			77.2492			4	 8192M 	 UseParallelGC 
1	20459.5		15.7529		2129.329775		3.99129		79.7467			84.5801			4	 8192M 	 UseSerialGC 
6	20217.2		14.5761		2654.251279		3.73036		82.7317			86.6216			4	 8192M 	 UseShenandoahGC 
3	20316.9		13.9452		1749.218772		3.40838		81.819			85.858			4	 8192M 	 UseZGC 
```

Below is the data for each GCPolicy with 1c-8G configuration. In 10 trials, it didn't pick SerialGC.
```
Trial   THROUGHPUT      RESPONSE_TIME   MAX_RESPONSE_TIME    RESPONSE_TIME_50p  RESPONSE_TIME_95p       RESPONSE_TIME_97p    CPU_REQ    MEM_REQ GC_POLICY
1	5750.9		19.717		4494.694224		0.840208	133.599			190.149			1	 8192M 	 UseG1GC 
7	6235.2		17.2235		4003.897704		0.749258	105.335			132.198			1	 8192M 	 UseParallelGC 
9	5530.69		18.0135		4605.443452		0.72012		106.817			134.356			1	 8192M 	 UseShenandoahGC 
2	5539.67		22.4398		4366.767055		0.763493	107.236			133.794			1	 8192M 	 UseZGC 
```

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

