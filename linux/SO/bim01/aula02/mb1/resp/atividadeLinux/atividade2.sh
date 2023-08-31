# 1) Criar novo diretório e entrar nele
mkdir ~/lab_directory
cd ~/lab_directory

# 2) Criar arquivos
touch musica1.mp3 imagem1.jpg filme1.avi
touch musica2.mp3 imagem2.jpg filme2.avi
touch musica3.mp3 imagem3.jpg filme3.avi
touch musica4.mp3 imagem4.jpg filme4.avi
touch musica5.mp3 imagem5.jpg filme5.avi
touch musica6.mp3 imagem6.jpg filme6.avi

# 3) Mover arquivos
mv musica1.mp3 ~/Música
mv imagem2.jpg ~/Imagens
mv filme3.avi ~/Vídeos
mv musica4.mp3 ~/Música
mv imagem5.jpg ~/Imagens
mv filme6.avi ~/Vídeos

# 4) Criar diretórios
mkdir ~/Amigos ~/Familia ~/Trabalho

# 5) Copiar arquivos
cp musica1.mp3 musica2.mp3 musica3.mp3 ~/Amigos
cp musica4.mp3 musica5.mp3 ~/Trabalho

# 6) Remover arquivos
rm musica6.mp3
rm filme3.avi

# 7) Remover arquivos da pasta Trabalho
rm -rf ~/Trabalho/*

# 8) Remover diretório vazio
rmdir ~/Familia

# 9) Remover diretório e seus arquivos
rm -rf ~/Amigos