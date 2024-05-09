import sys

script_name = sys.argv[0]
print("Script name:", script_name)
if len(sys.argv) > 1:
    print("Arguments passed:", sys.argv[1:])

# sys.exit()

print("Platform:", sys.platform)
print("Python version:", sys.version)

print("Python search path:", sys.path)

sys.stdout.write("This is written to stdout\n")
sys.stderr.write("This is written to stderr\n")