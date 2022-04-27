#class method using decorators

class Student:
    degree=4
    @classmethod        #decorator

    def has_degree(cls,name):
        print(name,"completed degree in", cls.degree,"years!!")

Student.has_degree("Renu")      #possible without creating a object!!!
