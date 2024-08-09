from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def atletas(request):
    atletas = [
        {"nome": "Leo Jardim", "idade": "29", 
         "posicao": "goleiro", 
         "nascimento": "Ribeirão Preto (SP)", 
         "foto": "LeoJardim.png"},
        {"nome": "Léo", "idade": "28", 
         "posicao": "zagueiro", 
         "nascimento": "Rio de Janeiro (RJ)", 
         "foto": "Léo.png"},
         {"nome": "Maicon", "idade": "35", 
         "posicao": "zagueiro", 
         "nascimento": "Barretos (SP)", 
         "foto": "Maicon.png"},
         {"nome": "Paulo Henrique", "idade": "28", 
         "posicao": "Lateral-Direito", 
         "nascimento": "Sete Barras (SP)", 
         "foto": "PH.png"},
         {"nome": "Lucas Piton", "idade": "23", 
         "posicao": "Lateral-Esquerdo", 
         "nascimento": "Jundiaí (SP)", 
         "foto": "LucasPiton.png"},
         {"nome": "Hugo Moura", "idade": "26", 
         "posicao": "Volante", 
         "nascimento": "Rio Claro (RJ)", 
         "foto": "HugoMoura.png"},
         {"nome": "Mateus Carvalho", "idade": "22", 
         "posicao": "Volante", 
         "nascimento": "Tucuruí (PA)", 
         "foto": "MateusCarvalho.png"},
         {"nome": "Philippe Coutinho", "idade": "32", 
         "posicao": "Meio-Campista", 
         "nascimento": "Rio de Janeiro (RJ)", 
         "foto": "Coutinho.png"},
         {"nome": "Payet", "idade": "37", 
         "posicao": "Meio-Campista", 
         "nascimento": "Saint-Pierre, Ilha da Reunião (FRA)", 
         "foto": "Payet.png"},
         {"nome": "Vegetti", "idade": "35", 
         "posicao": "Atacante", 
         "nascimento": "Santo Domingo (ARG)", 
         "foto": "Vegetti.png"},
         {"nome": "GB", "idade": "19", 
         "posicao": "Atacante", 
         "nascimento": "Rio de Janeiro (RJ)", 
         "foto": "GB.png"}

    ]

    context = {
        "atletas": atletas,
    }
    return render(request, "atletas.html", context)

def sobre(request):
    return render(request, "sobre.html")