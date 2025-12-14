import sys
import json
import os
import requests

def translate_line(text: str) -> str:
    url = "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-en-ru"
    token = os.getenv("HF_API_TOKEN")
    headers = {
        "Authorization": f"Bearer {token}",
    }
    res = requests.post(url, headers=headers, json={"inputs": text})

    if res.ok:
        data = res.json()
        if isinstance(data, list) and "translation_text" in data[0]:
            return data[0]["translation_text"]
    return text

def translate_srt(in_srt: str, out_srt: str):
    with open(in_srt, "r", encoding="utf-8") as f:
        lines = f.readlines()

    out_lines = []
    i = 0
    while i < len(lines):
        if i + 2 < len(lines) and "-->" in lines[i + 1]:
            num = lines[i]
            timecode = lines[i + 1]
            text = lines[i + 2].strip()
            blank = lines[i + 3] if i + 3 < len(lines) else "\n"

            translated = translate_line(text) if text else ""
            out_lines.extend([num, timecode, translated + "\n", blank])
            i += 4
        else:
            out_lines.append(lines[i])
            i += 1

    with open(out_srt, "w", encoding="utf-8") as f:
        f.writelines(out_lines)

if __name__ == "__main__":
    translate_srt(sys.argv[1], sys.argv[2])
    print(json.dumps({"translated_srt": sys.argv[2]}))