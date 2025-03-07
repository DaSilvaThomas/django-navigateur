from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Ajout des formulaires
from .forms import LoginForm, RegistrationForm

# Ajout du modèle pour la base de données
from .models import HistoriqueDeRecherche

# Nettoyage des données
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Graphique
from pyvis.network import Network


def login_view(request):
    if request.user.is_authenticated:  # Vérifie si l'utilisateur est déjà connecté
        return redirect('home')  # Redirige vers la page d'accueil

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'browser/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige vers la page de connexion après la déconnexion


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après l'inscription
            return redirect('home')  # Redirige vers la page d'accueil après inscription
    else:
        form = RegistrationForm()

    return render(request, 'browser/registration.html', {'form': form})


@login_required(login_url='login')  # Redirige vers /login si non connecté
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Les utilisateurs non connecté sont redirigés vers la page login
    
    url = request.GET.get('url', '')

    graph_html = ""  # On initialisation le graphique HTML

    if url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        domaine_principal = urlparse(url).netloc  # Récupération du domaine principal (exemple : "google.com")
        liens_internes = set()  # On créé une collection non ordonnée et sans doublons
        liens_externes = set()
        images_nb = len(soup.find_all('img'))
        tableaux_nb = len(soup.find_all('table'))

        for link in soup.find_all('a', href=True):  # Récupération de toutes les balises <a> qui contiennent un href
            href = urljoin(url, link['href'])
            href_parse = urlparse(href)
            if domaine_principal in href:
                href_chemin = href_parse.path  # On récupère le chemin après le nom de domaine
                if href_chemin:  # Pour éviter les chemins vides
                    liens_internes.add(href_chemin)
            else:
                liens_externes.add(href_parse.netloc)  # On affiche seulement le nom de domaine

        liens_internes_nb = len(liens_internes)
        liens_externes_nb = len(liens_externes)

        # Création du graphe Pyvis
        net = Network(height="100%", width="100%", bgcolor="#ffffff", font_color="black", directed=True)
        net.toggle_physics(False)
        net.add_node(domaine_principal, label=domaine_principal, color="#ff5733", size=20, x=0, y=0)

        espacement_y = 50

        # Placer les liens internes (à droite) avec le label à droite
        for i, lien in enumerate(liens_internes):
            y_position = (i - liens_internes_nb / 2) * espacement_y  # Répartition verticale
            net.add_node(
                lien,
                label=lien,  # Le label est le texte visible
                title=lien,  # Tooltip au survol
                color="#33ff57",
                size=10,
                x=400,  # Liens internes à droite
                y=y_position,
                physics=False
            )
            net.add_edge(domaine_principal, lien, color="#33ff57")

        # Placer les liens externes (à gauche) avec le label à gauche
        for i, lien in enumerate(liens_externes):
            y_position = (i - liens_externes_nb / 2) * espacement_y  # Répartition verticale
            net.add_node(
                lien,
                label=lien,  # Le label est le texte visible
                title=lien,  # Tooltip au survol
                color="#3357ff",
                size=10,
                x=-400,  # Liens externes à gauche
                y=y_position,
                physics=False
            )
            net.add_edge(domaine_principal, lien, color="#3357ff")

        graph_html = net.generate_html()

        # Supprimer toutes les balises <center> et <h1> générées par Pyvis
        graph_html = graph_html.replace("<center>", "").replace("</center>", "")
        graph_html = graph_html.replace("<h1>", "").replace("</h1>", "")

        liens_internes_nb = len(liens_internes)
        liens_externes_nb = len(liens_externes)

        HistoriqueDeRecherche.objects.create(
            utilisateur=request.user,
            url=url,
            liens_internes=liens_internes_nb,
            liens_externes=liens_externes_nb,
            images=images_nb,
            tableaux=tableaux_nb
        )

    # Récupération des 4 derniers urls visités par l'utilisateur
    historique = HistoriqueDeRecherche.objects.filter(utilisateur=request.user).order_by('-date')[:4]

    return render(request, 'browser/home.html', {
        'graph_html': graph_html,
        'liens_internes': liens_internes_nb if url else 0,
        'liens_externes': liens_externes_nb if url else 0,
        'images': images_nb if url else 0, 
        'tableaux': tableaux_nb if url else 0,
        'historique': historique,
    })
