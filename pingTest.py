import subprocess
state = subprocess.call(["ping", "8.8.8.8", "-c1", "-W2", "-q"])
print(state)
