LOGICOD — VERSION AMÉLIORÉE

1) Installer Python 3.11 ou plus récent.
2) Décompresser le dossier du projet dans un emplacement simple, par exemple C:\LogiCOD.
3) Ouvrir le dossier, cliquer dans la barre d'adresse de l'Explorateur Windows, taper cmd puis Entrée.
4) Créer l'environnement et installer les dépendances :
   python -m venv .venv
   .venv\Scripts\activate
   python -m pip install -r requirements.txt
5) Copier .env.example vers .env puis renseigner les clés nécessaires.
6) Lancer :
   python -m uvicorn main:app --reload
7) Ouvrir http://127.0.0.1:8000
   Documentation API : http://127.0.0.1:8000/docs

IA
- Gemini : renseigner GEMINI_API_KEY dans .env. Obtenir la clé dans Google AI Studio.
- Si la clé Gemini est vide, le backend conserve l'intégration Anthropic existante et utilise ANTHROPIC_API_KEY.
- Ne partagez jamais le fichier .env et ne mettez pas de clé dans index.html.

WHATSAPP RÉEL
- Créer/configurer une application Meta avec WhatsApp Business Platform / Cloud API.
- Renseigner WHATSAPP_TOKEN et WHATSAPP_PHONE_NUMBER_ID.
- Dans WhatsApp Manager, créer et faire approuver un modèle de confirmation avec trois variables de corps : nom du client, référence commande, montant MAD. Renseigner son nom exact dans WHATSAPP_TEMPLATE_NAME. Adapter WHATSAPP_TEMPLATE_LANGUAGE au code de langue du modèle.
- Déployer le backend sur une URL HTTPS publique et configurer cette URL + /api/whatsapp/webhook dans Meta.
- Utiliser WHATSAPP_VERIFY_TOKEN comme jeton de vérification et renseigner WHATSAPP_APP_SECRET pour valider la signature des webhooks.
- Les messages initiés par l'entreprise doivent respecter les règles Meta et utiliser un modèle approuvé lorsque requis. L'envoi ne fonctionnera pas tant que Meta et les identifiants ne sont pas configurés.

CIRCONSTANCES D'ÉCHEC
- Dans une commande expédiée, cliquer sur « Résultat : échec / compte rendu ».
- Renseigner le motif, les circonstances, le contact client, le transporteur et l'action suivante.
- Les tentatives sont conservées dans l'historique et l'onglet Analyses > Analyse livraison.

IMPORTANT
- Une migration SQLite non destructive ajoute les tables et colonnes manquantes au démarrage.
- Les données historiques manquantes ne sont pas reconstituées artificiellement.
- Les commandes de démonstration sont fictives.
