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

The CPU benchmark is executed from within the Ubuntu virtual machine on both hypervisor platforms using the following command:

```bash
sysbench cpu --cpu-max-prime=20000 run
