import random
from nameGen import names_by_country

class Driver:
    def __init__(self, is_rookie=False):
        self.country = random.choice(list(names_by_country.keys()))
        self.name = random.choice(names_by_country[self.country])
        self.is_rookie = is_rookie

        if self.is_rookie:
            self.age = random.randint(18, 22)
        else:
            self.age = random.randint(18, 45)

        self.peak = random.randint(24, 40)

        self.skills = self.generate_skills()

        print(f"Driver: {self.name}, Country: {self.country}, Age: {self.age}, Peak: {self.peak}, Rookie: {self.is_rookie}")


    def generate_skills(self):
        skills = {}

        skill_names = {
            'start',
            'concentration',
            'overtaking',
            'experience',
            'speed',
            'rain',
            'car set-up',
            'physicality',
            'potential'
        }

        for skill in skill_names:
            if skill == 'experience' and self.is_rookie:
                skills[skill] = round(random.uniform(1.0, 5.0), 1)
            elif skill == "potential":
                skills[skill] = round(random.uniform(6.5, 10.0), 1)
            elif skill == "experience":
                skills[skill] = round(random.uniform(5.0, 10.0), 1)
            else:
                skills[skill] = round(random.uniform(1.0, 10.0), 1)

        return skills
    
    def __str__(self):
        skills_str = ', '.join([f"{k}: {v}" for k, v in self.skills.items()])
        return (f"Name: {self.name}, Country: {self.country}, Age: {self.age}, "
                f"Peak: {self.peak}, Rookie: {self.is_rookie}\nSkills: {skills_str}")
    



# Example of creating a driver
rookie_driver = Driver(is_rookie=True)
veteran_driver = Driver(is_rookie=False)

# Print driver information using __str__
print(rookie_driver)
print(veteran_driver)