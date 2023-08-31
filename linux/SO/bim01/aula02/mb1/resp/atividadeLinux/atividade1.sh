
# 1) Criar pasta atividade e entrar nela
mkdir ~/atividade
cd ~/atividade

# 2) Criar arquivos
touch SO_alunos0.txt SO_alunos1.txt SO_alunos2.txt SO_alunos3.txt SO_alunos4.txt SO_alunos5.txt
touch TC_alunos0.txt TC_alunos1.txt TC_alunos2.txt
touch ProvaA.doc ProvaB.doc
touch TrabalhoA.doc TrabalhoB.doc TrabalhoC.doc TrabalhoD.doc TrabalhoE.doc TrabalhoF.doc TrabalhoG.doc

# 3) Criar subdiretórios
mkdir Provas Trabalhos Atividades_Alunos SO

# 4) Mover arquivos
mv SO_alunos*.txt SO/
mv Prova*.doc Provas/

# 5) Copiar arquivos
cp TC_alunos*.txt Atividades_Alunos/

# 6) Criar subdiretórios
mkdir Provas/N1 Provas/N2

# 7) Criar subdiretório e mover arquivos
mkdir Trabalhos/2018
mv Trabalho*.doc Trabalhos/2018/

# 8) Mover arquivos
mv ProvaA.doc Provas/N1/
mv ProvaB.doc Provas/N2/

# 9) Voltar à pasta atividade e remover arquivos sobrando
cd ~/atividade
rm -f *.txt *.doc

# 10) Remover arquivos com número 0 antes da extensão
rm -f *[0-9].*

# 11) Remover arquivos .txt da pasta Atividades_Alunos
cd Atividades_Alunos
rm -f *.txt

# 12) Remover tudo
cd ~/atividade
rm -rf *