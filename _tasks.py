import subprocess

subprocess.run(["git", "init"])
subprocess.run(["git", "checkout", "-b", "main"])
subprocess.run(["git", "add", "."])  # this is the line that causes the teardown problem
