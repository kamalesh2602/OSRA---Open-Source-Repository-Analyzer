import SearchBar from "./SearchBar";

interface HeroProps {
  setRepository: (repo: any) => void;
}

export default function Hero({ setRepository }: HeroProps) {
  return (
    <section className="flex min-h-[70vh] flex-col items-center justify-center px-6">
      <div className="max-w-4xl text-center">

        <h1 className="mb-6 text-6xl font-black">
          Open Source Repository Analyzer
        </h1>

        <p className="mb-12 text-lg text-slate-400">
          Analyze any public GitHub repository using Machine Learning and GitHub Analytics.
        </p>

        <SearchBar setRepository={setRepository} />

      </div>
    </section>
  );
}