from flask import Flask, render_template_string, redirect, url_for
import json

from apipytohn import gerar_qr_code_personalizado 

app = Flask(__name__)

#tela inicial
@app.route('/')
def home():
    
    dados_aluno = "JOEL_R12345"
    recurso_selecionado = "EXERCICIO_FOCO_2MIN"
    
    dados_gerados = gerar_qr_code_personalizado(dados_aluno, recurso_selecionado)
    
    
    dados_formatados = json.dumps(json.loads(dados_gerados), indent=2, ensure_ascii=False)
    
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>MVP - Seleção de Perfil</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            
            /* Fundo e Container do Dispositivo */
            body {{ 
                display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; 
                background-color: #f0f0f0; 
                font-family: 'Roboto', sans-serif;
            }}
            .app-screen {{
                width: 360px; 
                height: 640px; 
                background-color: #FFFFFF;
                box-shadow: 0 0 15px rgba(0,0,0,0.2);
                border-radius: 8px;
                overflow: hidden;
                padding: 40px 20px;
                box-sizing: border-box;
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
                position: relative; /* Necessário para o modal */
            }}
            
            h1 {{
                font-size: 24px;
                color: #333;
                font-weight: 400;
                margin-bottom: 50px;
                margin-top: 50px;
            }}
            
            .profile-card {{
                width: 100%;
                height: 180px;
                border-radius: 16px;
                margin-bottom: 20px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                transition: transform 0.2s;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                text-decoration: none; /* Remove sublinhado do link */
                color: inherit;
            }}
            .profile-card:hover {{
                transform: translateY(-2px);
            }}
            
            /* Estilos específicos das cartas (baseados nas cores da imagem) */
            .child-card {{
                background: linear-gradient(135deg, #E3F2FD, #BBDEFB); 
            }}
            
            .adult-card {{
                background: linear-gradient(135deg, #F3E5F5, #E1BEE7); 
            }}
            
            .icon-circle {{
                width: 70px;
                height: 70px;
                border-radius: 50%;
                margin-bottom: 10px;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 30px;
            }}

            .child-card .icon-circle {{
                background-color: #90CAF9;
                color: #1976D2;
            }}
            
            .adult-card .icon-circle {{
                background-color: #CE93D8;
                color: #8E24AA;
            }}
            
            .profile-card span {{
                font-size: 18px;
                font-weight: 700;
            }}

            /* Seção de Evidência (Removida) */
            
            .button {{ 
                background-color: #00BCD4; 
                color: white; 
                padding: 10px; 
                margin-bottom: 10px;
                border-radius: 5px; 
                text-decoration: none; 
                display: block; 
                font-weight: bold; 
                font-size: 14px;
                text-align: center;
            }}

            pre {{ text-align: left; background-color: #eee; padding: 10px; border-radius: 5px; font-size: 8px; white-space: pre-wrap; }}

            /* --- ESTILOS DO MODAL DE LOGIN --- */
            
            .modal-overlay {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.5); /* Fundo escurecido */
                display: none; /* Começa escondido */
                justify-content: center;
                align-items: center;
                z-index: 10;
            }}
            
            .modal-content {{
                background-color: #FFFFFF;
                padding: 25px;
                border-radius: 12px;
                width: 85%;
                max-width: 300px;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            }}
            
            .modal-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 20px;
            }}
            
            .modal-header h2 {{
                font-size: 18px;
                font-weight: 700;
                color: #333;
            }}
            
            .close-button {{
                cursor: pointer;
                font-size: 20px;
                color: #999;
            }}
            
            .modal-body label {{
                display: block;
                margin-bottom: 8px;
                font-size: 14px;
                font-weight: 400;
                color: #555;
            }}
            
            .pin-input {{
                width: 100%;
                padding: 12px;
                border: 2px solid #EEE;
                border-radius: 8px;
                font-size: 16px;
                text-align: center;
                margin-bottom: 10px;
                letter-spacing: 5px;
            }}
            
            .pin-hint {{
                font-size: 12px;
                color: #999;
                margin-bottom: 25px;
            }}

            .modal-footer {{
                display: flex;
                justify-content: space-between;
                gap: 10px;
            }}
            
            .modal-footer .btn {{
                padding: 12px;
                border: none;
                border-radius: 8px;
                font-weight: bold;
                cursor: pointer;
                flex: 1;
                transition: background-color 0.2s;
            }}
            
            .btn-cancel {{
                background-color: #F8F8F8;
                color: #333;
                border: 1px solid #DDD;
            }}
            
            .btn-enter {{
                background-color: #9C27B0; /* Cor Roxa/Violeta */
                color: white;
            }}
            
        </style>
        <!-- Ícones do Font Awesome -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    <body>
        <div class="app-screen">
            <h1>Bem-vindo(a)! Quem vai usar o App hoje?</h1>
            
            <!-- Card 1: Eu sou a Criança (REDICIONA PARA A TELA DE SCAN) -->
            <a href="{url_for('scan_screen')}" class="profile-card child-card">
                <div class="icon-circle">
                    <i class="fas fa-user"></i>
                </div>
                <span>Eu sou a Criança</span>
            </a>

            <!-- Card 2: Sou Pai/Professor (ABRE O MODAL DE LOGIN) -->
            <div id="adult-card" class="profile-card adult-card">
                <div class="icon-circle">
                    <i class="fas fa-lock"></i>
                </div>
                <span>Sou Pai/Professor</span>
            </div>

            <!-- MODAL DE LOGIN -->
            <div id="login-modal" class="modal-overlay">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2>Login do Responsável</h2>
                        <span id="close-modal" class="close-button">&times;</span>
                    </div>
                    <div class="modal-body">
                        <label for="pin-acesso">Digite o PIN de acesso:</label>
                        <input type="password" id="pin-acesso" class="pin-input" maxlength="4" placeholder="****">
                        <p class="pin-hint">PIN de demonstração: 1234</p>
                    </div>
                    <div class="modal-footer">
                        <button id="cancel-login" class="btn btn-cancel">Cancelar</button>
                        <button id="enter-login" class="btn btn-enter">Entrar</button>
                    </div>
                </div>
            </div>

            <!-- Seção de Prova de Backend (MANTIDA NO CÓDIGO MAS FORA DA INTERFACE VISÍVEL) -->
            <div style="display:none;">
                <pre id="backend-proof">{dados_formatados}</pre>
            </div>
            
        </div>
        
        <script>
            document.addEventListener('DOMContentLoaded', () => {{
                const adultCard = document.getElementById('adult-card');
                const loginModal = document.getElementById('login-modal');
                const closeModal = document.getElementById('close-modal');
                const cancelLogin = document.getElementById('cancel-login');
                const enterLogin = document.getElementById('enter-login');
                const pinInput = document.getElementById('pin-acesso');

                // Função para abrir o modal
                adultCard.addEventListener('click', () => {{
                    loginModal.style.display = 'flex';
                }});

                // Função para fechar o modal
                const close = () => {{
                    loginModal.style.display = 'none';
                    pinInput.value = ''; // Limpa o campo
                }};

                closeModal.addEventListener('click', close);
                cancelLogin.addEventListener('click', close);

                // Lógica de simulação de login
                enterLogin.addEventListener('click', () => {{
                    const pin = pinInput.value;
                    if (pin === '1234') {{
                        alert('Login Simulado BEM-SUCEDIDO! Redirecionando para o Painel do Responsável...');
                        // Em um app real, aqui redirecionaria para o dashboard
                        close();
                    }} else {{
                        alert('PIN Incorreto. Tente novamente. (Dica: 1234)');
                        pinInput.value = '';
                    }}
                }});
                
                // Previne que o clique no overlay feche o modal (opcional, mas comum)
                loginModal.addEventListener('click', (e) => {{
                    if (e.target === loginModal) {{
                        // close();
                    }}
                }});
            }});

            // Função de alerta customizada (Substitui o alert() padrão)
            function alert(message) {{
                const existingAlert = document.getElementById('custom-alert');
                if (existingAlert) existingAlert.remove();

                const alertBox = document.createElement('div');
                alertBox.id = 'custom-alert';
                alertBox.style.cssText = `
                    position: fixed; top: 20px; right: 20px; 
                    background-color: #26A69A; color: white; 
                    padding: 15px 25px; border-radius: 8px; 
                    box-shadow: 0 4px 10px rgba(0,0,0,0.2); 
                    z-index: 1000; font-size: 14px;
                `;
                alertBox.textContent = message;
                document.body.appendChild(alertBox);

                setTimeout(() => {{
                    alertBox.remove();
                }}, 3000);
            }}
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

# TELA DE ESCANEAMENTO
@app.route('/scan')
def scan_screen():
    
    dados_aluno = "JOEL_R12345"
    recurso_selecionado = "EXERCICIO_FOCO_2MIN"
    
    dados_gerados = gerar_qr_code_personalizado(dados_aluno, recurso_selecionado)
    
    dados_json = json.loads(dados_gerados)
    nome_recurso = dados_json.get("detalhes", {}).get("nome", "Recurso Não Encontrado")
    
    dados_formatados = json.dumps(dados_json, indent=2, ensure_ascii=False)
    
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>MVP - Tela de Escaneamento</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            
            /* Styles for the app screen */
            body {{ 
                display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; 
                background-color: #f0f0f0; 
                font-family: 'Roboto', sans-serif;
            }}
            .app-screen {{
                width: 360px; 
                height: 640px; 
                background-color: #FFFFFF;
                box-shadow: 0 0 15px rgba(0,0,0,0.2);
                border-radius: 8px; 
                overflow: hidden;
                padding: 40px 20px 20px 20px;
                box-sizing: border-box;
                display: flex; /* Adicionado para centralizar e organizar melhor */
                flex-direction: column;
                align-items: center;
            }}
            
            h1 {{
                font-size: 24px;
                color: #26A69A; 
                font-weight: 700;
                margin-bottom: 30px;
                text-align: center;
            }}
            
            .scanner-frame {{
                margin: 30px auto;
                width: 250px;
                height: 250px;
                border: 3px dashed #26A69A; 
                border-radius: 12px;
                background-color: #E0F7FA; 
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                cursor: pointer;
            }}
            
            .camera-icon {{
                font-size: 40px;
                color: #26A69A;
                margin-bottom: 10px;
            }}
            
            .scanner-text {{
                font-size: 14px;
                color: #555;
            }}
            
            .small-link {{
                margin-top: 20px;
                font-size: 14px;
                color: #777;
                text-decoration: underline;
                cursor: pointer;
            }}

            /* result-box removido */
            
            .button {{ 
                background-color: #00BCD4; 
                color: white; 
                padding: 12px; 
                margin-top: 100px; /* Ajuste para centralizar o botão de voltar */
                border-radius: 5px; 
                text-decoration: none; 
                display: block; 
                font-weight: bold; 
                text-align: center;
                width: 100%;
            }}

            pre {{ text-align: left; background-color: #eee; padding: 10px; border-radius: 5px; font-size: 8px; white-space: pre-wrap; }}

        </style>
        <!-- Icones do Font Awesome -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    <body>
        <div class="app-screen">
            <h1>Hora de Focar! Escaneie seu código.</h1>
            
            <div class="scanner-frame">
                <i class="camera-icon fas fa-qrcode"></i> 
                <div class="scanner-text">Toque aqui para simular o escaneamento</div>
                <div style="font-size: 12px; color: #555; margin-top: 10px;">Aponte o código da pulseira dentro do quadro.</div>
            </div>

            <div class="small-link">
                <i class="fas fa-keyboard" style="margin-right: 5px;"></i> Inserir código manualmente
            </div>

            <!-- result-box removido -->

            <a href="{url_for('home')}" class="button" style="background-color: #999;">
                Voltar para Seleção de Perfil
            </a>

            <!-- Seção de Prova de Backend (MANTIDA NO CÓDIGO MAS FORA DA INTERFACE VISÍVEL) -->
            <div style="display:none;">
                <p style="font-size: 12px; margin-top: 15px;">Dados JSON gerados pelo backend (`apipytohn.py`):</p>
                <pre>{dados_formatados}</pre>
            </div>
            
        </div>
        <script>
            // Função de alerta customizada para a tela de scan também
            function alert(message) {{
                const existingAlert = document.getElementById('custom-alert');
                if (existingAlert) existingAlert.remove();

                const alertBox = document.createElement('div');
                alertBox.id = 'custom-alert';
                alertBox.style.cssText = `
                    position: fixed; top: 20px; right: 20px; 
                    background-color: #26A69A; color: white; 
                    padding: 15px 25px; border-radius: 8px; 
                    box-shadow: 0 4px 10px rgba(0,0,0,0.2); 
                    z-index: 1000; font-size: 14px;
                `;
                alertBox.textContent = message;
                document.body.appendChild(alertBox);

                setTimeout(() => {{
                    alertBox.remove();
                }}, 3000);
            }}
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    # iniciar servido
    print("\n--- SERVIDOR FLASK ATUALIZADO (FLUXO DE TELAS) ---")
    print("Acesse no seu navegador: http://127.0.0.1:5000/")
    print("--------------------------------------------------\n")
    app.run(debug=True)
