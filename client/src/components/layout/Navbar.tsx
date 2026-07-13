// import { Github } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="w-full border-b border-white/10 backdrop-blur-xl">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-5">
        <h1 className="text-xl font-bold tracking-wide text-white">
          OSRA
        </h1>

        <a
          href="https://github.com"
          target="_blank"
          rel="noreferrer"
          className="rounded-xl border border-white/10 bg-white/5 px-4 py-2 hover:bg-white/10"
        >
          GitHub
        </a>
      </div>
    </nav>
  );
}