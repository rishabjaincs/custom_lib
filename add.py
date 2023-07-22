import pandas as pd
import requests
import random

class add:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def random_add(self):
        return self.a + self.b + random.random()
    