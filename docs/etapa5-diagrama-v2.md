# Etapa 5 — Diagrama C4 (contêiner), versão 2

Gerado com prompt de mais contexto: apontando para `docs/etapa4-arquitetura.md`
(análise real de acoplamento) e `docs/etapa2-tdd.md`/`docs/etapa1-hook-evidencia.md`
(hooks e tdd-guard), pedindo explicitamente para representar os elementos
que a atividade "Harness e Arquitetura" de fato investigou — não só o
código de produção.

```mermaid
C4Container
    title Diagrama de Contêineres - ia-dev-lab (v2)

    Person(dev, "Desenvolvedora", "Aprova checkpoints, decide arquitetura")
    System_Ext(claudeCode, "Claude Code", "Agente de IA que lê e edita o repositório")
    System_Ext(tddGuard, "tdd-guard (plugin externo)", "Valida ciclo TDD; fail-open sem credencial de modelo")

    System_Boundary(repo, "ia-dev-lab (repositório)") {
        Container(validadores, "Validadores", "Python (stdlib)", "6 funções puras str->bool, zero import entre si")
        Container(testes, "Suíte de testes", "pytest + tdd-guard-pytest", "1 arquivo de teste por validador; grava .claude/tdd-guard/data/test.json")
        Container(hooks, "Guardrails do harness", "Python + JSON (.claude/hooks, settings.json)", "Bloqueia pip install não documentado antes de executar")
        Container(docs, "Documentação", "Markdown", "ADRs, comparações, log de sessão, checkpoints")
    }

    Rel(dev, claudeCode, "Dá comandos, aprova checkpoints")
    Rel(claudeCode, validadores, "Lê e edita")
    Rel(claudeCode, testes, "Roda pytest")
    Rel(claudeCode, docs, "Escreve")
    Rel(testes, validadores, "Importa e testa")
    Rel(testes, tddGuard, "Reporta resultado via tdd-guard-pytest")
    Rel(hooks, claudeCode, "Intercepta comando Bash antes de executar (PreToolUse)")
```
