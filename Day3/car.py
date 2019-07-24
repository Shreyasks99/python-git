from car1 import Car

bmw = Car("KA013060", 4)
omni = Car("KA013061",4)
nano = Car("KA013062",5)
city = Car("KA013063",6)
jazz = Car("KA013064",5)
bmw.start()
omni.start()
nano.start()
bmw.change_gears()
nano.change_gears()

lst = [bmw,omni,nano,city,jazz]

for car in lst:
    car.showinfo()
    c = len(list(filter(lambda x: x.is_started and x.count == 0,lst)))
print(f"No.of Cars which is started but no gears are added:{c}")