import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Directory for GIFs
GIF_DIR = "static/gifs"

# Ensure the GIF directory exists
if not os.path.exists(GIF_DIR):
    os.makedirs(GIF_DIR)

def load_route_gifs():
    """
    Scans the GIF_DIR and groups GIFs by route name based on filename prefixes.
    Adjust or extend route_name_map if your naming convention differs.
    """
    route_gifs = {}
    # Map filename prefixes to route names
    route_name_map = {
        '1bu': '1BU',
        'comm': 'Comm Ave',
        'fenway': 'Fenway'
    }
    
    for filename in os.listdir(GIF_DIR):
        if filename.lower().endswith('.gif'):
            lower_name = filename.lower()
            for prefix, route_name in route_name_map.items():
                if lower_name.startswith(prefix):
                    if route_name not in route_gifs:
                        route_gifs[route_name] = []
                    route_gifs[route_name].append(filename)
                    break
    return route_gifs

# Load GIFs based on directory and naming convention
ROUTE_GIFS = load_route_gifs()

# HTML Template
template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bus Route Visualizations</title>
<style>
  body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    margin: 20px;
    background-color: #f8f9fa;
    color: #333;
  }
  h1, h2, h3 {
    margin-bottom: 15px;
    font-weight: 600;
  }
  p {
    line-height: 1.6;
    margin-bottom: 20px;
  }
  form {
    margin-bottom: 20px;
  }
  select {
    padding: 5px;
    margin-right: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
  }
  input[type="submit"] {
    padding: 6px 12px;
    background-color: #007bff;
    color: #fff;
    border: none;
    font-size: 14px;
    border-radius: 4px;
    cursor: pointer;
  }
  input[type="submit"]:hover {
    background-color: #0056b3;
  }
  .gif-container {
    margin-bottom: 40px;
    text-align: center;
  }
  .gif-container img {
    max-width: 600px;
    border: 1px solid #ddd;
    border-radius: 4px;
    display: block;
    margin: 0 auto 5px auto;
    background-color: #fff;
    padding: 5px;
  }
  .gif-container p {
    margin: 0;
    font-size: 14px;
    color: #555;
  }
  .description {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 4px;
    border: 1px solid #ddd;
    margin-bottom: 30px;
  }
</style>
</head>
<body>
  <h1>Bus Route Visualizations</h1>
  <div class="description">
    <p>
      Welcome to the Bus Route Visualizations project! Here, we showcase animated gifs representing 
      the movements of buses along various routes. These animations are derived from GPS data collected 
      over time, processed to identify loops, stops, and average delays.
    </p>
    <p>
      Each animation provides a visual understanding of how the bus travels through its route, 
      including which stops it visits. By selecting a route from the dropdown menu below, you can 
      explore these animations to gain insights into route timing and  
      bus performance.
    </p>
  </div>

    <form method="POST">
    <select name="route_selection">
        {% for route in routes %}
        <option value="{{route}}" {% if selected_route == route %}selected{% endif %}>{{route}}</option>
        {% endfor %}
    </select>
    <input type="submit" value="View GIFs">
    </form>

  {% if gifs_for_route %}
    <h2>Showing Animations for {{ selected_route }}</h2>
    {% for gif in gifs_for_route %}
      <div class="gif-container">
        <img src="{{ url_for('static', filename='gifs/' + gif) }}" alt="GIF for {{ selected_route }}">
      </div>
    {% endfor %}
  {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_route = None
    gifs_for_route = []
    
    if request.method == 'POST':
        selected_route = request.form.get('route_selection')
        if selected_route in ROUTE_GIFS:
            gifs_for_route = ROUTE_GIFS[selected_route]
    
    return render_template_string(
        template,
        routes=sorted(ROUTE_GIFS.keys()),
        selected_route=selected_route,
        gifs_for_route=gifs_for_route
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
