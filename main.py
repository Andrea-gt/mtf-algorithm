from mtf_algorithm import mtf_algorithm

# Case 1
values = [0, 1, 2, 3, 4]
requests = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
mtf = mtf_algorithm(values, requests)
mtf.moveToFront()