# Performance Evaluation of Type-1 and Type-2 Hypervisors

---

## 1. Title

**Performance Evaluation of Type-1 and Type-2 Hypervisors: Proxmox VE (Type-1) vs VMware Workstation (Type-2)**

---

## 2. Objective

The purpose of this experiment is to create virtual machines with equivalent configurations on a Type-1 hypervisor (Proxmox VE) and a Type-2 hypervisor (VMware Workstation). Their CPU performance is then measured and compared using the Sysbench benchmarking tool under similar virtual machine conditions.

---

## 3. Hypervisors Used

| Part | Hypervisor | Hypervisor Type | Architecture / Deployment |
|---|---|---|---|
| Part A | Proxmox VE | Type-1 (Bare-Metal) | Installed and executed directly on the physical hardware |
| Part B | VMware Workstation | Type-2 (Hosted) | Operates as an application on top of a host operating system |

---

## 4. Common Virtual Machine Configuration

To make the comparison consistent and fair, both virtual machines are configured with equivalent hardware resources and software settings.

| Parameter | Configuration |
|---|---|
| Operating System | Ubuntu 22.04 LTS (64-bit) |
| Processor Allocation | 2 vCPU (1 Socket, 2 Cores) |
| Memory Allocation | 2 GB (2048 MB) |
| Virtual Disk Allocation | 20 GB |
| Benchmark Suite | Sysbench (CPU Benchmark) |

---

## 5. Benchmark Command

```bash
sysbench cpu --cpu-max-prime=20000 run
```
The CPU benchmark is executed from within the Ubuntu virtual machine on both hypervisor platforms using the same benchmark configuration

---

## 6. Experiment Structure

The experiment is organized into the following sections to carry out the hypervisor performance evaluation systematically:

- **Part A – Proxmox VE:**  
  Creation and configuration of the virtual machine on Proxmox VE, followed by Ubuntu installation, system-resource verification, and execution of the CPU benchmark.

- **Part B – VMware Workstation:**  
  Setup of an equivalent virtual machine using VMware Workstation, followed by Ubuntu installation, configuration verification, and execution of the same CPU benchmark.

- **Performance Comparison:**  
  The benchmark results obtained from both hypervisors are collected and compared using appropriate tables and graphical representations.

- **Analysis and Discussion:**  
  The observed performance values are examined to identify differences between the Type-1 and Type-2 virtualization environments and to understand their effect on CPU benchmark performance.

---

# PART A: Performance Analysis Using Type-1 Hypervisor – Proxmox VE

1. Accessing the Proxmox VE Web Interface
2. Accessing the Proxmox VE Login Page
3. Logging in to Proxmox VE
4. Understanding the Proxmox VE Interface
5. Creating a Virtual Machine in Proxmox VE
6. Configuring General Settings
7. Configuring the Operating System
8. Configuring System Settings
9. Configuring Virtual Disk
10. Configuring CPU Resources
11. Configuring Memory Resources
12. Configuring Network
13. Confirming Virtual Machine Configuration
14. Verifying the Created Virtual Machine
15. Starting the Virtual Machine
16. Opening the Virtual Machine Console
17. Installing Ubuntu Operating System
18. Verifying the Virtual Machine
19. Analyzing CPU Configuration
20. Analyzing Memory Configuration
21. Analyzing Disk Configuration
22. Monitoring System Resource Utilization
23. Installing Sysbench
24. Performing CPU Performance Analysis
25. Monitoring VM Resources from Proxmox VE

## PART B: PERFORMANCE ANALYSIS USING TYPE-2 HYPERVISOR – VMWARE WORKSTATION

1. Launching VMware Workstation
2. Selecting the Virtual Machine Configuration
3. Selecting the Guest Operating System Installation Method
4. Selecting the Guest Operating System
5. Naming the Virtual Machine
6. Configuring Virtual Disk Capacity
7. Customizing Virtual Machine Hardware
8. Completing Virtual Machine Creation
9. Starting the Virtual Machine
10. Installing Ubuntu Operating System
11. Restarting the Virtual Machine
12. Verifying the Virtual Machine Configuration
13. Verifying CPU Configuration
14. Verifying Memory Configuration
15. Verifying Disk Configuration
16. Monitoring System Resource Utilization
17. Installing Sysbench
18. Performing CPU Performance Analysis
19. Monitoring Resource Utilization in VMware Workstation

## Performance Visualization

The following graphs provide a visual representation of the CPU benchmark results obtained from Proxmox VE and VMware Workstation.

### CPU Throughput Comparison

The chart below compares the number of events processed per second by the two hypervisor environments.

<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/d961263c-5596-46c2-ba7e-016bc223f441" />


### CPU Latency Comparison

The following chart compares the latency measurements, including minimum, average, 95th percentile, and maximum latency values.
<img width="1600" height="960" alt="image" src="https://github.com/user-attachments/assets/ff915252-eb83-4cac-80c8-7858177d1989" />

---
