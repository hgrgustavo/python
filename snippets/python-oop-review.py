# python 3 simplest class
class MyFirstClass:
    pass
    
# namespaces C++ example (why not ~_^)
'''
    namespace ContosoData
    {
        class ObjectManager
        {
            public:
                void DoSomething() {}
        };
        void Func(ObjectManager) {}
    }
'''

# namespaces python example
def scope_test():
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    
    def do_global():
        global spam
        spam = "global spam"
    
    spam = "test spam"
    
    do_local()
    print("After local assignment: ", spam)
    
    do_nonlocal()
    print("After nonlocal assignment: ", spam)
    
    do_global()
    print("After global assignment: ", spam)
    
scope_test()
print("In global scope: ", spam)


# python 3 class definition syntax
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

# python 3 class objects
    
    # attribute reference
    class MyClass:
        """A simple example class"""
        i = 12345
        
        def f(self):
            return 'hello world'
    
    # python-style constructor (maybe?)
    def __init__(self):
        self.data = []
    
        # instantiation
        x = MyClass()
        
        # constructor with parameters
        class Complex:
            def __init__(self, realpart, imagpart):
                self.r = realpart
                self.i = imagpart
        x = Complex(3.0, -4.5)
        x.r, x.i
        
        
        # calling the method "MyClass.f"
        x = MyClass()
        x.f()
            # or...
            x = MyClass.f()
    
        # instance vars x class vars example
        class Dog:
            kind = 'canine'     # class var shared by all instances
            
            def __init__(self, name):
                self.name = name        # instance var unique to each instance
            
            d = Dog('Fido')
            e = Dog('Buddy')
            d.kind                      # shared by all dogs
            e.kind                      # shared by all dogs
            d.name                      # unique to d
            e.name                      # unique to e
            
    
        # mistaken example of a class var
        class Dog:
            tricks = []     # mistanken use of a class variable
            
            def __init__(self, name):
                self.name = name
            
            def add_trick(self, trick):
                self.tricks.append(trick)
                
            d = Dog('Fido)
            e = Dog('Buddy')
            
            d.add_trick('roll over')
            e.add_trick('play dead')
            
            d.tricks        # unexpectedly shared by all dogs
            
            ['roll over', 'play dead']
            
            
            
        
        
    
        
    
    
    
    





    
