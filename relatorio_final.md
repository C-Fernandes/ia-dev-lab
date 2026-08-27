# Relatório Final - Prática Assíncrona

**1. Ferramenta de IA configurada e motivo**
Configurei o Claude Code (CLI agent). Escolhi essa ferramenta pela facilidade de rodar direto no terminal do VS Code. Ele tem autonomia para ler os arquivos locais, executar comandos shell e fazer as edições diretamente, sem que eu precise ficar copiando e colando código do navegador.

**2. Trecho mais útil do CLAUDE.md**
O trecho que achei mais prático foi a convenção de pastas:
`- O código focado na regra de negócio deve ser mantido dentro da pasta src/.`
Isso foi muito útil porque evita que a IA crie um monte de arquivos soltos na raiz do repositório. O assistente já alocou os scripts no lugar certo logo na primeira tentativa.

**3. Diferença entre o prompt fraco e o eficaz (Etapa 4)**
No teste para criar uma validação de e-mail, o prompt fraco fez a IA gerar uma função muito complexa usando regex (`re`) e colocar os testes misturados no final do arquivo principal. Quando usei o prompt eficaz (dando contexto, restrições e exigindo validação separada), o código gerado foi muito mais limpo e a ferramenta criou a suíte de testes de forma isolada dentro da pasta `tests/`. O prompt bem estruturado eliminou o trabalho de refatoração manual.

**4. Obstáculo enfrentado e solução**
Na etapa de integração com o GitHub, rodei acidentalmente o comando de `remote add origin` com a string genérica de exemplo do roteiro, o que causou um erro fatal no primeiro `push`. Resolvi criando o repositório vazio na interface do GitHub, copiando a URL HTTPS real e usando `git remote set-url origin` no terminal para corrigir o caminho. Em relação à integração MCP, cheguei a criar o arquivo `.mcp.json` para o filesystem, mas percebi que o Claude Code usou sua autonomia no terminal para rodar `git log` diretamente e ver o último commit, em vez de depender estritamente do servidor MCP.
