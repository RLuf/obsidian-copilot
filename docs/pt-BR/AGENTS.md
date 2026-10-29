# AGENTS.md — docs/pt-BR

Instruções para agentes de IA que trabalham nas traduções pt-BR deste fork (mantido por Roger Luft / veilwaker). Para o restante do repositório, vale o `AGENTS.md` da raiz (upstream).

## Escopo

- Tudo que é tradução fica em `docs/pt-BR/`. Não editar os arquivos do upstream (`src/`, `docs/*.md` da raiz etc.): o fork precisa continuar sincronizável sem conflito.
- `skills/<nome>-ptbr/` são skills **instaláveis**: basta copiar a pasta para `<pasta do Copilot>/skills/` no vault (o padrão é `copilot/skills/`). Elas **não substituem** as embutidas, ficam ao lado delas.
- Os scripts `.sh`, `.cmd` e `.ps1` são cópias exatas dos que as skills embutidas usam. Não traduzir nem alterar.
- Código, comandos e YAML ficam idênticos ao original; só o texto corrido é traduzido.

## Índice e workflow

- `index.json` registra, para cada tradução, o arquivo de origem no upstream e o commit traduzido (`source_sha`).
- `.github/workflows/ptbr-index.yml` roda `.github/scripts/ptbr_index.py` toda semana. Quando a origem muda, ele marca a tradução como `desatualizada`, regenera a tabela do `README.md` e abre um PR mencionando `@jules`, `@copilot` e `@gemini-code-assist`.
- Ao atualizar uma tradução: corrigir o texto, colocar o novo commit em `source_sha`, rodar `python .github/scripts/ptbr_index.py` e registrar no `CHANGELOG.md`.

## Regras

- Não fazer merge sem a revisão do Jules (e de Copilot/Gemini, quando disponíveis).
- Manter os avisos de licença (AGPL-3.0 do Copilot; MIT do kepano para a obsidian-bases). Ver `NOTICE.md`.
- Nunca versionar pastas `archived/` ou `historico/`, nem segredos.
