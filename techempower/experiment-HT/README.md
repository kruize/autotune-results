## All the experiments in this folder were run on a dedicated infrastructure.

# Experiment to measure the overhead of hyper threading with TFB-Quarkus.
Representation of metrics in csv files can be seen at benchmarks [README](https://github.com/kruize/benchmarks/tree/master/techempower/README.md)

# Summary
With HT disabled, following are the observations when compared against HT enabled data.
- Throughput improved by ~6.47%
- Response time reduced by ~12%
- Max response time reduced by 3 times.

![Throughput](https://user-images.githubusercontent.com/17760990/135137239-ee2c614c-70d9-4bd2-92e0-3c2dc2ac6856.png)
![Response_time](https://user-images.githubusercontent.com/17760990/135137252-29e3d2bf-2821-4590-a8a9-53add36f11ce.png)
![Max_response_time](https://user-images.githubusercontent.com/17760990/135137272-822d8563-2ac5-4f1a-b265-b6d6f2e199a9.png)
![CPU_usage](https://user-images.githubusercontent.com/17760990/135137299-d9567eff-b968-4b0f-8dde-7b2ff81780a0.png)
![Memory_usage](https://user-images.githubusercontent.com/17760990/135137312-1d1b5cd0-a22a-41bf-ab58-5a313f68fd1a.png)

Note: The above experiment data is based on the configuration mentioned in [benchmark.yaml](./benchmark.yaml). 
