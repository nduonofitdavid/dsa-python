import os

def disk_usage(path: str) -> int:
    total = os.path.getsize(path)
    for structure in os.scandir(path):
        if structure.is_dir():
            nested_dir = os.path.join(path, structure)
            total += disk_usage(nested_dir)
    return total

directory = r'/home/nduonofit/ndurepo/dsa-python/chapterfour'
total_disk_usage = disk_usage(directory)
print(total_disk_usage)