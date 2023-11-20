import subprocess

files = ['habr.py', 'freeru.py']

for file in files:
    subprocess.Popen(args=['start', 'python', file], shell=True, stdout=subprocess.PIPE)