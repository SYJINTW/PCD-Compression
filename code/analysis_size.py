from pathlib import Path
import numpy as np
import pandas as pd
import os

RAW_DIR = "/mnt/data1/syjintw/point_cloud_compression/output_data"
COMPRESSED_DIR = "/mnt/data1/syjintw/point_cloud_compression/output_data_compress"
SAVE_PATH = "/mnt/data1/syjintw/point_cloud_compression/results/csv/all_cube_gof2_tf12_size.csv"
(Path(SAVE_PATH).parent).mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    dataset_names = ["longdress", "loot", "redandblack", "soldier"] # ["longdress", "loot", "redandblack", "soldier"]
    dataset_abbrs = ["ld", "loot", "rb", "sol"] # ["ld", "loot", "rb", "sol"]
    methods = ["cube"] # ["ours", "cube", "p2p"]
    gofs = [2] # [2] / [3]
    groups = [1, 2, 3, 4, 5, 6] # [1, 2, 3, 4, 5, 6] / [1, 2, 3, 4]
    frames = [1] # [1] / [1, 2]
    
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
