import os
import re

css = """
    /* ===== SEARCH BAR ===== */
    .search-wrap {
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 3rem auto 1rem;
      max-width: 600px;
      width: 90%;
    }

    .search-box {
      width: 100%;
      position: relative;
      display: flex;
      align-items: center;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 50px;
      padding: 0.5rem 1.5rem;
      transition: all 0.3s ease;
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
    }

    .search-box:focus-within {
      border-color: var(--a1);
      box-shadow: 0 0 20px color-mix(in srgb, var(--a1) 20%, transparent);
      transform: translateY(-2px);
    }

    .search-box svg {
      color: var(--muted);
      margin-right: 12px;
      flex-shrink: 0;
      transition: color 0.3s ease;
    }

    .search-box:focus-within svg {
      color: var(--a1);
    }

    .search-box input {
      width: 100%;
      background: transparent;
      border: none;
      color: var(--text);
      font-size: 1.05rem;
      padding: 0.75rem 0;
      outline: none;
      font-family: inherit;
    }

    .search-box input::placeholder {
      color: var(--muted);
    }

    /* HEADER */
"""

path = r"d:\Yogi\Yogesh\quick-do-pdf\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("    /* HEADER */", css)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("CSS injected successfully")
