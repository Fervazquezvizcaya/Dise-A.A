
def candles(height: list[int]) -> int:
    """
    Args:
        height (list[int]): The candles heights.
    
    Returns:
        int: The number of candles that are tallest
    """
    
    max_height = max(height)  # Encuentra la altura máxima
    #Se utiliza max(height) por practicidad pero tambien se podria usar un ciclo que es lo que hace la instruccion max(height)
    """
    if not height:
        return 0  # Maneja el caso donde la lista está vacía

    max_height = height[0]  # Inicializa max_height con el primer elemento
    for h in height:  # Recorre cada altura en la lista
        if h > max_height:
            max_height = h  # Actualiza max_height si se encuentra un valor mayor
    
    codigo que ejemplifica lo que hace la instruccion max()
    """
    count_max_height = 0      # Inicializa el contador
    
    """
    Ciclo que cuenta cuántas veces aparece la altura máxima,
    igual se puede usar un counter y nos ahorramos la estructura four,
    pero ocupare el four para poderce implementar mejor en pseuodocodigo y Diagrama F.
    """
    for h in height:
        if h == max_height:
            count_max_height += 1
    
    # count_max_height = height.count(max_height): esta linea sustituiria el ciclo for 
    
    return count_max_height  # Regresa el contador




if __name__ == "__main__":
    print(candles([4, 4, 1, 3])) # 2
    print(candles([1, 1, 1, 1, 1])) # 5
    print(candles([5, 3, 1, 3, 5, 3, 1, 3, 5])) # 3
    print(candles([10000, 10001, 10002, 10002, 10000])) # 2
    print(candles([999, 1000, 99, 912, 100])) # 1
