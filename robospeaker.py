import os

if __name__ == '__main__':
     x =  input("enter what you want to speak ")

     command = f"say {x}"
     os.system(command)
     
import pyjokes
joke = pyjokes.get_joke()
print(joke)