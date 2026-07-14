export type AnalysisSignalValue =
  | string
  | number
  | boolean
  | {
      width?: number;
      height?: number;
      [key: string]: unknown;
    };

export type AnalysisSignal = {
  id: string;
  label: string;
  value: AnalysisSignalValue;
  display_value: string;
  reference: string;
  status: string;
  risk_contribution: number;
  contribution_label: string;
  explanation: string;
  flag?: string | null;
};

export type MediaProfile = {
  type: "graphical" | "photographic" | "mixed_or_unknown";
  confidence: "low" | "medium" | "high";
  reasons: string[];
  scores?: {
    graphical?: number;
    photographic?: number;
  };
  disclaimer: string;
};

export type ImageAnalysisDetails = {
  dimensions?: {
    width?: number;
    height?: number;
  };
  format?: string;
  mode?: string;
  exif_present?: boolean;
  exif?: Record<string, string>;
  file_size_bytes?: number;
  aspect_ratio?: number;
  edge_density?: number;
  media_profile?: MediaProfile;
  flags?: string[];
  base_score?: number;
  signals?: AnalysisSignal[];
};

export type McpToolTraceEntry = {
  tool: string;
  transport: string;
  status: string;
};

export type AnalysisResponse = {
  request_id: string;
  media_type: string;
  risk_score: number;
  risk_level: string;
  flags: string[];
  summary: string;
  reasoning: string;
  confidence_explanation: string;
  recommended_action: string;

  technical_details?: {
    security?: Record<string, unknown>;
    analysis?: ImageAnalysisDetails;
    claim?: string;
    mcp_tool_trace?: McpToolTraceEntry[];
    prompt_preview?: {
      prompt_version?: string;
      system_prompt?: string;
      user_prompt?: string;
    };
  };
};