def city_generator():
    yield ('London')
    yield ('Paris')
    yield ('Zurich')
    yield ('Amsterdam')
    yield ('Barcelona')
    yield ('Santorini')

city = city_generator()
print(next(city))
print(next(city))
print(next(city))
print(next(city))