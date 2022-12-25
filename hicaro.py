from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree


def main():
    console = Console(record=True, width=100)

    tree = Tree("🤓 [link=https://drive.google.com/drive/folders/1HEgd8xXOdbcE1ve6Uhzkxa3vlJ06AfjY?usp=share_link]Hícaro Dânrlley")
    tree.add("🇧🇷 Brazilian")
    tree.add("😉 19 years-old")
    tree.add("🔧 Back-end developer")
    tree.add("📚 Computer Science student at [link=https://ufal.br/]UFAL")
    contact_tree = Tree("📇 Contact:")
    contact_tree.add("✉️: [link=mailto:hdanrlley1@gmail.com]hdanrlley1@gmail.com")
    contact_tree.add("LinkedIn️: [link=https://www.linkedin.com/in/hicaromiguel/]hicaromiguel")
    tree.add(contact_tree)

    about = "I've been writing code for 3 years in multiple programming languages, such as Python, Rust, Go and Dart. Nowadays, I work as mobile developer with Flutter and I have a side project called 'Icarus', which is a compiler being written in Rust for my own programming language."

    panel = Panel.fit(about, box=box.DOUBLE, title="About me", width=60)
    console.print(Columns([panel, tree]))

    CONSOLE_HTML_FORMAT = """<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>"""
    console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)


if __name__ == "__main__":
    main()
