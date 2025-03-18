

class Animal:
    
    def __init__(self,nameP,genderP,speedP:int):
        self.name=nameP
        self.gender=genderP
        self.speed=speedP
        self.messages={
            "walkMess":f"{nameP} is walking",
            "runMess":f"{nameP} is running at {speedP}",
            "eatMess":f"{nameP} is eating",
            "sleepMess":f"{nameP} is sleeping"
        }

    def walk(self):
        return self.messages["walkMess"]
    def run(self):
        return self.messages["runMess"]
    def eat(self):
        return self.messages["eatMess"]
    def sleep(self):
        return self.messages["sleepMess"]
    def displayInfo(self):
        print('Animal: ',self.name)
        print("Animal has this functions")
        for key, item in self.messages:
            print(f"{key} {item}")

class Dog(Animal):
    def __init__(self, nameP, genderP, speedP):
        super().__init__(nameP, genderP, speedP)
        self.messages={
            "walkMess":f"{nameP} is walking",
            "runMess":f"{nameP} is running at {speedP}",
            "eatMess":f"{nameP} is eating",
            "sleepMess":f"{nameP} is sleeping",
            "barkMessage":f"{nameP} is barking"
        }
    def bark(self):
        return self.messages["barkMessage"]


class Horse(Animal):
    def __init__(self, nameP, genderP, speedP):
        super().__init__(nameP, genderP, speedP)
        self.messages={
            "walkMess":f"{nameP} is walking",
            "runMess":f"{nameP} is running at {speedP}",
            "eatMess":f"{nameP} is eating",
            "sleepMess":f"{nameP} is sleeping",
            "":f"{nameP} is barking"
        }
    def bark(self):
        return self.messages["barkMessage"]


class Lion(Animal):
    def __init__(self, nameP, genderP, speedP):
        super().__init__(nameP, genderP, speedP)
        self.messages={
            "walkMess":f"{nameP} is walking",
            "runMess":f"{nameP} is running at {speedP}",
            "eatMess":f"{nameP} is eating",
            "sleepMess":f"{nameP} is sleeping",
            "hunt":f"{nameP} hunting"
        }
    def hunt(self):
        return self.messages["hunt"]





