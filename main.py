class MyClass:
    class_variable = 0

    def __init__(self):
        print("__init__ çalıştı.")
        self.class_variable = 1
        MyClass.class_method()
        MyClass.static_method()
        self.instance_method()

    @staticmethod
    def static_method():
        print("static method çalıştı.")
        print("Sınıf özelliği (class_variable):", MyClass.class_variable)

    def instance_method(self):
        print("instance method çalıştı")
        print("Sınıf özelliği (class_variable):", self.class_variable)

    @classmethod
    def class_method(cls):
        print("class method çalıştı")
        print("Sınıf özelliği (class_variable):", cls.class_variable)


MyClass.static_method()
my_class = MyClass()
my_class.instance_method()
my_class.class_method()
MyClass.class_method()
my_class.static_method()