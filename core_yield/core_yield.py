def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

x = city_generator()

print x.next()
print x.next()
print x.next()
print x.next()