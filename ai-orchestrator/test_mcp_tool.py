import json
import os

from mcp_client import analyze_image_via_mcp, security_scan_via_mcp


TEST_IMAGE_PATH = "/Users/martinenke/Desktop/test.png"


def main() -> None:
    if not os.path.isfile(TEST_IMAGE_PATH):
        raise FileNotFoundError(
            f"Test image not found: {TEST_IMAGE_PATH}"
        )

    print("\nTesting MCP security tool...\n")

    security_result, security_trace = security_scan_via_mcp(
        file_path=TEST_IMAGE_PATH,
        declared_mimetype="image/png",
        media_type="image",
    )

    print("Security result:")
    print(json.dumps(security_result, indent=2))

    print("\nSecurity trace:")
    print(json.dumps(security_trace, indent=2))

    print("\nTesting MCP image analysis tools...\n")

    analysis_result, analysis_trace = analyze_image_via_mcp(
        file_path=TEST_IMAGE_PATH,
    )

    print("Analysis result:")
    print(json.dumps(analysis_result, indent=2))

    print("\nAnalysis trace:")
    print(json.dumps(analysis_trace, indent=2))


if __name__ == "__main__":
    main()