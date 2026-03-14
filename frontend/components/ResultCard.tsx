type ResultCardProps = {
  title: string;
  children: React.ReactNode;
};

export default function ResultCard({ title, children }: ResultCardProps) {
  return (
    <section className="rounded-2xl border border-white/10 bg-white/5 p-5 shadow-lg backdrop-blur">
      <h2 className="mb-3 text-lg font-semibold text-white">{title}</h2>
      <div className="text-sm leading-6 text-zinc-300">{children}</div>
    </section>
  );
}