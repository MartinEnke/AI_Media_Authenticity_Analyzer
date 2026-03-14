export type AnalysisResponse = {
  request_id: string;
  media_type: string;
  authenticity_score: number;
  risk_level: string;
  flags: string[];
  summary: string;
  reasoning: string;
  confidence_explanation: string;
  recommended_action: string;
  technical_details?: {
    security?: Record<string, unknown>;
    analysis?: Record<string, unknown>;
    claim?: string;
    prompt_preview?: {
      prompt_version?: string;
      system_prompt?: string;
      user_prompt?: string;
    };
  };
};