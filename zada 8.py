def apdate_car_info(**car):
    car['is_availabl'] = True
    return car

print(apdate_car_info(brend = 'BMW', praise = 10000))
