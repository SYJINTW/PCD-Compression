"""
python compress_ply_bz2.py \
--input /Users/syjintw/Desktop/NUS/pcd_compression/PCD-Compression/dataset/results/Output/rb2_1/cube/mv/frame1 \
--output /Users/syjintw/Desktop/NUS/pcd_compression/PCD-Compression/dataset/results/compressed/rb2_1/cube/mv/frame1
"""
from plyfile import PlyData, PlyElement
from pathlib import Path
import argparse
import numpy as np
# import bz2
import os

def compress_and_move(input_path, output_dir):
    bz2_path = input_path.parent/f"{input_path.name}.bz2"
    os.system(f"bzip2 -k {input_path}")
    os.system(f"mv {bz2_path} {output_dir}")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change the position (x, y, z) from float64 (double) to float32 (float).")
    
    # Example arguments
    parser.add_argument('--input', type=str, required=True, help='The input dir.')
    parser.add_argument('--output', type=str, required=True, help='The output dir and the ply file will follow the ply from input dir.')

    args = parser.parse_args()

    input_dir = Path(f"{args.input}")
    output_dir = Path(f"{args.output}")
    output_dir.mkdir(parents=True, exist_ok=True)

    for input_path in input_dir.glob("*"):
        compress_and_move(input_path, output_dir)

# # Load the original PLY file (binary or ascii)
# inter_ply = PlyData.read('/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32/frame1.ply')
# file_size_bytes = os.path.getsize('/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32/frame1.ply')
# print(file_size_bytes)

# inter_vertices = inter_ply['vertex'].data
# np.save("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_inter.npy", inter_vertices)
# with open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_inter.npy", "rb") as f_in:
#     with bz2.open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_inter.npy.bz2", "wb") as f_out:
#         f_out.write(f_in.read())
        
# file_size_bytes = os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_inter.npy.bz2")
# print(file_size_bytes)

# file_size_bytes = os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32_delta/frame1.ply.bz2")
# print(file_size_bytes)

# file_size_bytes = os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32/frame1.ply.bz2")
# print(file_size_bytes)

# # vertex_dtype = [
# #     ('x', 'f4'), 
# #     ('y', 'f4'), 
# #     ('z', 'f4'),
# #     ('red', 'u1'), 
# #     ('green', 'u1'), 
# #     ('blue', 'u1')
# # ]

# # vertex_data = np.array(
# #     list(zip(
# #         inter_vertices['x'], inter_vertices['y'], inter_vertices['z'],
# #         inter_vertices['red'], inter_vertices['green'], inter_vertices['blue']
# #     )),
# #     dtype=vertex_dtype
# # )

# # # === Create PlyElement ===
# # ply_out = PlyElement.describe(vertex_data, 'vertex')

# # # === Save as new PLY file ===
# # PlyData([ply_out], text=False).write('/home/syjintw/Desktop/NUS/pcd_compression/inter.ply')

# # file_size_bytes = os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/inter.ply")
# # print(file_size_bytes)
