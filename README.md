# SI-RenderDoc-OBJ: Zero-Dependency RenderDoc CSV Mesh to Blender Wavefront .OBJ Converter

**Created by [SI NEWS](https://www.youtube.com/channel/UC4m6veQiZdc_pAfxKQluRgA) • Official companion repo for *"RenderDoc and AI: Extract Any 3D Model and Shader From Any PC Game for Free"*.**

When you capture a 3D frame inside **[RenderDoc](https://renderdoc.org)**, the Mesh Viewer only exports raw vertex/index spreadsheets (`.csv`) with columns like `VTX, IDX, POSITION.x, POSITION.y, POSITION.z, NORMAL.x, TEXCOORD.x`. Blender 4 cannot import raw RenderDoc CSV dumps directly, and third-party Blender plugins break across every Blender update.

`si-renderdoc-obj` is the **missing piece**: a zero-dependency Python 3 standard-library converter (`si_csv_to_obj.py`) + Claude skill (`SKILL.md`) that:
1. **Auto-detects Position, UV (`TEXCOORD`), and Normal columns** in any RenderDoc `VS Out` or `VS In` CSV export.
2. **Un-projects perspective-divided `SV_Position` coordinates (`x/w, y/w, z/w`)** when capturing post-projection stages.
3. **Flips DirectX/Vulkan V-texture coordinates (`1.0 - v`)** automatically so dumped DDS/PNG albedo textures align 1:1 in Blender.
4. **Outputs a clean Wavefront `.obj` + `.mtl` material file** ready to drag-and-drop into Blender, Godot 4, or Unreal Engine.

## Quick Start (Windows PowerShell)
```powershell
git clone https://github.com/Grokeador/si-renderdoc-obj
cd si-renderdoc-obj
python -m unittest discover -s tests -v
python si_csv_to_obj.py --input drawcall_vsout.csv --out model.obj --texture albedo.png
```

MIT Licensed — Built by [SI NEWS](https://www.youtube.com/channel/UC4m6veQiZdc_pAfxKQluRgA).
