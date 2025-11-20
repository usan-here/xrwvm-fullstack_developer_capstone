from .models import CarMake, CarModel

def initiate():
    # Create a CarMake if not exists
    make, created = CarMake.objects.get_or_create(
        name="Toyota",
        defaults={"description": "Reliable Japanese cars"}
    )

    # Create CarModels
    CarModel.objects.get_or_create(
        car_make=make,
        name="Corolla",
        type="SEDAN",
        dealer_id=1,
        year=2020,
    )

    CarModel.objects.get_or_create(
        car_make=make,
        name="RAV4",
        type="SUV",
        dealer_id=1,
        year=2023,
    )

    CarModel.objects.get_or_create(
        car_make=make,
        name="Prius Wagon",
        type="WAGON",
        dealer_id=1,
        year=2019,
    )
