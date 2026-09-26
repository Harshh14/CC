# Hypervisor Performance Comparison

## Overview

This section provides an empirical comparison of CPU performance between a **Type-1 bare-metal hypervisor (Proxmox VE)** and a **Type-2 hosted hypervisor (VMware Workstation)**.

Both virtual environments were configured with the same hardware resources and software setup: **Ubuntu 24.04, 2 vCPU, 2 GB RAM, and 20 GB virtual disk**. The CPU performance was evaluated using the Sysbench workload with a prime-number limit of `20000`.

---

## Performance Comparison Table

| **Performance Metric** | **Type-1: Proxmox VE** | **Type-2: VMware Workstation** | **Performance Difference / Observation** |
|---|---:|---:|---|
| **Hypervisor Architecture** | **Type-1 (Bare-Metal)** | **Type-2 (Hosted)** | Direct hardware access compared with an additional host OS layer |
| **Guest Operating System** | **Ubuntu 24.04 LTS** | **Ubuntu 24.04 LTS** | Same operating system |
| **Allocated vCPU** | **2 vCPU** | **2 vCPU** | Same allocation |
| **Allocated RAM** | **2 GB** | **2 GB** | Same allocation |
| **Allocated Disk** | **20 GB** | **20 GB** | Same allocation |
| **Total Execution Time** | **10.0005 s** | **10.0006 s** | Fixed 10-second benchmark window |
| **Total Events Processed** | **17,494** | **7,077** | **+147.2% more events** with Proxmox VE |
| **Events per Second (Throughput)** | **1,749.16** | **707.43** | **2.47× higher throughput** with Proxmox VE |
| **Average Latency** | **0.57 ms** | **1.41 ms** | **59.6% lower latency** with Proxmox VE |

---
## Graphical Comparsion 
<img width="1635" height="962" alt="image" src="https://github.com/user-attachments/assets/a673fc5e-6e46-4758-ae25-5b590a7b5238" />
