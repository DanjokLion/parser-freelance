import subprocess

files = ['server/parsers/habr.py', 'server/parsers/freejob.py']

for file in files:
    subprocess.Popen(['python', file], shell=True, stdout=subprocess.PIPE)
