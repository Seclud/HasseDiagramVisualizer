import hasse
import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
# Disclaimer:
# Эта программа была создана в образовательных целях и предназначена для визуализации диаграмм Хассе :nerd:

# Как пользоваться:
# 1. Устанавливаете модули hasse, matplotlib, networkx, если их нет
# 2. Запускаете скрипт
# 3. Вводите все по инструкции
# 4. Получаете картинку
# 5. Надеяться, что в программе нет багов и картинка правильная
# (Я проверял на разных диаграммах из беседы, вроде все выдавало правильно, но на всякий проверяйте своими мозгами).

# Пожалуйста, обратите внимание:
# - Хотя я старался обеспечить точность этой программы, я не могу гарантировать, что она не содержит ошибок.
# - Пожалуйста, всегда проверяйте результаты с помощью других источников или собственных вычислений.
# - Эта программа предоставляется "как есть", без каких-либо гарантий.
# - Я не несу ответственности за любые последствия, возникшие в результате использования этой программы.
# ChatGPT can make mistakes. Consider checking important information.


# numbers = [1, 2, 3, 4, 5, 6, 10, 15, 20, 24, 30, 120] Это просто для теста, не обращайте внимания
numbers = list(map(int, input("Напишите ваши цифры через ПРОБЕЛ в ПОРЯДКЕ ВОЗРАСТАНИЯ: ").split()))


def create_poset(numbers):
    chains = []
    for r in range(1, len(numbers) + 1):
        for subset in combinations(numbers, r):
            if all(subset[i] % subset[i - 1] == 0 for i in range(1, len(subset))):
                chains.append(subset)
    poset = hasse.PoSet.from_chains(*chains)
    return poset


def create_layers(G):
    levels = {node: 0 for node in G.nodes}
    for node in nx.topological_sort(G):
        for pred in G.predecessors(node):
            levels[node] = max(levels[node], levels[pred] + 1)
    layers = [[] for _ in range(max(levels.values()) + 1)]
    for node, level in levels.items():
        layers[level].append(node)
    return layers


def draw_poset(poset):
    G = poset.hasse
    layers = create_layers(G)
    pos = {}
    for i, layer in enumerate(layers):
        for j, node in enumerate(layer):
            pos[node] = (j, -i)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1200)
    plt.show()


poset = create_poset(numbers)
draw_poset(poset)
