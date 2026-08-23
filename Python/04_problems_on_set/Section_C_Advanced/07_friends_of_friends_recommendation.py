A_friends = {'B', 'C'}
B_friends = {'A', 'D'}
C_friends = {'A', 'D', 'E'}

recommendations = B_friends | C_friends

recommendations = recommendations - A_friends
recommendations.remove('A')

print("Recommendations for A =", recommendations)