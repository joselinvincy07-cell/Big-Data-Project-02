import subprocess


with open("input.txt", "r") as infile, open("map_output.txt", "w") as outfile:
    subprocess.run(["python", "mapper.py"], stdin=infile, stdout=outfile)


with open("map_output.txt", "r") as infile:
    lines = infile.readlines()

lines.sort()

with open("sorted_output.txt", "w") as outfile:
    outfile.writelines(lines)


with open("sorted_output.txt", "r") as infile, open("final_output.txt", "w") as outfile:
    subprocess.run(["python", "reducer.py"], stdin=infile, stdout=outfile)

print("Processing Completed!")
print("Check final_output.txt")
