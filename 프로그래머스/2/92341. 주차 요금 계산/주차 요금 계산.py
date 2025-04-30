import math


def transform_minute(start_time, end_time):
    hour, minute = start_time.split(":")
    start_time = int(hour) * 60 + int(minute)
    hour, minute = end_time.split(":")
    end_time = int(hour) * 60 + int(minute)
    return end_time - start_time


def solution(fees, records):
    answer = []
    car_dict = {}
    basic_time, basic_fee, unit_time, unit_fee = fees
    times = {}
    fees_dict = {}
    for r in records:
        time, car, status = r.split()
        if car not in times:
            times[car] = 0
        if car not in car_dict and status == "IN":
            car_dict[car] = time
        elif car in car_dict and status == 'OUT':
            in_time = car_dict.pop(car)
            out_time = time
            during = transform_minute(in_time, out_time)
            times[car] += during
    for k in car_dict:
        times[k] += transform_minute(car_dict[k], "23:59")

    for t in times:
        if times[t] <= basic_time:
            fees_dict[t] = basic_fee
        else:
            fees_dict[t] = basic_fee + math.ceil((times[t] - basic_time) / unit_time) * unit_fee

    keys = list(fees_dict.keys())

    keys.sort()

    return [fees_dict[k] for k in keys]