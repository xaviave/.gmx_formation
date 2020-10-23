import os
import sys


from ArgParser import ArgParser


class GMXTestHandler(ArgParser):
    results: list = []
    test_dir: str = os.path.abspath(os.path.join("gmx_correct_me", "tests"))
    given_dir: str

    FUNCTIONS = {
        "gmx_putchar": ["a", "b", "|", "6"],
        "gmx_print_alphabet": ["abcdefghijklmnopqrstuvwxyz\n"],
        "gmx_print_numbers": ["0123456789"],
        "gmx_print_me": ["aaaaaaaaaaa", "bbbbbbbbbbb", "123", ""],
        "gmx_is_negative": ["bar", "foo", "bar", "bar"],
        "gmx_is_unique": [
            "012 013 014 015 016 017 018 019 023 024 025 026 027 028 029 034 035 036 037 038 039 045 046 047 048 049 056 057 058 059 067 068 069 078 079 089 123 124 125 126 127 128 129 134 135 136 137 138 139 145 146 147 148 149 156 157 158 159 167 168 169 178 179 189 234 235 236 237 238 239 245 246 247 248 249 256 257 258 259 267 268 269 278 279 289 345 346 347 348 349 356 357 358 359 367 368 369 378 379 389 456 457 458 459 467 468 469 478 479 489 567 568 569 578 579 589 678 679 689 789"
        ],
        "gmx_print_too_much": ["jbon", "u", "", "", "vxavoubgxavoubgxavoubgxavoubgxa"],
        "gmx_knows": ["13", "2", "0", "1"],
    }

    PROGRAMS = {
        "lenght": {"given": ["bonjour", "skuuuuuuuuuuiiiiii"], "except": ["7", "18"]},
        "uppercase": {
            "given": ["OUI", "eueueuue", "OFFofofoFOFfoffofoOFFOF"],
            "except": ["OUI", "EUEUEUUE", "OFFOFOFOFOFFOFFOFOOFFOF"],
        },
        "xavbg": {
            "given": [""],
            "except": [
                "1\n2\nXav\n4\nBg\nXav\n7\n8\nXav\nBg\n11\nXav\n13\n14\nXav\n16\n17\nXav\n19\nBg\nXav\n22\n23\nXav\nBg\n26\nXav\n28\n29\nXav\n31\n32\nXav\n34\nBg\nXav\n37\n38\nXav\nBg\n41\nXav\n43\n44\nXav\n46\n47\nXav\n49\n"
            ],
        },
    }

    """
        Override Method
    """

    def _add_parser_args(self, parser):
        super()._add_parser_args(parser)
        parser.add_argument("dir", action="store", help="directory of render")

    """
        Private Method
    """

    @staticmethod
    def execute_program(prog: str, c_files: list):
        stdout_file = f"{prog}.gmx"
        os.system(
            f"gcc -Wall -Wextra -Werror -o {prog} {' '.join(c_files)} && ./{prog} > {stdout_file}"
        )
        return stdout_file

    def diff_file(
        self,
        stdout_file: str,
        name: str,
        expected_data: list,
    ):
        try:
            with open(stdout_file) as f:
                g_data = f.read().split("/")
                if g_data != expected_data:
                    return (
                        f"{name}: " "\033[93m" + f"Your function doesn't work {g_data}" + "\033[0m"
                    )
        except FileNotFoundError:
            return f"{name}: " "\033[93m" + "Compilation Error" + "\033[0m"
        return f"{name}: " "\033[92m" + "Ok" + "\033[0m"

    def _test_functions(self):
        for func_name in self.FUNCTIONS:
            stdout_file = self.execute_program(
                func_name,
                [
                    os.path.join(self.given_dir, f"{func_name}.c"),
                    os.path.join(self.test_dir, f"main_{func_name}.c"),
                ],
            )
            self.results.append(self.diff_file(stdout_file, func_name, self.FUNCTIONS[func_name]))

    def _test_programs(self):
        for c_prog in self.PROGRAMS:
            c_prog_path = os.path.join(self.given_dir, f"{c_prog}.c")
            os.system(f"gcc -o {c_prog} {c_prog_path}")
            for i, l in enumerate(self.PROGRAMS[c_prog]["given"]):
                os.system(f"./{c_prog} {l} > {c_prog}.gmx")
                self.results.append(
                    self.diff_file(f"{c_prog}.gmx", c_prog, [self.PROGRAMS[c_prog]["except"][i]])
                )

    def _print_result(self):
        for r in sorted(set(self.results)):
            print(r)

    def _clean(self):
        for k in [*self.FUNCTIONS.keys(), *self.PROGRAMS.keys()]:
            try:
                os.remove(k)
                os.remove(f"{k}.gmx")
            except FileNotFoundError:
                pass

    def _check_directory(self, dir):
        if os.path.exists(dir) == False:
            print(f"Directory {dir} doesn't exist, check it")
            sys.exit(-1)
        self.given_dir = os.path.abspath(dir)

    def __init__(self):
        super().__init__()
        self._check_directory(self.get_args("dir", ""))
        self._test_functions()
        self._test_programs()
        self._print_result()
        self._clean()
