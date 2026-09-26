async function loadFlags() {
  const res = await fetch("/api/flags");
  if (!res.ok) return { feature_resta: false };
  return res.json();
}

async function calculate(op, a, b) {
  const res = await fetch(`/api/${op}?a=${a}&b=${b}`);
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.error || "Error en la operación");
  }
  return res.json();
}

document.addEventListener("DOMContentLoaded", async () => {
  const flags = await loadFlags();
  const restaBtn = document.getElementById("btn-resta");
  if (flags.feature_resta) {
    restaBtn.hidden = false;
  }

  document.querySelectorAll("[data-op]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const a = Number(document.getElementById("a").value);
      const b = Number(document.getElementById("b").value);
      const op = btn.getAttribute("data-op");
      try {
        const data = await calculate(op, a, b);
        document.getElementById("result").textContent = `Resultado: ${data.result}`;
      } catch (e) {
        document.getElementById("result").textContent = e.message;
      }
    });
  });
});
