from flask import Flask

app = Flask( __name__)

@app.route("/")
def home():
    
    html_content = """
    <h1>Lista de Componentes de PC</h1>
    <ul>
        <li>Processador (CPU): AMD Ryzen 7 9800X3D</li>
        <li>Placa-mãe (Motherboard): ASUS TUF GAMING X670E-PLUS WIFI</li>
        <li>Memória RAM: XPG Lancer Blade RGB DDR5-6000 32GB CL30</li>
        <li>Placa de Vídeo (GPU):  ZOTAC RTX 5070 Ti Solid Core OC 16GB</li>
        <li>Armazenamento (SSD/HDD): XPG GAMMIX S70 BLADE PCIe Gen4 M.2 2TB</li>
        <li>Fonte de Alimentação (PSU): LEADEX VII Platinum PRO 1000W ATX 3.1</li>
        <li>Gabinete (CASE): DarkFlash DK431</li>
        <li>Refrigeramento (COOLER): ID-Cooling FX360 INF 360mm ARGB Liquid Cooler</li>
        <li>Sistema Operacional(SO): Windows 11 Pro 25H2 64 bit</li>
    </ul>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)