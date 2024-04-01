from opencart import *

# fonctionnalites presentes: bloquer ventes, liste des clients cconnectes, liste des transactions en cours, bloquer/autoriser acces web, lister les catalogues

if __name__ == "__main__":
    root = tk.Tk()
    app = OpenCartApp(root)
    app.run()