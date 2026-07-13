import { useState } from "react";
import { Search } from "lucide-react";

export default function SearchBar() {
  const [url, setUrl] = useState("");

  function handleAnalyze() {
    console.log(url);
  }

  return (
    <div className="mx-auto flex max-w-3xl gap-4">

      <input
        type="text"
        placeholder="https://github.com/facebook/react"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="flex-1 rounded-2xl border border-white/10 bg-white/5 px-6 py-4 outline-none backdrop-blur-xl transition focus:border-blue-500"
      />

      <button
        onClick={handleAnalyze}
        className="flex items-center gap-2 rounded-2xl bg-blue-600 px-8 py-4 font-semibold transition hover:bg-blue-500"
      >
        <Search size={20} />
        Analyze
      </button>

    </div>
  );
}