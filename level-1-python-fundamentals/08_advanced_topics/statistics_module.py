"""
    Statistics module -> mean, median, mode, standard deviation
"""

import statistics

### Avearge student score - Education, HR Performance
scores = [85, 90, 78, 92, 88]
print("Mean:", statistics.mean(scores))
print("median:", statistics.median(scores))

### Detecting outliers - Fraud detection, sensor error correction
data = [10, 12, 14, 13, 100]
mean = statistics.mean(data)
stdev = statistics.stdev(data)
outliers = [x for x in data if abs(x-mean) < 2  * stdev]
print("Outliers:", outliers)

### Predicting trends - Business forecasting inventory planning
sales = [100, 120, 130, 150, 170]
growth_rate = statistics.mean([sales[i+1] - sales[i] for i in range(len(sales)-1)])
print("Average growth rate:", growth_rate)


