# LOCKIN OS

A personal operating system for exam prep, training, money and building. It's one HTML file with no framework, no build step and no backend.

**Live:** https://parzzivalll.github.io/lockin-os/ (on a phone: open it, then Share → *Add to Home Screen*)

## Modules

| | |
|---|---|
| **COMMAND** | What's next, how much is left, required pace, checkpoint, streak |
| **GOALS** | Vision board with Pinterest boards and a soundtrack music player (songs saved in your browser, lock-screen controls) |
| **BITSAT** | Queue engine (prerequisites, checkpoints), velocity engine, official syllabus, drill bank, PYQ links, full-length mock simulator with analysis, error log |
| **COLLEGE** | Attendance: how many classes you can still miss. Also labs (record + observation), courses, assignments, question bank |
| **TASKS / HABITS** | Todo list; Loop-style habit strength scores |
| **BODY** | Posture, gym, diet |
| **FINANCE** | Trading terminal, journal, P&L analytics, risk engine, watch-only Solana wallets, cash flow, India tax estimate, calendar |
| **BUILD / LOG** | Projects and startups; monthly review |

## Run

Open `index.html`, or serve the folder:

```bash
python -m http.server 8000
```

## Data and privacy

- Everything is stored in your browser's `localStorage`. Nothing leaves it unless you turn on **Settings → Sync**, which uses *your own* free Supabase project, locked to your login with row-level security. Or use **Export / Import JSON**.
- Wallets are **watch-only**, using public addresses. It never asks for a seed phrase or private key.
- Question imports stay in your browser. No third-party question content ships in this repo.
- Tax numbers are estimates, not advice.

## Personal builds

Keep a private copy with your own seed data, wrapped in markers:

```js
/*@@P*/ personal code /*@@E public replacement @@X*/
```

```bash
python tools/build_public.py path/to/private.html index.html
```

The build swaps in the public side and refuses to write if a deny-listed token survives.
