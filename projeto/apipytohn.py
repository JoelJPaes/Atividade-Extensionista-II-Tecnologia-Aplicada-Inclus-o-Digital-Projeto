import qrcode
import json

atividades_disponiveis = {
    "EXERCICIO_FOCO_2MIN": {"nome": "Respiração do Balão", "instrucao": "Siga o balão na tela por 1 minuto para acalmar.", "tipo": "visual"},
    "AUDIO_CALMO_3MIN": {"nome": "Ouvir Sons da Natureza", "instrucao": "Feche os olhos e ouça os sons por 3 minutos.", "tipo": "auditivo"},
    "ALONGAMENTO_RAPIDO": {"nome": "Alongamento do Gato", "instrucao": "Imite um gato se espreguiçando por 1 minuto.", "tipo": "motor"}
}

def gerar_qr_code_personalizado(id_aluno: str, id_recurso: str) -> str:
    """
    Gera um QR Code com dados do aluno e do recurso personalizado.
    O QR Code contém um JSON seguro com as informações.
    """
    if id_recurso not in atividades_disponiveis:
        return json.dumps({"erro": f"Recurso '{id_recurso}' não encontrado."})

    dados_para_qr = {
        "aluno": id_aluno,
        "recurso_id": id_recurso,
        "detalhes": atividades_disponiveis[id_recurso]
    }

    dados_json_str = json.dumps(dados_para_qr, ensure_ascii=False)
    
   
    
    return dados_json_str
