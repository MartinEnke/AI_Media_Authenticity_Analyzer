# Evaluation Report

## Overview

### Mode: rule

- Total cases: 8
- Successful cases: 8
- Failed cases: 0
- Average latency (ms): 983.19
- Average authenticity score: 0.33
- Summary present rate: 1.0
- Reasoning present rate: 1.0
- Confidence present rate: 1.0
- Fallback rate: 0.0
- Average reasoning length: 639.0
- Average confidence length: 143.5
- Expected flag pass rate: 0.88

### Mode: llm

- Total cases: 8
- Successful cases: 8
- Failed cases: 0
- Average latency (ms): 1088.82
- Average authenticity score: 0.33
- Summary present rate: 1.0
- Reasoning present rate: 1.0
- Confidence present rate: 1.0
- Fallback rate: 1.0
- Average reasoning length: 639.0
- Average confidence length: 231.5
- Expected flag pass rate: 0.88

## Per-case Results

### her_real_portrait_01 | mode=rule | prompt=v1

- Latency (ms): 969.99
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: False
- Reasoning length: 661
- Confidence length: 148
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.776. The measured edge density is 0.0218. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure.

- Label: real
- Expected risk: low
- Predicted risk: low
- Risk correct: True
- Prompt version: v1
### her_real_portrait_01 | mode=llm | prompt=v1

- Latency (ms): 1260.6
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: True
- Reasoning length: 661
- Confidence length: 236
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.776. The measured edge density is 0.0218. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure. LLM fallback was used because the external reasoning model was temporarily unavailable.

- Label: real
- Expected risk: low
- Predicted risk: low
- Risk correct: True
- Prompt version: v1
### her_real_portrait_02 | mode=rule | prompt=v1

- Latency (ms): 965.77
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: False
- Reasoning length: 661
- Confidence length: 148
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.808. The measured edge density is 0.0054. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure.

- Label: real
- Expected risk: low
- Predicted risk: low
- Risk correct: True
- Prompt version: v1
### her_real_portrait_02 | mode=llm | prompt=v1

- Latency (ms): 1010.86
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: True
- Reasoning length: 661
- Confidence length: 236
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.808. The measured edge density is 0.0054. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure. LLM fallback was used because the external reasoning model was temporarily unavailable.

- Label: real
- Expected risk: low
- Predicted risk: low
- Risk correct: True
- Prompt version: v1
### her_ai_portrait_01 | mode=rule | prompt=v1

- Latency (ms): 963.58
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: False
- Reasoning length: 661
- Confidence length: 148
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.732. The measured edge density is 0.0249. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure.

- Label: ai_generated
- Expected risk: medium
- Predicted risk: low
- Risk correct: False
- Prompt version: v1
### her_ai_portrait_01 | mode=llm | prompt=v1

- Latency (ms): 1057.15
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: True
- Reasoning length: 661
- Confidence length: 236
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.732. The measured edge density is 0.0249. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure. LLM fallback was used because the external reasoning model was temporarily unavailable.

- Label: ai_generated
- Expected risk: medium
- Predicted risk: low
- Risk correct: False
- Prompt version: v1
### her_ai_portrait_02 | mode=rule | prompt=v1

- Latency (ms): 942.75
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: False
- Reasoning length: 661
- Confidence length: 148
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.748. The measured edge density is 0.0056. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure.

- Label: ai_generated
- Expected risk: medium
- Predicted risk: low
- Risk correct: False
- Prompt version: v1
### her_ai_portrait_02 | mode=llm | prompt=v1

- Latency (ms): 1240.1
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: True
- Reasoning length: 661
- Confidence length: 236
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.748. The measured edge density is 0.0056. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure. LLM fallback was used because the external reasoning model was temporarily unavailable.

- Label: ai_generated
- Expected risk: medium
- Predicted risk: low
- Risk correct: False
- Prompt version: v1
### me_real_portrait_01 | mode=rule | prompt=v1

- Latency (ms): 993.06
- Authenticity score: 0.25
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel
- Fallback used: False
- Reasoning length: 573
- Confidence length: 130
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The measured aspect ratio is 0.783. The measured edge density is 0.0705. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is limited because the result is driven by a single or weak indicator that could also occur in legitimate edited media.

- Label: real
- Expected risk: low
- Predicted risk: low
- Risk correct: True
- Prompt version: v1
### me_real_portrait_01 | mode=llm | prompt=v1

- Latency (ms): 1053.16
- Authenticity score: 0.25
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel
- Fallback used: True
- Reasoning length: 573
- Confidence length: 218
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The measured aspect ratio is 0.783. The measured edge density is 0.0705. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is limited because the result is driven by a single or weak indicator that could also occur in legitimate edited media. LLM fallback was used because the external reasoning model was temporarily unavailable.

- Label: real
- Expected risk: low
- Predicted risk: low
- Risk correct: True
- Prompt version: v1
### me_real_portrait_02 | mode=rule | prompt=v1

- Latency (ms): 1055.74
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: False
- Reasoning length: 661
- Confidence length: 148
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.783. The measured edge density is 0.0225. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure.

- Label: real
- Expected risk: low
- Predicted risk: low
- Risk correct: True
- Prompt version: v1
### me_real_portrait_02 | mode=llm | prompt=v1

- Latency (ms): 1028.81
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: True
- Reasoning length: 661
- Confidence length: 236
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.783. The measured edge density is 0.0225. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure. LLM fallback was used because the external reasoning model was temporarily unavailable.

- Label: real
- Expected risk: low
- Predicted risk: low
- Risk correct: True
- Prompt version: v1
### me_ai_portrait_01 | mode=rule | prompt=v1

- Latency (ms): 1032.37
- Authenticity score: 0.25
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel
- Fallback used: False
- Reasoning length: 573
- Confidence length: 130
- Expected min flags passed: False
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The measured aspect ratio is 0.769. The measured edge density is 0.0308. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is limited because the result is driven by a single or weak indicator that could also occur in legitimate edited media.

- Label: ai_generated
- Expected risk: medium
- Predicted risk: low
- Risk correct: False
- Prompt version: v1
### me_ai_portrait_01 | mode=llm | prompt=v1

- Latency (ms): 1025.91
- Authenticity score: 0.25
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel
- Fallback used: True
- Reasoning length: 573
- Confidence length: 218
- Expected min flags passed: False
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The measured aspect ratio is 0.769. The measured edge density is 0.0308. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is limited because the result is driven by a single or weak indicator that could also occur in legitimate edited media. LLM fallback was used because the external reasoning model was temporarily unavailable.

- Label: ai_generated
- Expected risk: medium
- Predicted risk: low
- Risk correct: False
- Prompt version: v1
### me_ai_portrait_02 | mode=rule | prompt=v1

- Latency (ms): 942.3
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: False
- Reasoning length: 661
- Confidence length: 148
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.763. The measured edge density is 0.0175. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure.

- Label: ai_generated
- Expected risk: medium
- Predicted risk: low
- Risk correct: False
- Prompt version: v1
### me_ai_portrait_02 | mode=llm | prompt=v1

- Latency (ms): 1033.96
- Authenticity score: 0.35
- Risk level: low
- Recommended action: allow_with_logging
- Flags: has_alpha_channel, very_low_edge_density
- Fallback used: True
- Reasoning length: 661
- Confidence length: 236
- Expected min flags passed: True
- Summary: In relation to the user's question, the uploaded image contains indicators that warrant manual review.
- Reasoning: In relation to the user's question ('Is this image AI-generated?'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media. The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows. The image has very low edge density, suggesting unusually smooth or low-detail content. The measured aspect ratio is 0.763. The measured edge density is 0.0175. The image mode is RGBA. The detected file signature is png. These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation.
- Confidence: Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure. LLM fallback was used because the external reasoning model was temporarily unavailable.

- Label: ai_generated
- Expected risk: medium
- Predicted risk: low
- Risk correct: False
- Prompt version: v1