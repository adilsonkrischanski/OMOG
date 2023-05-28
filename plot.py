import matplotlib.pyplot as plt

from Curves.Base import Pointer
from Curves.Base import Vector

from Curves.hermite import Hemite


# pontos = [[0,0],[4,3],[7,3], [6,9]]
# vetores = [[1,3],[3,3],[2,5],[2,3]]
pontos = [[0,0],[4,3]]
vetores = [[1,3],[1,0]]

curves = []

for i in range(0,len(pontos)-1):
    h = Hemite(pontos[i],pontos[i+1],vetores[i],vetores[i+1])

    plt.scatter([pontos[i][0], pontos[i][0]], [pontos[i+1][1], pontos[i+1][1]], c='red', label='Pontos')
    plt.scatter([vetores[i][0] + pontos[i][0], vetores[i+1][0] + pontos[i+1][0]], [vetores[i][1] + pontos[i][1], vetores[i+1][1] + pontos[i+1][1]], c='green', label='Pontos de controle')
    plt.arrow(pontos[i][0], pontos[i][1], vetores[i][0], vetores[i][1], head_width=0.2, head_length=0.3, color='red')
    curves.append(h.hermite_curve())


plt.arrow(pontos[len(pontos)-1][0], pontos[len(pontos)-1][1], vetores[len(pontos)-1][0], vetores[len(pontos)-1][1],head_width=0.2, head_length=0.3, color='red')


for curve in curves:
    plt.plot(curve[:, 0], curve[:, 1], label='Curva de Hermite')






# plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curva de Hermite')
plt.grid(True)
plt.show()



