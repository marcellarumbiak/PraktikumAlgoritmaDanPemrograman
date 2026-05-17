fname = input('Masukkan nama file: ')
try:
  fhand = open(fname)
except FileNotFoundError:
  print("file tidak ditemukan: ", fname)
  exit()

counts = dict()
for line in fhand:
  if line.startswith('From '):
    words = line.split()
    time = words[5]
    hour = time[:2]
    counts[hour] = counts.get(hour, 0) + 1

lst = list()
for key, val in counts.items():
  lst.append((key, val))

lst.sort()

for hour, count in lst:
  print(hour, count)
