import requests
import subprocess
from concurrent.futures import ThreadPoolExecutor


def download_package(package):
    subprocess.run(["pip", "download", "-d", "~/Downloads/packages", package.strip()])
    print(f"downloading the package {package.strip()}")


def main():
    url = "https://pypi.org/simple/"
    call = requests.get(url)
    packages_list = []
    packages_list_final = []

    for package in call.text.split('<a href="/simple/'):
        output = package.split('</a>\n')
        packages_list.append(output)

    for index, blank in enumerate(packages_list):
        if '' in blank:
            packages_list[index].pop()

    for ind, item in enumerate(packages_list):
        placeholder = packages_list[ind][0].replace('">', '')
        placeholder = placeholder.split("/")
        packages_list_final.append(placeholder[0])

    with open("packages.txt", "w") as file:
        for line in packages_list_final:
            if line.startswith("antchain") or line.startswith("0") or line.startswith("<") or len(line) > 15:
                pass
            else:
                file.write(f"{line}\n")

    with open("packages.txt", "r") as file:
        content = file.readlines()

        max_workers = 7  # Adjust this as per your system's capacity
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(download_package, content)


if __name__ == "__main__":
    main()
