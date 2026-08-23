A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

intersection = len(A & B)
union = len(A | B)
similarity = intersection / union

print(f"Jaccard similarity = {intersection} / {union} = {similarity:.4f}")
