# PimPam Reproducibility Guide
This repo aims at reproducing the results of [PimPam](https://people.iiis.tsinghua.edu.cn/~gaomy/pubs/slides/pimpam.sigmod24.slides.pdf). The official implementation of PimPam is available at this [repo](https://github.com/tsinghua-ideal/PimPam). The following instruction will guide you through the process of reproducing the following experiments in the paper:
1. Comparison of the overall performance of PimPam with GraphPi. (Fig 11)
1. Comparison of the preprocessing cost of PimPam with GraphPi. (Tab 3)
1. Breakdown analysis of the impacts of adaptive thread collaboration and load-aware task assignment. (Fig 12)
1. Accuracy of the predict model for task assignment. (Fig 13)
1. Performance impact of dynamic bitmap. (Fig 14)
1. Proof of the performance gain is not worth the cost of a more accurate model. (Tab 4)
1. Searching for the optimal threshold for adaptive thread collaboration. (Fig 15)
1. Comparison to Pangolin (a GPU-based framekwork). (Fig 16)
1. Comparison to Khuzdul (a distributed framework). (Fig 17)

## Environment
PimPam and GraphPi runs on UPMEM. Here is the hardware and software configuration used in the paper:
- CPU:  two Intel Xeon Silver 4216 processors with 64 physical cores in total, running at 2.1GHz.
- Traditional Memory: 4 DIMMs of traditional DDR4 memory, with 256GB capacity and 38.4GB/s bandwidth in total.
- DPU: 2560 DPUs, running at 350MHz.
- PIM Memory: 20 DDR4-2400 DIMMs, with 160GB capacity, containing the DPUs mentioned above.
- OS: Debian GNU/Linux 10 with kernel version 4.19
- Host compiler: GCC 8.3.0
- DPU support: UPMEM SDK 2023.2.0 based on clang 12.0.0.

Since UPMEM isn't equipped with GPUs, Pangolin is run on a separate server with the following configuration:
- CPU: two Intel Xeon Gold 5218R processors (40 physical cores in total)
- GPU: four NVIDIA RTX 3090 GPUs, each with 24GB memory
- CUDA: 12.2

Khuzdul is run on a cluster of 8 servers with the following configuration:
- two AMD EPYC 7H12 64-core processors running at 1.5GHz each with 512GB memory
- 100Gb Ethernet interconnection with TCP/IP protocol

## Experiments
### Running PimPam Experiments
The following should be done on UPMEM.
1. Prepare data: Run `make data_pimpam`.
1. Make sure the system is setup properly: `cd PimPam && make test`.
The last line of the output should be `All fine` and the answer should be `608389`.
To pass the test, UPMEM SDK should be installed properly before this. If not, follow the instructions in its [website](https://sdk.upmem.com/2023.2.0/01_Install.html).
If you have installed the SDK but the test still fails, there are two possible causes. First, check whether you have access to DPUs (in which case allocation will fail). Second, there are bad DPUs. Find and disable them. You may uncomment line 9 of `PimPam/include/common.h` and rerun `make test`. The macro `CPU_RUN` will run the pattern matching on CPU to check which DPU produces the wrong answer.
1. Run the experiments: `cd .. && make run_pimpam`. It may take a few hours.

### Running GraphPi Experiments
The following should be done on UPMEM.
1. Make sure MPI is installed. If not, run `sudo apt-get install mpich`.
1. Run the experiments: `make run_graphpi`.

### Running Pangolin Experiments
The following should be done on a server with GPUs.
1. Make sure the correct `CUDA_ARCH` has been specified at line 7 of `pangolin/src/pangolin/common.mk`. See also line 14 to 24 of `pangolin/src/common.mk`.
1. Run the experiments: `make run_pangolin`.

### About Khuzdul
Since Khuzdul is not open sourced, we obtain the code directly from the author to conduct our experiments. However, we are not authorized to publish the code in this repo. Instead, we provide the results measured before in order to reproduce the figure. Some of the experiments overlap with their original paper, where the statistics support the results we have obtained. Furthermore, comparison to distributed system is only a minor part of our paper, so we believe this is acceptable.

## Collecting Results
The results produced by the experiments above are stored in the `results` directory. Since the experimetns are run on different machines, you should manually combine the `results` directories from each machine into one before proceeding.

## Reproducing Figures and Tables
Now we assume all the results have been stored in one place. Then run `make all`. This will produce all the figures and tables mentioned above in `reproduce` directory. If you are able to run only part of the experiments, then you can optionally reproduce some of the figures or tables. Here are the dependencies.
1. `make fig11`: pimpam and graphpi
1. `make tab3`: pimpam and graphpi
1. `make fig12`: pimpam
1. `make fig13`: pimpam
1. `make fig14`: pimpam
1. `make tab4`: pimpam
1. `make fig15`: pimpam
1. `make fig16`: pimpam and pangolin
1. `make fig17`: pimpam

Note that the figures and tables are generated using `matplotlib` and `pandas`. Make sure they are installed before running the commands above.
