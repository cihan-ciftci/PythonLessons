# ORNEK 1
"""
for i in range(5):
    for j in range(i+1):
        print("* ", end="")
    print()
"""
# ORNEK 2
"""
for i in range(5):
    for j in range(5-i):
        print("* ", end="")
    print()
"""
# ORNEK 3
"""
for i in range(5):
    for j in range(5):
        print("* ", end="")
    print()
"""
# ORNEK 4
"""
for i in range(5):
    for j in range(5 - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()
"""

# ORNEK 5
n = 9
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i-1):
        print("* ", end="")
    print()
