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

# Encontrar os índices das frequências com amplitudes altas (indicando ruído)
indices_ruido = np.where(np.abs(fft) > 10)[0]
frequencia_ruido = frequencia_fft[indices_ruido]

# Criar uma máscara de filtro para remover frequências abaixo de um certo limiar
mascara_filtro = np.zeros(len(fft))
mascara_filtro[np.abs(frequencia_fft) < 10] = 1

# Aplicar a máscara de filtro à FFT para obter um sinal filtrado
sinal_filtrado = np.fft.ifft(fft * mascara_filtro)

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