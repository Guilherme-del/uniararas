import numpy as np
import matplotlib.pyplot as plot

# Definir a taxa de amostragem, frequência e período
taxa_amostragem = 200
frequencia = 10
periodo = 1 / frequencia

# Gerar o array de tempo
tempo = np.arange(-3 * periodo, 3 * periodo, 1 / taxa_amostragem)

# Gerar o sinal original (forma de onda senoidal)
sinal_original = 10 * np.sin(2 * np.pi * frequencia * tempo)

# Gerar ruído aleatório
ruido = 2 * np.random.randn(len(sinal_original))

# Adicionar o ruído ao sinal original
sinal_ruidoso = sinal_original + ruido

# Realizar a FFT e calcular o espectro de frequência
frequencia_fft = np.fft.fftfreq(len(sinal_ruidoso), 1 / taxa_amostragem)
fft = np.fft.fft(sinal_ruidoso)
"""
 Encontrar os índices das frequências com amplitudes altas (indicando ruído):
 Nesse caso, as frequências com amplitudes maiores que 10 foram consideradas como ruído. 
 Essa é uma escolha arbitrária para fins ilustrativos.
 """
indices_ruido = np.where(np.abs(fft) > 10)[0]
frequencia_ruido = frequencia_fft[indices_ruido]

# Criar uma máscara de filtro para remover frequências abaixo de um certo limiar
mascara_filtro = np.zeros(len(fft))
"""
Define a máscara de filtro:
Nesse caso específico, o filtro foi escolhido para remover as frequências abaixo de 10 Hz. No entanto, 
a escolha do valor 10 Hz é apenas um exemplo arbitrário e pode variar dependendo dos requisitos e características do sinal.
A seleção do limiar do filtro é uma escolha empírica e depende da natureza do sinal e do ruído presente nele.
"""
mascara_filtro[np.abs(frequencia_fft) < 10] = 1
"""
Aplicar a máscara de filtro à FFT para obter um sinal filtrado:


A máscara de filtro é uma matriz de zeros do mesmo tamanho que a FFT. Os elementos da máscara de filtro correspondentes às frequências abaixo do limiar são definidos como 1, indicando que essas frequências serão mantidas. 
As frequências acima do limiar permanecem como zero na máscara de filtro, indicando que serão filtradas (removidas).
Por fim, a máscara de filtro é aplicada à FFT multiplicando-a elemento por elemento:
"""
sinal_filtrado = np.fft.ifft(fft * mascara_filtro)
"""
A multiplicação da FFT pelo filtro (máscara) é equivalente a aplicar o filtro na frequência.
 Em seguida, a IFFT (Transformada Rápida de Fourier Inversa) é aplicada para obter o sinal filtrado no domínio do tempo.
"""
# Plotar os resultados
plot.figure(figsize=(10, 8))
plot.subplot(2, 2, 1)
plot.plot(tempo, sinal_original)
plot.title('Sinal Original')
plot.subplot(2, 2, 2)
plot.plot(tempo, sinal_ruidoso)
plot.title('Sinal com Ruído')
plot.subplot(2, 2, 3)
plot.plot(frequencia_fft, np.abs(fft))
plot.title('Espectro de Frequência')
plot.subplot(2, 2, 4)
plot.plot(tempo, np.real(sinal_filtrado))
plot.title('Sinal Filtrado')
plot.tight_layout()
plot.show()

"""
Portanto, o filtro escolhido nesse código específico remove as frequências abaixo do limiar especificado,
com o objetivo de filtrar o ruído presente no sinal original. 
O valor do limiar pode ser ajustado com base na análise do espectro de frequência e nas características do sinal e do ruído específicos da aplicação.
"""