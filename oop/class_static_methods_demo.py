#class_static_methods_demo.py

class Calculator:
    #Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print (f"Calculation_type: {cls.calculation_type}")
        return a * b