import os
import imghdr
from typing import Dict, Any


def validate_basic_file_properties(file_path: str, declared_mimetype: str, media_type: str) -> Dict[str, Any]:
    flags = []
    issues = []

    exists = os.path.exists(file_path)
    size_bytes = os.path.getsize(file_path) if exists else 0

    if not exists:
        return {
            "trusted": False,
            "flags": ["file_missing"],
            "issues": ["Uploaded file could not be found on disk."],
            "size_bytes": 0,
            "detected_type": None,
            "mimetype_matches": False,
        }

    if size_bytes == 0:
        flags.append("empty_file")
        issues.append("The uploaded file is empty.")

    detected_type = None
    mimetype_matches = True

    if media_type == "image":
        detected_type = imghdr.what(file_path)

        image_type_map = {
            "jpeg": "image/jpeg",
            "png": "image/png",
            "webp": "image/webp",
        }

        expected_mimetype = image_type_map.get(detected_type)
        if expected_mimetype != declared_mimetype:
            mimetype_matches = False
            flags.append("mimetype_mismatch")
            issues.append(
                f"Declared mimetype '{declared_mimetype}' does not match detected image type '{detected_type}'."
            )

    trusted = len(flags) == 0

    return {
        "trusted": trusted,
        "flags": flags,
        "issues": issues,
        "size_bytes": size_bytes,
        "detected_type": detected_type,
        "mimetype_matches": mimetype_matches,
    }