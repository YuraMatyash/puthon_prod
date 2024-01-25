def route_info(setl):
    if ('distance' in setl) and (type(setl['distance']) == int):
        return f"Distance to your destination is {setl['distance']}"

    if ('speed' and 'time' in setl):
        return f"Speed to your destination is {setl['speed'] * setl['time']}"

    return f"No information about your destination"

print(route_info({'distance' : 3445}))

print(route_info({'speed' : 220, 'time' : 3}))

print(route_info({'my_sed' : 35}))
