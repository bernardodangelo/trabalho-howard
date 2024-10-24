## Instruções para Execução do Código

1. **Abrir a Máquina Virtual**
   - Inicie o Oracle VM VirtualBox e abra a máquina virtual configurada para o projeto.

2. **Executar o Código em Python**
   - No Visual Studio Code, abra o arquivo `principal.py`.
   - Abra o terminal integrado no Visual Studio Code.
   - Execute o código com o seguinte comando:
     ```bash
     python principal.py
     ```

3. **Configurar o Banco de Dados**
   - Abra o Oracle SQL Developer.
   - Navegue até a pasta `sql` onde estão localizados os scripts:
     - `create_table_ponto.sql`
     - `inserting_samples_records.sql`
   - Abra ambos os arquivos.

4. **Executar os Scripts SQL**
   - Com ambos os arquivos abertos, pressione `F5` (Run Script) em cada um deles para que o script seja executado e os dados sejam inseridos no banco de dados.
