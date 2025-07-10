import os
from pathlib import Path

CODE_DIR = "/mnt/data1/syjintw/point_cloud_compression/PCD-Compression/code"
DATA_DIR = "/mnt/data1/syjintw/point_cloud_compression/output_data"
SAVE_PATH = "/mnt/data1/syjintw/point_cloud_compression/output_data_compress"

if __name__ == "__main__":
    dataset_names = ["longdress", "loot", "redandblack", "soldier"] # ["longdress", "loot", "redandblack", "soldier"]
    dataset_abbrs = ["ld", "loot", "rb", "sol"] # ["ld", "loot", "rb", "sol"]
    methods = ["cube"] # ["ours", "cube", "p2p"]
    gofs = [3] # [2] / [3]
    groups = [1, 2, 3, 4] # [1, 2, 3, 4, 5, 6] / [1, 2, 3, 4]
    frames = [1, 2] # [1] / [1, 2]
    
    code_path = Path(CODE_DIR)/"compress_ply_bz2.py"
    
    for dataset_name, dataset_abbr in zip(dataset_names, dataset_abbrs):
        for method in methods:
            for gof in gofs:
                for group in groups:
                    for frame in frames:
                        input_path = Path(DATA_DIR)/f"{dataset_abbr}{gof}_{group}"/f"{method}"/"mv"/f"frame{frame}"
                        output_path = Path(SAVE_PATH)/f"{dataset_abbr}{gof}_{group}"/f"{method}"/"mv"/f"frame{frame}"
                        os.system(f"python {code_path} \
                                --input {input_path} \
                                --output {output_path}")
