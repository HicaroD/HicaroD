from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree


def main():
    console = Console(record=True, width=100)

    tree = Tree("🤓 [link=https://websiteportfolio13.herokuapp.com]Hícaro Dânrlley")
    tree.add("🇧🇷 Brazilian")
    tree.add("😉 19 years-old")
    tree.add("🔧 Back-end developer")
    tree.add("📚 Computer Science student at [link=https://ufal.br/]UFAL")
    tree.add("📇 Contact me via [link=mailto:hdanrlley1@gmail.com]e-mail")

    about = "I'm currently looking for my first job opportunity as back-end developer. I'm very passionate about compilers, that's why I've been working on a compiler for my own programming language called idk."

    panel = Panel.fit(about, box=box.DOUBLE, title="About me", width=60)
    console.print(Columns([panel, tree]))

    CONSOLE_HTML_FORMAT = """<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>"""
    console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)


if __name__ == "__main__":
    main()
