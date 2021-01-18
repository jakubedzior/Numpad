import os


with open('state.txt', 'r') as f:
    if f.read() == 'True':
        exit()
