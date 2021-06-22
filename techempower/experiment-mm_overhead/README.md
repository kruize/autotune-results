## All the experiments in this folder were run on shared infrastructure and require to be validated on a dedicated infrastructure.

# Experiment to measure the overhead of micrometer(MM) with TFB-Quarkus.
Representation of metrics in csv files can be seen at benchmarks [README](https://github.com/kruize/benchmarks/tree/master/techempower/README.md)

# Summary 

![Response time](https://user-images.githubusercontent.com/17760990/122808792-f173a400-d2ea-11eb-8971-2b82381f722d.png)

Above graph shows with MM enabled, response time has increased by ~14% when compared against with No MM.

![Memory Usage](https://user-images.githubusercontent.com/17760990/122808797-f3d5fe00-d2ea-11eb-80be-616303c8c345.png)

Above graph shows with MM enabled, memory usage has increased by ~3.6% when compared against with No MM.

Note: The same numbers were not reproducible all the time in the shared infrastructure. But, confirmed with [extra](/extras) runs, there is a similar overhead like mentioned in summary.
