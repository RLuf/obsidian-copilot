---
name: copilot-youtube-transcript-ptbr
description: Busca a transcrição de um vídeo do YouTube usando o Copilot Plus. Use quando o usuário compartilhar uma URL do YouTube e quiser o conteúdo, um resumo ou citações. Requer uma licença ativa do Copilot Plus.
license: AGPL-3.0
metadata:
  idioma: pt-BR
  traducao: "Roger Luft (veilwaker), 2026"
  origem: "logancyang/obsidian-copilot src/builtinSkills/builtinSkills.ts @ e3c91bf (skill embutida copilot-youtube-transcript)"
---

# Copilot: transcrição do YouTube (pt-BR)

Busca a transcrição de um vídeo do YouTube por meio do Copilot Plus.

## Como executar

Encontre o caminho absoluto deste arquivo SKILL.md no disco e então execute o script ao lado dele que corresponde ao sistema operacional. Execute-o como comando de shell com a sua ferramenta de comandos de shell (por exemplo, `Bash` no Claude Code, `shell` no OpenCode, `exec_command` no Codex). O comando está em sintaxe de shell, não em JavaScript nem TypeScript: nunca o passe como código de uma ferramenta de execução de código.
Não é necessário nenhum runtime adicional — `sh` (macOS/Linux) e `cmd`/PowerShell (Windows) estão sempre presentes.

No macOS ou Linux:

```bash
sh "/absolute/path/to/this/skill/directory/youtube-transcript.sh" "<youtube-url>"
```

No Windows, execute o wrapper `.cmd`. No PowerShell é obrigatório prefixá-lo com o operador de chamada `&` (o PowerShell trata um caminho entre aspas, sozinho, como string e não o executa); no cmd, execute o caminho entre aspas sem o `&`:

```powershell
& "/absolute/path/to/this/skill/directory/youtube-transcript.cmd" "<youtube-url>"
```

Ambos imprimem o resultado no stdout.

## Se o Copilot Plus não estiver ativo

Se o script terminar dizendo que o Copilot Plus está indisponível, NÃO tente de novo. Faça o que a mensagem diz: recorra à sua própria capacidade nativa equivalente para atender ao pedido, quando tiver uma (caso contrário, diga ao usuário que não está disponível) — nunca recuse nem bloqueie o usuário. Só mencione fazer upgrade ou renovar o Copilot Plus quando a mensagem do script convidar explicitamente a isso, e mantenha esse aviso curto e cordial.

## Licença

Tradução pt-BR © 2026 Roger Luft (veilwaker). Original © Logan Yang e contribuidores (Copilot for Obsidian), sob AGPL-3.0. Os scripts desta pasta são cópias sem alteração dos scripts da skill embutida.
