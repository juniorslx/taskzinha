# Projeto Django - Mensagens

Projeto Django simples com formulário para enviar mensagens e lista para exibi-las com horário. Inclui botão para excluir mensagens.

---

## Requisitos

- Python 3.8+
- Django 5.2+

---

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
2. Crie e ative o ambiente virtual
No Windows (PowerShell):

powershell
Copiar
Editar
python -m venv venv
.\venv\Scripts\Activate.ps1
No Linux/macOS:

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Faça as migrações e crie o banco de dados
bash
Copiar
Editar
python manage.py migrate
5. Rode o servidor
bash
Copiar
Editar
python manage.py runserver
6. Acesse no navegador
Abra o navegador e acesse:

cpp
Copiar
Editar
http://127.0.0.1:8000/
Django Admin
Para acessar o painel admin:

Crie um superusuário (se ainda não criou):

bash
Copiar
Editar
python manage.py createsuperuser
Acesse:

arduino
Copiar
Editar
http://127.0.0.1:8000/admin/
Funcionalidades
Enviar mensagens com nome e texto

Listar mensagens enviadas com horário

Excluir mensagens com botão na lista

Observações
Não esqueça de ativar o ambiente virtual antes de rodar comandos

O banco usado é SQLite para simplicidade, fica no arquivo db.sqlite3
