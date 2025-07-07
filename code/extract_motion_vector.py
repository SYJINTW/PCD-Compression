"""
python extract_motion_vector.py \
--input /Users/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32 \
--output /Users/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32_delta \
--intra_frame_num 0 \
--num_of_inter 1
"""
import argparse
from pathlib import Path
from plyfile import PlyData, PlyElement
import numpy as np

def cal_delta_and_save(intra_path, inter_ply, output_path):
    # Load the original PLY file (binary or ascii)
    intra_ply = PlyData.read(intra_path)
    inter_ply = PlyData.read(inter_ply)

    intra_vertices = intra_ply['vertex'].data
    inter_vertices = inter_ply['vertex'].data

    intra_points = np.stack([intra_vertices['x'], intra_vertices['y'], intra_vertices['z']], axis=1)
    inter_points = np.stack([inter_vertices['x'], inter_vertices['y'], inter_vertices['z']], axis=1)

    intra_colors = np.stack([intra_vertices['red'], intra_vertices['green'], intra_vertices['blue']], axis=1)
    inter_colors = np.stack([inter_vertices['red'], inter_vertices['green'], inter_vertices['blue']], axis=1)

    delta_points = inter_points - intra_points
    delta_colors = inter_colors.astype(np.int16) - intra_colors.astype(np.int16)
    
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
            delta_points[:, 0], delta_points[:, 1], delta_points[:, 2],
            delta_colors[:, 0], delta_colors[:, 1], delta_colors[:, 2]
        )),
        dtype=vertex_dtype
    )

    # === Create PlyElement ===
    ply_out = PlyElement.describe(vertex_data, 'vertex')

    # === Save as new PLY file ===
    PlyData([ply_out], text=False).write(output_path)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change the inter-frame to motion vectors (delta-frame).")
    
    # Example arguments
    parser.add_argument('--input', type=str, required=True, help='The input dir.')
    parser.add_argument('--output', type=str, required=True, help='The output dir and the ply file will follow the ply from input dir.')
    parser.add_argument('--intra_frame_num', type=int, required=True, help='The frame number of intra-frame')
    parser.add_argument('--num_of_inter', type=int, required=True, help='The number of following frames (inter-frame).')

    args = parser.parse_args()
    
    input_dir = Path(f"{args.input}")
    output_dir = Path(f"{args.output}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for frame in range(args.intra_frame_num + 1, (args.intra_frame_num + args.num_of_inter + 1)):
        intra_path = Path(input_dir)/f"frame{frame-1}.ply"
        inter_path = Path(input_dir)/f"frame{frame}.ply"
        output_path = Path(output_dir)/f"frame{frame}.ply"
        cal_delta_and_save(intra_path, inter_path, output_path)
        
    