from flask import Flask, request, render_template
from solution import Solution

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    heights = request.form.get('heights')
    heights_list = list(map(int, heights.split(',')))
    try:
        result = Solution().largestRectangleArea(heights_list)
        return render_template('index.html', result=result, heights=heights)
    except ValueError as e:
        return render_template('index.html', error=str(e), heights=heights)

if __name__ == '__main__':
    app.run(debug=True)
