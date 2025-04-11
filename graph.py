import matplotlib.pyplot as plt

data = {
    (1, 1, 1): 234.5293,
    (1, 1, 4): 233.7171,
    (1, 1, 16): 234.5327,
    (1, 4, 1): 230.8971,
    (1, 4, 4): 233.3242,
    (1, 4, 16): 243.0156,
    (1, 16, 1): 240.4330,
    (1, 16, 4): 235.2364,
    (1, 16, 16): 237.1109,
    (4, 1, 4): 414.4754,
    (4, 1, 16): 395.3577,
    (4, 4, 1): 385.2164,
    (4, 4, 4): 395.6956,
    (4, 4, 16): 420.1295,
    (4, 16, 1): 413.9354,
    (4, 16, 4): 383.4907,
    (4, 16, 16): 413.2005,
    (16, 1, 1): 395.5901,
    (16, 1, 4): 416.6924,
    (16, 1, 16): 417.9447,
    (16, 4, 1): 391.2336,
    (16, 4, 4): 391.6298,
    (16, 4, 16): 392.4688,
    (16, 16, 1): 384.1184,
    (16, 16, 4): 381.2296,
    (16, 16, 16): 381.8630,
}

# Extracting thread configurations and time values
threads = [str(config) for config in data.keys()]
times = list(data.values())

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.bar(threads, times, color='skyblue')
plt.xlabel('Thread Configurations')
plt.ylabel('Time')
plt.title('Execution Time vs Thread Configurations')
plt.xticks(rotation=90)
plt.tight_layout()

# Saving the plot as an image file
plt.savefig('execution_time_vs_thread_configurations.png')
plt.show()
