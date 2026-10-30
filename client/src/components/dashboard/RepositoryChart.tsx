
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
    Legend,
} from "chart.js";

import { Bar } from "react-chartjs-2";

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
    Legend
);

interface Props {
    repository: any;
}

export default function RepositoryChart({ repository }: Props) {
    const data = {
        labels: [
            "Stars",
            "Forks",
            "Watchers",
            "Issues",
        ],

        datasets: [
            {
                label: "Repository Metrics",

                data: [
                    repository.stars,
                    repository.forks,
                    repository.watchers,
                    repository.open_issues,
                ],

                backgroundColor: [
                    "rgba(56, 189, 248, 0.75)",
                    "rgba(167, 139, 250, 0.75)",
                    "rgba(52, 211, 153, 0.75)",
                    "rgba(251, 146, 60, 0.75)",
                ],

                borderColor: [
                    "#38bdf8",
                    "#a78bfa",
                    "#34d399",
                    "#fb923c",
                ],

                borderWidth: 1,
                borderRadius: 8,
            },
        ],
    };

    const options = {
        responsive: true,
        maintainAspectRatio: true,

        plugins: {
            legend: {
                labels: {
                    color: "#e2e8f0",
                },
            },

            tooltip: {
                enabled: true,
            },
        },

        scales: {
            x: {
                ticks: {
                    color: "#cbd5e1",
                },
                grid: {
                    color: "rgba(255,255,255,0.08)",
                },
            },

            y: {
                beginAtZero: true,
                ticks: {
                    color: "#cbd5e1",
                },
                grid: {
                    color: "rgba(255,255,255,0.08)",
                },
            },
        },
    };

    return (
        <div className="rounded-3xl border border-white/10 bg-white/5 p-6">
            <h2 className="mb-6 text-xl font-semibold">
                Repository Metrics
            </h2>

            <Bar data={data} options={options} />
        </div>
    );
}
