def taxi_cost(trip_length: int, waiting_time: int = 0) -> int | None:
    """Вычисляет и возвращает стоимость поездки на такси, если вычисление невозможно возвращает None"""
    
    base_cost = 80
    trip_price = trip_length / 150 * 6
    price_waiting_time = waiting_time * 3
    fine = 80
    if trip_length >= 0 and waiting_time >= 0:
        price = base_cost + trip_price + price_waiting_time
        if trip_length == 0:
            price += fine
            
        return round(price)
        
    return print("None")
        
# >>> taxi_cost(1190)
# 128
# >>> taxi_cost(900, 3)
# 125
# >>> taxi_cost(0, 3)
# 169
# >>> taxi_cost(-1206, -56)
# None