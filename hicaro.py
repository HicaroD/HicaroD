from pathlib import Path
import json
import rich
from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table
from rich.layout import Layout

def get_projects():
    path = Path("projects.json")
    if not path.is_file():
        print("Error: projects.json not found")
        exit(1)

    with open(path, "r") as file:
        json_file = json.load(file)
        return json_file


def get_project_table(projects):
    projects_table = Table(title="Projects", show_header=True, header_style="bold", show_lines=True, width=60)
    projects_table.add_column("Name")
    projects_table.add_column("Description")
    projects_table.add_column("Tools")

    for project in projects:
        project_name_with_link = f"[link={project['link']}]{project['name']}"
        projects_table.add_row(
            project_name_with_link,
            project["description"],
            project["tools"],
        )

    return projects_table


def get_personal_information_tree():
    tree = Tree(
        "🤓 [link=https://drive.google.com/drive/folders/1HEgd8xXOdbcE1ve6Uhzkxa3vlJ06AfjY?usp=share_link]Hícaro Dânrlley"
    )
    tree.add("🇧🇷 Brazilian")
    tree.add("😉 19 years-old")
    tree.add("🔧 Back-end developer")
    tree.add("📚 Computer Science student at [link=https://ufal.br/]UFAL")
    contact_tree = Tree("📇 Contact:")
    contact_tree.add("✉️: [link=mailto:hdanrlley1@gmail.com]hdanrlley1@gmail.com")
    contact_tree.add(
        "LinkedIn️: [link=https://www.linkedin.com/in/hicaromiguel/]hicaromiguel"
    )
    tree.add(contact_tree)
    return tree


def get_about_me_panel():
    about = """I've been writing code for 3 years in Python, Go, Rust and Dart. Nowadays, I work as Flutter mobile developer and I really love to work on open source projects. Feel free to see some of them below 😄."""
    panel = Panel.fit(about, box=box.DOUBLE, title="About me", width=60)
    return panel


def main():
    console = Console(record=True, width=100)
    personal_info_tree = get_personal_information_tree()

    projects = get_projects()
    print(projects)
    project_table = get_project_table(projects)

    about_me_panel = get_about_me_panel()

    console.print(Columns([about_me_panel, personal_info_tree]))
    console.print(project_table)

    CONSOLE_HTML_FORMAT = """<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>"""
    console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)

if __name__ == "__main__":
    main()
