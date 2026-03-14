type ScoreBadgeProps = {
  score: number;
  risk: string;
};

export default function ScoreBadge({ score, risk }: ScoreBadgeProps) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur">
      <p className="text-sm text-zinc-400">Authenticity Score</p>
      <p className="mt-2 text-3xl font-semibold text-white">{score.toFixed(2)}</p>

      <div className="mt-3 inline-flex rounded-full border border-white/10 bg-black/20 px-3 py-1 text-sm text-zinc-200">
        Risk: {risk}
      </div>
    </div>
  );
}