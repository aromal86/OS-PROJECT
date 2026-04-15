import os
import hashlib


def get_file_hash(filepath):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()
    except:
        return None


def find_duplicates(directory):
    print(f"Scanning {directory} for duplicates...")
    hashes = {}
    duplicates = []

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            file_hash = get_file_hash(full_path)

            if file_hash:
                if file_hash in hashes:
                    duplicates.append((full_path, hashes[file_hash]))
                    print(f"Duplicate found: {full_path} == {hashes[file_hash]}")
                else:
                    hashes[file_hash] = full_path

    print(f"Found {len(duplicates)} duplicate files.")