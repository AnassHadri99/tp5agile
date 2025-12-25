def greet(name):
    """Fonction qui accueille l'utilisateur par son nom"""
    return f"Bonjour, {name}! Bienvenue dans notre application!"

def main():
    print("Hello, World! Version 2.0")
    nom = input("Entrez votre nom: ")
    print(greet(nom))

if __name__ == "__main__":
    main()