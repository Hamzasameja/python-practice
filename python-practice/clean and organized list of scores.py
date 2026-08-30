scores = [85, 92, 85, 78, 92, 100, 78, 85]

print("Original scores:")
print(scores)

unique_scores = list(set(scores))
unique_scores.sort()
print("\nUnique scores (sorted):")
print(unique_scores)

most_common = max(unique_scores, key=lambda score: scores.count(score))
print("\nMost repeated score: " + str(most_common) + " (appears " + str(scores.count(most_common)) + " times)")