from flask import Flask, render_template, request, redirect, url_for, send_file
from config import LANGUAGE_MAP
from gtts import gTTS
import replicate
import os

app = Flask(__name__)

def generate_audio_stream(translated_text):
    tts = gTTS(translated_text)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

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
            "yorickvp/llava-v1.6-vicuna-13b:0603dec596080fa084e26f0ae6d605fc5788ed2b1a0358cd25010619487eae63",
            input={"prompt": full_prompt}
         )

        # Consume the generator and join the output
            result = "".join(output).strip() if output else ""
            translated_text = result if result else "[Translation failed or empty output]"

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

# Route that calls the function and streams audio
@app.route('/speak', methods=['POST'])
def speak():
    translated_text = request.form['translated_text']
    audio_stream = generate_audio_stream(translated_text)
    return send_file(audio_stream, mimetype='audio/mpeg')

@app.route("/clear", methods=["POST"])
def clear():
    return redirect(url_for("index"))

app.config["DEBUG"] = True

if __name__ == "__main__":
    app.run()
