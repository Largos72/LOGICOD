import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main
from fastapi.testclient import TestClient


def test_score_donnees_manquantes_ne_penalisent_pas():
    result = main.calculer_score('14:30', 'Adresse complète, quartier Maarif, Casablanca', '0661000001', 'Casablanca', 450, {})
    assert result['score'] == 0
    assert result['facteurs'] == []


def test_score_explicable_et_plafonne():
    result = main.calculer_score('02:30', 'Rue', '0661000001', 'Casablanca', 2500, {})
    assert 0 <= result['score'] <= 100
    assert {x['code'] for x in result['facteurs']} >= {'HEURE_NUIT', 'ADRESSE_TRES_COURTE', 'MONTANT_ELEVE'}


def test_compte_rendu_echec_et_analytics(tmp_path):
    main.DB_PATH = str(tmp_path / 'test.db')
    with TestClient(main.app) as client:
        created = client.post('/api/orders', json={
            'nom': 'Client Test', 'telephone': '0661000001', 'ville': 'Casablanca',
            'heure_commande': '14:30', 'adresse_textuelle': 'Rue principale quartier Maarif Casablanca', 'montant': 450
        })
        assert created.status_code == 201, created.text
        order_id = created.json()['order']['id']
        shipped = client.post(f'/api/orders/{order_id}/status', json={'statut': 'Expédiée'})
        assert shipped.status_code == 200, shipped.text
        failure = client.post(f'/api/orders/{order_id}/delivery', json={
            'resultat': 'echec', 'motif': 'Client absent',
            'circonstances': 'Le livreur est arrivé mais le client était absent.',
            'contact_client': 'Appel sans réponse', 'transporteur': 'Transporteur test',
            'prochaine_action': 'Rappeler le client demain'
        })
        assert failure.status_code == 200, failure.text
        attempts = client.get(f'/api/orders/{order_id}/delivery-attempts').json()['tentatives']
        assert len(attempts) == 1
        assert attempts[0]['circonstances'].startswith('Le livreur est arrivé')
        analytics = client.get('/api/analytics/deliveries').json()
        assert analytics['echecs'] == 1
        assert analytics['motifs'][0]['motif'] == 'Client absent'
