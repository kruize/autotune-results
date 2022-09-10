This directory contains the experiment results of the Renaissance Benchmark taking Prometheus Metrics.
# Prereuisites
To generate the results from the Renaissance Benchmark,we need to:  

 Firstly,install a kubernetes cluster(here minikube) and prometheus which can be done from the [Autotune Installation](https://github.com/kruize/autotune/blob/master/docs/autotune_install.md). 
 
 Secondly we need to clone the scripts required for running the renaissance benchmark which can be done from [Benchmarks](https://github.com/Prakalp23/benchmarks/tree/renaissance) repository.This contains a number of performance scripts that we have built for the Renaissance benchmark to collect the data from the Prometheus metrics and parse the results.
 Then,clone this repo for a reference to results and for getting the Python scripts to determine the accuracy of various ML algorithms on the dataset collected
 
 `git clone https://github.com/Prakalp23/autotune-results.git`
 
 You,also need to pull the docker image of renaissance onto your local system
 
  Download a driver (docker or podman)
 
 [Docker](https://docs.docker.com/engine/install/)
 
 [Podman](https://podman.io/getting-started/installation)
 
 Use the installed driver to pull the Renaissance docker image
 
 `podman pull prakalp23/renaissance1041:latest`
 
 `docker pull prakalp23/renaissance1041:latest`
 # For Running The Benchmark
 
 Start the minikube cluster,here we use podman as a driver,you can use a driver of your choice
 
 `minikube start --driver=podman`
 
 Then you need to head over to the directory where the performance scripts are located
 
 `cd ./perf`
 
 Then,you need to run the below command to trigger a run with the numbers of warmups measures and iterations being your choice,also the cpu and memory to be used can be set by the user
 
 `./renaissance-run.sh --clustertype=minikube -s localhost -e ./results -w 1 -m 1 -i 1 --iter=1 -r -n default  --cpureq=1.5 --memreq=3152M --cpulim=1.5 --memlim=3152M -b "page-rank" -g prakalp23/renaissance1041:latest -d 60`
 
 Here giving -g and the image name is a must as without that the run won't work.
 
 Renaissance is a collection of many different microbenchmarks such as page-rank,naive-bayes,log-regression more details can be found on [Renaissance Benchmark](https://github.com/renaissance-benchmarks/renaissance)
 
 To specify a particular benchmark such as naive-bayes in place of page-rank we can use
 
 `./renaissance-run.sh --clustertype=minikube -s localhost -e ./results -w 5 -m 5 -i 1 --iter=3 -r -n default   -b "naive-bayes" -g prakalp23/renaissance1041:latest -d 60`
 
 The details about each command such as -s -g can be found inside the scripts in benchmarks repo [Benchmarks](https://github.com/Prakalp23/benchmarks/tree/renaissance)
 
 After the results are generated use the featurizer.py to turn the data into a csv format and the model.py to perform Accuracy testing of ML Algorithms on the csv file
 
 To further understand the flow of the project,refer the presentation present on this repository.
 
 `
