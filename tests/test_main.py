import sys
import os

# Ajouter le répertoire parent au path pour importer main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import greet

def test_greet():
    """Test de la fonction greet"""
    result = greet("Alice")
    assert result == "Bonjour, Alice! Bienvenue dans notre application!"
    
def test_greet_with_different_name():
    """Test avec un autre nom"""
    result = greet("Bob")
    assert result == "Bonjour, Bob! Bienvenue dans notre application!"