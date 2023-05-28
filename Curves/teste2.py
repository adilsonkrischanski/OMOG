import numpy as np
import matplotlib.pyplot as plt

def hermite_curve(points, tangents, num_samples=100):
    t = np.linspace(0, 1, num_samples)  # Parâmetro de interpolação
    
    # Construção da matriz de Hermite
    matrix = np.array([[2, -2, 1, 1],
                       [-3, 3, -2, -1],
                       [0, 0, 1, 0],
                       [1, 0, 0, 0]])
    
    curve = []
    
    for i in range(len(points) - 1):
        p0, p1 = points[i], points[i + 1]
        t0, t1 = tangents[i], tangents[i + 1]
        
        # Construção dos vetores de entrada para a matriz de Hermite
        vector_x = np.array([p0[0], p1[0], t0[0], t1[0]])
        vector_y = np.array([p0[1], p1[1], t0[1], t1[1]])
        vector_z = np.array([p0[2], p1[2], t0[2], t1[2]])
        
        # Cálculo dos coeficientes de Hermite
        coef_x = np.matmul(matrix, vector_x)
        coef_y = np.matmul(matrix, vector_y)
        coef_z = np.matmul(matrix, vector_z)
        
        # Avaliação da curva para cada valor de t
        for j in range(num_samples):
            t_j = np.array([t[j]**5, t[j]**4, t[j]**3, t[j]**2, t[j], 1])
            
            x = np.dot(coef_x, t_j)
            y = np.dot(coef_y, t_j)
            z = np.dot(coef_z, t_j)
            
            curve.append([x, y, z])
    
    return curve

# Definição dos pontos de controle e vetores tangentes
points = [[0, 0, 0], [1, 1, 1], [2, -1, 2], [3, 0, 1]]
tangents = [[1, 1, 0], [1, -1, 1], [0, 1, -1], [1, 0, 0]]

# Geração da curva de Hermite
curve = hermite_curve(points, tangents)

# Separação das coordenadas x, y e z
x = [point[0] for point in curve]
y = [point[1] for point in curve]
z = [point[2] for point in curve]

# Plotagem da curva
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)

# Configuração dos rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Exibição do gráfico
plt.show()

