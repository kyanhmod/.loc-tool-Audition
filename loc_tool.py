#!/usr/bin/env python3
"""
Audition LOC <-> SLK Converter
Thuat toan: Byte-wise XOR 0x64 (Symmetric)
Khong crash, khong xoa file goc, ho tro batch convert.
"""
import sys
import os

XOR_KEY = 0x64

def convert_file(input_path: str, output_path: str = None):
    if not os.path.exists(input_path):
        print(f"[-] Khong tim thay file: {input_path}")
        return False

    if output_path is None:
        base, ext = os.path.splitext(input_path)
        if ext.lower() == ".loc":
            output_path = base + ".slk"
        elif ext.lower() == ".slk":
            output_path = base + ".loc"
        else:
            output_path = base + "_converted" + ext

    try:
        with open(input_path, "rb") as fin:
            data = fin.read()

        # Thuc hien XOR 0x64
        converted = bytes(b ^ XOR_KEY for b in data)

        with open(output_path, "wb") as fout:
            fout.write(converted)

        print(f"[+] Thanh cong: {input_path} -> {output_path} ({len(converted):,} bytes)")
        return True
    except Exception as e:
        print(f"[-] Loi khi xu ly {input_path}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Cach dung:")
        print("  python loc_tool.py <file_input.loc | file_input.slk> [file_output]")
        print("  Hoac keo tha file vao script.")
        return

    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    convert_file(inp, out)

if __name__ == "__main__":
    main()
