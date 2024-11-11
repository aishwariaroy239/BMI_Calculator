from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = ""
    result = None  # Initialize result to avoid reference before assignment

    if request.method == "POST":
        name = request.form.get("name")
        mode = request.form.get("mode")
        height = float(request.form.get("height"))
        weight = float(request.form.get("weight"))
        
        # Calculate BMI
        if mode == "1":  # Kg/m^2
            bmi = weight / (height ** 2)
        elif mode == "2":  # Pounds/inches^2
            bmi = (weight / (height ** 2)) * 703
        
        # Determine BMI category
        if bmi is not None:
            if bmi < 18.5:
                category = "underweight"
            elif bmi <= 24.9:
                category = "normal weight"
            elif bmi <= 29.9:
                category = "overweight"
            elif bmi <= 34.9:
                category = "obese"
            elif bmi <= 39.9:
                category = "severely obese"
            else:
                category = "morbidly obese"
            
            result = f"{name}, your BMI is {bmi:.2f}. You are {category}."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)