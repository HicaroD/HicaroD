from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

def generate_readme_file(console):
    CONSOLE_HTML_FORMAT = """<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>"""
    console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)

def main():
    console = Console(record=True, width=100)

    tree = Tree("🤓 [link=https://websiteportfolio13.herokuapp.com]Hícaro Dânrlley")
    tree.add("🔧 Back-end developer")
    tech_tree = Tree("💻 Technologies")
    tech_tree.add("🐍 Python")
    tech_tree.add("🦀 Rust")
    tree.add(tech_tree)

    about = "I'm currently looking for my first job opportunity as back-end developer. Lately I've been working on a compiler for my own programming language called idk."

    panel = Panel.fit(
        about, box=box.DOUBLE, title="About me", width=60
    )
    console.print(Columns([panel, tree]))
    generate_readme_file(console)

if __name__ == "__main__":
    main()
