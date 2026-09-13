# 2. Manter validadores como funções independentes em `src/`

- Status: Aceito
- Data: 2026-09-13

## Contexto

O projeto acumulou 6 módulos de validação (`validador_email`,
`validador_email_simples`, `validador_cep`, `validador_placa`,
`validador_cartao_credito`, `validador_hora`), todos seguindo o mesmo
padrão: uma função pura `str -> bool`, sem estado, sem import de outro
módulo de `src/`. A Etapa 4 desta atividade pediu uma revisão arquitetural
explícita: o projeto deveria virar mais modular (ex.: um pacote
`validadores/` com subestrutura), extrair um serviço, ou continuar como
está?

A análise do código real (ver `docs/etapa4-arquitetura.md`) mostrou:
217 linhas de produção, zero acoplamento entre módulos de `src/`
(`grep` confirma uma única importação externa, `re`, e nenhuma importação
entre arquivos do projeto), e alta coesão dentro de cada arquivo. A única
repetição encontrada foi um padrão de poucas linhas (checar tipo + limpar
string) repetido em 4 dos 6 validadores — duplicação de código, não
acoplamento.

## Decisão

Manter os validadores como estão: funções independentes, um arquivo por
validador, dentro de `src/`, sem introduzir um pacote/subpasta
`validadores/` nem extrair qualquer parte como serviço separado.

Critérios que sustentam a decisão:

- **Tamanho:** abaixo do limiar que justificaria dividir em subpacotes.
- **Acoplamento:** já é zero; reestruturar em subpastas não reduziria
  dependência nenhuma, só adicionaria indireção.
- **Coesão:** alta — um arquivo, uma responsabilidade, um contrato
  uniforme e testado.
- **Extração de serviço:** não há necessidade de deploy independente,
  escala independente, ou times diferentes donos de partes diferentes do
  código — nenhuma das razões usuais para extrair serviço se aplica a um
  projeto de laboratório de uma pessoa.

A duplicação pontual identificada (checagem de tipo + normalização
repetida em 4 arquivos) é registrada como possível melhoria futura, não
como justificativa para mudança estrutural agora.

## Consequências

- Novos validadores devem seguir o mesmo padrão (`str -> bool`, arquivo
  próprio em `src/`, teste próprio em `tests/`) até que o volume de
  duplicação realmente incomode (ex.: a partir do 6º/7º validador com o
  mesmo trecho repetido, extrair um helper comum como `src/_texto.py`).
- Não criar um pacote `validadores/` nem mover código para uma estrutura
  de serviço enquanto os critérios acima não mudarem (ex.: se o projeto
  crescer para exigir deploy ou API própria).
- Revisitar esta ADR se o número de módulos ou a complexidade de algum
  validador crescer o suficiente para violar os critérios de tamanho ou
  coesão usados aqui.
