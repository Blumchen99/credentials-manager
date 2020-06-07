from lib.store import file


file.write_lines(
    "name.txt",
    "storage/",
    [
        "NAME: test123",
        "PASSWORD: 123456",
        "SERVICE: justatest"
    ]
)