class Car:

    def __init__(self, car_model,no_of_gears,is_started,is_stopped):
        self.car_model = car_model
        self.no_of_gears = no_of_gears
        self.is_started = is_started
        self.is_stopped = is_stopped
        self.count=0

    def start(self):
        if self.is_started:
            print("Car is already started")
        else:
            print(f"Car with the model:{self.car_model} is started")
            self.is_started=True

    def stop(self):
        if self.is_started:
            print(f"Car with the model:{self.car_model} is stopped")
            self.is_started=False
        else:
            print("Car is already stopped")

    def change_gears(self):
        if self.is_started:
            if self.count < self.no_of_gears:
                self.count +=1 
                print(f"Car with the model:{self.car_model} changed the gears....{self.count}")
            else:
                print(f"Reached maximum gears....{self.count}")
        else:
            print("Car is stopped and cannot chamge the gears")

    def showinfo(self):
        print(f"{self.car_model}-Gears:{self.no_of_gears} Started:{self.is_started}  Added:{self.count}")

