# Etapa 4 — Revisão arquitetural com apoio de IA

## 1. Resumo da arquitetura atual (gerado a partir do código real)

**Módulos** (`src/`, 6 arquivos, 217 linhas):

| Módulo | Responsabilidade | Dependências externas |
|---|---|---|
| `hello.py` | script de saudação inicial, 1 linha | nenhuma |
| `validador_email.py` | valida e-mail via regex + regras RFC | stdlib `re` |
| `validador_email_simples.py` | valida e-mail estruturalmente, sem regex | nenhuma |
| `validador_cep.py` | valida CEP brasileiro | nenhuma |
| `validador_placa.py` | valida placa de veículo (antigo + Mercosul) | nenhuma |
| `validador_cartao_credito.py` | valida número de cartão via Luhn | nenhuma |
| `validador_hora.py` | valida horário HH:MM | nenhuma |

**Dependências entre módulos:** nenhuma. `grep -n "^import\|^from" src/*.py`
retorna uma única ocorrência (`validador_email.py` importa `re`, da
biblioteca padrão). Nenhum arquivo em `src/` importa outro arquivo de
`src/`.

**Testes** (`tests/`, 5 arquivos, 233 linhas): um arquivo de teste por
módulo validador, cada um importando exatamente o módulo correspondente
via `sys.path.insert` apontando para `src/`. Não há fixtures ou utilitários
de teste compartilhados entre arquivos.

**Acoplamento:** zero acoplamento entre módulos de `src/`. Cada validador é
uma função pura (`str -> bool`), sem estado, sem I/O, sem dependência de
outro validador. O único "acoplamento" real do projeto é estrutural (todo
teste depende do mesmo truque de `sys.path.insert` para achar `src/`, em
vez de o projeto ser instalável como pacote).

**Duplicação (não é acoplamento, mas é uma repetição de padrão):** 4 dos 5
validadores (`cep`, `placa`, `cartao_credito`, `hora`) repetem a mesma
sequência: checar `isinstance(x, str)`, normalizar removendo separadores
(`-`, espaço), validar tamanho/formato. Não compartilham código nenhum
entre si — cada um reimplementa a checagem de tipo e a normalização do
zero.

## 2. Decisão arquitetural

**O projeto está no tamanho certo. Não deve virar mais modular do que já é
nem justifica extrair um serviço.**

Critérios usados (vistos em aula):

- **Tamanho:** 217 linhas de código de produção, 6 arquivos. Abaixo de
  qualquer limiar razoável para dividir em subpacotes ou serviços — extrair
  serviço faz sentido quando há necessidade de deploy independente, escala
  independente, ou times diferentes donos de partes diferentes do código;
  nenhuma dessas condições existe aqui (projeto de laboratório de uma
  pessoa).
- **Acoplamento:** já é o mínimo possível (zero entre módulos). Modularizar
  mais não reduziria acoplamento porque não há acoplamento a reduzir —
  criar subpastas por "tipo de validador" ou um pacote `validadores/`
  adicionaria estrutura sem remover nenhuma dependência real.
- **Coesão:** alta dentro de cada arquivo (uma função, uma responsabilidade,
  um contrato `str -> bool` testado). Isso é o oposto do sintoma que pede
  divisão (um módulo fazendo coisas não relacionadas).
- **Contratos:** já são claros e uniformes (mesma assinatura, mesmo tipo de
  retorno, docstring explicando o que valida e o que não valida) — não há
  contrato implícito ou ambíguo que uma extração resolveria.

**Único ponto de melhoria real identificado, e que NÃO justifica extração
de serviço:** a duplicação de "checar tipo + normalizar string" entre os 4
validadores citados poderia virar um helper pequeno (`src/_texto.py` com
algo como `normalizar(valor: str, remover: str) -> str | None`), reduzindo
~3-4 linhas repetidas por arquivo. Isso é um refactor de nível "função
compartilhada dentro do mesmo pacote", não uma mudança arquitetural — é
justamente o tipo de decisão que os critérios acima ajudam a não confundir:
duplicação pequena e localizada não é sinal de acoplamento nem de módulo
grande demais, é só uma oportunidade de DRY que pode esperar até incomodar
de verdade (ex.: quando aparecer o 6º ou 7º validador com o mesmo padrão).
