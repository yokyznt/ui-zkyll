import io, json, os, re, sys, time, urllib.parse, urllib.request, zipfile

API = "https://moxen.cl/api/descarga.php"
CODIGO = "REGALO_MOXEN"
DESTINO = os.environ.get("ZKYLL_RECURSOS", r"D:\moxen\recursos")
CATEGORIAS = {
    "navegacion", "texto", "interruptores", "cargas", "cursor", "fondos", "scroll",
    "galerias", "transiciones", "iconos", "tresd", "generativo", "media",
    "diagramas", "portadas",
}


def pagina():
    req = urllib.request.Request("https://moxen.cl/recursos.html", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36", "Accept": "text/html,*/*;q=0.8", "Accept-Language": "es"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    m = re.search(r'<script[^>]*id="recursos-datos"[^>]*>(.*?)</script>', html, re.S)
    return json.loads(m.group(1))


def main():
    solo = set(sys.argv[1:]) or CATEGORIAS
    datos = pagina()
    pendientes = [(k, v["categoria"]) for k, v in datos.items() if v["categoria"] in solo]
    for k, c in pendientes:
        salida = os.path.join(DESTINO, c, k)
        if os.path.isdir(salida) and os.listdir(salida):
            continue
        cuerpo = urllib.parse.urlencode({"codigo": CODIGO, "recursos": k}).encode()
        bruto = urllib.request.urlopen(urllib.request.Request(API, data=cuerpo), timeout=60).read()
        os.makedirs(salida, exist_ok=True)
        zipfile.ZipFile(io.BytesIO(bruto)).extractall(salida)
        time.sleep(0.2)
    print(f"{len(pendientes)} recursos en {DESTINO}")


main()
