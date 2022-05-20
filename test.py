from iteration_utilities import deepflatten


def plainlist(listdata: list): 
    try:
        result = list(deepflatten(listdata));
    except TypeError :
        print("Error en formato de la lista")
    else:
        print(result)


# [1, [2, [3, [4, 5]]]]
# [6, [1, [2, 3], 4], 5]
# [[[1, 2,], 3], 4, 5]


plainlist(5)
plainlist([5,7])
plainlist([[[1, 2,], 3], 4, 5])
