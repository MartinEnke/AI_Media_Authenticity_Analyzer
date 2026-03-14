"use client";

import { useState } from "react";
import UploadForm from "@/components/UploadForm";
import ResultCard from "@/components/ResultCard";
import ScoreBadge from "@/components/ScoreBadge";
import type { AnalysisResponse } from "@/types/analysis";

export default function HomePage() {
  const [result, setResult] = useState<AnalysisResponse | null>(null);

  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <div className="mx-auto max-w-5xl px-6 py-12">
        <header className="mb-10">
          <p className="text-sm uppercase tracking-[0.2em] text-zinc-500">
            AI Engineering Portfolio Project
          </p>
          <h1 className="mt-3 text-4xl font-bold tracking-tight">
            AI Media Authenticity Analyzer
          </h1>
          <p className="mt-4 max-w-2xl text-zinc-400">
            Analyze images for heuristic authenticity signals, structured reasoning,
            and explainable risk classification.
          </p>
        </header>

        <div className="grid gap-6 lg:grid-cols-[1fr_1.2fr]">
          <UploadForm onResult={setResult} />

          <div className="space-y-6">
            {result ? (
              <>
                <ScoreBadge
                  score={result.authenticity_score}
                  risk={result.risk_level}
                />

                <ResultCard title="Summary">
                  <p>{result.summary}</p>
                </ResultCard>

                <ResultCard title="Detected Flags">
                  {result.flags.length ? (
                    <ul className="list-disc space-y-1 pl-5">
                      {result.flags.map((flag) => (
                        <li key={flag}>{flag}</li>
                      ))}
                    </ul>
                  ) : (
                    <p>No flags detected.</p>
                  )}
                </ResultCard>

                <ResultCard title="Reasoning">
                  <p>{result.reasoning}</p>
                </ResultCard>

                <ResultCard title="Confidence Explanation">
                  <p>{result.confidence_explanation}</p>
                </ResultCard>

                <ResultCard title="Recommended Action">
                  <p>{result.recommended_action}</p>
                </ResultCard>
              </>
            ) : (
              <div className="rounded-2xl border border-dashed border-white/10 bg-white/[0.03] p-8 text-zinc-500">
                Upload an image to see the authenticity analysis results.
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}