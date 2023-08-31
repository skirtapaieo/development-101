def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    data.sort()
    middle_index = len(data) // 2
    if len(data) % 2 == 0:
        return (data[middle_index - 1] + data[middle_index]) / 2
    else:
        return data[middle_index]

def calculate_mode(data):
    counts = {num: data.count(num) for num in data}
    return max(counts.keys(), key=lambda x: counts[x])

def calculate_sample_variance(data, mean):
    return sum((num - mean) ** 2 for num in data) / (len(data) - 1)

def calculate_standard_deviation(sample_variance):
    return sample_variance ** 0.5

def calculate_confidence_interval(mean, standard_deviation, sample_size):
    standard_error = standard_deviation / (sample_size ** 0.5)
    margin_of_error = 1.96 * standard_error
    return [mean - margin_of_error, mean + margin_of_error]

def get_statistics(input_list):
    sorted_input = sorted(input_list)
    mean = calculate_mean(sorted_input)
    median = calculate_median(sorted_input)
    mode = calculate_mode(sorted_input)
    sample_variance = calculate_sample_variance(sorted_input, mean)
    sample_standard_deviation = calculate_standard_deviation(sample_variance)
    mean_confidence_interval = calculate_confidence_interval(mean, sample_standard_deviation, len(sorted_input))
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval
    }
