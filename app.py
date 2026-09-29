from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Datos de precios reales de Azure y AWS (por hora en USD)
CLOUD_SERVICES = {
    "azure": [
        {"service": "Virtual Machine B1s", "category": "Compute", "price_per_hour": 0.0104, "description": "1 vCPU, 1 GB RAM"},
        {"service": "Virtual Machine B2s", "category": "Compute", "price_per_hour": 0.0416, "description": "2 vCPU, 4 GB RAM"},
        {"service": "Azure SQL Database", "category": "Database", "price_per_hour": 0.0150, "description": "Basic tier, 5 DTUs"},
        {"service": "Blob Storage (LRS)", "category": "Storage", "price_per_gb": 0.018, "description": "Per GB/month"},
        {"service": "Azure Functions", "category": "Serverless", "price_per_million": 0.20, "description": "Per 1M executions"},
        {"service": "Azure Kubernetes Service", "category": "Containers", "price_per_hour": 0.10, "description": "Managed cluster"},
    ],
    "aws": [
        {"service": "EC2 t3.micro", "category": "Compute", "price_per_hour": 0.0104, "description": "2 vCPU, 1 GB RAM"},
        {"service": "EC2 t3.small", "category": "Compute", "price_per_hour": 0.0208, "description": "2 vCPU, 2 GB RAM"},
        {"service": "RDS MySQL", "category": "Database", "price_per_hour": 0.0160, "description": "db.t3.micro"},
        {"service": "S3 Storage", "category": "Storage", "price_per_gb": 0.023, "description": "Per GB/month"},
        {"service": "Lambda", "category": "Serverless", "price_per_million": 0.20, "description": "Per 1M requests"},
        {"service": "EKS Cluster", "category": "Containers", "price_per_hour": 0.10, "description": "Managed cluster"},
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/prices')
def get_prices():
    return jsonify(CLOUD_SERVICES)

@app.route('/api/compare/<category>')
def compare_by_category(category):
    azure = [s for s in CLOUD_SERVICES['azure'] if s['category'].lower() == category.lower()]
    aws = [s for s in CLOUD_SERVICES['aws'] if s['category'].lower() == category.lower()]
    return jsonify({"azure": azure, "aws": aws})

if __name__ == '__main__':
    app.run(debug=True)