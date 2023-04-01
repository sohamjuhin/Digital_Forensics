import os
import hashlib

def hash_file("crime"): #file name
    """Return the SHA-1 hash of the given file"""
    sha1 = hashlib.sha1()
    with open("crime", 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def find_duplicate_files(root_folder):
    """Find duplicate files in the given folder and its subfolders"""
    hashes = {}
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            file_hash = hash_file(full_path)
            if file_hash in hashes:
                hashes[file_hash].append(full_path)
            else:
                hashes[file_hash] = [full_path]
    return {k: v for k, v in hashes.items() if len(v) > 1}

if __name__ == '__main__':
    duplicates = find_duplicate_files('/path/to/folder')
    for hash_value, files in duplicates.items():
        print(f'{len(files)} files have the same SHA-1 hash:')
        for file_path in files:
            print(f'\t{file_path}')
