import SearchBar from "../home/SearchBar";

export default function Hero() {
  return (
    <section className="flex min-h-[85vh] flex-col items-center justify-center px-6">
      <div className="max-w-4xl text-center">

        <h1 className="mb-6 text-6xl font-black leading-tight">
          Open Source
          <br />
          Repository Analyzer
        </h1>

        <p className="mb-12 text-lg text-slate-400">
          Analyze any public GitHub repository using Machine Learning,
          GitHub metadata and interactive analytics.
        </p>

        <SearchBar />

      </div>
    </section>
  );
}