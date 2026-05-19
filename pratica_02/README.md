
Bem-vindo(a) à **Prática 02PR** da disciplina **Fundamentos de Programação**.

Esta atividade foi organizada para ser entregue **via GitHub**, utilizando o fluxo de trabalho por **fork + branch + pull request (PR)**.

O objetivo aqui não é apenas resolver os exercícios, mas também praticar uma rotina real de desenvolvimento com:

- organização de arquivos;
- versionamento com Git;
- envio por branch;
- abertura de Pull Request;
- clareza e padronização na entrega.

---

## 📂 Estrutura esperada no repositório

O repositório da turma segue o modelo **monorepo**: cada prática possui sua própria pasta, e dentro dela cada estudante cria sua pasta individual para entrega.

### Estrutura esperada para esta prática

```bash
ads-logica-unifg-2026.1/
└── pratica 02PR/
    ├── README.md
    └── seu-nome-sobrenome/
        ├── ex01.py
        ├── ex02.py
        ├── ex03.py
        ├── ex04.py
        ├── ex05.py
        ├── ex06.py
        ├── ex07.py
        ├── ex08.py
        ├── ex09.py
        ├── ex10.py
        ├── ex11.py
        ├── ex12.py
        ├── ex13.py
        ├── ex14.py
        ├── ex15.py
        └── ex16.py
```

> **Importante:** a sua pasta pessoal deve seguir o padrão:
>
> ```bash
> nome-sobrenome
> ```
>
> Tudo em minúsculas, sem espaço e sem acento.

Exemplo:

```bash
anderson-oliveira
maria-silva
joao-pedro-santos
```

---

## 🛠️ Passo 1 — Fazer o fork do repositório

A entrega deve ser feita a partir de um **fork** do repositório da turma.

### Repositório base

```bash
https://github.com/marcolinoee/ads-logica-unifg-2026.1
```

### O que fazer

1. Acesse o repositório da turma.
2. Clique no botão **Fork**.
3. Isso criará uma cópia do repositório na sua conta do GitHub.

---

## 💻 Passo 2 — Clonar o seu fork

Depois de fazer o fork, clone o **seu repositório** para o computador.

```bash
git clone https://github.com/SEU_USUARIO/ads-logica-unifg-2026.1.git
cd ads-logica-unifg-2026.1
```

Substitua `SEU_USUARIO` pelo seu usuário real do GitHub.

---

## 🔁 Passo 3 — Configurar o repositório original como upstream

Esse passo permite atualizar o seu fork com as mudanças publicadas no repositório principal da turma.

```bash
git remote add upstream https://github.com/marcolinoee/ads-logica-unifg-2026.1.git
```

Para conferir se deu certo:

```bash
git remote -v
```

---

## 🔄 Passo 4 — Sincronizar o seu repositório antes de começar

Antes de iniciar a atividade, atualize sua branch `main`:

```bash
git checkout main
git pull upstream main
git push origin main
```

---

## 🌿 Passo 5 — Criar uma branch para a prática

Nunca desenvolva a atividade diretamente na `main`.

Crie uma branch específica para esta entrega:

```bash
git checkout -b entrega-pratica-02pr
```

---

## 📁 Passo 6 — Criar sua pasta dentro de `pratica 02PR`

Entre na pasta da atividade e crie sua pasta pessoal:

```bash
cd "pratica 02PR"
mkdir seu-nome-sobrenome
```

Depois, entre na sua pasta:

```bash
cd seu-nome-sobrenome
```

---

## 🧠 Passo 7 — Desenvolver os exercícios

Você deverá resolver os exercícios abaixo e salvar cada solução em um arquivo separado.

### Regra de nomenclatura dos arquivos

Use exatamente este padrão:

```bash
ex01.py
ex02.py
ex03.py
...
ex16.py
```

---

# 📘 Lista de Exercícios — Prática 02PR

## Nível 1 — Execução guiada

### Exercício 01 — Número positivo, negativo ou zero
Crie um programa que leia um número inteiro e informe se ele é:
- positivo;
- negativo;
- ou zero.

**Estrutura esperada:** `if`, `elif`, `else`.

---

### Exercício 02 — Classificação por idade
Leia a idade de uma pessoa e informe se ela é:
- menor de idade;
- maior de idade;
- idosa (considere idosa a partir de 60 anos).

**Estrutura esperada:** condicional encadeada.

---

### Exercício 03 — Par ou ímpar de 1 a 20
Usando `for`, exiba os números de **1 a 20** e informe ao lado de cada um se ele é **par** ou **ímpar**.

**Estruturas esperadas:** `for` + `if`.

---

### Exercício 04 — Senha de acesso
Usando `while`, leia uma senha até que o usuário digite a palavra:

```text
acesso
```

Quando a senha correta for digitada, exiba:

```text
Acesso liberado.
```

**Estrutura esperada:** `while`.

---

## Nível 2 — Execução operacional

### Exercício 05 — Contar números positivos
Solicite **10 números** ao usuário usando `for` e informe ao final **quantos são positivos**.

**Estruturas esperadas:** `for` + contador + `if`.

---

### Exercício 06 — Validação de nota
Peça uma nota de **0 a 10** e use `while` para validar a entrada até que o valor informado seja aceitável.

**Estrutura esperada:** `while` com validação.

---

### Exercício 07 — Soma dos números pares
Leia **8 valores inteiros** e calcule a soma **apenas dos números pares**.

**Estruturas esperadas:** `for` + `if` + acumulador.

---

### Exercício 08 — Tabuada
Crie um programa que exiba a tabuada de um número informado pelo usuário, de **1 a 10**, utilizando `for`.

**Estrutura esperada:** `for`.

---

## Nível 3 — Execução analítica

### Exercício 09 — Reajuste salarial
Desenvolva um algoritmo que leia o salário de um funcionário e aplique reajuste conforme as regras:

- **15%** para salários até **R$ 1.500,00**;
- **10%** para salários entre **R$ 1.500,01** e **R$ 3.000,00**;
- **5%** para salários acima de **R$ 3.000,00**.

Ao final, mostre:
- salário original;
- percentual aplicado;
- novo salário.

**Estrutura esperada:** `if`, `elif`, `else`.

---

### Exercício 10 — Menu simples
Crie um menu com as opções:

```text
1 - Somar
2 - Subtrair
0 - Sair
```

O programa deve continuar exibindo o menu enquanto o usuário **não escolher 0**.

Se escolher:
- `1`: leia dois números e mostre a soma;
- `2`: leia dois números e mostre a subtração;
- `0`: encerre o programa;
- qualquer outro valor: mostre mensagem de opção inválida.

**Estruturas esperadas:** `while` + `if/elif/else`.

---

### Exercício 11 — Classificação da turma
Leia a quantidade de alunos da turma. Depois, usando `for`, leia a média de cada aluno e informe quantos ficaram:

- aprovados (`média >= 7`);
- em recuperação (`média >= 4 e < 7`);
- reprovados (`média < 4`).

Ao final, exiba os três totais.

**Estruturas esperadas:** `for` + contadores + `if/elif/else`.

---

### Exercício 12 — Classificação de compras
Solicite o valor de várias compras e classifique cada uma em:

- `sem desconto`;
- `desconto básico`;
- `desconto especial`.

O programa deve continuar até que o operador decida encerrar.

> **Importante:** você deve definir no código os critérios de cada faixa e registrar isso em comentário.

**Estruturas esperadas:** `while` + `if/elif/else`.

---

## Nível 4 — Execução estratégica

### Exercício 13 — Depuração de loop infinito
Analise um código com `while` que deveria contar de **10 até 1**, mas entra em **loop infinito**.

Sua tarefa é:
1. registrar no comentário do arquivo qual era o problema;
2. explicar por que o laço não terminava;
3. apresentar a versão corrigida.

**Estrutura esperada:** análise + correção com `while`.

---

### Exercício 14 — Reescrita de while para for
Reescreva um algoritmo feito com `while` para uma versão equivalente com `for`.

No final do arquivo, escreva um comentário explicando:
- por que a versão com `for` pode ficar mais legível;
- em que situação o `while` ainda seria mais adequado.

---

### Exercício 15 — Maior nota da sequência
Resolva o problema: **ler 5 notas e informar a maior**, usando `for`.

Ao final do arquivo, responda em comentário:
- seria adequado usar `while` nesse problema?
- em que contexto isso faria sentido?

---

### Exercício 16 — Questionário com sentinela
Projete um algoritmo para ler respostas de um questionário com as opções:

- `S` para sim;
- `N` para não.

O programa deve continuar até que o usuário digite:

```text
FIM
```

Ao final, informe quantos `S` foram digitados.

No final do arquivo, inclua um comentário justificando por que a estrutura principal escolhida foi adequada.

**Estruturas esperadas:** `while` + sentinela + contador.

---

## ⭐ Desafio extra (opcional)

Se quiser enriquecer sua entrega, crie também:

```bash
desafio_extra.py
```

### Desafio extra — Sistema simples de lançamento de desempenho
Crie um programa que:

1. leia o nome de um estudante;
2. leia a quantidade de acertos (de 0 a 20);
3. valide essa entrada;
4. calcule o percentual de acertos;
5. classifique o desempenho em:
   - Excelente;
   - Satisfatório;
   - Em atenção;
   - Crítico;
6. permita continuar cadastrando estudantes até que o operador escolha sair;
7. mostre a média percentual da turma ao final.

---

## 🧾 Regras de ouro (checklist)

Para que sua atividade seja considerada correta, verifique se você cumpriu todos os itens abaixo:

- [ ] Criei meu **fork** do repositório.
- [ ] Atualizei minha `main` antes de começar.
- [ ] Trabalhei em uma branch separada.
- [ ] Criei minha pasta com o padrão `nome-sobrenome`.
- [ ] Salvei os arquivos com nomes `ex01.py` até `ex16.py`.
- [ ] Não alterei arquivos de colegas.
- [ ] Testei os programas antes de enviar.
- [ ] Fiz commit com mensagem clara.
- [ ] Enviei minha branch para o GitHub.
- [ ] Abri meu Pull Request.

---

## 🧼 Regras de qualidade do código

Todos os exercícios devem seguir estas orientações:

- usar nomes de variáveis claros e descritivos;
- manter a identação correta;
- incluir comentário inicial explicando o objetivo do arquivo;
- exibir mensagens claras para entrada e saída;
- evitar variáveis genéricas demais como `x`, `y` e `z` quando houver alternativa melhor;
- sempre que possível, testar casos de borda.

### Modelo de comentário inicial sugerido

```python
# ex01.py
# Objetivo: ler um número inteiro e informar se ele é positivo, negativo ou zero.
```

---

## 📦 Passo 8 — Adicionar, commitar e enviar

Depois de concluir os arquivos, volte para a raiz do repositório e faça:

```bash
git add .
git commit -m "feat: entrega pratica 02pr - Seu Nome"
git push origin entrega-pratica-02pr
```

---

## 🔀 Passo 9 — Abrir o Pull Request (PR)

No GitHub:

1. Acesse o seu fork;
2. clique em **Compare & pull request**;
3. abra o PR para o repositório original.

### Título sugerido do PR

```text
[PRATICA 02PR] Seu Nome Completo
```

### No corpo do PR, você pode escrever

- dificuldades encontradas;
- o que aprendeu;
- exercícios em que teve mais dúvida;
- melhorias que faria depois.

---

## 📝 Critérios de avaliação sugeridos

A correção poderá considerar:

- funcionamento dos programas;
- uso adequado de `if`, `while` e `for`;
- organização da pasta e dos arquivos;
- legibilidade do código;
- cumprimento do padrão de entrega;
- comentários explicativos nos exercícios reflexivos.

---

## 📌 Orientação final

Antes de abrir o PR, confirme:

- se a sua pasta está dentro de `pratica 02PR`;
- se o nome da pasta está correto;
- se os arquivos estão com nomes padronizados;
- se a branch correta foi enviada;
- se o PR está apontando para o repositório original.

---

## ✅ Entrega final

A entrega será considerada concluída quando você:

1. enviar sua branch para o seu fork;
2. abrir um Pull Request;
3. manter sua atividade organizada dentro da pasta da prática.

---

Bom trabalho e bons estudos! 🚀
