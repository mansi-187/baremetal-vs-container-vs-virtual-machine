# Distributed Sorting & Performance Analysis using Hadoop and Spark

## Overview
This project focuses on performance analysis of distributed sorting algorithms using Hadoop MapReduce and Apache Spark. The objective was to benchmark and compare their performance on large datasets in a cloud environment.

---

## Technologies Used
- Hadoop MapReduce
- Apache Spark
- HDFS (Hadoop Distributed File System)
- Yarn
- Cloud-based Virtual Machines
- Linux Environment

---

## Project Objectives
- Setup Hadoop Cluster in cloud
- Configure Hadoop & Yarn for distributed processing
- Perform sorting using:
  - Hadoop Sort
  - Spark Sort
- Compare performance across varying:
  - Dataset sizes: 16GB, 32GB, 64GB
  - VM configurations: RAM & Instance Types
- Measure execution time of sorting tasks
- Analyze performance impact based on resources

---

## Files Included
| File | Description |
|------|-------------|
| core-site.xml | Hadoop core configuration |
| hdfs-site.xml | HDFS configuration |
| mapred-site.xml | MapReduce configuration |
| yarn-site.xml | Resource management configuration |
| pom.xml | Maven configuration for Hadoop programs |
| vault64GB.log | Execution log for performance |

---

## Execution Steps
```bash
# Run Hadoop Sort
hadoop jar hadoop-mapreduce-examples.jar sort /input /output

# Run Spark Sort
spark-submit --class SortApp your_spark_sort_script.py

