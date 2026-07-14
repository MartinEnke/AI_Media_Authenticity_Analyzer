"use client";

import { useState } from "react";

import ResultCard from "@/components/ResultCard";
import ScoreBadge from "@/components/ScoreBadge";
import UploadForm from "@/components/UploadForm";
import type {
  AnalysisResponse,
  AnalysisSignal,
} from "@/types/analysis";


function formatAction(action: string): string {
  return action
    .split("_")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}


function getSignalStatusStyles(signal: AnalysisSignal): string {
  if (signal.risk_contribution >= 0.15) {
    return "border-red-400/20 bg-red-400/10 text-red-200";
  }

  if (signal.risk_contribution > 0) {
    return "border-amber-400/20 bg-amber-400/10 text-amber-200";
  }

  return "border-emerald-400/20 bg-emerald-400/10 text-emerald-200";
}


function SignalCard({ signal }: { signal: AnalysisSignal }) {
  return (
    <article className="rounded-xl border border-white/10 bg-black/20 p-4">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <h3 className="font-medium text-white">{signal.label}</h3>

          <p className="mt-1 text-2xl font-semibold tracking-tight text-white">
            {signal.display_value}
          </p>
        </div>

        <span
          className={`rounded-full border px-3 py-1 text-xs font-medium ${getSignalStatusStyles(
            signal,
          )}`}
        >
          {signal.status}
        </span>
      </div>

      <dl className="mt-4 space-y-2 text-xs">
        <div className="flex flex-col gap-1 sm:flex-row sm:justify-between">
          <dt className="text-zinc-500">Reference</dt>
          <dd className="text-zinc-300 sm:text-right">{signal.reference}</dd>
        </div>

        <div className="flex flex-col gap-1 sm:flex-row sm:justify-between">
          <dt className="text-zinc-500">Score contribution</dt>
          <dd
            className={
              signal.risk_contribution > 0
                ? "font-medium text-amber-300 sm:text-right"
                : "text-zinc-300 sm:text-right"
            }
          >
            {signal.contribution_label}
          </dd>
        </div>
      </dl>

      <p className="mt-4 border-t border-white/10 pt-4 text-sm leading-6 text-zinc-400">
        {signal.explanation}
      </p>
    </article>
  );
}


export default function HomePage() {
  const [result, setResult] = useState<AnalysisResponse | null>(null);

  const signals = result?.technical_details?.analysis?.signals ?? [];
  const mediaProfile =
    result?.technical_details?.analysis?.media_profile;

  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <div className="mx-auto max-w-6xl px-6 py-12">
        <header className="mb-10">
          <p className="text-sm uppercase tracking-[0.2em] text-zinc-500">
            AI Engineering Portfolio Project
          </p>

          <h1 className="mt-3 text-4xl font-bold tracking-tight">
            AI Media Authenticity Analyzer
          </h1>

          <p className="mt-4 max-w-2xl text-zinc-400">
            Analyze images for heuristic authenticity signals, structured
            reasoning, and explainable risk classification.
          </p>

          <p className="mt-3 max-w-2xl text-xs leading-5 text-zinc-600">
            Results are heuristic indicators, not proof that an image is
            authentic or AI-generated.
          </p>
        </header>

        <div className="grid items-start gap-6 lg:grid-cols-[0.9fr_1.3fr]">
          <div className="lg:sticky lg:top-6">
            <UploadForm onResult={setResult} />
          </div>

          <div className="space-y-6">
            {result ? (
              <>
                <ScoreBadge
                  score={result.risk_score}
                  risk={result.risk_level}
                />

                {mediaProfile ? (
                  <ResultCard title="Detected Media Profile">
                    <div className="flex flex-wrap items-start justify-between gap-4">
                      <div>
                        <p className="text-2xl font-semibold capitalize text-white">
                          {mediaProfile.type.replaceAll("_", " ")}
                        </p>

                        <p className="mt-1 text-sm text-zinc-400">
                          Profile confidence:{" "}
                          <span className="font-medium capitalize text-zinc-200">
                            {mediaProfile.confidence}
                          </span>
                        </p>
                      </div>

                      <span className="rounded-full border border-sky-400/20 bg-sky-400/10 px-3 py-1 text-xs font-medium text-sky-200">
                        Context classification
                      </span>
                    </div>

                    {mediaProfile.reasons.length > 0 ? (
                      <div className="mt-5">
                        <p className="mb-2 text-xs font-medium uppercase tracking-wide text-zinc-500">
                          Classification signals
                        </p>

                        <ul className="space-y-2">
                          {mediaProfile.reasons.map((reason) => (
                            <li
                              key={reason}
                              className="flex gap-2 text-sm text-zinc-300"
                            >
                              <span className="text-zinc-600">•</span>
                              <span>{reason}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    ) : null}

                    <p className="mt-5 border-t border-white/10 pt-4 text-xs leading-5 text-zinc-500">
                      {mediaProfile.disclaimer}
                    </p>
                  </ResultCard>
                ) : null}

                <ResultCard title="Summary">
                  <p>{result.summary}</p>
                </ResultCard>

                {signals.length > 0 ? (
                  <ResultCard title="Analyzed Signals">
                    <div className="grid gap-4 xl:grid-cols-2">
                      {signals.map((signal) => (
                        <SignalCard key={signal.id} signal={signal} />
                      ))}
                    </div>
                  </ResultCard>
                ) : null}

                <ResultCard title="Detected Flags">
                  {result.flags.length > 0 ? (
                    <div className="flex flex-wrap gap-2">
                      {result.flags.map((flag) => (
                        <span
                          key={flag}
                          className="rounded-full border border-amber-400/20 bg-amber-400/10 px-3 py-1 text-xs text-amber-200"
                        >
                          {flag}
                        </span>
                      ))}
                    </div>
                  ) : (
                    <p>No heuristic flags were detected.</p>
                  )}
                </ResultCard>

                <ResultCard title="Reasoning">
                  <p>{result.reasoning}</p>
                </ResultCard>

                <ResultCard title="Confidence Explanation">
                  <p>{result.confidence_explanation}</p>
                </ResultCard>

                <ResultCard title="Recommended Action">
                  <p>{formatAction(result.recommended_action)}</p>
                </ResultCard>

                {result.technical_details?.mcp_tool_trace?.length ? (
                  <ResultCard title="Analysis Pipeline">
                    <ol className="space-y-3">
                      {result.technical_details.mcp_tool_trace.map(
                        (entry, index) => (
                          <li
                            key={`${entry.tool}-${index}`}
                            className="flex items-center justify-between gap-4 rounded-xl border border-white/10 bg-black/20 px-4 py-3"
                          >
                            <div className="flex items-center gap-3">
                              <span className="flex h-7 w-7 items-center justify-center rounded-full bg-white/10 text-xs text-zinc-300">
                                {index + 1}
                              </span>

                              <div>
                                <p className="font-medium text-zinc-200">
                                  {entry.tool}
                                </p>

                                <p className="text-xs text-zinc-500">
                                  {entry.transport}
                                </p>
                              </div>
                            </div>

                            <span className="text-xs font-medium text-emerald-300">
                              {entry.status}
                            </span>
                          </li>
                        ),
                      )}
                    </ol>
                  </ResultCard>
                ) : null}
              </>
            ) : (
              <div className="rounded-2xl border border-dashed border-white/10 bg-white/[0.03] p-8 text-zinc-500">
                <p className="font-medium text-zinc-400">
                  No analysis available
                </p>

                <p className="mt-2 text-sm">
                  Upload an image to inspect its forensic heuristic signals.
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}