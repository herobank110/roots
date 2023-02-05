import subprocess

def f():
    p= subprocess.Popen(r"cmd /C dir src\frames /B", stdout=subprocess.PIPE)
    stdout, _ = p.communicate()
    x = sorted(stdout.decode().splitlines(), reverse=True)
    for filename in x:
        print(f'<link rel="prefetch" as="image" href="frames/{filename}" />')
    print("")
    for filename in x:
        print(f"""<div class="frameImg" style="background-image:url('frames/{filename}')"></div>""")


if __name__ == "__main__":
    f()