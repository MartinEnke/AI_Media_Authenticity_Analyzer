import os
from typing import Any, Dict, List

import numpy as np
from PIL import ExifTags, Image


EDGE_DENSITY_THRESHOLD = 0.03
MIN_IMAGE_DIMENSION = 256
SMALL_FILE_SIZE_THRESHOLD = 10_000
MIN_ASPECT_RATIO = 0.25
MAX_ASPECT_RATIO = 4.0


def extract_metadata_tool(file_path: str) -> Dict[str, Any]:
    """
    Extract basic image metadata used by the forensic heuristic pipeline.
    """
    with Image.open(file_path) as img:
        width, height = img.size

        exif_data: Dict[str, str] = {}
        raw_exif = img.getexif()

        if raw_exif:
            for tag_id, value in raw_exif.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                exif_data[str(tag)] = str(value)

        return {
            "dimensions": {
                "width": width,
                "height": height,
            },
            "format": img.format,
            "mode": img.mode,
            "exif_present": bool(exif_data),
            "exif": exif_data,
            "file_size_bytes": os.path.getsize(file_path),
        }


def compute_edge_density_tool(file_path: str) -> Dict[str, Any]:
    """
    Calculate a lightweight edge-density heuristic.

    This is not a trained AI-image detector. It measures average neighboring
    pixel-intensity differences and normalizes the result to a 0–1 range.
    """
    with Image.open(file_path) as img:
        grayscale = img.convert("L")
        arr = np.array(grayscale, dtype=np.float32)

    if arr.shape[0] < 2 or arr.shape[1] < 2:
        return {"edge_density": 0.0}

    horizontal_difference = np.abs(np.diff(arr, axis=1))
    vertical_difference = np.abs(np.diff(arr, axis=0))

    edge_strength = (
        np.mean(horizontal_difference)
        + np.mean(vertical_difference)
    )

    edge_density = float(edge_strength / 255.0)

    return {
        "edge_density": round(edge_density, 4),
    }


def _build_signal(
    *,
    signal_id: str,
    label: str,
    value: Any,
    display_value: str,
    reference: str,
    status: str,
    risk_contribution: float,
    contribution_label: str,
    explanation: str,
    flag: str | None = None,
) -> Dict[str, Any]:
    """
    Build a consistent, frontend-friendly explanation object.
    """
    return {
        "id": signal_id,
        "label": label,
        "value": value,
        "display_value": display_value,
        "reference": reference,
        "status": status,
        "risk_contribution": risk_contribution,
        "contribution_label": contribution_label,
        "explanation": explanation,
        "flag": flag,
    }

def infer_media_profile(
    metadata: Dict[str, Any],
    edge_density: float,
    aspect_ratio: float,
) -> Dict[str, Any]:
    """
    Estimate the broad visual/media profile using transparent heuristics.

    This is not a trained image classifier. It only provides context for
    interpreting structural signals such as edge density and alpha channels.
    """
    image_format = str(metadata.get("format", "")).upper()
    image_mode = str(metadata.get("mode", ""))
    exif_present = bool(metadata.get("exif_present", False))
    has_alpha_channel = "A" in image_mode

    graphical_score = 0
    photographic_score = 0

    graphical_reasons = []
    photographic_reasons = []

    if image_format == "PNG":
        graphical_score += 1
        graphical_reasons.append(
            "PNG is commonly used for screenshots, illustrations, and graphical assets"
        )

    if image_format in {"JPEG", "JPG"}:
        photographic_score += 1
        photographic_reasons.append(
            "JPEG is commonly used for photographic images"
        )

    if has_alpha_channel:
        graphical_score += 2
        graphical_reasons.append(
            "The image contains an alpha channel used for transparency"
        )

    if edge_density < 0.03:
        graphical_score += 2
        graphical_reasons.append(
            "The image has very low edge density"
        )
    elif edge_density >= 0.08:
        photographic_score += 1
        photographic_reasons.append(
            "The image contains comparatively high structural detail"
        )

    if 0.8 <= aspect_ratio <= 1.25:
        graphical_score += 1
        graphical_reasons.append(
            "The image uses a near-square aspect ratio"
        )

    if exif_present:
        exif = metadata.get("exif", {})

        camera_fields = {
            "Make",
            "Model",
            "DateTimeOriginal",
            "LensModel",
            "ExposureTime",
            "FNumber",
            "ISOSpeedRatings",
            "PhotographicSensitivity",
        }

        detected_camera_fields = [
            field for field in camera_fields if field in exif
        ]

        if detected_camera_fields:
            photographic_score += 3
            photographic_reasons.append(
                "Camera-related EXIF fields were detected"
            )
        else:
            graphical_score += 1
            graphical_reasons.append(
                "Metadata is present but contains no clear camera-capture fields"
            )
    else:
        graphical_score += 1
        graphical_reasons.append(
            "No camera metadata was detected"
        )

    score_difference = abs(graphical_score - photographic_score)

    if graphical_score > photographic_score:
        profile_type = "graphical"
        reasons = graphical_reasons

        if score_difference >= 4:
            confidence = "high"
        elif score_difference >= 2:
            confidence = "medium"
        else:
            confidence = "low"

    elif photographic_score > graphical_score:
        profile_type = "photographic"
        reasons = photographic_reasons

        if score_difference >= 3:
            confidence = "high"
        elif score_difference >= 2:
            confidence = "medium"
        else:
            confidence = "low"

    else:
        profile_type = "mixed_or_unknown"
        confidence = "low"
        reasons = (
            graphical_reasons[:2]
            + photographic_reasons[:2]
        )

    return {
        "type": profile_type,
        "confidence": confidence,
        "reasons": reasons,
        "scores": {
            "graphical": graphical_score,
            "photographic": photographic_score,
        },
        "disclaimer": (
            "This is a heuristic media-profile estimate, not a trained "
            "image classification result."
        ),
    }


def detect_image_structure_flags_tool(
    metadata: Dict[str, Any],
    edge_density: float,
) -> Dict[str, Any]:
    """
    Interpret extracted image properties as transparent heuristic signals.

    The thresholds are configured project heuristics. They are not universal
    forensic standards and should not be interpreted as proof that an image
    is authentic or AI-generated.
    """
    flags: List[str] = []
    signals: List[Dict[str, Any]] = []
    base_score = 0.2

    dimensions = metadata.get("dimensions", {})
    width = int(dimensions.get("width", 0))
    height = int(dimensions.get("height", 0))

    exif_present = bool(metadata.get("exif_present", False))
    mode = str(metadata.get("mode", ""))
    file_size_bytes = int(metadata.get("file_size_bytes", 0))

    aspect_ratio = width / height if height else 0.0
    media_profile = infer_media_profile(
    metadata=metadata,
    edge_density=edge_density,
    aspect_ratio=aspect_ratio,
)
    profile_type = media_profile["type"]
    has_alpha_channel = "A" in mode

    # Metadata signal
    if exif_present:
        signals.append(
            _build_signal(
                signal_id="metadata",
                label="Image metadata",
                value=True,
                display_value="Present",
                reference="Metadata may be present or absent in both authentic and edited images",
                status="Available",
                risk_contribution=0.0,
                contribution_label="No score increase",
                explanation=(
                    "The file contains metadata. Metadata presence alone does not "
                    "establish whether an image is authentic or AI-generated."
                ),
            )
        )
    else:
        flags.append("missing_metadata")
        base_score += 0.15

        signals.append(
            _build_signal(
                signal_id="metadata",
                label="Image metadata",
                value=False,
                display_value="Not detected",
                reference="Metadata is often removed during export, editing, or sharing",
                status="Missing",
                risk_contribution=0.15,
                contribution_label="+0.15 risk score",
                explanation=(
                    "No EXIF metadata was detected. This is a weak heuristic because "
                    "many legitimate images lose metadata during editing, screenshots, "
                    "messaging, or web export."
                ),
                flag="missing_metadata",
            )
        )

    # Resolution signal
    is_very_low_resolution = (
        width < MIN_IMAGE_DIMENSION
        or height < MIN_IMAGE_DIMENSION
    )

    if is_very_low_resolution:
        flags.append("very_low_resolution")
        base_score += 0.10

        resolution_status = "Very low"
        resolution_contribution = 0.10
        resolution_contribution_label = "+0.10 risk score"
        resolution_flag = "very_low_resolution"
        resolution_explanation = (
            "At least one image dimension is below the configured minimum. "
            "Low resolution limits the amount of forensic detail available."
        )
    else:
        resolution_status = "Within configured range"
        resolution_contribution = 0.0
        resolution_contribution_label = "No score increase"
        resolution_flag = None
        resolution_explanation = (
            "Both dimensions meet the configured minimum for this heuristic."
        )

    signals.append(
        _build_signal(
            signal_id="resolution",
            label="Image resolution",
            value={
                "width": width,
                "height": height,
            },
            display_value=f"{width} × {height} px",
            reference=(
                f"Configured minimum: "
                f"{MIN_IMAGE_DIMENSION} px per dimension"
            ),
            status=resolution_status,
            risk_contribution=resolution_contribution,
            contribution_label=resolution_contribution_label,
            explanation=resolution_explanation,
            flag=resolution_flag,
        )
    )

    # Aspect-ratio signal
    unusual_aspect_ratio = (
        aspect_ratio > MAX_ASPECT_RATIO
        or aspect_ratio < MIN_ASPECT_RATIO
    )

    if unusual_aspect_ratio:
        flags.append("unusual_aspect_ratio")
        base_score += 0.10

        aspect_status = "Outside configured range"
        aspect_contribution = 0.10
        aspect_contribution_label = "+0.10 risk score"
        aspect_flag = "unusual_aspect_ratio"
        aspect_explanation = (
            "The image has an unusually wide or tall aspect ratio according "
            "to the configured heuristic. This is not specific to AI generation."
        )
    else:
        aspect_status = "Within configured range"
        aspect_contribution = 0.0
        aspect_contribution_label = "No score increase"
        aspect_flag = None
        aspect_explanation = (
            "The aspect ratio falls within the configured structural range."
        )

    signals.append(
        _build_signal(
            signal_id="aspect_ratio",
            label="Aspect ratio",
            value=round(aspect_ratio, 3),
            display_value=f"{aspect_ratio:.3f}",
            reference=(
                f"Configured range: "
                f"{MIN_ASPECT_RATIO}–{MAX_ASPECT_RATIO}"
            ),
            status=aspect_status,
            risk_contribution=aspect_contribution,
            contribution_label=aspect_contribution_label,
            explanation=aspect_explanation,
            flag=aspect_flag,
        )
    )

        # Alpha-channel signal
    if has_alpha_channel:
        flags.append("has_alpha_channel")

        if profile_type == "graphical":
            alpha_contribution = 0.01
            alpha_contribution_label = "+0.01 risk score"
            alpha_explanation = (
                "The image contains transparency information. Alpha channels are "
                "common in graphical PNG assets, screenshots, illustrations, and "
                "edited images. Because the media profile is graphical, this signal "
                "receives reduced weight."
            )
        else:
            alpha_contribution = 0.05
            alpha_contribution_label = "+0.05 risk score"
            alpha_explanation = (
                "The image contains transparency information. Alpha channels are "
                "common in PNG graphics, screenshots, edited assets, and generated "
                "images, so this is only a weak contextual signal."
            )

        base_score += alpha_contribution

        alpha_status = "Present"
        alpha_flag = "has_alpha_channel"
    else:
        alpha_status = "Not present"
        alpha_contribution = 0.0
        alpha_contribution_label = "No score increase"
        alpha_flag = None
        alpha_explanation = (
            "No alpha channel was detected in the image color mode."
        )

    signals.append(
        _build_signal(
            signal_id="alpha_channel",
            label="Alpha channel",
            value=has_alpha_channel,
            display_value="Present" if has_alpha_channel else "Not present",
            reference="Transparency is common in edited PNG assets",
            status=alpha_status,
            risk_contribution=alpha_contribution,
            contribution_label=alpha_contribution_label,
            explanation=alpha_explanation,
            flag=alpha_flag,
        )
    )

    # File-size signal
    is_very_small_file = file_size_bytes < SMALL_FILE_SIZE_THRESHOLD

    if is_very_small_file:
        flags.append("very_small_file_size")
        base_score += 0.10

        file_size_status = "Very small"
        file_size_contribution = 0.10
        file_size_contribution_label = "+0.10 risk score"
        file_size_flag = "very_small_file_size"
        file_size_explanation = (
            "The file is smaller than the configured threshold. Strong "
            "compression or minimal image content may reduce available evidence."
        )
    else:
        file_size_status = "Above configured minimum"
        file_size_contribution = 0.0
        file_size_contribution_label = "No score increase"
        file_size_flag = None
        file_size_explanation = (
            "The file size is above the configured small-file threshold."
        )

    signals.append(
        _build_signal(
            signal_id="file_size",
            label="File size",
            value=file_size_bytes,
            display_value=f"{file_size_bytes / 1024:.1f} KB",
            reference=(
                f"Configured minimum: "
                f"{SMALL_FILE_SIZE_THRESHOLD / 1000:.0f} KB"
            ),
            status=file_size_status,
            risk_contribution=file_size_contribution,
            contribution_label=file_size_contribution_label,
            explanation=file_size_explanation,
            flag=file_size_flag,
        )
    )

        # Edge-density signal
    has_very_low_edge_density = (
        edge_density < EDGE_DENSITY_THRESHOLD
    )

    if has_very_low_edge_density:
        flags.append("very_low_edge_density")

        if profile_type == "graphical":
            edge_contribution = 0.03
            edge_contribution_label = "+0.03 risk score"
            edge_explanation = (
                "The measured edge density is below the configured threshold. "
                "Low edge density is common in flat, smooth, minimalist, or "
                "illustrative graphics. Because the media profile is graphical, "
                "this signal receives reduced weight."
            )
        else:
            edge_contribution = 0.10
            edge_contribution_label = "+0.10 risk score"
            edge_explanation = (
                "The measured edge density is below the configured threshold. "
                "This can occur in smooth, blurry, minimalist, heavily processed, "
                "or generated images, so it should not be treated as proof by itself."
            )

        base_score += edge_contribution

        edge_status = "Unusually low"
        edge_flag = "very_low_edge_density"
    else:
        edge_status = "At or above threshold"
        edge_contribution = 0.0
        edge_contribution_label = "No score increase"
        edge_flag = None
        edge_explanation = (
            "The measured edge density meets the configured threshold."
        )

    signals.append(
        _build_signal(
            signal_id="edge_density",
            label="Edge density",
            value=edge_density,
            display_value=f"{edge_density:.4f}",
            reference=(
                f"Configured threshold: "
                f"≥ {EDGE_DENSITY_THRESHOLD:.2f}"
            ),
            status=edge_status,
            risk_contribution=edge_contribution,
            contribution_label=edge_contribution_label,
            explanation=edge_explanation,
            flag=edge_flag,
        )
    )

    return {
        "aspect_ratio": round(aspect_ratio, 3),
        "edge_density": edge_density,
        "media_profile": media_profile,
        "signals": signals,
        "flags": flags,
        "base_score": round(min(base_score, 0.95), 2),
    }