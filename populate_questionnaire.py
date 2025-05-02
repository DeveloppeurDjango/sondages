import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sondages.settings')
django.setup()

from sondage.models import Section, Question, Option

# Clear existing data (optional, comment out if you don't want to clear)
Section.objects.all().delete()
Question.objects.all().delete()
Option.objects.all().delete()

# Section 1: Informations générales
s1 = Section.objects.create(name="Informations générales")

# New questions for Nom, Prénom, Profession
q00a = Question.objects.create(section=s1, number="Q00A", text="Nom", is_text=True)
q00b = Question.objects.create(section=s1, number="Q00B", text="Prénom", is_text=True)
q00c = Question.objects.create(section=s1, number="Q00C", text="Profession", is_text=True)

q1 = Question.objects.create(section=s1, number="Q01", text="Sexe")
Option.objects.create(question=q1, text="Masculin")
Option.objects.create(question=q1, text="Féminin")

q2 = Question.objects.create(section=s1, number="Q02", text="Âge")
Option.objects.create(question=q2, text="Moins de 25 ans")
Option.objects.create(question=q2, text="25-35 ans")
Option.objects.create(question=q2, text="36-45 ans")
Option.objects.create(question=q2, text="Plus de 45 ans")

q3 = Question.objects.create(section=s1, number="Q03", text="Votre statut dans le projet Clinique des Entrepreneurs Africains")
Option.objects.create(question=q3, text="Salarié(e) permanent")
Option.objects.create(question=q3, text="Salarié(e) à temps partiel")
Option.objects.create(question=q3, text="Membre de l’organisation COFEDA")
Option.objects.create(question=q3, text="Formateur(trice) ou expert(e)")
Option.objects.create(question=q3, text="Volontaire (bénévole)")
Option.objects.create(question=q3, text="Participant(e) entrepreneur(e)")
Option.objects.create(question=q3, text="Équipe de projet")

q4 = Question.objects.create(section=s1, number="Q04", text="Type de contrats")
Option.objects.create(question=q4, text="Contrat à durée déterminée")
Option.objects.create(question=q4, text="Contrat à durée indéterminée")
Option.objects.create(question=q4, text="Contrat de bénévolat")
Option.objects.create(question=q4, text="Contrat de prestation de services")
Option.objects.create(question=q4, text="Contrat de partenariat")

q5 = Question.objects.create(section=s1, number="Q05", text="Depuis combien de temps êtes-vous impliqué(e) dans le programme ?")
Option.objects.create(question=q5, text="Moins de 6 mois")
Option.objects.create(question=q5, text="6 mois - 1 an")
Option.objects.create(question=q5, text="1 - 3 ans")
Option.objects.create(question=q5, text="Plus de 3 ans")

# Section 2: Gestion des Volontaires
s2 = Section.objects.create(name="Gestion des Volontaires")

q6 = Question.objects.create(
    section=s2,
    number="Q06",
    text="Dans quelle mesure pensez-vous que les défis suivants affectent la mobilisation et la gestion des volontaires dans les projets communautaires ?",
    is_likert=True
)
challenges_q6 = [
    "Manque de motivation des volontaires",
    "Absence de formation",
    "Faible reconnaissance du travail",
    "Encadrement insuffisant",
    "Insuffisance des ressources logistiques",
    "Manque de communication"
]
for challenge in challenges_q6:
    Option.objects.create(question=q6, text=challenge)

q7 = Question.objects.create(
    section=s2,
    number="Q07",
    text="Dans quelle mesure les stratégies suivantes vous semblent-elles efficaces pour attirer, encadrer et fidéliser les volontaires dans les projets communautaires ?",
    is_likert=True
)
strategies_q7 = [
    "Organisation de formation pour volontaires",
    "Remise de certificats ou reconnaissance officielle",
    "Implication des leaders locaux",
    "Communication régulière sur les objectifs du projet",
    "Clarté des rôles et responsabilités",
    "Inclusion des volontaires dans la prise de décision"
]
for strategy in strategies_q7:
    Option.objects.create(question=q7, text=strategy)

# Section 3: Stratégies de Mobilisation et Fidélisation
s3 = Section.objects.create(name="Stratégies de Mobilisation et Fidélisation")

q8 = Question.objects.create(
    section=s3,
    number="Q08",
    text="Dans quelle mesure pensez-vous que les actions suivantes sont efficaces pour mobiliser les volontaires et les ressources locales dans les projets communautaires ?",
    is_likert=True
)
actions_q8 = [
    "Sensibilisation à travers les leaders communautaires",
    "Utilisation des réseaux sociaux ou médias locaux",
    "Campagnes d'information porte-à-porte",
    "Organisation d'activités collectives (forums, journées citoyennes)",
    "Collaboration avec les écoles, universités, églises ou associations locales",
    "Implication des bénéficiaires dès la conception du projet"
]
for action in actions_q8:
    Option.objects.create(question=q8, text=action)

q9 = Question.objects.create(
    section=s3,
    number="Q09",
    text="Dans quelle mesure pensez-vous que les actions suivantes sont efficaces pour fidéliser les volontaires dans les projets communautaires ?",
    is_likert=True
)
actions_q9 = [
    "Reconnaissance publique ou symbolique",
    "Suivi et accompagnement personnalisé",
    "Participation des volontaires à la prise de décision",
    "Opportunité de formation ou développement personnel",
    "Bon climat de travail et esprit d'équipe",
    "Petites incitations matérielles (repas, transport, t-shirts...)"
]
for action in actions_q9:
    Option.objects.create(question=q9, text=action)

# Section 4: Mobilisation des Ressources
s4 = Section.objects.create(name="Mobilisation des Ressources (Humaines, matérielles, financières)")

q10 = Question.objects.create(
    section=s4,
    number="Q10",
    text="Dans quelle mesure pensez-vous que les actions suivantes sont efficaces pour mobiliser les ressources humaines locales (volontaires, animateurs, leaders...) dans les projets communautaires ?",
    is_likert=True
)
actions_q10 = [
    "Implication des leaders communautaires",
    "Organisation de séances d'information et de sensibilisation",
    "Identification des compétences locales disponibles",
    "Valorisation du rôle des volontaires dans la communauté",
    "Offrir des opportunités de formation ou de montée en compétences"
]
for action in actions_q10:
    Option.objects.create(question=q10, text=action)

q11 = Question.objects.create(
    section=s4,
    number="Q11",
    text="Dans quelle mesure les stratégies suivantes sont-elles efficaces pour mobiliser des ressources matérielles, financières, techniques pour les projets communautaires ?",
    is_likert=True
)
strategies_q11 = [
    "Appel aux dons locaux (entreprises, diaspora, citoyens)",
    "Organisation d'événements de collecte de fonds",
    "Partenariats avec des institutions locales",
    "Valorisation de ressources en nature (locaux, matériels, temps de travail ...)"
]
for strategy in strategies_q11:
    Option.objects.create(question=q11, text=strategy)

# Section 5: Perspectives et Améliorations
s5 = Section.objects.create(name="Perspectives et Améliorations")

q12 = Question.objects.create(
    section=s5,
    number="Q12",
    text="Dans quelle mesure pensez-vous qu’il est prioritaire de renforcer les actions suivantes pour améliorer la gestion des ressources humaines dans les projets communautaires ?",
    is_likert=True
)
actions_q12 = [
    "Renforcement des capacités du personnel encadrant",
    "Formalisation des procédures de gestion des volontaires",
    "Création d’un système de suivi et d’évaluation des volontaires",
    "Amélioration de la communication interne et externe du projet"
]
for action in actions_q12:
    Option.objects.create(question=q12, text=action)

q13 = Question.objects.create(
    section=s5,
    number="Q13",
    text="Dans quelle mesure les actions suivantes contribueraient-elles efficacement à améliorer la mobilisation et la fidélisation des volontaires et des ressources locales ?",
    is_likert=True
)
actions_q13 = [
    "Mise en place d’un système de reconnaissance des volontaires",
    "Adaptation des stratégies de mobilisation aux réalités locales",
    "Instauration d’un dialogue régulier avec les acteurs locaux"
]
for action in actions_q13:
    Option.objects.create(question=q13, text=action)

print("Database populated successfully!")