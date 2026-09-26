# Part A: Performance Analysis Using Type-1 Hypervisor – Proxmox VE

## 1. Accessing Proxmox VE

Proxmox VE is a bare-metal Type-1 hypervisor that runs directly on physical server hardware and is managed remotely through its secure web-based management interface.

### Steps

1. Open a web browser on a client machine connected to the same network.

2. Enter the Proxmox VE web interface URL:

```text
https://PROXMOX_SERVER_IP:8006
```
If a self-signed SSL certificate warning is displayed, proceed by accepting the certificate.
Log in to the Proxmox VE dashboard using the assigned administrative credentials, including:
Username
Password
Authentication Realm

## 2. Creating the Virtual Machine

Create a new virtual machine on the Proxmox VE node using the **Create VM** option available in the top-right corner of the management interface.

Configure the virtual machine with the following settings:

### General

- **Node:** Select the designated Proxmox node (e.g., `pve`)
- **VM ID:** Assigned/Allocated ID
- **Name:** `CC-Experiment1-Type1`

### Operating System

- **Source:** Use CD/DVD Disk Image file (ISO)
- **Storage:** `local` / assigned ISO storage
- **ISO Image:** Select the Ubuntu 22.04 ISO
- **Guest OS Type:** Linux / Kernel 6.x – 2.6

### System

- **Graphics Card:** Default
- **Machine:** Default
- **BIOS:** Default (SeaBIOS)
- **SCSI Controller:** Default (VirtIO SCSI)

### Disk

- **Bus/Device:** SCSI / Default
- **Storage:** `local-lvm` / assigned storage
- **Disk Size:** `20 GB`

### CPU

- **Sockets:** `1`
- **Cores:** `2`
- **Total vCPU:** `2`
- **CPU Type:** Default (kvm64 / host)

### Memory

- **RAM:** `2048 MiB (2 GB)`

### Network

- **Bridge:** `vmbr0`
- **Model:** VirtIO (paravirtualized) / Default

### Confirmation

- Verify all the configured parameters before creating the virtual machine.
- Check that the VM settings match the required experimental configuration.
- Click **Finish** to provision the virtual machine.

---

## 3. Installing Ubuntu Operating System

1. Locate the newly created virtual machine (`CC-Experiment1-Type1`) from the datacenter inventory displayed on the left side of the Proxmox interface.

2. Select the VM and click **Start** to power it on.

3. Open the VM's **Console (noVNC)** option to access the graphical display through the browser.

4. Proceed with the standard Ubuntu installation process:

   - Select the required language and keyboard layout.
   - Choose the standard installation option.
   - Select the allocated **20 GB virtual disk** (`/dev/sda` or `/dev/vda`) as the installation destination.
   - Configure the timezone, system username, and password.
   - Allow the installation to complete and restart the virtual machine.

---

## 4. Verifying System Configuration

After Ubuntu has been installed, log in to the virtual machine and use the terminal to verify the allocated hardware resources and system configuration.

### Operating System and System Information

```bash
# Check operating system, kernel version, and system architecture
hostnamectl
# Display CPU architecture, socket information, and core allocation
lscpu
# Check available RAM and memory usage
free -h
# Display disk partitions and storage usage
df -h
# Monitor active processes and CPU utilization in real time
top
```
### Purpose of the Verification Commands

- `hostnamectl`: Confirms system hostname, operating system release, kernel, and hardware architecture.
- `lscpu`: Displays CPU architecture, core count (2 cores), socket configuration, and virtualization parameters.
- `free -h`: Confirms allocated RAM (~2.0 GiB) and swap usage.
- `df -h`: Confirms disk partitions and mounted virtual storage availability.
- `top`: Provides a real-time dynamic view of active system tasks, CPU utilization, and load averages.

## 5. Installing Sysbench

Update the Ubuntu package information and install the Sysbench benchmarking utility using the following commands:

```bash
sudo apt update
sudo apt install sysbench -y
sysbench --version
```

## 6. Running the CPU Performance Benchmark

```text
Execute the CPU benchmark using Sysbench with a prime-number calculation limit of 20,000.

sysbench cpu --cpu-max-prime=20000 run

After the benchmark finishes, record the following performance values:

- Total execution time
- Total number of events
- Events completed per second (throughput)
- Latency measurements: minimum, average, and maximum
```

---

## 7. Resource Monitoring

```text
Open the virtual machine's summary page in the Proxmox VE management interface:

Datacenter → Proxmox Node → Virtual Machine (CC-Experiment1-Type1) → Summary

Monitor and record the resource-related metrics associated with the virtual machine and its underlying host environment.

The following parameters should be observed:

- CPU utilization percentage
- Memory allocation and current consumption
- Network I/O throughput through vmbr0
- Virtual disk read/write throughput
```

---

## 8. Implementation Evidances (Outputs)
Screenshot 1: Proxmox Dashboard
