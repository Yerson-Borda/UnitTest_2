from flask import Flask, request, render_template
from solution import Solution

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    heights = request.form.get('heights')

    if not heights.strip():  # Check for empty or whitespace input
        return render_template('index.html', error="ValueError: Heights input cannot be empty", heights=heights)

    try:
        heights_list = list(map(int, heights.split(',')))
        result = Solution().largestRectangleArea(heights_list)
        return render_template('index.html', result=result, heights=heights)
    except ValueError as e:
        return render_template('index.html', error=f"ValueError: {str(e)}", heights=heights)


if __name__ == '__main__':
    app.run(debug=True)
