class Life:
    def hobbies(self):
        print("piano")
        print("football")
        print(len("coding"))

class Male(Life):
    pass

class Female(Life):
    pass

male1 = Male()
male1.hobbies()

female1 = Female()
female1.hobbies()

