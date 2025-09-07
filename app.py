from flask import Flask, render_template, request, redirect, url_for
from config import LANGUAGE_MAP
import replicate
import os

app = Flask(__name__)

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_text = request.form["prompt"]
        selected_language = request.form["style"]

        # Word limit check
        word_count = len(original_text.split())
        if word_count > 50:
            translated_text = f"[Too long: {word_count} words. Please limit to 50 words or fewer.]"
            return render_template("index.html",
                                original_text=original_text,
                                translated_text=translated_text,
                                selected_language=selected_language)

        full_prompt = f"Translate to {selected_language.capitalize()}: {original_text}"
        print("Prompt sent to model:", full_prompt)

        try:
            output = replicate.run(
                "qwen/qwen3-235b-a22b-instruct-2507",
                input={"prompt": full_prompt}
            )
            print("Raw output from Replicate:", output)
                
            if output and isinstance(output, list):
            # Join non-empty strings into one clean sentence
                translated_text = " ".join([line.strip() for line in output if line.strip()])
            else:
                translated_text = "[Translation failed or empty output]"

        except Exception as e:
            print("Error during translation:", e)
            translated_text = "[Translation error]"

        return render_template("index.html",
                               original_text=original_text,
                               translated_text=translated_text,
                               selected_language=selected_language)

    # This is the fallback for GET requests (e.g., when the page first loads)
    return render_template("index.html",
                           original_text="",
                           translated_text=None,
                           selected_language="")

@app.route("/clear", methods=["POST"])
def clear():
    return redirect(url_for("index"))

app.config["DEBUG"] = True

if __name__ == "__main__":
    app.run()
