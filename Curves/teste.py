# import numpy as np
# import matplotlib.pyplot as plt

# def hermite_curve(points):
#     t = np.linspace(0, 1, 100)  # Parâmetro t variando de 0 a 1
#     curve = np.zeros((len(t), 2))  # Matriz para armazenar os pontos da curva

#     for i in range(len(t)):
#         ti = t[i]
#         t2 = ti * ti
#         t3 = t2 * ti
#         t4 = t3 * ti
#         t5 = t4 * ti

#         p0 = points[0]
#         p1 = points[1]
#         m0 = points[2]
#         m1 = points[3]
#         d0 = points[4]
#         d1 = points[5]

#         h00 = 6 * t5 - 15 * t4 + 10 * t3
#         h10 = t5 - 3 * t4 + 3 * t3 - ti * ti * ti
#         h01 = -6 * t5 + 15 * t4 - 10 * t3
#         h11 = t5 - 2 * t4 + t3

#         x = h00 * p0[0] + h10 * m0[0] + h01 * p1[0] + h11 * m1[0]
#         y = h00 * p0[1] + h10 * m0[1] + h01 * p1[1] + h11 * m1[1]

#         curve[i] = [x, y]

#     return curve

# # Exemplo de uso
# points = [[0, 0], [1, 1], [1, 2], [3, 4], [4, 3], [5, 5]]  # Pontos de controle: P0, P1, M0, M1, D0, D1
# curve = hermite_curve(points)

# # Plotagem da curva
# print(curve)
# plt.plot(curve[:, 0], curve[:, 1], label='Curva de Hermite')
# plt.scatter([point[0] for point in points], [point[1] for point in points], c='red', label='Pontos de controle')
# plt.legend()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Curva de Hermite')
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt

# def plotar_vetor(ponto_inicial, vetor):
#     plt.arrow(ponto_inicial[0], ponto_inicial[1], vetor[0], vetor[1], head_width=0.2, head_length=0.3, color='red')
#     plt.scatter(ponto_inicial[0], ponto_inicial[1], color='blue', label='Ponto Inicial')
#     plt.scatter(ponto_inicial[0] + vetor[0], ponto_inicial[1] + vetor[1], color='green', label='Ponto Final')
#     plt.legend()
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Vetor entre dois pontos')
#     plt.grid(True)
#     plt.axis('equal')  # Configura o mesmo tamanho para os eixos x e y

# # Exemplo de uso
# ponto_inicial = [0, 0]
# vetor = [3, 4]

# plotar_vetor([0,0], [2,6])
# plotar_vetor([3,4], [ 1,4])
# plotar_vetor([4,3], [2,3])

# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def hermite_curve(p0, p1, m0, m1):
    t = np.linspace(0, 1, 100)  # Parâmetro t variando de 0 a 1
    curve = np.zeros((len(t), 2))  # Matriz para armazenar os pontos da curva

    for i in range(len(t)):
        ti = t[i]
        t2 = ti * ti
        t3 = t2 * ti

        h00 = 2 * t3 - 3 * t2 + 1
        h10 = t3 - 2 * t2 + ti
        h01 = -2 * t3 + 3 * t2
        h11 = t3 - t2

        x = h00 * p0[0] + h10 * m0[0] + h01 * p1[0] + h11 * m1[0]
        y = h00 * p0[1] + h10 * m0[1] + h01 * p1[1] + h11 * m1[1]

        curve[i] = [x, y]

    return curve

# Exemplo de uso
p0 = [0, 0]  # Ponto inicial
p1 = [1, 2]  # Ponto final
m0 = [2, 1]  # Vetor de controle no ponto inicial
m1 = [1, 3]  # Vetor de controle no ponto final

curve = hermite_curve(p0, p1, m0, m1)

# Plotagem dos vetores em forma de seta
plt.arrow(p0[0], p0[1], m0[0], m0[1], head_width=0.2, head_length=0.3, color='red')
plt.arrow(p1[0], p1[1], m1[0], m1[1], head_width=0.2, head_length=0.3, color='red')



# Plotagem da curva
plt.plot(curve[:, 0], curve[:, 1], label='Curva de Hermite')
plt.scatter([p0[0], p1[0]], [p0[1], p1[1]], c='red', label='Pontos')
plt.scatter([m0[0] + p0[0], m1[0] + p1[0]], [m0[1] + p0[1], m1[1] + p1[1]], c='green', label='Pontos de controle')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curva de Hermite')
plt.grid(True)
plt.show()




