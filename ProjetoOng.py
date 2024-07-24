import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from datetime import datetime
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='ong'
)

cursor = conexao.cursor()

class Animal:
    def __init__(self, nome, data_nascimento, especie, porte, pelagem, sexo, observacoes, idade):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._especie = especie
        self._porte = porte
        self._pelagem = pelagem
        self._sexo = sexo
        self._observacoes = observacoes
        self.idade = idade
    
    def __str__(self):
        return (f"Nome: {self._nome}, Data de Nascimento: {self._data_nascimento}, "
                f"Espécie: {self._especie}, Porte: {self._porte}, Pelagem: {self._pelagem}, "
                f"Sexo: {self._sexo}, Observações: {self._observacoes}, idade: {self.idade}")
    
    def get_nome(self):
        return self._nome
    
    def get_data_nascimento(self):
        return self._data_nascimento
    
    def get_especie(self):
        return self._especie
    
    def get_porte(self):
        return self._porte
    
    def get_pelagem(self):
        return self._pelagem
    
    def get_sexo(self):
        return self._sexo
    
    def get_observacoes(self):
        return self._observacoes
    
    def set_nome(self, nome):
        self._nome = nome
    
    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento
    
    def set_especie(self, especie):
        self._especie = especie
    
    def set_porte(self, porte):
        self._porte = porte
    
    def set_pelagem(self, pelagem):
        self._pelagem = pelagem
    
    def set_sexo(self, sexo):
        self._sexo = sexo
    
    def set_observacoes(self, observacoes):
        self._observacoes = observacoes
    
    def set_idade(self, idade):
        self.idade = idade
   
    def get_idade(self):
        return self.get_idade
    
    
class Adotante:
    def __init__(self, nome_completo, cpf, endereco, contato):
        self._nome_completo = nome_completo
        self._cpf = cpf
        self._endereco = endereco
        self._contato = contato
        self._animais_adotados = []
       
    def adotar_animal(self, animal):
        self._animais_adotados.append(animal)
    
    def __str__(self):
        animais = ', '.join([animal.nome for animal in self._animais_adotados]) if self._animais_adotados else "Nenhum"
        return (f"Nome Completo: {self._nome_completo}, CPF: {self._cpf}, "
                f"Endereço: {self._endereco}, Contato: {self._contato}, Animais Adotados: {animais}")
    
    def get_nome_completo(self):
        return self._nome_completo
    
    def get_cpf(self):
        return self._cpf
    
    def get_endereco(self):
        return self._endereco
    
    def get_contato(self):
        return self._contato
    
    def get_animais_adotados(self):
        return self._animais_adotados
    
    def set_nome_completo(self, nome_completo):
        self._nome_completo = nome_completo
    
    def set_cpf(self, cpf):
        self._cpf = cpf
    
    def set_endereco(self, endereco):
        self._endereco = endereco
    
    def set_contato(self, contato):
        self._contato = contato
    
    def set_animais_adotados(self, animais_adotados):
        self._animais_adotados = animais_adotados

def inserir_animal():
    def salvar_animal():
        nome = entry_nome.get().strip()
        data_nascimento = entry_data_nascimento.get().strip()
        especie = entry_especie.get().strip().lower()
        porte = entry_porte.get().strip().lower()
        pelagem = entry_pelagem.get().strip()
        sexo = entry_sexo.get().strip().lower()
        observacoes = entry_observacoes.get().strip()

        try:
            data_nascimento_str = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            idade = calcular_idade(data_nascimento_str)
        except ValueError:
             messagebox.showerror("Erro", "Formato de data inválido. Utilize o formato AAAA-MM-DD.")
             return     
        
#tratar as entradas erradas.
        if especie not in ["cachorro", "gato"]:
            messagebox.showerror("Erro", "Espécie inválida. Por favor, digite 'Cachorro' ou 'Gato'.")
            return
        if porte not in ["pequeno", "medio", "grande"]:
            messagebox.showerror("Erro", "Porte inválido. Por favor, digite Pequeno, Medio ou Grande")
            return
        if sexo not in ["macho", "femea"]:
            messagebox.showerror("Erro", "Sexo inválido. Por favor, digite Macho ou Femea")
            return
        
        try:
#passar os valores pro banco de dados            
            comando = 'INSERT INTO cadastros (nome, data_nascimento, especie, porte, pelagem, sexo, observacoes, idade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            valores = (nome, data_nascimento_str, especie, porte, pelagem, sexo, observacoes, idade)
            
            cursor.execute(comando, valores)
            conexao.commit()
            messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
            janela_animal.destroy()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro no banco de dados: {err}")

    janela_animal = tk.Toplevel()
    janela_animal.title("Cadastrar Animal")

    tk.Label(janela_animal, text="Nome").grid(row=0, column=0)
    entry_nome = tk.Entry(janela_animal)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela_animal, text="Data de Nascimento (AAAA-MM-DD)").grid(row=1, column=0)
    entry_data_nascimento = tk.Entry(janela_animal)
    entry_data_nascimento.grid(row=1, column=1)

    tk.Label(janela_animal, text="Espécie (Cachorro ou Gato)").grid(row=2, column=0)
    entry_especie = tk.Entry(janela_animal)
    entry_especie.grid(row=2, column=1)

    tk.Label(janela_animal, text="Porte (Pequeno, Medio, Grande)").grid(row=3, column=0)
    entry_porte = tk.Entry(janela_animal)
    entry_porte.grid(row=3, column=1)

    tk.Label(janela_animal, text="Pelagem").grid(row=4, column=0)
    entry_pelagem = tk.Entry(janela_animal)
    entry_pelagem.grid(row=4, column=1)

    tk.Label(janela_animal, text="Sexo (Macho ou femea)").grid(row=5, column=0)
    entry_sexo = tk.Entry(janela_animal)
    entry_sexo.grid(row=5, column=1)

    tk.Label(janela_animal, text="Observações").grid(row=6, column=0)
    entry_observacoes = tk.Entry(janela_animal)
    entry_observacoes.grid(row=6, column=1)

    tk.Button(janela_animal, text="Salvar", command=salvar_animal).grid(row=7, column=0, columnspan=2, pady=10)
#calcular a idade maxima
def calcular_idade(data_nascimento):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

#Listar os animais
def listar_animais():
    lista = " SELECT idcadastros, nome, data_nascimento, especie, porte, pelagem, sexo, observacoes, idade  FROM cadastros WHERE idAdotantes is null"
    cursor.execute(lista)
    resultados = cursor.fetchall() #fetchall(listar em sql) 
    janela_lista = tk.Toplevel()
    cabecalhos = ["ID", "Nome", "Data de Nascimento", "Espécie", "Porte", "Pelagem", "Sexo", "Observações", "idade"]

   
    for col, cabecalho in enumerate(cabecalhos):
        tk.Label(janela_lista, text=cabecalho, padx=10, pady=5, relief=tk.RIDGE, bg="grey").grid(row=0, column=col, sticky="nsew")

    
    for row, resultado in enumerate(resultados, start=1):
        for col, dado in enumerate(resultado):
            tk.Label(janela_lista, text=dado, padx=10, pady=5, relief=tk.RIDGE).grid(row=row, column=col, sticky="nsew")

    
    for i in range(len(cabecalhos)):
        janela_lista.grid_columnconfigure(i, weight=1, uniform="col")
    for i in range(len(resultados) + 1):
        janela_lista.grid_rowconfigure(i, weight=1)
       
#Cadastrar os adotantes
def inserir_adotante():
    def salvar_adotante():
        nome_completo = entry_nome_completo.get().strip()
        cpf = entry_cpf.get().strip()
        endereco = entry_endereco.get().strip()
        contato = entry_contato.get().strip()
        animais_adotados = entry_animais_adotados.get().strip()

        comando = 'INSERT INTO adotantes (nome_completo, cpf, endereco, contato, animais_adotados) VALUES (%s, %s, %s, %s, %s)'
        valores = (nome_completo, cpf, endereco, contato, animais_adotados)

        try:
            cursor.execute(comando, valores)
            conexao.commit()
            messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
            janela_adotante.destroy()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro no banco de dados: {err}")

    janela_adotante = tk.Toplevel()
    janela_adotante.title("Cadastrar Adotante")

    tk.Label(janela_adotante, text="Nome Completo").grid(row=0, column=0)
    entry_nome_completo = tk.Entry(janela_adotante)
    entry_nome_completo.grid(row=0, column=1)

    tk.Label(janela_adotante, text="CPF").grid(row=1, column=0)
    entry_cpf = tk.Entry(janela_adotante)
    entry_cpf.grid(row=1, column=1)

    tk.Label(janela_adotante, text="Endereço").grid(row=2, column=0)
    entry_endereco = tk.Entry(janela_adotante)
    entry_endereco.grid(row=2, column=1)

    tk.Label(janela_adotante, text="Contato").grid(row=3, column=0)
    entry_contato = tk.Entry(janela_adotante)
    entry_contato.grid(row=3, column=1)

    tk.Label(janela_adotante, text="Animais Adotados").grid(row=4, column=0)
    entry_animais_adotados = tk.Entry(janela_adotante)
    entry_animais_adotados.grid(row=4, column=1)

    tk.Button(janela_adotante, text="Salvar", command=salvar_adotante).grid(row=5, column=0, columnspan=2, pady=10)
#Listar os adotantes
def listar_adotantes():
    janela_lista_adotantes = tk.Toplevel()
    lista = "SELECT * FROM adotantes"
    cursor.execute(lista)
    resultados = cursor.fetchall()  
    
    cabecalhos = ["ID", "Nome", "Cpf", "endereco", "contato", "animais_adotados"]

   
    for col, cabecalho in enumerate(cabecalhos):
        tk.Label(janela_lista_adotantes, text=cabecalho, padx=10, pady=5, relief=tk.RIDGE, bg="grey").grid(row=0, column=col, sticky="nsew")

    
    for row, resultado in enumerate(resultados, start=1):
        for col, dado in enumerate(resultado):
            tk.Label(janela_lista_adotantes, text=dado, padx=10, pady=5, relief=tk.RIDGE).grid(row=row, column=col, sticky="nsew")

    
    for i in range(len(cabecalhos)):
        janela_lista_adotantes.grid_columnconfigure(i, weight=1, uniform="col")
    for i in range(len(resultados) + 1):
        janela_lista_adotantes.grid_rowconfigure(i, weight=1)

#adotar animal
def adotar_animal():
    def filtrar_animais():
        adotante_id = entry_adotante_id.get().strip()
        especie = entry_especie.get().strip().lower()
        porte = entry_porte.get().strip().lower()
        sexo = entry_sexo.get().strip().lower()
        idade_maxima = (entry_idade_maxima.get().strip())
        
        query = "SELECT * FROM cadastros WHERE idAdotantes is null"
        valores = []

        if especie:
            query += " AND especie = %s"
            valores.append(especie)
        if porte:
            query += " AND porte = %s"
            valores.append(porte)
        if sexo:
            query += " AND sexo = %s"
            valores.append(sexo)
        if idade_maxima:
            query += " AND idade <= %s"
            valores.append(idade_maxima)
            
        cursor.execute(query, tuple(valores))
        resultados = cursor.fetchall()

        for widget in frame_resultados.winfo_children():
            widget.destroy()

        if not resultados:
            messagebox.showinfo("Nenhum Resultado", "Nenhum animal encontrado com os filtros fornecidos.")
            return

        cabecalhos = ["ID", "Nome", "Data de Nascimento", "Espécie", "Porte", "Pelagem", "Sexo", "Observações"]

        for col, cabecalho in enumerate(cabecalhos):
            tk.Label(frame_resultados, text=cabecalho, padx=10, pady=5, relief=tk.RIDGE, bg="grey").grid(row=0, column=col, sticky="nsew")

        for row, resultado in enumerate(resultados, start=1):
            for col, dado in enumerate(resultado):
                tk.Label(frame_resultados, text=dado, padx=10, pady=5, relief=tk.RIDGE).grid(row=row, column=col, sticky="nsew")

        def selecionar_animal():
            animal_id = entry_animal_id.get().strip()
            if not animal_id:
                messagebox.showerror("Erro", "Por favor, insira o ID do animal que deseja adotar.")
                return

            cursor.execute("SELECT * FROM cadastros WHERE idcadastros = %s", (animal_id,))
            animal = cursor.fetchone()

            if not animal:
                messagebox.showerror("Erro", "ID do animal não encontrado.")
                return

            try:
                cursor.execute("INSERT INTO adocoes (adotante_id, animal_id, data_adocao) VALUES (%s, %s, %s)",
                               (adotante_id, animal_id, date.today()))

                cursor.execute("UPDATE cadastros SET idAdotantes = %s WHERE idcadastros = %s", (adotante_id, animal_id))
                conexao.commit()

                cursor.execute("SELECT animais_adotados FROM adotantes WHERE idAdotantes = %s", (adotante_id,))
                animais_adotados = cursor.fetchone()[0]
                animais_adotados = int(animais_adotados)
                novo_total_adotados = animais_adotados + 1

                cursor.execute("UPDATE adotantes SET animais_adotados = %s WHERE idAdotantes = %s", (novo_total_adotados, adotante_id))
                conexao.commit()

                messagebox.showinfo("Sucesso", "Adoção realizada com sucesso!")
                janela_adocao.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro no banco de dados: {err}")

        tk.Label(frame_resultados, text="ID do Animal para Adotar").grid(row=len(resultados) + 1, column=0)
        entry_animal_id = tk.Entry(frame_resultados)
        entry_animal_id.grid(row=len(resultados) + 1, column=1)
        tk.Button(frame_resultados, text="Adotar", command=selecionar_animal).grid(row=len(resultados) + 2, column=0, columnspan=2, pady=10)

    janela_adocao = tk.Toplevel()
    janela_adocao.title("Adotar Animal")

    tk.Label(janela_adocao, text="ID do Adotante").grid(row=0, column=0)
    entry_adotante_id = tk.Entry(janela_adocao)
    entry_adotante_id.grid(row=0, column=1)

    tk.Label(janela_adocao, text="Espécie (Cachorro ou Gato)").grid(row=1, column=0)
    entry_especie = tk.Entry(janela_adocao)
    entry_especie.grid(row=1, column=1)

    tk.Label(janela_adocao, text="Porte (Pequeno, Medio, Grande)").grid(row=2, column=0)
    entry_porte = tk.Entry(janela_adocao)
    entry_porte.grid(row=2, column=1)

    tk.Label(janela_adocao, text="Sexo (Macho ou Femea)").grid(row=3, column=0)
    entry_sexo = tk.Entry(janela_adocao)
    entry_sexo.grid(row=3, column=1)

    tk.Label(janela_adocao, text="Idade Máxima").grid(row=4, column=0)
    entry_idade_maxima = tk.Entry(janela_adocao)
    entry_idade_maxima.grid(row=4, column=1)

    tk.Button(janela_adocao, text="Filtrar", command=filtrar_animais).grid(row=5, column=0, columnspan=2, pady=10)

    frame_resultados = tk.Frame(janela_adocao)
    frame_resultados.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    janela_adocao.grid_columnconfigure(0, weight=1)
    janela_adocao.grid_rowconfigure(5, weight=1)

    janela_adocao.mainloop()

#lista de adoçoes
def listar_adocoes():
    janela_lista_adocoes = tk.Toplevel()
    lista = """
    SELECT 
        a.idadocoes, 
        adot.nome_completo, 
        an.nome, 
        a.data_adocao 
    FROM 
        adocoes as a 
    JOIN 
        adotantes as adot 
    ON 
        a.adotante_id = adot.idAdotantes 
    JOIN 
        cadastros an 
    ON 
        a.animal_id = an.idCadastros
    """
    cursor.execute(lista)
    resultados = cursor.fetchall()  
    cabecalhos = ["ID", "Nome do Adotante", "Nome do Animal", "Data da Adoção"]

    for col, cabecalho in enumerate(cabecalhos):
        tk.Label(janela_lista_adocoes, text=cabecalho, padx=10, pady=5, relief=tk.RIDGE, bg="grey").grid(row=0, column=col, sticky="nsew")

    for row, resultado in enumerate(resultados, start=1):
        for col, dado in enumerate(resultado):
            tk.Label(janela_lista_adocoes, text=dado, padx=10, pady=5, relief=tk.RIDGE).grid(row=row, column=col, sticky="nsew")

    for i in range(len(cabecalhos)):
        janela_lista_adocoes.grid_columnconfigure(i, weight=1, uniform="col")
    for i in range(len(resultados) + 1):
        janela_lista_adocoes.grid_rowconfigure(i, weight=1)

def alterar_observacoes():
    def salvar_observacoes():
        id_animal = entry_id_animal.get().strip()
        novas_observacoes = entry_observacoes.get().strip()

        if not id_animal or not novas_observacoes:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            comando = 'UPDATE cadastros SET observacoes = %s WHERE idcadastros = %s'
            valores = (novas_observacoes, id_animal)
            cursor.execute(comando, valores)
            conexao.commit()
            messagebox.showinfo("Sucesso", "Observações atualizadas com sucesso!")
            janela_observacoes.destroy()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro no banco de dados: {err}")

    janela_observacoes = tk.Toplevel()
    janela_observacoes.title("Alterar Observações")

    tk.Label(janela_observacoes, text="ID do Animal").grid(row=0, column=0)
    entry_id_animal = tk.Entry(janela_observacoes)
    entry_id_animal.grid(row=0, column=1)

    tk.Label(janela_observacoes, text="Novas Observações").grid(row=1, column=0)
    entry_observacoes = tk.Entry(janela_observacoes)
    entry_observacoes.grid(row=1, column=1)

    tk.Button(janela_observacoes, text="Salvar", command=salvar_observacoes).grid(row=2, column=0, columnspan=2, pady=10)

def main():
    root = tk.Tk()
    root.title("ONG Sistema de Adoção")

    tk.Button(root, text="Cadastrar Animal", command=inserir_animal, bg = "#27E665").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    botao_listar = tk.Button(root, text="Listar Animais", command=listar_animais, bg = "#24CEFF")
    botao_listar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    tk.Button(root, text="Cadastrar Adotante", command=inserir_adotante, bg = "#27E665").grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    tk.Button(root, text="Listar Adotantes", command=listar_adotantes, bg = "#24CEFF").grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    tk.Button(root, text="Cadastrar Adoção", command=adotar_animal, bg = "#27E665").grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    tk.Button(root, text="Listar Adoções", command=listar_adocoes, bg = "#24CEFF").grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    tk.Button(root, text="Alterar observaçoes", command=alterar_observacoes, bg = "grey").grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    
    root.mainloop()

if __name__ == "__main__":
    main()


cursor.close()
conexao.close()
