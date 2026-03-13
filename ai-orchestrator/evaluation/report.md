# Evaluation Report

## Overview

### Mode: rule

- Total cases: 2
- Successful cases: 2
- Failed cases: 0
- Average latency (ms): 1004.0
- Average authenticity score: 0.55
- Summary present rate: 1.0
- Reasoning present rate: 1.0
- Confidence present rate: 1.0
- Fallback rate: 0.0
- Average reasoning length: 904.0
- Average confidence length: 138.0
- Expected flag pass rate: 1.0

### Mode: llm

- Total cases: 2
- Successful cases: 2
- Failed cases: 0
- Average latency (ms): 1092.08
- Average authenticity score: 0.55
- Summary present rate: 1.0
- Reasoning present rate: 1.0
- Confidence present rate: 1.0
- Fallback rate: 1.0
- Average reasoning length: 904.0
- Average confidence length: 226.0
- Expected flag pass rate: 1.0

## Per-case Results

### case_001 | mode=rule

- Latency (ms): 941.56
- Authenticity score: 0.55
- Risk level: medium
- Recommended action: manual_check
- Flags: very_low_resolution, unusual_aspect_ratio, has_alpha_channel, very_low_edge_density
- Fallback used: False
- Reasoning length: 901
- Confidence length: 138
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image has very limited resolution in at least one dimension, reducing traceability and making manipulation assessment harder. The image uses an unusual aspect ratio, which can appear in banners, crops, composites, or generated assets. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 12.531. The measured edge density is 0.0279. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate because several independent heuristic indicators point in the same direction, but none of them alone is definitive.

### case_001 | mode=llm

- Latency (ms): 1119.51
- Authenticity score: 0.55
- Risk level: medium
- Recommended action: manual_check
- Flags: very_low_resolution, unusual_aspect_ratio, has_alpha_channel, very_low_edge_density
- Fallback used: True
- Reasoning length: 901
- Confidence length: 226
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image has very limited resolution in at least one dimension, reducing traceability and making manipulation assessment harder. The image uses an unusual aspect ratio, which can appear in banners, crops, composites, or generated assets. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 12.531. The measured edge density is 0.0279. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate because several independent heuristic indicators point in the same direction, but none of them alone is definitive. LLM fallback was used because the external reasoning model was temporarily unavailable.

### case_002 | mode=rule

- Latency (ms): 1066.43
- Authenticity score: 0.55
- Risk level: medium
- Recommended action: manual_check
- Flags: very_low_resolution, unusual_aspect_ratio, has_alpha_channel, very_low_edge_density
- Fallback used: False
- Reasoning length: 907
- Confidence length: 138
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Does this image look manipulated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image has very limited resolution in at least one dimension, reducing traceability and making manipulation assessment harder. The image uses an unusual aspect ratio, which can appear in banners, crops, composites, or generated assets. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 12.531. The measured edge density is 0.0279. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate because several independent heuristic indicators point in the same direction, but none of them alone is definitive.

### case_002 | mode=llm

- Latency (ms): 1064.65
- Authenticity score: 0.55
- Risk level: medium
- Recommended action: manual_check
- Flags: very_low_resolution, unusual_aspect_ratio, has_alpha_channel, very_low_edge_density
- Fallback used: True
- Reasoning length: 907
- Confidence length: 226
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Does this image look manipulated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image has very limited resolution in at least one dimension, reducing traceability and making manipulation assessment harder. The image uses an unusual aspect ratio, which can appear in banners, crops, composites, or generated assets. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 12.531. The measured edge density is 0.0279. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate because several independent heuristic indicators point in the same direction, but none of them alone is definitive. LLM fallback was used because the external reasoning model was temporarily unavailable.
