## All the experiments in this folder were run on a dedicated infrastructure.

# Experiment to measure the overhead of micrometer(MM) with TFB-Quarkus.
Representation of metrics in csv files can be seen at benchmarks [README](https://github.com/kruize/benchmarks/tree/master/techempower/README.md)

# Summary 

![Response time](https://user-images.githubusercontent.com/17760990/126127840-8d0eb366-92b3-477b-ab4d-6f8371a8cd0d.png)

Above graph shows with MM enabled, response time has increased by ~2% when compared against with No MM.

![Memory Usage](https://user-images.githubusercontent.com/17760990/126127938-42309c68-8b0c-46cf-b9c6-ba9fc74111fa.png)

Above graph shows with MM enabled, memory usage has increased by ~4% when compared against with No MM.

Note: The above experiment data is based on the configuration mentioned in [benchmark.yaml](./benchmark.yaml). The CPU usage with the configuration is ~0.7 core. We had issues increasing the CPU usage without any blocked requests in TFB application. Need to debug to find the cause, and the overhead data will be updated with increased CPU usage as well.
