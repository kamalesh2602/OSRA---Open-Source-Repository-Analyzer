interface Props {
  repository: any;
}

function Card({ title, value }: { title: string; value: any }) {
  return (
    <div className="rounded-3xl border border-white/10 bg-white/5 p-6">
      <h3 className="text-slate-400">{title}</h3>

      <p className="mt-3 text-3xl font-bold">
        {value}
      </p>
    </div>
  );
}

export default function OverviewCards({ repository }: Props) {
  return (
    <div className="mx-auto mb-20 grid max-w-7xl grid-cols-1 gap-6 px-8 md:grid-cols-2 lg:grid-cols-3">

      <Card title="⭐ Stars" value={repository.stars} />

      <Card title="🍴 Forks" value={repository.forks} />

      <Card title="🐞 Open Issues" value={repository.open_issues} />

      <Card title="💻 Language" value={repository.language} />

      <Card title="👀 Watchers" value={repository.watchers} />

      <Card title="📦 Size" value={repository.size} />

    </div>
  );
}