import os
from pathlib import Path

CODE_DIR = "/Users/syjintw/Desktop/NUS/pcd_compression/PCD-Compression/code"
DATA_DIR = "/Users/syjintw/Desktop/NUS/pcd_compression/PCD-Compression/dataset/results/Output"
SAVE_PATH = "/Users/syjintw/Desktop/NUS/pcd_compression/PCD-Compression/dataset/results/compress"

if __name__ == "__main__":
    dataset_names = ["redandblack"] # ["redandblack"]
    dataset_abbrs = ["rb"] # ["rb"]
    methods = ["ours", "cube", "p2p"] # ["ours", "cube", "p2p"]
    gofs = [2] # [2]
    groups = [1, 2] # [1]
    frames = [1] # [1]
    
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
