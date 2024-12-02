import json
import subprocess
import argparse
import os

def load_repos(file_path):
    with open(file_path, 'r') as file:
        repos_data = json.load(file)
    return repos_data

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Clone repositories from a JSON file.')
    parser.add_argument('--start-path', default='/Users/fddiferd/Library/Mobile Documents/com~apple~CloudDocs/Downloads',
                        help='Desired starting file path where repositories will be cloned (default: /Downloads)')
    parser.add_argument('--repos-file', default='repos.json',
                        help='Path to the repos.json file (default: repos.json)')
    args = parser.parse_args()

    start_path = args.start_path
    repos_file = args.repos_file

    # Ensure the starting path exists
    if not os.path.isdir(start_path):
        print(f"Error: The directory '{start_path}' does not exist.")
        return

    # Load repositories from the specified repos.json file
    if not os.path.isfile(repos_file):
        print(f"Error: The repos file '{repos_file}' does not exist.")
        return

    repos_data = load_repos(repos_file)
    repos_list = repos_data.get('repos', [])

    if not repos_list:
        print("Error: No repositories found in the repos.json file.")
        return

    # Change the current working directory to the starting path
    os.chdir(start_path)

    for repo_url in repos_list:
        print(f"Cloning repository from URL: {repo_url}")
        subprocess.run(['git', 'clone', repo_url])

if __name__ == "__main__":
    main()