import random


def turrets_generator():
    def shoot(self):
        print("Shooting")

    def search(self):
        print("Searching")

    def talk(self):
        print("Talking")

    while True:
        neuroticism = random.randint(0, 100)
        openness = random.randint(0, 100 - neuroticism)
        conscientiousness = random.randint(0, 100 - neuroticism - openness)
        extraversion = random.randint(0, 100 - neuroticism - openness - conscientiousness)
        agreeableness = 100 - neuroticism - openness - conscientiousness - extraversion
        turret = type('Turret', (object,),
                      dict(neuroticism=neuroticism, openness=openness, conscientiousness=conscientiousness,
                           extraversion=extraversion, agreeableness=agreeableness, shoot=shoot, search=search,
                           talk=talk))
        yield turret()


if __name__ == "__main__":
    turrets = turrets_generator()
    for i in range(3):
        print(f"\t*** Turret {i + 1} ***")
        turret = next(turrets)
        print(f"* Name of class: {type(turret).__name__} *")
        print(f"Neuroticism = {turret.neuroticism}")
        print(f"Openness = {turret.openness}")
        print(f"Conscientiousness = {turret.conscientiousness}")
        print(f"Extraversion = {turret.extraversion}")
        print(f"Agreeableness = {turret.agreeableness}")
        turret.shoot()
        turret.search()
        turret.talk()
        print()
