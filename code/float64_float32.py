"""
python float64_float32.py \
--input /Users/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours \
--output /Users/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32
"""
import argparse
from pathlib import Path
from plyfile import PlyData, PlyElement
import numpy as np

def load_and_save(input_path, output_path):
    # Load the original PLY file (binary or ascii)
    frame_ply = PlyData.read(input_path)

    vertices = frame_ply['vertex'].data

    vertex_dtype = [
        ('x', 'f4'), 
        ('y', 'f4'), 
        ('z', 'f4'),
        ('red', 'u1'), 
        ('green', 'u1'), 
        ('blue', 'u1')
    ]

    vertex_data = np.array(
        list(zip(
            vertices['x'], vertices['y'], vertices['z'],
            vertices['red'], vertices['green'], vertices['blue']
        )),
        dtype=vertex_dtype
    )

    # === Create PlyElement ===
    ply_out = PlyElement.describe(vertex_data, 'vertex')

    # === Save as new PLY file ===
    PlyData([ply_out], text=False).write(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change the position (x, y, z) from float64 (double) to float32 (float).")
    
    # Example arguments
    parser.add_argument('--input', type=str, required=True, help='The input dir.')
    parser.add_argument('--output', type=str, required=True, help='The output dir and the ply file will follow the ply from input dir.')

    args = parser.parse_args()

    input_dir = Path(f"{args.input}")
    output_dir = Path(f"{args.output}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for input_path in input_dir.glob("*.ply"):
        output_path = output_dir/f"{input_path.stem}.ply"
        load_and_save(input_path, output_path)
        
        
        
    
    