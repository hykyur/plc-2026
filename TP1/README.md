<div align="center">
# TP1 — Expressão Regular: strings binárias sem a substring `011`

## **Autor**

**Nome:** Caio de Souza Lins

**Número de aluno:** A112802

**Foto:**

<img src="../pic/picture.png" alt="myself" width="200"> 

</div>

## Problema

Dado um conjunto de strings, queremos **aceitar** apenas aquelas que:

1. são compostas **exclusivamente** pelos caracteres `0` e `1` (strings binárias), e
2. **não contêm** a substring `011`.

Isto significa rejeitar dois tipos de strings:

- as que contêm `011` em qualquer posição (ex.: `011`, `0011`, `1011`, `01101`);
- as que têm algum carácter que não seja `0` ou `1` (ex.: `012`, `abc`).

## A expressão regular

```python
regex = r"^(?!.*?011)[0-1]*$"
```

### Decomposição

| Parte        | Nome                         | Significado |
|--------------|------------------------------|-------------|
| `r"..."`     | *raw string* do Python       | Faz com que o Python não interprete `\` como escape; é boa prática para expressões regulares. |
| `^`          | âncora de início             | A correspondência tem de começar no início da string. |
| `(?!...)`    | *negative lookahead*         | Verifica, **sem consumir caracteres**, que o que vem a seguir **não** corresponde ao padrão interior. Se corresponder, a expressão falha. |
| `.*?`         | qualquer sequência           | Dentro do lookahead: zero ou mais caracteres quaisquer, permitindo “saltar” para qualquer posição da string com operador não greedy. |
| `011`        | literal                      | A substring proibida. |
| `[0-1]*`     | classe de caracteres + fecho de Kleene | Zero ou mais caracteres, cada um `0` ou `1` (equivalente a `[01]*`). |
| `$`          | âncora de fim                | A correspondência tem de terminar no fim da string. |

### Como cada parte resolve o problema

**1. Rejeitar strings com `011` — `^(?!.*?011)`**

Como o lookahead está logo a seguir a `^`, é avaliado uma única vez, na posição 0.
O padrão `.*?011` tenta encontrar `011` depois de *qualquer* prefixo, ou seja, em
**qualquer posição** da string. Se o encontrar, o lookahead negativo falha e a
string inteira é rejeitada. Como o lookahead não consome caracteres, depois de
passar a verificação a leitura continua novamente a partir do início da string.

**2. Aceitar apenas `0` e `1` — `[0-1]*$`**

Depois da verificação, `[0-1]*` consome a string carácter a carácter, aceitando
apenas `0` ou `1`. O `$` obriga a que esta sequência chegue até ao fim da string:
se aparecer outro carácter qualquer (`2`, `a`, espaço, …), `[0-1]*` pára antes
dele, o `$` não corresponde e a string é rejeitada.

O `*` (em vez de `+`) faz com que a string vazia `""` também seja aceite, já que
é trivialmente binária e não contém `011`.

**Combinação:** a string só é aceite se *ambas* as condições se verificarem —
o lookahead garante a ausência de `011` e `^[0-1]*$` garante que todos os
caracteres são binários.

### Nota sobre `re.fullmatch`

O script usa `re.fullmatch`, que já exige que o padrão cubra a string inteira.
Por isso as âncoras `^` e `$` são redundantes neste contexto, mas mantêm a
expressão correta se for usada com `re.match` ou `re.search`.

## Exemplos

| String    | Resultado | Motivo |
|-----------|-----------|--------|
| `""`      | Aceite    | String vazia, sem `011` |
| `0`, `1`  | Aceite    | Binária, sem `011` |
| `01`, `10`, `11`, `00` | Aceite | Binária, sem `011` |
| `101`, `111`, `1001`   | Aceite | Binária, sem `011` |
| `011`     | Rejeitada | Contém `011` no início |
| `0011`    | Rejeitada | Contém `011` na posição 1 |
| `0110`    | Rejeitada | Contém `011` no início |
| `1011`    | Rejeitada | Contém `011` no fim |
| `00110`, `01101` | Rejeitada | Contêm `011` |
| `012`, `abc` | Rejeitada | Contêm caracteres que não são `0`/`1` |

### Intuição (linguagem regular)

Numa string binária sem `011`, os `1` seguidos só podem aparecer no início:
a partir do primeiro `0`, cada `1` tem de vir isolado e imediatamente a seguir
a um `0`. Uma expressão equivalente sem lookahead é:

```
^1*(0|01)*$
```

A versão com lookahead é mais direta de ler, pois exprime literalmente
“não contém `011`” e “só tem `0` e `1`”.

## Execução

```bash
python tp1_re.py
```