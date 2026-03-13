import os
from typing import Dict, Any
from PIL import Image, ExifTags
import numpy as np


def extract_metadata_tool(file_path: str) -> Dict[str, Any]:
    img = Image.open(file_path)
    width, height = img.size

    exif_data = {}
    raw_exif = img.getexif()

    if raw_exif:
        for tag_id, value in raw_exif.items():
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            exif_data[str(tag)] = str(value)

    return {
        "dimensions": {"width": width, "height": height},
        "format": img.format,
        "mode": img.mode,
        "exif_present": bool(exif_data),
        "exif": exif_data,
        "file_size_bytes": os.path.getsize(file_path),
    }


def compute_edge_density_tool(file_path: str) -> Dict[str, Any]:
    img = Image.open(file_path).convert("L")
    arr = np.array(img, dtype=np.float32)

    if arr.shape[0] < 2 or arr.shape[1] < 2:
        return {"edge_density": 0.0}

    gx = np.abs(np.diff(arr, axis=1))
    gy = np.abs(np.diff(arr, axis=0))

    edge_strength = np.mean(gx) + np.mean(gy)
    edge_density = float(edge_strength / 255.0)

    return {"edge_density": round(edge_density, 4)}


def detect_image_structure_flags_tool(metadata: Dict[str, Any], edge_density: float) -> Dict[str, Any]:
    flags = []
    base_score = 0.2

    width = metadata["dimensions"]["width"]
    height = metadata["dimensions"]["height"]
    exif_present = metadata["exif_present"]
    mode = metadata["mode"]
    file_size_bytes = metadata["file_size_bytes"]

    if not exif_present:
        flags.append("missing_metadata")
        base_score += 0.15

    if width < 256 or height < 256:
        flags.append("very_low_resolution")
        base_score += 0.10

    aspect_ratio = width / height if height else 0
    if aspect_ratio > 4 or aspect_ratio < 0.25:
        flags.append("unusual_aspect_ratio")
        base_score += 0.10

    if "A" in mode:
        flags.append("has_alpha_channel")
        base_score += 0.05

    if file_size_bytes < 10_000:
        flags.append("very_small_file_size")
        base_score += 0.10

    if edge_density < 0.03:
        flags.append("very_low_edge_density")
        base_score += 0.10

    return {
        "aspect_ratio": round(aspect_ratio, 3),
        "edge_density": edge_density,
        "flags": flags,
        "base_score": min(base_score, 0.95),
    }