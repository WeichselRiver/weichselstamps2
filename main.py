import tomllib

with open("marken.toml", "rb") as f:
    data = tomllib.load(f)

print(data["1"])
