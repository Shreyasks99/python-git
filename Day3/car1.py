class Car:

    def __init__(self, regno, no_of_gears):
        self.regno = regno
        self.no_of_gears = no_of_gears
        self.is_started = False
        self.count=0

    def start(self):
        if self.is_started:
            print("Car is already started")
        else:
            print(f"Car with the regno:{self.regno} is started")
            self.is_started=True

    def stop(self):
        if self.is_started:
            print(f"Car with the regno:{self.regno} is stopped")
            self.is_started=False
        else:
            print("Car is already stopped")
    def change_gears(self):
        if self.is_started:
            if self.count < self.no_of_gears:
                self.count +=1 
                print(f"Car with the regno:{self.regno} changed the gears....{self.count}")
            else:
                print(f"Reached maximum gears....{self.count}")
        else:
            print("Car is stopped and cannot chamge the gears")

    def showinfo(self):
        print(f"{self.regno}-Started:{self.is_started} Gears:{self.no_of_gears} Added:{self.count}")

