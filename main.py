import markdown
import pdfkit

# Leitura do arquivo Markdown com codificação UTF-8
with open("converter.md", "r", encoding="utf-8") as md_file:
    markdown_content = md_file.read()

# Converter Markdown para HTML e adicionar estilo CSS e meta charset para UTF-8
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif; /* Define Arial como a fonte padrão */
            font-size: 12pt;  /* Tamanho da fonte padrão */
        }}
    </style>
</head>
<body>
    {markdown.markdown(markdown_content)}
</body>
</html>
"""

# Salvar o HTML gerado em um arquivo
with open("convertido.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

# Gerar PDF a partir do HTML com fonte padrão e codificação UTF-8
pdfkit.from_string(html_content, "convertido.pdf")

print("HTML e PDF gerados com sucesso.")

