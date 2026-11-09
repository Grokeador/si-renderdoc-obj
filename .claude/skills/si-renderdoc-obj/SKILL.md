---
name: si-renderdoc-obj
description: Convert RenderDoc Mesh Viewer CSV exports (VS In / VS Out) into clean Wavefront .obj and .mtl 3D models with UV flip and perspective unprojection.
---

# SI-RenderDoc-OBJ Skill

1. In RenderDoc **Mesh Viewer**, export the Drawcall table (`VS In` or `VS Out`) to `.csv` and save the bound Albedo texture as `.png`.
2. Run:
   ```sh
   python si_csv_to_obj.py --input mesh_dump.csv --out mesh_clean.obj --texture albedo.png
   ```
3. Import `mesh_clean.obj` into Blender 4 (`File -> Import -> Wavefront .obj`).
