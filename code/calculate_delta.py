from plyfile import PlyData, PlyElement
import numpy as np
import bz2
import os

# Load the original PLY file (binary or ascii)
intra_ply = PlyData.read('/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32/frame0.ply')
inter_ply = PlyData.read('/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32/frame1.ply')

file_size_bytes = os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32/frame0.ply")
print(file_size_bytes)

file_size_bytes = os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32/frame1.ply")
print(file_size_bytes)

# # Save it as ASCII format
# intra_ply.text = True
# intra_ply.write('/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_ascii/frame0.ply')
# inter_ply.text = True
# inter_ply.write('/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_ascii/frame1.ply')

intra_vertices = intra_ply['vertex'].data
inter_vertices = inter_ply['vertex'].data

intra_points = np.stack([intra_vertices['x'], intra_vertices['y'], intra_vertices['z']], axis=1)
inter_points = np.stack([inter_vertices['x'], inter_vertices['y'], inter_vertices['z']], axis=1)

intra_colors = np.stack([intra_vertices['red'], intra_vertices['green'], intra_vertices['blue']], axis=1)
inter_colors = np.stack([inter_vertices['red'], inter_vertices['green'], inter_vertices['blue']], axis=1)

delta_points = inter_points - intra_points
delta_colors = inter_colors.astype(np.int16) - intra_colors.astype(np.int16)

# print(delta_points)
print(delta_colors)
delta_colors = delta_colors + 255
print(delta_colors)

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
PlyData([ply_out], text=False).write('/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32_delta/frame1.ply')

np.save("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_pos.npy", delta_points)
with open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_pos.npy", "rb") as f_in:
    with bz2.open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_pos.npy.bz2", "wb") as f_out:
        f_out.write(f_in.read())
        
np.save("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_col.npy", delta_colors)
with open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_col.npy", "rb") as f_in:
    with bz2.open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_col.npy.bz2", "wb") as f_out:
        f_out.write(f_in.read())

np.save("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_x.npy", delta_points[:, 0])
with open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_x.npy", "rb") as f_in:
    with bz2.open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_x.npy.bz2", "wb") as f_out:
        f_out.write(f_in.read())
        
np.save("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_y.npy", delta_points[:, 1])
with open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_y.npy", "rb") as f_in:
    with bz2.open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_y.npy.bz2", "wb") as f_out:
        f_out.write(f_in.read())
        
np.save("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_z.npy", delta_points[:, 2])
with open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_z.npy", "rb") as f_in:
    with bz2.open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_z.npy.bz2", "wb") as f_out:
        f_out.write(f_in.read())

np.save("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_r.npy", delta_colors[:, 0])
with open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_r.npy", "rb") as f_in:
    with bz2.open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_r.npy.bz2", "wb") as f_out:
        f_out.write(f_in.read())
        
np.save("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_g.npy", delta_colors[:, 1])
with open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_g.npy", "rb") as f_in:
    with bz2.open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_g.npy.bz2", "wb") as f_out:
        f_out.write(f_in.read())
        
np.save("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_b.npy", delta_colors[:, 2])
with open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_b.npy", "rb") as f_in:
    with bz2.open("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_b.npy.bz2", "wb") as f_out:
        f_out.write(f_in.read())
        
file_size_bytes = os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_float32_delta/frame1.ply")
print(file_size_bytes)

file_size = 0
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_pos.npy")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_col.npy")
print(file_size)

file_size = 0
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_pos.npy.bz2")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_col.npy.bz2")
print(file_size)

file_size = 0
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_x.npy")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_y.npy")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_z.npy")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_r.npy")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_g.npy")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_np/data_b.npy")
print(file_size)

file_size = 0
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_x.npy.bz2")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_y.npy.bz2")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_z.npy.bz2")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_r.npy.bz2")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_g.npy.bz2")
file_size = file_size + os.path.getsize("/home/syjintw/Desktop/NUS/pcd_compression/dataset/longdress/ours_bz2/data_b.npy.bz2")
print(file_size)

# file_size_bytes = os.path.getsize("../data_x.npy.bz2")
# print(file_size_bytes)