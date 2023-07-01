import openai, json
from flask import Flask, render_template, request 
from dotenv import dotenv_values

config = dotenv_values('.env')
openai.api_key = config['OPEN_AI_API_KEY']

app = Flask(__name__,
    template_folder='templates',
    static_url_path="",
    static_folder="static"
)

def get_colors(input):
    prompt = f"""
        ###Instructions###
        You are a color palette generating bot. 
        You should generate colors according to the theme, or mood provided to you as input.
        You should generate 2 to 5 colors for a single prompt.

        Desired Output Format: JSON array of hexadecimal color codes

        Q: nature, sage, earth
        A: ["#edf1d6", "#9dc08b", "#609966", "#40513b"]
        
        Q: the italian flag
        A: ['#008000', '#ff0000', '#ffffff']

        Text: {input}

        Result:
    """

    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=200
    )
    
    # display_colors(json.loads(response['choices'][0]['text']))
    return json.loads(response['choices'][0]['text'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/palette', methods=['POST'])
def prompt_to_palette():
    query = request.form.get("query")
    # OPENAI Completion Call
    colors = get_colors(query)
    # Return the list of colors
    return {"colors": colors}


if (__name__ == '__main__'):
    app.run(debug=True)