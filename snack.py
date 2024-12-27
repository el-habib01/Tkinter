import tkinter as tk
from tkinter import ttk

fenetre = tk.Tk()
fenetre.geometry("800x800")
fenetre.title("Restaurant Interface Graphique")

fenetre.configure(bg="navy")

style = ttk.Style()
style.configure("TButton",font="Arial", background="gold",foreground="black",padding=10,)


Introduction = tk.Label(fenetre, text="🌟 Bienvenue dans notre restaurant 🌟", font=("Arial", 20, "bold"), bg="navy", fg="gold")
Introduction.pack(pady=30)

fenetregauche = tk.Frame(fenetre, width=400, bg="navy")
fenetregauche.pack(side="left", fill="y", padx=20)

fenetredroite = tk.Frame(fenetre, width=400, bg="navy")
fenetredroite.pack(side="right", fill="y", padx=20)

menu = {
    "Pizza": 40,
    "Tacos": 49,
    "Sandwich": 30,
    "Burger": 32,
    "Frites": 15,
    "Nuggets": 35,
    "Soda": 15,
    "Limonade": 18
}

platschoisie = {}

prixtotale = 0

def ajouterauplats(plat):
    global prixtotale
    if plat in platschoisie:
        platschoisie[plat] += 1
    else:
        platschoisie[plat] = 1
    prixtotale =prixtotale+ menu[plat]
    refraichecommandes()


def affichermenu():
    fenetremenue = tk.Toplevel(fenetre)
    fenetremenue.title("Menu du Restaurant")
    fenetremenue.geometry("400x400")
    fenetremenue.configure(bg="navy")

    menue = tk.Label(fenetremenue, text="\n----------Voile le menue----------------"
      "\n Pizza :    40 DH"
      "\n Tacos :    49 DH"
      "\n Sandwich : 30 DH"
      "\n Burger :   32 DH"
      "\n Frites :   15 DH"
      "\n Nuggets :  35 DH"
      "\n Soda :     15 DH"
      "\n Limonade : 18 DH"
      "\n------------------------------------------", font=("Arial", 14), bg="navy", fg="gold")
    menue.pack(pady=20)

bouttonmenue = ttk.Button(fenetregauche, text="Afficher le Menu", command=affichermenu )
bouttonmenue.pack(pady=20, fill='x')

for plat in menu:
    boutton = ttk.Button(fenetregauche, text=f"{plat}", command=lambda plat=plat: ajouterauplats(plat))
    boutton.pack(fill='x', pady=5)



placedeplatschoisie = tk.Frame(fenetredroite, bg="navy")
placedeplatschoisie.pack(pady=20, fill="both")

def refraichecommandes():
    for widget in placedeplatschoisie.winfo_children():
        widget.destroy()

    global prixtotale
    for plat, quantity in platschoisie.items():
        placeplats = tk.Frame(placedeplatschoisie, bg="navy")
        placeplats.pack(pady=5, fill="x")


        plat_label = tk.Label(placeplats,text=f"{plat}: {quantity} x {menu[plat]} DH",font=("Arial", 12),bg="navy",fg="white",)
        plat_label.pack(side="left")

        bouttonsuprimmer = ttk.Button(placeplats,text="Supprimer",command=lambda plat=plat: supprimerplat(plat))
        bouttonsuprimmer.pack(side="right")

    total_label = tk.Label(
        placedeplatschoisie,
        text=f"\n💰 Total: {prixtotale} DH",font=("Arial", 14),bg="navy",fg="white",)
    total_label.pack(pady=20)

def supprimerplat(plat):
    global prixtotale
    if plat in platschoisie:
        prixtotale -= menu[plat]
        platschoisie[plat] -= 1
        if platschoisie[plat] <= 0:
            del platschoisie[plat]
    refraichecommandes()


def reintaliser():
    global platschoisie, prixtotale
    platschoisie = {}
    prixtotale = 0
    refraichecommandes()

bouttonreintaliser= ttk.Button(fenetredroite, text="Réintaliser", command=reintaliser)
bouttonreintaliser.pack(pady=20, fill='x')


fenetre.mainloop()