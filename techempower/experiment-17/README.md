## All the experiments in this folder were run on dedicated infrastructure.

# Goal of the experiment:
- Maximize Throughput.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data

This experiment uses constant container tunables. The configuration used is cpu request and limit set to 4 ; memory request and limit set to 4096M.
Along with the above tunables, other JVM options hardcoded are "-server -XX:MAXRamPercentage=70".
Quarkus tunable quarkus.datasource.jdbc.initial-size is set same as quarkus.datasource.jdbc.min-size to avoid min-size being picked with default when min-size is set higher than initial-size.
Hotspot tunable ParallelGCThreads set same as ConcGCThreads to avoid JVM exit when ParallelGCThreads are less than ConcGCThreads.

- The baseline and autotune configurations from the experiment is updated at [config.csv](config.csv). 
- This experiment uses Optuna TPE_multivariate algorithm and Quarkus version 2.9.1.F.
- Trial 104 is considered as the best configuration in the experiment.
- Comparing the best configuration from autotune with the baseline, 2% improvement in Throughput is observed.

![Throughput](plots/Throughput.png)

![CPU](plots/cpu.png)

![Memory](plots/memory.png)

- Tunable Importance plot shows the importance of each tunable in an experiment. 
- TieredCompilation had the highest importance followed by TieredStopAtLevel, NewRatio and gcpolicy tunables.

![Tunable_Importance](plots/tunable_importance.png)


- Optimization History plots shows the objective value for all the trials and the best value in an experiment.

![Optimization History](plots/optimization_history.png)


- Contour plots shows the parameter relationship.
- Below contour plot shows the relation between TieredStopAtLevel and NewRatio 
- This plot shows, NewRatio tunable gave the best objective value when NewRatio is >=6 and TieredStopAtLevel>2 most of the times. The ligher area in the plot indicates high objective value. 
- The default values of NewRatio is 2 and TieredStopAtLevel is 4. 
- Although, the best configuration of the experiment picked NewRatio as 10 and TieredStopAtLevel as 2, there are other combinations which can help tune the experiments.
- This is one of the parameter relation generated in this experiment.

![NewRatio vs TieredStopAtLevel_Contour](contour_tieredstopatlevel_newratio.png)


- Parallel Coordinate plot shows the high-dimensional parameter relationships in an experiment.
- Below plot shows the relationship with all the tunables available in an experimnt.

![Parallel_Coordinate for all tunables](parallel_coordinate.png)


![Throughput Vs Trials](plots/throughputVStrials.png)


### Configuration Details:
```
- JVM                   openjdk:11.0.6
- Quarkus               2.9.1.F
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
