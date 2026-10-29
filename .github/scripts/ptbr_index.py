#!/usr/bin/env python3
"""Atualiza o indice das traducoes pt-BR (docs/pt-BR/index.json + README.md).

Para cada entrada, consulta no upstream o ultimo commit que alterou o arquivo
de origem. Se for diferente do commit traduzido (`source_sha`), marca a
traducao como "desatualizada". Regenera a tabela do README entre os marcadores
e escreve `changed=true|false` em $GITHUB_OUTPUT.

Uso: GITHUB_TOKEN=... python .github/scripts/ptbr_index.py
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "docs" / "pt-BR" / "index.json"
README = ROOT / "docs" / "pt-BR" / "README.md"
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"


def latest_sha(repo, branch, path, token):
    url = f"https://api.github.com/repos/{repo}/commits?path={path}&sha={branch}&per_page=1"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    return data[0]["sha"] if data else None


def table(idx):
    repo, branch = idx["upstream"], idx["branch"]
    rows = [
        "| Tradução | Origem (upstream) | Commit traduzido | Último commit upstream | Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for e in idx["entries"]:
        src = e["source"]
        rows.append(
            f"| [{e['translation']}]({e['translation']}) "
            f"| [`{src}`](https://github.com/{repo}/blob/{branch}/{src}) "
            f"| `{e['source_sha'][:7]}` | `{(e.get('upstream_sha') or e['source_sha'])[:7]}` "
            f"| {e['status']} |"
        )
    rows.append("")
    rows.append(f"_Verificado em: {idx.get('checked_at', 'n/d')}_")
    return "\n".join(rows)


def main():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    before = json.dumps(idx["entries"], sort_keys=True)

    for e in idx["entries"]:
        up = latest_sha(idx["upstream"], idx["branch"], e["source"], token)
        if up is None:
            e["status"] = "origem não encontrada"
            continue
        e["upstream_sha"] = up
        e["status"] = "atualizada" if up == e["source_sha"] else "desatualizada"

    changed = json.dumps(idx["entries"], sort_keys=True) != before
    if changed:
        from datetime import datetime, timezone
        idx["checked_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    text = README.read_text(encoding="utf-8")
    a, b = text.index(START) + len(START), text.index(END)
    README.write_text(text[:a] + "\n" + table(idx) + "\n" + text[b:], encoding="utf-8")

    stale = [e["translation"] for e in idx["entries"] if e["status"] != "atualizada"]
    print("changed=" + str(changed).lower())
    print("desatualizadas: " + (", ".join(stale) or "nenhuma"))
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(f"changed={str(changed).lower()}\n")
            fh.write(f"stale={' '.join(stale)}\n")


if __name__ == "__main__":
    sys.exit(main())
