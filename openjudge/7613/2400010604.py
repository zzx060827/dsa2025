n = int(input())
samples = []
for _ in range(n):
    samples.append(float(input()))

if n <= 2:
    print("Invalid input")
else:
    samples_sorted = sorted(samples)
    valid_samples = samples_sorted[1:-1]
    average = sum(valid_samples) / len(valid_samples)
    max_error = max(abs(sample - average) for sample in valid_samples)
    print("{0:.2f} {1:.2f}".format(average, max_error))