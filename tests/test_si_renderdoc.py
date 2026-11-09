import tempfile
import unittest
from pathlib import Path
import si_csv_to_obj as m

SAMPLE_CSV = """VTX,IDX,POSITION.x,POSITION.y,POSITION.z,NORMAL.x,NORMAL.y,NORMAL.z,TEXCOORD0.x,TEXCOORD0.y
0,0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.25
1,1,1.0,0.0,0.0,0.0,0.0,1.0,1.0,0.25
2,2,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.75
"""


class TestSiRenderDocObj(unittest.TestCase):
    def test_converts_positions_normals_and_flipped_uvs(self):
        res = m.convert_renderdoc_csv_to_obj(SAMPLE_CSV, flip_v=True, mtllib_name="hero.mtl")
        self.assertEqual(res["vertexCount"], 3)
        self.assertEqual(res["triangleCount"], 1)
        self.assertTrue(res["hasUV"])
        self.assertTrue(res["hasNormals"])
        self.assertIn("mtllib hero.mtl", res["objText"])
        self.assertIn("vt 0.000000 0.750000", res["objText"])  # 1.0 - 0.25 = 0.75
        self.assertIn("f 1/1/1 2/2/2 3/3/3", res["objText"])

    def test_deduplicates_shared_indices(self):
        csv2 = SAMPLE_CSV + "3,0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.25\n4,2,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.75\n5,3,-1.0,1.0,0.0,0.0,0.0,1.0,0.5,0.5\n"
        res = m.convert_renderdoc_csv_to_obj(csv2)
        self.assertEqual(res["vertexCount"], 4)
        self.assertEqual(res["triangleCount"], 2)

    def test_missing_position_raises(self):
        with self.assertRaises(ValueError):
            m.convert_renderdoc_csv_to_obj("VTX,IDX,COLOR.r,COLOR.g\n0,0,1.0,1.0\n")

    def test_cli_writes_obj_and_mtl(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            csv_p = p / "dump.csv"
            obj_p = p / "out.obj"
            csv_p.write_text(SAMPLE_CSV, encoding="utf-8")
            rc = m.main(["--input", str(csv_p), "--out", str(obj_p), "--texture", "suit_albedo.png"])
            self.assertEqual(rc, 0)
            self.assertTrue(obj_p.exists())
            self.assertTrue((p / "out.mtl").exists())


if __name__ == "__main__":
    unittest.main()
