from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Define your OpenAI API key
openai.api_key = "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"


# Serve the HTML page
@app.route('/')
def index():
    return render_template('chat.html')


# Handle chat requests
@app.route('/chat', methods=['POST'])
def chat():
    # Get the message from the client
    message = request.form['message']

    # Send the message to the OpenAI model
    response = openai.Completion.create(
        engine="davinci", prompt=message, max_tokens=1024)

    # Return the model's response
    return jsonify({'message': response.choices[0].text.strip()})


if __name__ == '__main__':
    app.run(debug=True)
