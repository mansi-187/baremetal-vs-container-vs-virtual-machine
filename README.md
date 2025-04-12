# Cloud Computing - Resource Benchmarking on Containers, VMs, and Bare Metal

## Overview
This project is part of CS553 Cloud Computing coursework, focusing on benchmarking and analyzing the performance of system resources — CPU, Memory, and Disk — across different environments:
- Bare Metal (Host Machine)
- Docker Containers
- Virtual Machines (VM)

The objective is to evaluate and compare the efficiency of each environment while running specific workloads and resource-intensive scripts.

---

## Technologies & Tools Used
- Bash Scripting
- Docker Containers
- Virtual Machines (VM)
- Linux Shell
- Performance Benchmarking

---

## Directory Structure

```
cs553-spring2024-hw2/
│
├── CPU/
│  ├── cpubare.sh            # CPU test on Bare Metal
│  ├── cpucontainer.sh       # CPU test inside Docker Container
│  └── cpuvm                 # CPU test on Virtual Machine
├── Memory/
│   ├── membare.sh          # Memory test on Bare Metal
│   ├── memcontainer.sh     # Memory test inside Docker Container
│   ├── memvm.sh            # Memory test on Virtual Machine
│   └── efficiency.sh       # Memory Efficiency Analysis Script
├── Disk/
│   └── diskcontainer.sh    # Disk Benchmarking Script
│
├── README.md               # Project Documentation
├── readme.txt              # Instructions
└── cloud hw2.pdf           # Assignment Report

```

