# 🧾 OCR Ticket Scanner -- API

API Flask permettant d'extraire automatiquement les informations d'un
ticket de caisse grâce à l'OCR (EasyOCR).\
Elle reçoit une image encodée en Base64, analyse le ticket et renvoie
les données structurées en JSON.

## 🚀 Fonctionnalités

-   Lecture OCR d'un ticket via **EasyOCR**
-   Extraction :
    -   Nom du magasin\
    -   Adresse\
    -   Numéro de téléphone\
    -   SIRET\
    -   Date\
    -   Articles (nom + prix)
-   Retour des données au format **JSON**
-   API simple à appeler (`/scan`)
-   Compatible avec des clients mobiles ou web (CORS activé)

## 📦 Installation

``` bash
git clone <repo>
cd <projet>
pip install -r requirements.txt
```

## ▶️ Lancer le serveur

``` bash
python app.py
```

Le serveur démarre sur :

    http://0.0.0.0:8080

## 📡 Utilisation de l'API

### Endpoint : `/scan`

**Méthodes :** POST, GET\
**Corps attendu (JSON) :**

``` json
{
  "base64String": "<image_base64>"
}
```

**Réponse :**

``` json
{
  "shop": {
    "name": "",
    "address": "",
    "nb_article": "",
    "date": "",
    "phone": "",
    "siret": ""
  },
  "articles": [
    {
      "name": "",
      "price": ""
    }
  ]
}
```

## 🛠 Technologies

-   Python 3\
-   Flask + Flask-CORS\
-   EasyOCR\
-   OpenCV\
-   PyTorch

## 📁 Structure

    app.py              # API Flask
    OcrModule.py        # Module OCR et formattage JSON
    requirements.txt    # Dépendances
