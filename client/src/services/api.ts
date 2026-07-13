const API_URL = "http://127.0.0.1:8000";

export async function analyzeRepository(url: string) {
  const response = await fetch(`${API_URL}/repository/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to analyze repository");
  }

  return response.json();
}