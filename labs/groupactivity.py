class Car:
  def __init__(self, brand, model, year, mileage, price):
      self.brand = brand
      self.model = model
      self.year = year
      self.mileage = mileage
      self.price = price

  def display_info(self):
    print(f"Brand: {self.brand}")
    print(f"Model: {self.model}")
    print(f"Year: {self.year}")
    print(f"Mileage: {self.mileage}")
    print(f"Price: {self.price}")

  def set_price(self, price):
    self.price = price

  def get_price(self):
    return self.price


class Sedan(Car):
  def __init__(self, brand, model, year, mileage, price, fuel, comfort):
      super().__init__(brand, model, year, mileage, price)
      self.fuel = int(fuel)
      self.comfort = 1  # comfort levels 1-3


class SUV(Car):
  def __init__(self, brand, model, year, mileage, price, fwd, offroad):
      super().__init__(brand, model, year, mileage, price)
      self.fwd = False
      self.offroad = False


class Truck(Car):
  def __init__(self, brand, model, year, mileage, price, load, hitch):
      super().__init__(brand, model, year, mileage, price)
      self.load = load
      self.hitch = hitch

civic = Sedan("Honda", "Civic", 2020, 20000, 8000, "gasoline", "very comfortable")
civic.display_info()
civic.update_price(7000)


silverado = Truck("Chevrolet", "Silverado", 2024, 5000, 50000, 3200, True)
silverado.display_info()
silverado.update_price(48000)