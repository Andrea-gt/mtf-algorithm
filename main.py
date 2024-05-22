"""
    Andrea Ximena Ramirez Recinos
    Carne 21874
    Universidad del Valle de Guatemala
    Analisis y Diseno de Algoritmos
    Ciclo I, 2024

    MTF Algorithm Worksheet
"""

from mtf_algorithm import mtf_algorithm

separator = "═" * 52
values = [0, 1, 2, 3, 4]

print(f"{separator}")
print("Results for Question 1:")
print(f"{separator}")
requests = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
mtf = mtf_algorithm(values, requests)
mtf.moveToFront()

print(f"\n{separator}")
print("Results for Question 2:")
print(f"{separator}")
requests = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
mtf = mtf_algorithm(values, requests)
mtf.moveToFront()

print(f"\n{separator}")
print("Results for Question 3 (Best Case):")
print(f"{separator}")
requests = [0] * 20
mtf = mtf_algorithm(values, requests)
mtf.moveToFront()

print(f"\n{separator}")
print("Results for Question 4 (Worst Case):")
print(f"{separator}")
requests = [4, 3, 2, 1, 0] * 4
mtf = mtf_algorithm(values, requests)
mtf.moveToFront()

print(f"\n{separator}")
print("Results for Question 5:")
print(f"{separator}")
requests = [2] * 20
mtf = mtf_algorithm(values, requests)
mtf.moveToFront()

print(f"\n{separator}")
requests = [3] * 20
mtf = mtf_algorithm(values, requests)
mtf.moveToFront()

print(f"\n{separator}")
print("Results for Question 6 (Best Case):")
print(f"{separator}")
requests = [0] * 20
mtf = mtf_algorithm(values, requests)
mtf.IMTF()

print(f"\n{separator}")
print("Results for Question 6 (Worst Case):")
print(f"{separator}")
requests = [4, 3, 2, 1, 0] * 4
mtf = mtf_algorithm(values, requests)
mtf.IMTF()