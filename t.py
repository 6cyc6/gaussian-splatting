import os
import numpy as np
import polyscope as ps
import pymeshlab

PATH = "/home/galois/git_downloads/6cyc6/gaussian-splatting"
ms = pymeshlab.MeshSet()
# ms.load_new_mesh(os.getcwd()+"/output/e3c9c301-d/input.ply")
ms.load_new_mesh(os.getcwd()+"/output/e3c9c301-d/point_cloud/iteration_30000/point_cloud.ply")

vertices = ms.current_mesh().vertex_matrix()
faces = ms.current_mesh().edge_matrix()

color = ms.current_mesh().vertex_color_matrix()

ps.set_up_dir("z_up")
ps.set_navigation_style("free")
ps.set_ground_plane_mode("none")

print(vertices)
print(faces)

ps.init()
ps.register_point_cloud("1", vertices, color=color[:, :3])
# ps.register_surface_mesh("first mesh", vertices, faces)
ps.show()


