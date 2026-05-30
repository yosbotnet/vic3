# vic3

Personal Victoria 3 knowledge base — YouTube tutorials and a campaign playthrough distilled into a strategy wiki.

📖 **Read it:** <https://yosbotnet.github.io/vic3/>

## Layout

- `transcripts/` — raw YouTube captions (39 videos)
- `notes/` — per-video study notes
- `wiki/` — synthesized topic-organized strategy wiki (the published site)
- `scripts/` — fetch & convert tooling
- `docs/superpowers/` — design specs and implementation plans

## Sources

- Tutorials: [Generalist Gaming Victoria 3 Tutorials](https://www.youtube.com/playlist?list=PL1QPWs6KwuOCu0dfHoKgsySV3xE_eQ9Z8)
- Comprehensive tutorial: [The Comprehensive Victoria 3 Tutorial (2025) | Iberian Twilight](https://www.youtube.com/watch?v=P_PzglCFo9I) by Tarkusarkusar
- Campaigns: [Victoria 3: Japan Becomes a Superpower! | The Great Wave](https://www.youtube.com/playlist?list=PLsT4scrqjQbTSBvfQQBpMnGQzcwkteRvp); [Restoring the Spanish Empire as Cuba](https://www.youtube.com/watch?v=rKZwT9G7Dq8)

## Build locally

```sh
pip install mkdocs-material
mkdocs serve
```

The wiki is auto-deployed to GitHub Pages on every push to `main` via `.github/workflows/docs.yml`.
