## All the experiments in this folder were run on dedicated infrastructure. 

# Goal of the experiment:
- Minimize transaction response time.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data
- Min response time is observed with following configuration
```
[Layer]        [Tunable]                [Default, Range]      Best Config
[Hotspot]	GCPolicy		[ , ]		      =  ParallelGC

```
This experiment is to find the suitable GC policy with Java 11 for a specific cpu and memory resources. Requests and limits of cpu and memory resources is set to same.
All the experiments use "-server -XX:MaxRAMPercentage=70"

Multiple small experiments with 10 trials were done as part of this experiment with following cpu and memory resources.
- 4 cores - 3072 M. Data for this configuration is at [experiment-data-4c-3G.csv](experiment-data-4c-3G.csv)
- 1 core  - 3072 M. Data for this configuration is at [experiment-data-1c-3G.csv](experiment-data-1c-3G.csv)
- 4 cores - 8192 M. Data for this configuration is at [experiment-data-4c-8G.csv](experiment-data-4c-8G.csv)
- 1 core  - 8192 M. Data for this configuration is at [experiment-data-1c-8G.csv](experiment-data-1c-8G.csv)

With all the above configurations, ParallelGC showed good Throughput and Response time.
Below are the charts of Throughput, Response_time Vs GCPolicy for different cpu-memory configurations.

Below is the data for each GCPolicy with 4c-3G configuration.
```
Trial	THROUGHPUT	RESPONSE_TIME	MAX_RESPONSE_TIME    RESPONSE_TIME_50p	RESPONSE_TIME_95p	RESPONSE_TIME_97p    CPU_REQ	MEM_REQ GC_POLICY
20	19950.80	13.94		1799.65			3.55		81.47			85.63			4	 3072M 	 UseG1GC 
14	23558.90	7.75		2212.95			2.17		68.18			77.11			4	 3072M 	 UseParallelGC 
3	20034.30	18.08		2407.42			4.84		81.39			85.71			4	 3072M 	 UseSerialGC 
6	19379.30	15.97		2447.45			3.92		84.12			87.74			4	 3072M 	 UseShenandoahGC 
```
Below is the data for each GCPolicy with 1c-3G configuration.
```
Trial	THROUGHPUT	RESPONSE_TIME	MAX_RESPONSE_TIME    RESPONSE_TIME_50p	RESPONSE_TIME_95p	RESPONSE_TIME_97p    CPU_REQ	MEM_REQ	GC_POLICY
17	5394.34		23.68		7194.99			0.80		132.48			138.74			1	 3072M 	 UseG1GC 
6	6125.29		18.43		6837.51			0.77		107.07			116.62			1	 3072M 	 UseParallelGC 
12	5521.98		29.29		5526.04			0.89		136.00			165.17			1	 3072M 	 UseSerialGC 
3	5099.04		27.64		6663.64			0.85		186.89			197.93			1	 3072M 	 UseShenandoahGC 

```

Below is the data for each GCPolicy with 4c-8G configuration. In 10 trials, it didn't pick G1GC.
```
Trial   THROUGHPUT      RESPONSE_TIME   MAX_RESPONSE_TIME    RESPONSE_TIME_50p  RESPONSE_TIME_95p       RESPONSE_TIME_97p    CPU_REQ    MEM_REQ GC_POLICY
9	20258.40	13.67		2125.64			3.59		81.21			85.43			4	 8192M 	 UseG1GC 
14	22227.40	9.53		2211.32			2.55		73.97			80.72			4	 8192M 	 UseParallelGC 
10	20064.70	17.45		2019.37			4.66		80.46			85.13			4	 8192M 	 UseSerialGC 
6	20463.70	12.88		2463.77			3.20		80.43			85.14			4	 8192M 	 UseShenandoahGC 
```

Below is the data for each GCPolicy with 1c-8G configuration. In 10 trials, it didn't pick SerialGC.
```
Trial   THROUGHPUT      RESPONSE_TIME   MAX_RESPONSE_TIME    RESPONSE_TIME_50p  RESPONSE_TIME_95p       RESPONSE_TIME_97p    CPU_REQ    MEM_REQ GC_POLICY
20	5344.06		25.57		5543.04			0.85		111.08			187.61			1	 8192M 	 UseG1GC 
19	6088.81		22.50		5398.98			0.79		107.65			135.15			1	 8192M 	 UseParallelGC 
1	5530.11		28.76		5777.47			0.90		133.43			185.76			1	 8192M 	 UseSerialGC 
11	5352.46		23.45		5701.98			0.79		133.74			187.65			1	 8192M 	 UseShenandoahGC 
```

### Configuration Details:
```
- JDK                   eclipse-temurin:11
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

