// Light/dark toggle. The initial theme is set by the inline script in layouts/_partials/head/js.html.
const root = document.documentElement;
const lightModePref = window.matchMedia("(prefers-color-scheme: light)");

function setTheme(theme, persist) {
  root.setAttribute("data-theme", theme);
  if (persist) {
    try {
      localStorage.setItem("theme", theme);
    } catch (e) {}
  }
  document.querySelectorAll(".theme-toggle").forEach((button) => {
    button.setAttribute("aria-checked", String(theme === "dark"));
  });
}

setTheme(root.getAttribute("data-theme") || "dark", false);

document.querySelectorAll(".theme-toggle").forEach((button) => {
  button.addEventListener("click", () => {
    setTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark", true);
  });
});

// Follow OS changes, as the Astro Cactus theme does
lightModePref.addEventListener("change", (e) => setTheme(e.matches ? "light" : "dark", true));
