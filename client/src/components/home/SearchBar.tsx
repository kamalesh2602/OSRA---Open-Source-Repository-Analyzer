import { useState } from "react";
import { analyzeRepository } from "../../services/api";

interface SearchBarProps {
  setRepository: (repo: any) => void;
}

export default function SearchBar({ setRepository }: SearchBarProps) {
  const [url, setUrl] = useState("");

  const handleAnalyze = async () => {
    try {
      const data = await analyzeRepository(url);
      setRepository(data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="mx-auto flex max-w-3xl gap-4">

      <input
        type="text"
        placeholder="https://github.com/facebook/react"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="flex-1 rounded-2xl border border-white/10 bg-white/5 px-6 py-4 text-white outline-none"
      />

      <button
        onClick={handleAnalyze}
        className="rounded-2xl bg-blue-600 px-8 py-4 font-semibold hover:bg-blue-500"
      >
        Analyze
      </button>

    </div>
  );
}