from code import read_input, size, solve_part1, solve_part2, space_to_freed

exampleLines = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split('\n')

exampleRoot = {
    'a': {
        'e': {
            'i': 584,
        },
        'f': 29116,
        'g': 2557,
        'h.lst': 62596,
    },
    'b.txt': 14848514,
    'c.dat': 8504156,
    'd': {
        'j': 4060174,
        'd.log': 8033020,
        'd.ext': 5626152,
        'k': 7214296,
    }
}

assert read_input(exampleLines) == exampleRoot
assert size(exampleRoot) == 48381165
assert solve_part1(exampleRoot, 100_000) == 95437
assert solve_part2(exampleRoot, 70_000_000, space_to_freed(exampleRoot, 70_000_000, 30_000_000)) == 24933642
print('Tests passed')
