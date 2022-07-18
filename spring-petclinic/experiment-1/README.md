## All the experiments in this folder were run on dedicated infrastructure.

# Goal of the experiment:
- Maximize Throughput.

- For details on slo and benchmark, look into [benchmark.yaml](benchmark.yaml)

# Summary of data

### Configuration Details:
```
- JVM                   openj9-0.21.0
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


Note: Best configuration from multiple trials is picked based on high throughput, no errors while running the load and ensuring the data has met the convergence criteria.
Each trial would have an individual configuartion based on the tunables.For information on the configuration of a particular trial, look into experiment-data.csv
