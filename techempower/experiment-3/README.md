## All the experiments in this folder were run on shared infrastructure and require to be validated on a dedicated infrastructure. Manual runs are being run to reproduce the data with the best configuration which will be updated at [manuals](/manuals) dir

# Summary of data
- Min response time is observed with following configuration
```
   [Layer]            [Tunable]              [Default, Range]      Best Config
[Quarkus]   quarkus.thread-pool.core-threads   [1, 3-24]           =    15
[Quarkus]   quarkus.thread-pool.queue-size     [unbounded, 0-1000] =   748
[Quarkus]   quarkus.datasource.jdbc.min-size   [0, 2-10]           =     2
[Quarkus]   quarkus.datasource.jdbc.max-size   [20, 20-48]         =    44
[Hotspot]   maxinlinelevel                     [9, 9-50]           =    16
[Container] cpuRequest                         [None, 1-3.2]       =  2.47
[Container] memoryRequest                      [None, 270M-1024M]  =  900M
```

Note: Best configuration from multiple trials is picked based on having least response time, no errors while running the load and ensuring the data has met the convergence criteria.
Each trial would have an individual configuartion based on the tunables.For information on the configuration of a particular trial, look into experiment-data.csv
