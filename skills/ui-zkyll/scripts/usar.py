import os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def raiz():
    env = os.environ.get("ZKYLL_RECURSOS")
    if env:
        return env
    local = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "recursos")
    return local if os.path.isdir(local) else r"D:\moxen\recursos"


def buscar(slug):
    base = raiz()
    for cat in sorted(os.listdir(base)):
        ruta = os.path.join(base, cat, slug, "moxen-" + slug)
        if os.path.isdir(ruta):
            return cat, ruta
    return None, None


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("uso: usar.py <carpeta_destino> <slug> [slug ...]")
        return
    destino, slugs = args[0], args[1:]
    for slug in slugs:
        cat, ruta = buscar(slug)
        if not ruta:
            print(f"{slug}: no existe")
            continue
        salida = os.path.join(destino, "zkyll", slug)
        if os.path.isdir(salida):
            shutil.rmtree(salida)
        shutil.copytree(ruta, salida, ignore=shutil.ignore_patterns("LICENCIA.txt"))
        html = open(os.path.join(ruta, "index.html"), encoding="utf-8").read()
        main_html = re.search(r"<main[^>]*>(.*?)</main>", html, re.S)
        if main_html:
            open(os.path.join(salida, "demo-main.html"), "w", encoding="utf-8").write(main_html.group(1).strip())
        enlaces = re.findall(r'<link[^>]+rel="stylesheet"[^>]*>', html)
        scripts = re.findall(r'<script[^>]*src="[^"]+"[^>]*></script>', html)
        print(f"== {slug} ({cat}) -> {salida}")
        for e in enlaces + scripts:
            print("  ", e)
        print("   marcado de la demo: zkyll/%s/demo-main.html" % slug if main_html else "   sin <main>: revisar index.html")


main()
