"use client";

import { useState } from "react";
import type { AnalysisResponse } from "@/types/analysis";

type UploadFormProps = {
  onResult: (result: AnalysisResponse) => void;
};

export default function UploadForm({ onResult }: UploadFormProps) {
  const [file, setFile] = useState<File | null>(null);
  const [claim, setClaim] = useState("Is this image AI-generated?");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    if (!file) {
      setError("Please select an image first.");
      return;
    }

    setError("");
    setLoading(true);

    try {
      const apiBaseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
      console.log("API URL:", apiBaseUrl);

      if (!apiBaseUrl) {
        throw new Error("Missing NEXT_PUBLIC_API_BASE_URL");
      }

      const formData = new FormData();
      formData.append("file", file);
      formData.append("claim", claim);

      const response = await fetch(`${apiBaseUrl}/analyze/image`, {
        method: "POST",
        body: formData,
      });

      console.log("Response status:", response.status);

      if (!response.ok) {
        const text = await response.text();
        throw new Error(text || "Request failed.");
      }

      const data: AnalysisResponse = await response.json();
      console.log("Analysis result:", data);

      onResult(data);
    } catch (err) {
      console.error("Upload error:", err);
      setError(err instanceof Error ? err.message : "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="rounded-2xl border border-white/10 bg-white/5 p-6 shadow-xl backdrop-blur"
    >
      <div className="space-y-4">
        <div>
          <label className="mb-2 block text-sm font-medium text-zinc-200">
            Upload image
          </label>
          <input
            type="file"
            accept="image/png,image/jpeg,image/webp"
            onChange={(e) => {
              const selectedFile = e.target.files?.[0] ?? null;
              setFile(selectedFile);
            }}
            className="block w-full rounded-xl border border-white/10 bg-black/20 p-3 text-sm text-zinc-200"
          />
          {file ? (
            <p className="mt-2 text-xs text-zinc-400">Selected: {file.name}</p>
          ) : null}
        </div>

        <div>
          <label className="mb-2 block text-sm font-medium text-zinc-200">
            Claim / question
          </label>
          <input
            type="text"
            value={claim}
            onChange={(e) => setClaim(e.target.value)}
            placeholder="Is this image AI-generated?"
            className="block w-full rounded-xl border border-white/10 bg-black/20 p-3 text-sm text-zinc-200"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="inline-flex rounded-xl bg-white px-4 py-2 text-sm font-medium text-black transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {loading ? "Analyzing..." : "Analyze Image"}
        </button>

        {error ? <p className="text-sm text-red-400">{error}</p> : null}
      </div>
    </form>
  );
}