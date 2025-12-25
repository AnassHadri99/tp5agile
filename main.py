def greet(name):
    """Fonction qui accueille l'utilisateur par son nom"""
    return f"Bonjour, {name}!"

def main():
    print("Hello, World!")
    nom = input("Entrez votre nom: ")
    print(greet(nom))

if __name__ == "__main__":
    main()