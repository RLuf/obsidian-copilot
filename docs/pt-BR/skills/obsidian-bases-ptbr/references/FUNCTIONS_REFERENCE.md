# Referência de funções das Bases

## Funções globais

| Função | Finalidade |
| --- | --- |
| <code>date(value)</code> | Interpreta uma string de data |
| <code>duration(value)</code> | Interpreta uma string de duração |
| <code>now()</code> / <code>today()</code> | Data e hora atuais / data atual |
| <code>if(condition, yes, no?)</code> | Valor condicional |
| <code>number(value)</code> | Converte para número |
| <code>link(path, display?)</code> | Cria um link |
| <code>file(path)</code> | Resolve um objeto de arquivo |
| <code>list(value)</code> | Normaliza um valor para lista |
| <code>image(path)</code> / <code>icon(name)</code> | Cria valores renderizáveis |

## Métodos comuns

- String: <code>contains</code>, <code>startsWith</code>, <code>endsWith</code>, <code>lower</code>, <code>trim</code>, <code>replace</code>, <code>split</code>, <code>isEmpty</code>.
- Número: <code>abs</code>, <code>ceil</code>, <code>floor</code>, <code>round</code>, <code>toFixed</code>.
- Lista: <code>contains</code>, <code>containsAll</code>, <code>containsAny</code>, <code>filter</code>, <code>map</code>, <code>reduce</code>, <code>flat</code>, <code>join</code>, <code>sort</code>, <code>unique</code>.
- Arquivo: <code>asLink</code>, <code>hasLink</code>, <code>hasTag</code>, <code>hasProperty</code>, <code>inFolder</code>.
- Link: <code>asFile</code>, <code>linksTo</code>.
- Objeto: <code>keys</code>, <code>values</code>, <code>isEmpty</code>.
- Expressão regular: <code>matches</code>.

Os campos de data incluem <code>year</code>, <code>month</code>, <code>day</code>, <code>hour</code>, <code>minute</code> e <code>second</code>. Os métodos de data incluem <code>date()</code>, <code>format()</code>, <code>time()</code> e <code>relative()</code>.

Os campos de duração são <code>days</code>, <code>hours</code>, <code>minutes</code>, <code>seconds</code> e <code>milliseconds</code>.
Duration não suporta diretamente métodos numéricos de arredondamento.
