# Etapa 5 — Diagrama C4 (contêiner), versão 1

Gerado com prompt curto e genérico ("gere um diagrama C4 de contêiner deste
projeto Python"), sem apontar para `docs/etapa4-arquitetura.md` nem para o
que a atividade de fato investigou (hooks, tdd-guard, checkpoints).

```mermaid
C4Container
    title Diagrama de Contêineres - ia-dev-lab (v1)

    Person(dev, "Desenvolvedor")

    System_Boundary(sistema, "ia-dev-lab") {
        Container(scripts, "Scripts de validação", "Python", "Funções de validação: e-mail, CEP, placa, cartão, hora")
        Container(testes, "Suíte de testes", "pytest", "Testes unitários dos scripts")
    }

    Rel(dev, scripts, "Usa/edita")
    Rel(testes, scripts, "Testa")
```
