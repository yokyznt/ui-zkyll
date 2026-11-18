import os, re, sys

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "catalogo")
LOCAL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "recursos")
RECURSOS = os.environ.get("ZKYLL_RECURSOS") or (LOCAL if os.path.isdir(LOCAL) else "D:/moxen/recursos")


def main():
    if len(sys.argv) < 2:
        print("uso: buscar.py <palabra> [palabra ...]")
        return
    palabras = [p.lower() for p in sys.argv[1:]]
    for nombre in sorted(os.listdir(BASE)):
        if nombre == "INDEX.md" or not nombre.endswith(".md"):
            continue
        cat = nombre[:-3]
        for linea in open(os.path.join(BASE, nombre), encoding="utf-8"):
            if not linea.startswith("| `"):
                continue
            if all(p in linea.lower() for p in palabras):
                celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
                slug = celdas[0].strip("`")
                ruta = os.path.join(RECURSOS, cat, slug, "moxen-" + slug)
                print(f"{cat}/{slug} | {celdas[1]} | {celdas[2]} | deps: {celdas[3]}")
                print(f"   {ruta}")


main()
