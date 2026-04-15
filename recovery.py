import os
import shutil


def recover_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    print(f"Attempting recovery from {source_dir}...")
    recovered_count = 0

    for dirpath, _, filenames in os.walk(source_dir):
        for file in filenames:
            # Simple logic: Recover text and log files
            if file.endswith(".txt") or file.endswith(".log"):
                source_path = os.path.join(dirpath, file)
                dest_path = os.path.join(dest_dir, f"recovered_{file}")

                try:
                    shutil.copy2(source_path, dest_path)
                    print(f"Recovered: {file}")
                    recovered_count += 1
                except Exception as e:
                    print(f"Failed to recover {file}: {e}")

    print(f"Recovery complete. Total files recovered: {recovered_count}")