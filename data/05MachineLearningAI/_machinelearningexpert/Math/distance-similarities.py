
class Metrics():
    def euclidean_distance(X, Y):
        return round(sum([(x - y)**2 for x, y in zip(X, Y)])**0.5, 4)

    def manhattan_distance(X, Y):
        return round(sum([abs(x - y) for x, y in zip(X, Y)]), 4)

    def cosine_similarity(X, Y):
        dot_product = sum(x * y for x, y in zip(X, Y))
        magnitude_X = sum(x**2 for x in X)**0.5
        magnitude_Y = sum(y**2 for y in Y)**0.5
        return round(dot_product / (magnitude_X * magnitude_Y), 4)

    def jaccard_similarity(X, Y):
        intersection = len(set(X) & set(Y))
        union = len(set(X) | set(Y))
        return round(intersection / union, 4)

    def distances_and_similarities(X, Y):
        similarity = Metrics()
        return [
            similarity.euclidean_distance(X, Y),
            similarity.manhattan_distance(X, Y),
            similarity.cosine_similarity(X, Y),
            similarity.jaccard_similarity(X, Y)]

X = [1, 3, 4, 5]
Y = [7, 6, 3, 1]
print(compute_metrics(X, Y))
