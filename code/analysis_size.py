from pathlib import Path
import numpy as np
import pandas as pd
import os

RAW_DIR = "/Users/syjintw/Desktop/NUS/pcd_compression/PCD-Compression/dataset/results/Output"
COMPRESSED_DIR = "/Users/syjintw/Desktop/NUS/pcd_compression/PCD-Compression/dataset/results/compress"
SAVE_PATH = "/Users/syjintw/Desktop/NUS/pcd_compression/PCD-Compression/dataset/results/csv/size.csv"
(Path(SAVE_PATH).parent).mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    dataset_names = ["redandblack"] # ["redandblack"]
    dataset_abbrs = ["rb"] # ["rb"]
    methods = ["ours", "cube", "p2p"] # ["ours", "cube", "p2p"]
    gofs = [2] # [2]
    groups = [1, 2] # [1]
    frames = [1] # [1]
    
    results = [] # [["dataset_name", "method", "gof", "group", "frame", "step", "raw_size", "compressed_size"]]
    for dataset_name, dataset_abbr in zip(dataset_names, dataset_abbrs):
        for method in methods:
            for gof in gofs:
                for group in groups:
                    for frame in frames:
                        raw_path = Path(RAW_DIR)/f"{dataset_abbr}{gof}_{group}"/f"{method}"/"mv"/f"frame{frame}"
                        compressed_path = Path(COMPRESSED_DIR)/f"{dataset_abbr}{gof}_{group}"/f"{method}"/"mv"/f"frame{frame}"
                        for raw_file_path in raw_path.glob("*"):
                            filename = raw_file_path.stem
                            step = int(filename.split("_step")[-1])
                            raw_size = os.path.getsize(raw_file_path) # bytes
                            compressed_size = os.path.getsize(compressed_path/f"{raw_file_path.name}.bz2") # bytes
                            data = [dataset_name, method, gof, group, frame, step, raw_size, compressed_size]
                            results.append(data)
                            
    # print(results)
    df = pd.DataFrame(results, columns=["dataset_name", "method", "gof", "group", "frame", "step", "raw_size", "compressed_size"])
    df.to_csv(SAVE_PATH, index=False)        
