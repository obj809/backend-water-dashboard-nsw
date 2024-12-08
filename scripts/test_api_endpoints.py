# scripts/test_api_endpoints.py

import requests
import os
import json

# Base URL of the Flask API
BASE_URL = "http://localhost:5001/api"

# Endpoints to test
ENDPOINTS = [
    {"path": "/", "method": "GET", "description": "Main welcome route"},
    {"path": "/dams", "method": "GET", "description": "List all dams"},
    {"path": "/dams/{dam_id}", "method": "GET", "description": "Get dam by ID", "sample_data": {"dam_id": "203042"}},
    {"path": "/latest_data", "method": "GET", "description": "List all latest dam data entries"},
    {"path": "/latest_data/{dam_id}", "method": "GET", "description": "Get latest data for a specific dam by ID", "sample_data": {"dam_id": "203042"}},
    {"path": "/dam_resources", "method": "GET", "description": "List all dam resources"},
    {"path": "/dam_resources/{resource_id}", "method": "GET", "description": "Get dam resource by ID", "sample_data": {"resource_id": 1}},
    {"path": "/specific_dam_analysis", "method": "GET", "description": "List all specific dam analyses"},
    {"path": "/specific_dam_analysis/{dam_id}", "method": "GET", "description": "Get specific dam analyses by dam ID", "sample_data": {"dam_id": "203042"}},
    {"path": "/overall_dam_analysis", "method": "GET", "description": "List all overall dam analyses"},
    {"path": "/overall_dam_analysis/{analysis_date}", "method": "GET", "description": "Get overall dam analysis by date", "sample_data": {"analysis_date": "2023-01-01"}},
    {"path": "/dam_groups", "method": "GET", "description": "List all dam groups"},
    {"path": "/dam_groups/{group_name}", "method": "GET", "description": "Get dam group by name", "sample_data": {"group_name": "small_dams"}},
    {"path": "/dam_group_members", "method": "GET", "description": "List all dam group members"},
    {"path": "/dam_group_members/{group_name}", "method": "GET", "description": "Get members by group name", "sample_data": {"group_name": "small_dams"}},
]

def test_endpoint(endpoint, base_url=BASE_URL):
    """Tests an API endpoint with the given method and path."""
    path = endpoint["path"]
    method = endpoint["method"]
    description = endpoint["description"]
    sample_data = endpoint.get("sample_data", {})

    # Replace placeholders in path with sample data
    for key, value in sample_data.items():
        path = path.replace(f"{{{key}}}", str(value))

    url = f"{base_url}{path}"
    params = {"limit": 10} if "limit" in path or "?" in path else None  # Add limit if applicable
    print(f"Testing {method} {url} - {description}")

    try:
        if method == "GET":
            response = requests.get(url, params=params)
        else:
            raise ValueError(f"Unsupported method: {method}")

        if response.status_code == 200:
            try:
                # Try parsing JSON and limiting results to 10 if it's a list
                content = response.json()
                if isinstance(content, list):
                    content = content[:10]  # Limit to 10 records if applicable
                return {"url": url, "status_code": 200, "description": description, "content": content}
            except json.JSONDecodeError:
                return {"url": url, "status_code": 200, "description": description, "content": "Response is not valid JSON"}
        elif response.status_code == 404:
            return {"url": url, "status_code": 404, "description": description, "content": "No data found"}
        else:
            return {"url": url, "status_code": response.status_code, "description": description, "content": response.text}
    except requests.RequestException as e:
        return {
            "url": url,
            "status_code": "ERROR",
            "description": description,
            "content": f"Request failed: {e}"
        }

def main():
    results = []

    for endpoint in ENDPOINTS:
        result = test_endpoint(endpoint)
        results.append(result)

    # Save results to a JSON file
    output_file = os.path.join(os.path.dirname(__file__), "api_test_results.json")
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"API test results saved to {output_file}")

if __name__ == "__main__":
    main()
