import random
import pandas as pd
from driver import Driver

def create_driver_database(num_drivers=100):
    drivers = []

    for _ in range(num_drivers):
        is_rookie = random.choice([True, False])
        driver = Driver(is_rookie=is_rookie)

        driver_data = {
            "Name": driver.name,
            "Country": driver.country,
            "Age": driver.age,
            "Peak": driver.peak,
            "Rookie": driver.is_rookie,
            "Start": driver.skills['start'],
            "Concentration": driver.skills['concentration'],
            "Overtaking": driver.skills['overtaking'],
            "Experience": driver.skills['experience'],
            "Speed": driver.skills['speed'],
            "Rain": driver.skills['rain'],
            "Car set-up": driver.skills['car set-up'],
            "Physicality": driver.skills['physicality'],
            "Potential": driver.skills['potential']
        }
        drivers.append(driver_data)

    print("Creating DataFrame...")
    df = pd.DataFrame(drivers)
    print("DataFrame created.")

    print("Saving to CSV and JSON...")
    df.to_csv("drivers.csv", index=False)
    df.to_json("driver_database.json", orient="records", indent=4)
    print("Driver database created and saved to CSV and JSON.")

    return df

# Run the function
create_driver_database(2)  # Small number to quickly check functionality
