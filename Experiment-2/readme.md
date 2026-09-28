
# Cloud Computing Lab: Performance Analysis of Virtual Machines vs Containers

A comprehensive experimental performance evaluation comparing **Type-2 Virtual Machines (VMware Workstation)** with **OS-Level Containers (Docker)** under standardized, identical workloads for **CPU, Memory, and Disk I/O**.

---

## Table of Contents

1. Repository Structure
2. Project Abstract & Objectives
3. Experimental Environment & Specifications
4. Architecture Overview: VM vs Container
5. Prerequisites & Environment Setup
6. Experiment 1: CPU Performance Benchmark
7. Experiment 2: Memory Performance Benchmark & Resource Monitoring
8. Experiment 3: Disk I/O Performance Benchmark
9. Comprehensive Performance Comparison Table
10. Visual Performance Graphs
11. Key Findings & Conclusion

## 1. Project Abstract & Objectives

### Abstract

Virtualization is a key technology used in modern cloud computing environments. Two widely used approaches are:

1. **Hardware Virtualization (Virtual Machines):** Uses a hypervisor to create isolated virtual hardware environments in which complete guest operating systems can run independently.
2. **Operating System-Level Virtualization (Containers):** Uses kernel features such as namespaces and control groups (`cgroups`) to provide isolated application environments while sharing the host operating system kernel.

This project presents an experimental performance comparison between an **Ubuntu Virtual Machine running on VMware Workstation** and a **Docker Container running on an Ubuntu host system**. The evaluation focuses on CPU processing, memory performance, and storage I/O characteristics under standardized workloads.

### Objectives

- Evaluate **CPU computation throughput and latency** using `sysbench` prime-number calculations with both single-threaded and multi-threaded configurations.
- Measure **memory bandwidth and operation throughput** using the `sysbench memory` benchmark.
- Analyze **storage I/O performance** for sequential and random Read/Write workloads using `fio` with direct I/O (`--direct=1`).
- Monitor background system resource utilization using `vmstat`.
- Compare the measured performance results, calculate percentage differences, and analyze the virtualization overhead associated with both deployment models.

## 3. Experimental Environment & Specifications

| **Component**                 | **Specification**                                      |
| ----------------------------- | ------------------------------------------------------ |
| **Host Operating System**     | Windows 11 64-bit                                      |
| **Hypervisor**                | VMware Workstation                                     |
| **Guest Operating System**    | Ubuntu 24.04.4 LTS (Linux kernel 6.8.0-31-generic)     |
| **Virtual CPU Allocation**    | 2 vCPUs                                                |
| **RAM Allocation**            | 3.8 GiB DDR4                                           |
| **Storage Allocation**        | 40 GB Virtual Disk (SCSI `/dev/sda2`)                  |
| **Network Configuration**     | NAT Mode                                               |
| **Container Engine**          | Docker Engine 29.1.3 (build 29.1.3-0ubuntu3~24.04.2)  |
| **Benchmark Container Image** | `vm-container-benchmark` (Built on `ubuntu:24.04`)     |
| **Benchmarking Software**     | `sysbench 1.0.20`, `fio 3.36`, `sysstat/vmstat 12.6.1` |

## 5. Prerequisites & Environment Setup

### 5.1 Project Directory Structure & Hardware Logging

The benchmark workspace was created at `~/vm-vs-container-performance` with separate directories for documentation, raw benchmark results, processed CSV data, figures, scripts, and workload files.

```bash
mkdir -p ~/vm-vs-container-performance
cd ~/vm-vs-container-performance
mkdir -p docs results/raw results/processed results/figures scripts workloads

# Record system configuration
lscpu > docs/cpu-info.txt
free -h > docs/memory-info.txt
lsblk > docs/storage-info.txt
uname -a > docs/kernel-info.txt
```
