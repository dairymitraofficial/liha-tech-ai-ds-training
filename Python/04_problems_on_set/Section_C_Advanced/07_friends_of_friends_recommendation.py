friends_A = {'B', 'C'}
friends_B = {'A', 'D'}
friends_C = {'A', 'D', 'E'}

recommendations = (friends_B | friends_C) - friends_A - {'A'}

print("Recommendations for A =", recommendations)
