from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree


def get_contact_tree():
    contact_tree = Tree("📇 Contact:")
    contact_tree.add("✉️: [link=mailto:hdanrlley1@gmail.com]hdanrlley1@gmail.com")
    contact_tree.add(
        "LinkedIn️: [link=https://www.linkedin.com/in/hicaromiguel/]hicaromiguel"
    )
    return contact_tree


def get_personal_info_tree():
    personal_info_tree = Tree("🤓 [link=https://hicarod.github.io/]Hícaro Dânrlley")
    personal_info_tree.add("🇧🇷 Brazilian")
    personal_info_tree.add("😉 19 years-old")
    personal_info_tree.add("🔧 Back-end and mobile developer")
    personal_info_tree.add("📚 Computer Science student at [link=https://ufal.br/]UFAL")
    return personal_info_tree


def get_main_tree():
    main_tree = get_personal_info_tree()
    contact_tree = get_contact_tree()
    main_tree.add(contact_tree)
    return main_tree


def get_about_me_panel():
    about = """I'm a brazilian software developer and Computer Science student at Universidade Federal de Alagoas (UFAL). Nowadays, I work as a mobile developer with Flutter in Otimize Tech. In my spare time, I work on personal projects using many different technologies, such as Flutter, Python, NodeJS with Typescript, Rust, Go, Java, Docker, Docker Compose, MySQL, PostgreSQL, MongoDB and many more. I'm very passionate about compilers, software architecture, algorithms and data structures, back-end development and more."""
    panel = Panel.fit(about, box=box.DOUBLE, title="About me", width=60)
    return panel


def main():
    console = Console(record=True, width=100)
    personal_info_tree = get_main_tree()
    about_me_panel = get_about_me_panel()

    console.print(Columns([about_me_panel, personal_info_tree]))

    CONSOLE_HTML_FORMAT = """<pre style="font-family:Helvetica">{code}</pre>"""
    console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)


if __name__ == "__main__":
    main()
