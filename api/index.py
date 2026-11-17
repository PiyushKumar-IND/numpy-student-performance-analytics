import os
import pandas as pd
import plotly.express as px
from flask import Flask, render_template_string

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "students.csv")

@app.route("/")
def dashboard():

    df = pd.read_csv(DATA_PATH)

    total_students = len(df)
    average_marks = round(df["final_score"].mean(), 2)
    average_attendance = round(df["attendance"].mean(), 2)
    average_study = round(df["study_hours"].mean(), 2)

    excellent = len(df[df["final_score"] >= 80])
    good = len(df[(df["final_score"] >= 60) & (df["final_score"] < 80)])
    improvement = len(df[df["final_score"] < 60])

    low_attendance = len(df[df["attendance"] < 75])

    chart1 = px.histogram(
        df, x="final_score",
        title="Student Marks Distribution",
        nbins=15
    ).to_html(full_html=False)

    chart2 = px.box(
        df,
        y=["math", "science", "english"],
        title="Subject Performance Comparison"
    ).to_html(full_html=False)

    chart3 = px.scatter(
        df,
        x="study_hours",
        y="final_score",
        color="gender",
        title="Study Hours vs Final Score"
    ).to_html(full_html=False)

    chart4 = px.histogram(
        df,
        x="attendance",
        title="Attendance Distribution",
        nbins=15
    ).to_html(full_html=False)

    return render_template_string("""
    <html>
    <head>
        <title>Student Performance Analytics</title>
        <style>
            body {
                font-family: Arial;
                background: #f1f5f9;
                padding: 25px;
            }
            h1 { color: #172554; }
            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit,minmax(180px,1fr));
                gap: 15px;
            }
            .card {
                background: white;
                padding: 22px;
                border-radius: 12px;
                box-shadow: 0 2px 8px #ddd;
            }
            .charts {
                background: white;
                padding: 15px;
                margin-top: 20px;
                border-radius: 12px;
            }
            h2 { color: #1e40af; }
        </style>
    </head>

    <body>
        <h1>Student Performance Analytics Dashboard</h1>

        <div class="cards">
            <div class="card">
                <h3>Total Students</h3>
                <h2>{{ total }}</h2>
            </div>

            <div class="card">
                <h3>Average Marks</h3>
                <h2>{{ marks }}%</h2>
            </div>

            <div class="card">
                <h3>Average Attendance</h3>
                <h2>{{ attendance }}%</h2>
            </div>

            <div class="card">
                <h3>Average Study Hours</h3>
                <h2>{{ study }}</h2>
            </div>
        </div>

        <div class="charts">
            <h2>Student Categories</h2>
            <p>Excellent Students: {{ excellent }}</p>
            <p>Good Students: {{ good }}</p>
            <p>Needs Improvement: {{ improvement }}</p>
            <p>Low Attendance: {{ low_attendance }}</p>
        </div>

        <div class="charts">{{ chart1|safe }}</div>
        <div class="charts">{{ chart2|safe }}</div>
        <div class="charts">{{ chart3|safe }}</div>
        <div class="charts">{{ chart4|safe }}</div>

    </body>
    </html>
    """,
    total=total_students,
    marks=average_marks,
    attendance=average_attendance,
    study=average_study,
    excellent=excellent,
    good=good,
    improvement=improvement,
    low_attendance=low_attendance,
    chart1=chart1,
    chart2=chart2,
    chart3=chart3,
    chart4=chart4
    )