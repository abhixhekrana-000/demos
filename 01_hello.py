print("hello world")


# variables in python

name="12344"
print(name)

sheriyans_code="harsh bahiya"  # snake case
print(sheriyans_code)

# Datatypes in python

a=12   
print(type(a))


aj=45.6
print(type(aj))


# complex datatypes
v=34j
print(type(v))


# boolean datatypes
b=True
print(b)




import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("hello iam abhishek")
engine.runAndWait()

