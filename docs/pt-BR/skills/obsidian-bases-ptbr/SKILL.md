---
name: obsidian-bases-ptbr
description: Cria e edita Obsidian Bases (arquivos .base) com esquemas YAML, filtros, fórmulas, propriedades, resumos e visualizações válidos. Use para visualizações do Obsidian no estilo banco de dados ou quando o usuário mencionar Bases, arquivos .base, visualizações de tabela/cartões/lista, filtros, fórmulas ou resumos.
license: MIT
metadata:
  idioma: pt-BR
  traducao: "Roger Luft (veilwaker), 2026"
  origem: "logancyang/obsidian-copilot src/builtinSkills/obsidianSkills.ts @ 9198962, adaptado de kepano/obsidian-skills @ a1dc48e68138490d522c04cbf5822214c6eb1202"
---

# Obsidian Bases (pt-BR)

## Fluxo de trabalho

1. Leia o arquivo <code>.base</code> existente antes de editá-lo.
2. Defina o escopo global com <code>filters</code>.
3. Adicione valores calculados em <code>formulas</code> somente quando necessário.
4. Configure os nomes de exibição das propriedades e uma ou mais visualizações.
5. Valide o YAML, as referências de fórmulas, as aspas e as operações de data/duração.
6. Abra ou consulte a Base no Obsidian quando a CLI estiver disponível.

## Esquema

~~~yaml
filters:
  and:
    - 'file.ext == "md"'
    - 'status != "archived"'

formulas:
  days_until_due: 'if(due, (date(due) - today()).days.round(), "")'

properties:
  status:
    displayName: Status
  formula.days_until_due:
    displayName: "Days Until Due"

summaries:
  mean_rounded: 'values.mean().round(2)'

views:
  - type: table
    name: Active
    limit: 50
    filters:
      and:
        - 'status != "done"'
    order:
      - file.name
      - status
      - due
      - formula.days_until_due
    sort:
      - property: due
        direction: ASC
    groupBy:
      property: status
      direction: ASC
    summaries:
      formula.days_until_due: Average
~~~

As visualizações podem ser <code>table</code>, <code>cards</code> ou <code>list</code>.
Uma visualização <code>map</code> depende de suporte compatível a mapas.

<code>order</code> define quais propriedades uma visualização mostra; <code>sort</code> define a ordem das linhas, uma entrada <code>property</code>/<code>direction</code> por chave, aplicadas em sequência. O Obsidian só ordena por propriedades que também estejam listadas em <code>order</code>, então inclua ali toda propriedade de ordenação.

## Filtros e propriedades

Os filtros podem ser uma única expressão ou objetos <code>and</code>, <code>or</code> e <code>not</code> aninhados recursivamente. Os namespaces de propriedades são:

- propriedades da nota: <code>status</code> ou <code>note.status</code>
- metadados do arquivo: <code>file.name</code>, <code>file.path</code>, <code>file.folder</code>, <code>file.ctime</code>, <code>file.mtime</code>, <code>file.tags</code>, <code>file.links</code> e <code>file.backlinks</code>
- fórmulas: <code>formula.days_until_due</code>

Use <code>file.hasTag()</code>, <code>file.hasLink()</code>, <code>file.hasProperty()</code> e <code>file.inFolder()</code> para relações indexadas de arquivos. O valor <code>this</code> refere-se à própria Base, à nota que a incorpora ou ao arquivo ativo, dependendo de onde a Base é renderizada.

## Regras de fórmulas

- Proteja propriedades opcionais com <code>if()</code>.
- A subtração de datas retorna uma Duration, não um número. Acesse <code>.days</code>, <code>.hours</code> ou outro campo numérico antes de chamar métodos numéricos como <code>.round()</code>. Arredonde contagens de dias: numa mudança de horário de verão, <code>.days</code> pode ser fracionário.
- Todo <code>formula.X</code> usado por uma visualização ou configuração de propriedade precisa ter uma entrada <code>X</code> correspondente em <code>formulas</code>.
- Envolva fórmulas que contenham aspas duplas em aspas simples do YAML.
- Coloque entre aspas strings YAML que contenham caracteres especiais, especialmente dois-pontos e pontuação no início.

Leia a [Referência de funções](references/FUNCTIONS_REFERENCE.md) para funções e operações específicas por tipo, e os [Exemplos](references/EXAMPLES.md) para Bases completas de controle de tarefas e de notas diárias.

## Checklist de validação

- O documento é interpretado como YAML e tem uma lista <code>views</code>.
- <code>order</code>, <code>groupBy</code> e os resumos da visualização referenciam propriedades definidas de nota, de arquivo ou de fórmula.
- As aspas das fórmulas estão balanceadas e a matemática de duração acessa um campo numérico.
- Toda propriedade em <code>sort</code> também aparece no <code>order</code> daquela visualização.
- Uma incorporação nomeia a visualização exatamente como o seu <code>name</code>:

~~~markdown
![[My Base.base#View Name]]
~~~

## Atribuição

Tradução pt-BR © 2026 Roger Luft (veilwaker). Adaptado pelo Copilot for Obsidian a partir de <code>kepano/obsidian-skills</code> na revisão <code>a1dc48e68138490d522c04cbf5822214c6eb1202</code>, MIT © 2026 Steph Ango (@kepano). Veja <code>LICENSE</code>.
