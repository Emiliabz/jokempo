# Jokempo - Pedra, Papel e Tesoura

Um jogo interativo em Python de Pedra, Papel e Tesoura contra o computador.

## Funcionalidades

- ✅ Jogo contra o computador
- ✅ Escolha aleatória do computador
- ✅ Animação de "JO-KEM-PÔ" com delay
- ✅ Validação de jogadas
- ✅ Determinação de vencedor
- ✅ Interface simples e intuitiva

## Regras do Jogo

- **Pedra** vence **Tesoura**
- **Papel** vence **Pedra**
- **Tesoura** vence **Papel**

## Como Executar

```bash
python jokempo.py
```

## Menu

```
Vem jogar Jokempo comigo!
Suas opcoes:
[0] Pedra
[1] Papel
[2] Tesoura
```

Digite o número da sua escolha (0, 1 ou 2) e o computador fará sua escolha aleatória.

## Exemplo de Execução

```
Vem jogar Jokempo comigo!
Suas opcoes:
[0] Pedra
[1] Papel
[2] Tesoura
Qual eh a sua jogada? 0

--------------------
JO
KEM
PO!
--------------------
O computador escolheu Tesoura
O jogador escolheu Pedra
--------------------
JOGADOR VENCEU!
```

## Resultados Possíveis

- **EMPATE!** - Ambos fizeram a mesma escolha
- **JOGADOR VENCEU!** - Sua escolha vence a do computador
- **COMPUTADOR VENCEU!** - A escolha do computador vence a sua

## Bibliotecas Utilizadas

- `random.randint` - Escolha aleatória do computador
- `time.sleep` - Delay para efeito dramático na animação

## Requisitos

- Python 3.x

## Autor

Criado como exercício de programação em Python.

## Licença

Livre para uso educacional.
