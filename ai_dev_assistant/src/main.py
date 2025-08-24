import json
import os
import shutil
from generator.generator import generate_code

def main(config_path):
    """
    Orchestrates the application generation process.
    """
    with open(config_path, 'r') as f:
        config = json.load(f)

    app_name = config.get("appName", "my_app")
    output_dir = config.get("outputDir", f"generated_apps/{app_name}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Generating application '{app_name}' in '{output_dir}'...")

    # Copy data files
    for data_file in config.get("data", []):
        source_path = os.path.join('ai_dev_assistant', data_file['source'])
        dest_path = os.path.join(output_dir, data_file['name'])
        if os.path.exists(source_path):
            shutil.copy(source_path, dest_path)
            print(f"  - Copied data file {data_file['name']} to {dest_path}")

    for component in config.get("components", []):
        template_path = os.path.join('ai_dev_assistant/templates', component['template'])
        output_path = os.path.join(output_dir, component['outputFile'])
        context = {
            "config": config,
            "component": component
        }
        generate_code(template_path, output_path, context)
        print(f"  - Generated {component['name']} ({component['language']}) -> {output_path}")

    print("Application generation complete.")


if __name__ == "__main__":
    example_config = "ai_dev_assistant/examples/sales_dashboard.json"
    main(example_config)
