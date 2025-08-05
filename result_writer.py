def write_result(section_name, content):
    with open("output/result.txt", "a") as f:
        f.write(f"\n{'='*20} {section_name} {'='*20}\n")
        f.write(content + "\n")