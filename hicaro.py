from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree


def main():
    console = Console(record=True, width=100)

    tree = Tree("🤓 Hícaro Dânrlley")
    tree.add("🇧🇷 Brazilian")
    tree.add("😉 19 years-old")
    tree.add("🔧 Back-end developer")
    tree.add("📚 Computer Science student at [link=https://ufal.br/]UFAL")
    contact_tree = Tree("📇 Contact:")
    contact_tree.add("✉️: [link=mailto:hdanrlley1@gmail.com]hdanrlley1@gmail.com")
    contact_tree.add("LinkedIn️: [link=https://www.linkedin.com/in/hicaromiguel/]hicaromiguel")
    tree.add(contact_tree)

    about = "I'm currently looking for my first job opportunity as back-end developer. I'm very versatile and I can easily learn a new technology, such as programming languages and frameworks, in order to get the job done. I've been writing code since the beginning of 2021 in multiple programming languages, such Python, Rust, Go, C++, Dart and a bit more."

    panel = Panel.fit(about, box=box.DOUBLE, title="About me", width=60)
    console.print(Columns([panel, tree]))

    CONSOLE_HTML_FORMAT = """<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>"""
    console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)


if __name__ == "__main__":
    main()
