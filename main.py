from pathlib import Path
from pipelinex import __version__, configure_source, FlexibleContext


if __name__ == "__main__":
    print("pipelinex version: ", __version__)
    project_path = Path(__file__).resolve().parent
    print("project path: ", project_path)
    source_path = configure_source(project_path)
    print("source path: ", source_path)
    context = FlexibleContext(project_path)
    context.run()
