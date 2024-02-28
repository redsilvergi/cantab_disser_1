import os
import csv

a = "자양로"
b = "14"
c = a + b

file_path = os.path.join(os.getcwd(), "test.csv")
with open(file_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["a", "b", "c"])
    writer.writerow([a, b, c])

print(f"path: {file_path}")
